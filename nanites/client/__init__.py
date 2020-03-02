# coding: utf-8

"""
    Nanites Client

    This code provides a layer of insulation between the Swagger generated code
    and a client.  Returns swagger models.

    Essentially just maps a set of standard API function names to Swagger code, e.g.

        createPerson  -> PeopleApi.people_create
        readPerson    -> PeopleApi.people_read
        deletePerson  -> PeopleApi.people_delete
        updatePerson  -> PeopleApi.people_update
        listPeople    -> PeopleApi.people_list

    The Swagger models are returned, though these are relatively simple things with
    attributes corresponding to data fields.  Don't really need a wrapper for those.

    Arguments to the standard functions are attribute kwargs:

        createPerson(first_name='Vera', last_name='Min')

    which are converted to whatever Swagger wants.  Extra parameters are passed on to
    the Swagger code so you can use things like "async=True".  An ApiClient class can
    be specified as is done in the tests.

    Contact: ifx@fas.harvard.edu

"""
import re
import logging
from nanites.client.swagger.api_client import ApiClient
from nanites.client.swagger.models import *
from nanites.client.swagger.api import *
from nanites.client.swagger.rest import ApiException

logger = logging.getLogger(__name__)


MODEL_NAMES = {
    'Source': 'Sources',
    'Person': 'People',
    'User': 'Users',
    'Address': 'Addresses',
    'PersonAddress': 'PersonAddresses',
    'PersonAffiliation': 'PersonAffiliations',
    'Organization': 'Organizations',
    'Login': 'Logins',
    'Contact': 'Contacts',
    'Application': 'Applications',
}


OPERATIONS = [
    'create',
    'delete',
    'list',
    'plist',
    'update',
    'read'
]

common_doc = '''
        Default authentication uses settings.IFX_APP['token'] value.  Alternate token can be used by
        creating a new ApiClient with a new Configuration

        >>> from nanites.client.swagger import ApiClient, Configuration
        >>> from nanites.client import API
        >>> configuration = Configuration()
        >>> configuration.api_key = 'mynewtokenthatwillneverwork'
        >>> api_client = ApiClient(configuration=configuration)
        >>> API.listSomething(api_client=api_client)
'''

DOCS = {
    'createPerson': '''
        Create a Person.  Data dictionary input may include
        %s
    ''' % common_doc,
    'listPeople': '''
        Retrieve a list of rich Person objects, including contacts, addresses, and affiliations.
        People may be retrieved by username and login:

           people = listPeople(username='akitzmiller', login='RC AD')

        by primary email

           people = listPeople(primary_email='akitzmiller@g.harvard.edu')

        by any email contact associated with the user

           people = listPeople(email='aaron.kitzmiller@gmail.com')

        and can be sorted using the 'ordering' parameter with standard Django model conventions

           people = listPeople(ordering='-created')

        Because full objects are retrieved, large lists may take a long time.  For more efficient
        retrieval of large sets use the paged listing function (plistPeople) or specialized queries
        (getBasicsByLogin).
        %s
    ''' % common_doc,
    'plistPeople': '''
        Retrieve a list of people with explicit paging support.  Total matching records is always returned.

            >>> people_page = plistPeople(page_size=15, page=1)
            >>> people_page.count
            10030
            >>> len(people_page.results)
            15
            >>> people_page.results[0].full_name
            'Aaron J Kitzmiller'
            >>> people_page = API.plistPeople(page_size=15, page=2)
            >>> people_page.results[0].full_name
            'Mike Stopa'

        Results should be explicitly ordered when possible to ensure that pages are consistent.

            >>> people_page = API.plistPeople(page_size=15, page=1, ordering='-last_name')
            >>> people_page.results[0].full_name
            'David Zwicker'
        %s
    ''' % common_doc,
    'readPerson': '''
        Retrieve a single Person object by id.

            >>> person = API.readPerson(id=1)
            >>> person.full_name
            'Aaron J Kitzmiller'

        A full object is returned with contacts, affiliations, addresses, and logins

            >>> person.contacts[0].role
            'Primary Email'
            >>> person.contacts[0].contact.detail
            'akitzmiller@g.harvard.edu'
            >>> person.logins[0].username
            'akitzmiller'

        An exception is thrown for non-existent records.

            >>> try:
            ...     person = API.readPerson(id=10000000)
            ... except Exception as e:
            ...     print(e)
            ...
            Item not found in call to people_read using {'id': 10000000}
            >>>
        %s
    ''' % common_doc,
    'updateSource': '''
        Update a Source record.  The Source data must be a dictionary (not Source object)

            >>> source = API.readSource(name='nnin2person.py admin')
            >>> source.description = 'Automatically converted from NNIN database using nnin_admin as a source'
            >>> source_dict = source.to_dict()
            >>> updated = API.updateSource(**source_dict)
            >>> updated
            {'description': 'Automatically converted from NNIN database using nnin_admin '
                            'as a source',
            'id': 1,
            'name': 'Manual entry'}
            >>>
        %s
    ''' % common_doc,
}


