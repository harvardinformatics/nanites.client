# coding: utf-8

"""
    Nanites Client

    This code provides a layer of insulation between the Swagger generated code
    and a client.  Returns swagger models.

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
        %s

        Execute API function based on the model name and operation as
        determined by the function_name
        Model name should be capitalized and singular (e.g. Source).
        Operation should be one of
            create
            delete
            list
            read
            update
        ''' % api_func_name

        if not api_func_name in self.fnames:
            raise Exception('I am not familiar with the %s function' % api_func_name)

        # Parse the api func name for operation and model
        match = self.function_name_re.match(api_func_name)
        if not match:
            raise Exception('Function name %s cannot be parsed.' % api_func_name)
        operation = match.group(1)
        model_name = match.group(2)

        api_client = kwargs.pop('api_client', None)
        if not api_client:
            api_client = self.api_client

        # Model class
        model_class = globals()[model_name]

        # Collect data dict for api call using the model attributes
        data = {}
        for key in model_class.attribute_map.keys():
            if key in kwargs:
                data[key] = kwargs[key]

        # Swagger API class name e.g. SourcesApi
        api_class = globals()['%sApi' % MODEL_NAMES[model_name]]
        api = api_class(api_client=api_client)

        swagger_func_name = '%s_%s' % (MODEL_NAMES[model_name], operation)

        # Run in correct form.  updates and deletes require an id in most cases
        # though for "Source" it's a name
        # create requires a data dict, others use kwargs for some reason
        if operation == 'create':
            return self.call_api_func(api, swagger_func_name.lower(), data=data)
        elif operation == 'update':
            if model_name == 'Source':
                if 'name' not in data:
                    raise Exception('Source update requires a name')
                name = data.pop('name')
                return self.call_api_func(api, swagger_func_name.lower(), name=name, data=data)
            else:
                if 'id' not in data:
                    raise Exception('id required to update %s' % model_name)
                id = data.pop('id')
                return self.call_api_func(api, swagger_func_name.lower(), id=id, data=data)
        elif operation == 'delete':
            if model_name == 'Source':
                if 'name' not in data:
                    raise Exception('Source delete requires a name')
                name = data.pop('name')
                return self.call_api_func(api, swagger_func_name.lower(), name=name)
            else:
                if 'id' not in data:
                    raise Exception('id required to delete %s' % model_name)
                id = data.pop('id')
                return self.call_api_func(api, swagger_func_name.lower(), id=id, data=data)
        elif operation == 'list':
            response = self.call_api_func(api, swagger_func_name.lower(), **data)
            return response.results
        else:
            return self.call_api_func(api, swagger_func_name.lower(), **data)

    def call_api_func(self, api, func_name, *args, **kwargs):
        '''
        Calls the API function and converts RESTy exceptions into something normalish
        '''
        try:
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


API = SwaggerClient()