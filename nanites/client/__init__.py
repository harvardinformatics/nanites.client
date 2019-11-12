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
    'update',
    'read'
]


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
                '__doc__': 'This is a callable class that simulates a %s() method.' % fname,
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
        Special purpose getBasicsByLogin call
        '''
        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client
        api = GetBasicsByLoginApi(api_client=api_client)
        return self.call_api_func(api, 'get_basics_by_login_list', *args, **kwargs)

    def getOrgNames(self, *args, **kwargs):
        '''
        Special purpose getOrgNames call.  Returns just the names, rather than the GetOrgNames objects.
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


API = SwaggerClient()