# coding: utf-8

'''
Test getOrgList
'''

import unittest
import os
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestGetOrgListApi(ApiTest):
    '''
    Test for getOrgList API call
    '''

    def testGetOrgList(self):
        '''
        Ensure that all orgs are returned when member, member_role are not specified
        '''
        # Get the orgs
        orgs = API.getOrgList(org_tree='Research Computing AD')
        self.assertTrue(len(orgs) == len(data.ORGANIZATIONS), f'Incorrect number of orgs returned {len(orgs)}')

    def testGetOrgListMember(self):
        '''
        Ensure that correct org is returned when member is specified
        '''
        # Get the ifxid
        person = API.createPerson(**data.PEOPLE[1])

        # Get the orgs
        orgs = API.getOrgList(org_tree='Research Computing AD', member=person.ifxid, member_role='pi')
        self.assertTrue(len(orgs) == 1, f'Incorrect number of orgs returned {len(orgs)}')
        self.assertTrue(orgs[0].name in person.primary_affiliation, f'Incorrect org {orgs[0]}')
