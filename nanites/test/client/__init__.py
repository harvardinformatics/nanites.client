# coding: utf-8

'''
Test base class.  Sets up things like Organizations and cleans out accumulated data
'''
import logging
import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data

logger = logging.getLogger(__name__)


class ApiTest(unittest.TestCase):
    '''
    Initializes an api client that is used in the tests
    Runs a clean function in both setUp  and tearDown that will
    remove any object ids stored in the IDS dict

    Organizations are setup in the setUp method.

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configuration = Configuration()
        self.configuration.debug = False
        self.api_client = ApiClient(configuration=self.configuration)
        self.IDS = {
            'Contact': [],
            'Person': [],
            'Login': [],
            'Organization': [],
            'Address': [],
            'Source': [],
            'Application': [],
        }
        self.plurals = {
            'Contact': 'Contacts',
            'Person': 'People',
            'Login': 'Logins',
            'Organization': 'Organizations',
            'Address': 'Addresses',
            'Source': 'Sources',
            'Application': 'Applications',
        }

    def setUp(self):
        self.clean()
        for orgdata in data.ORGANIZATIONS:
            try:
                org = API.createOrganization(api_client=self.api_client, **orgdata)
                self.IDS['Organization'].append(org.id)
            except Exception:
                pass
        for applicationdata in data.APPLICATIONS:
            try:
                application = API.createApplication(api_client=self.api_client, **applicationdata)
            except Exception:
                pass
        for sourcedata in data.SOURCES:
            try:
                source = API.createSource(api_client=self.api_client, **sourcedata)
            except Exception:
                pass


    def tearDown(self):
        self.clean()

    def clean(self):
        for model_name, ids in self.IDS.items():
            results = API.apiFn('list%s' % self.plurals[model_name], api_client=self.api_client)
            for result in results:
                try:
                    if model_name in ['Source', 'Application']:
                        API.apiFn('delete%s' % model_name, api_client=self.api_client, name=result.name)
                    elif model_name == 'Person':
                        API.apiFn('deletePerson', api_client=self.api_client, ifxid=result.ifxid)
                    elif model_name == 'Organization':
                        API.apiFn('deleteOrganization', api_client=self.api_client, ifxorg=result.ifxorg)
                    elif model_name == 'Contact':
                        API.apiFn('deleteContact', api_client=self.api_client, ifxcon=result.ifxcon)
                    else:
                        API.apiFn('delete%s' % model_name, api_client=self.api_client, id=result.id)
                except Exception as e:
                    print('Error deleting id %s: %s' % (str(id), str(e)))