DEFAULT_LIST_PAGE_SIZE = 1000000000

class SwaggerClient(object):

    def __init__(self, api_client=None):
        self.api_client = api_client
        if not self.api_client:
            self.api_client = ApiClient()

        # Setup the valid function names for the client based on the MODEL_NAMES
        # and operations (e.g. 'create')
        self.fnames = []
        for singular, plural in MODEL_NAMES.items():
            for operation in ['create', 'delete', 'read', 'update']:
                self.fnames.append('%s%s' % (operation, singular))
            self.fnames.append('list%s' % plural)
            self.fnames.append('plist%s' % plural)

        # Setup a regex for splitting the model name and operation from the function name
        singulars_and_plurals = list(MODEL_NAMES.keys()) + list(MODEL_NAMES.values())
        restr = '(%s)(%s)' % ('|'.join(OPERATIONS), '|'.join(singulars_and_plurals))
        self.function_name_re = re.compile(restr)


        # OK.  Going to setup a bunch of callable classes that simulate regular
        # function calls, (e.g. createSource) but use the apiFn below
        def init(self, func):
            self.func = func
            self.func_name = self.__class__.__name__

        def call(self, *args, **kwargs):
            return self.func(api_func_name=self.func_name, *args, **kwargs)

        self.types = {}
        for fname in self.fnames:
            class_dict = {
                '__init__': init,
                '__call__': call,
                '__doc__': DOCS.get(fname, 'This is a callable class that simulates a %s() method.' % fname),
            }
            self.types[fname] = type(fname, (object,), class_dict)

    def apiFn(self, api_func_name, *args, **kwargs):
        '''
        Execute API function based on the model name and operation as
        determined by the function_name
        Model name should be capitalized and singular (e.g. Source).
        Operation should be one of
            create
            delete
            list
            read
            update
        '''

        if not api_func_name in self.fnames:
            raise Exception('I am not familiar with the %s function' % api_func_name)

        # Parse the api func name for operation and model
        match = self.function_name_re.match(api_func_name)
        if not match:
            raise Exception('Function name %s cannot be parsed.' % api_func_name)
        operation = match.group(1)
        model_name = match.group(2)

        # Model name might be plural, so switch it to singluar
        for k, v in MODEL_NAMES.items():
            if model_name == v:
                model_name = k

        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client

        # Model class
        model_class = globals()[model_name]

        # Collect data dict for api call using the model attributes
        data = {}
        for key in model_class.attribute_map.keys():
            if key in kwargs:
                data[key] = kwargs.pop(key)

        # Swagger API class name e.g. SourcesApi
        api_class = globals()['%sApi' % MODEL_NAMES[model_name]]
        api = api_class(api_client=api_client)

        if operation == 'plist':
            swagger_func_name = '%s_%s' % (MODEL_NAMES[model_name], 'list')
        else:
            swagger_func_name = '%s_%s' % (MODEL_NAMES[model_name], operation)

        # Run in correct form.  updates and deletes require an id in most cases
        # though for "Source" it's a name
        # create requires a data dict, others use kwargs for some reason
        if operation == 'create':
            return self.call_api_func(api, swagger_func_name.lower(), data=data, **kwargs)
        elif operation == 'update':
            if model_name == 'Source':
                if 'name' not in data:
                    raise Exception('Source update requires a name')
                name = data.pop('name')
                return self.call_api_func(api, swagger_func_name.lower(), name=name, data=data, **kwargs)
            else:
                if 'id' not in data:
                    raise Exception('id required to update %s' % model_name)
                id = data.pop('id')
                return self.call_api_func(api, swagger_func_name.lower(), id=id, data=data, **kwargs)
        elif operation == 'delete':
            if model_name in ['Source', 'Application']:
                if 'name' not in data:
                    raise Exception('%s delete requires a name' % model_name)
                name = data.pop('name')
                return self.call_api_func(api, swagger_func_name.lower(), name=name, **kwargs)
            else:
                if 'id' not in data:
                    raise Exception('id required to delete %s' % model_name)
                id = data.pop('id')
                return self.call_api_func(api, swagger_func_name.lower(), id=id, **kwargs)
        elif operation == 'list':
            kwargs['page'] = 1
            if 'page_size' not in kwargs:
                kwargs['page_size'] = DEFAULT_LIST_PAGE_SIZE
            response = self.call_api_func(api, swagger_func_name.lower(), **data, **kwargs)
            results = response.results

            # Use paging to get the total.  Because the default list page is so high,
            # this will probably only happen when pageing is set
            while response.count > len(results):
                kwargs['page'] += 1
                response = self.call_api_func(api, swagger_func_name.lower(), **data, **kwargs)
                results.extend(response.results)
            return results
        elif operation == 'plist':
            if 'page_size' not in kwargs:
                kwargs['page_size'] = DEFAULT_LIST_PAGE_SIZE
            response = self.call_api_func(api, swagger_func_name.lower(), **data, **kwargs)
            return response
        else:
            return self.call_api_func(api, swagger_func_name.lower(), **data, **kwargs)

    def call_api_func(self, api, func_name, *args, **kwargs):
        '''
        Calls the API function and converts RESTy exceptions into something normalish
        '''
        try:
            logger.debug('Calling %s on %s with args %s and kwargs %s' % (func_name, api, str(args), str(kwargs)))
            return getattr(api, func_name)(*args, **kwargs)
        except ApiException as e:
            logger.debug(str(e))
            if e.status == 404:
                raise Exception('Item not found in call to %s using %s' % (func_name, repr(kwargs)))
            elif e.status == 401:
                raise Exception('Not authorized to use %s' % func_name)
            else:
                raise

    def __getattr__(self, name):
        if name in self.fnames:
            functionByName = self.types[name](self.apiFn)
            return functionByName
        else:
            return self.__getattribute__(name)

    def __dir__(self):
        return sorted(
            set(
                super().__dir__() + self.fnames + list(self.__dict__.keys())
            )
        )

    def getBasicsByLogin(self, *args, **kwargs):
        '''
        Used by the Office Hours Sign In application, this method returns the
        username, full_name, primary_email, and lab_name for the user along with
        pi_full_name, and department_name.
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetBasicsByLoginApi(api_client=api_client)
        return self.call_api_func(api, 'get_basics_by_login_list', *args, **kwargs)

    def getUserList(self, *args, **kwargs):
        '''
        Used by the RC user list, this method returns the
        username:is_enabled, full_name, primary_email, and lab_name for the user along with
        pi_full_name, and department_slug.  A search term may be provided.
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetUserListApi(api_client=api_client)
        return self.call_api_func(api, 'get_user_list_list', *args, **kwargs)

    def getOrgNames(self, *args, **kwargs):
        '''
        Used by the Office Hours Sign In application, retrieves the full list of organization names
        for a specified org tree.

        By default organizational units are sorted so that the lower ranking units (e.g. Laboratory) are
        returned before higher ranking units (e.g. Institution).  This is to encourage users to be as specific as
        possible.

        Order and returned ranks can be changed by setting the ranks parameter to an comma separated list of
        org ranks in the order needed.  To return just departments and laboratories, department first:

        >>> orgs = API.getOrgNames(ranks='Department,Laboratory')
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetOrgNamesApi(api_client=api_client)
        objs = self.call_api_func(api, 'get_org_names_list', *args, **kwargs)
        return objs

    def getPiNames(self, *args, **kwargs):
        '''
        Special purpose getOrgNames call.  Returns just the names, rather than the GetOrgNames objects.
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetPiNamesApi(api_client=api_client)
        objs = self.call_api_func(api, 'get_pi_names_list', *args, **kwargs)
        return objs

    def getLocationInfo(self, *args, **kwargs):
        '''
        Location info based on user input
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetLocationInfoApi(api_client=api_client)
        return self.call_api_func(api, 'get_location_info_list', *args, **kwargs)

API = SwaggerClient()
