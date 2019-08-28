# coding: utf-8

'''
Test getPiNames
'''

import unittest
import os
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestGetPiNamesApi(ApiTest):
    '''
    Test for getPiNames API call
    '''

    def test_get_pi_names(self):
        '''
        Ensure that pi names are returned
        '''

        # Add the PI
        API.createPerson(api_client=self.api_client, **data.PEOPLE[1])

        # Add regular Person
        API.createPerson(api_client=self.api_client, **data.PEOPLE[0])

        pi_names = API.getPiNames()
        self.assertTrue(','.join(pi_names) == 'Slurpy Slurpiston', 'Incorrect PI names returned: %s' % str(pi_names))

    def test_get_pi_names_empty(self):
        '''
        Ensure that empty list is returned for no matches
        '''
        # Add the PI
        API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        pi_names = API.getPiNames(search='XXXXXXXXX')
        self.assertTrue(len(pi_names) == 0, 'Incorrect PI names returned: %s' % str(pi_names))

    def test_get_pi_names_search(self):
        '''
        Ensure that search works
        '''
        # Add the PI
        API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        pi_names = API.getPiNames(search='slurp')
        self.assertTrue(','.join(pi_names) == 'Slurpy Slurpiston', 'Incorrect PI names returned: %s' % str(pi_names))


if __name__ == '__main__':
    unittest.main()
