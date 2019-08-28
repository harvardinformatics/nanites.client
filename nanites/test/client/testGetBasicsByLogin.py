# coding: utf-8

'''
Test getBasicsByLogin
'''


from __future__ import absolute_import

import unittest
import os
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestGetBasicsByLoginApi(ApiTest):

    def test_get_basics_by_login(self):
        '''Create a login with a person attached, PI, lab, and department, then retrieve via get_basics_by_login
        '''
        # lab and department should be created by base class

        # Add the PI
        API.createPerson(api_client=self.api_client, **data.PEOPLE[1])

        # Add two logins / users, one with a lab-pi, one without
        i = 0
        logindata = data.LOGINS[i]
        logindata['person'] = data.PEOPLE[i]
        login = API.createLogin(api_client=self.api_client, **logindata)
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

        basics = API.getBasicsByLogin(login=login.username)
        self.assertTrue(len(basics) == 1, 'Incorrect number of results: %s' % str(basics))
        self.assertTrue(basics[0].username == login.username, 'Incorrect username: %s' % str(basics))
        self.assertTrue(basics[0].pi_full_name == data.PEOPLE[1]['full_name'], 'Incorrect PI name %s' % str(basics))
        self.assertTrue(basics[0].department_name == 'Derp', 'Incorrect department name %s' % str(basics))

    def test_get_basics_no_pi(self):
        '''
        Ensure that logins with no PI or department will be returned
        '''
        i = 2
        logindata = data.LOGINS[i]
        logindata['person'] = data.PEOPLE[i]
        login = API.createLogin(api_client=self.api_client, **logindata)
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

        basics = API.getBasicsByLogin(login=login.username)
        self.assertTrue(len(basics) == 1, 'Incorrect number of results: %s' % str(basics))
        self.assertTrue(basics[0].username == login.username, 'Incorrect username: %s' % str(basics))
        self.assertTrue(basics[0].pi_full_name is None, 'Incorrect PI name %s' % str(basics))
        self.assertTrue(basics[0].department_name is None, 'Incorrect department name %s' % str(basics))


if __name__ == '__main__':
    unittest.main()
