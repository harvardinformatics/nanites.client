# coding: utf-8

'''
Test base class.  Sets up things like Organizations and cleans out accumulated data
'''


from __future__ import absolute_import

import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from test.client import data


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
        self.configuration.debug = True
        self.api_client = ApiClient(configuration=self.configuration)
        self.IDS = {
            'Person': [],
            'Login': [],
            'Organization': [],
            'Address': [],
            'Source': [],
            'Application': [],
            'Contact': [],
        }

    def setUp(self):
        self.clean()
        for orgdata in data.ORGANIZATIONS:
            org = API.createOrganization(api_client=self.api_client, **orgdata)
            self.IDS['Organization'].append(org.id)

    def tearDown(self):
        self.clean()

    def clean(self):
        for model_name, ids in self.IDS.items():
            for i in range(len(ids)):
                id = self.IDS[model_name].pop()
                try:
                    API.apiFn('delete%s' % model_name, api_client=self.api_client, id=id)
                except Exception as e:
                    print('Error deleting id %s: %s' % (str(id), str(e)))

