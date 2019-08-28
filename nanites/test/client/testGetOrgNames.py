# coding: utf-8

'''
Test getOrgNames
'''

import unittest
import os
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestGetOrgNamesApi(ApiTest):
    '''
    Test for getOrgNames API call
    '''

    def test_get_org_names(self):
        '''
        Ensure that org names are returned in the proper order smallest (lab) to largest (institution)
        '''

        # Sort orgs by rank_order and join into a string
        rank_order = {
            'lab': 0,
            'department': 1,
            'facility': 2,
            'center': 3,
            'program': 4,
            'museum': 5,
            'institute': 6,
            'school': 7,
            'institution': 8,
        }
        ordered_orgs = sorted(data.ORGANIZATIONS, key=lambda org: rank_order[org['rank']])
        validstr = ','.join([org['name'] for org in ordered_orgs if org['rank'] != 'lab'])

        # Get the orgs and join into a string
        org_names = API.getOrgNames(org_tree='Research Computing AD')
        teststr = ','.join(org_names)

        # Stripping the code to make them match
        teststr = teststr.replace(' (MSCW)', '')

        self.assertTrue(teststr == validstr, 'Mismatch between valid (%s) and test (%s' % (validstr, teststr))

    def test_get_org_names_match_code(self):
        '''
        Ensure that org code can be matched
        '''

        # Get the orgs and join into a string
        org_names = API.getOrgNames(org_tree='Research Computing AD', search='MSCW')
        self.assertTrue(','.join(org_names) == 'University of Moscow (MSCW)', 'Incorrect result: %s' % str(org_names))

    def test_get_org_names_set_ranks(self):
        '''
        Ensure that ranks can be set
        '''

        # Get the orgs and join into a string
        org_names = API.getOrgNames(org_tree='Research Computing AD', ranks='Department')
        self.assertTrue(','.join(org_names) == 'Derp', 'Incorrect result: %s' % str(org_names))

    def test_get_org_names_empty(self):
        '''
        Ensure that empty result is an empty list
        '''

        # Get the orgs and join into a string
        org_names = API.getOrgNames(org_tree='Research Computing AD', search='XXXXXXXXX')
        self.assertTrue(len(org_names) == 0, 'Incorrect result: %s' % str(org_names))


if __name__ == '__main__':
    unittest.main()
