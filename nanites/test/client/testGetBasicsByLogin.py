# coding: utf-8

'''
Test getBasicsByLogin
'''


from __future__ import absolute_import

import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


# Maintain ids of created items so we can clean them up later
IDS = {
    "Person": [],
    "Organization": [],
    "Login": [],
}
class TestGetBasicsByLoginApi(ApiTest):

    def test_get_basics_by_login(self):
        '''Create a login with a person attached, PI, lab, and department, then retrieve vi get_basics_by_login
        '''
        # lab and department should be created by base class

        pi = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        self.IDS['Person'] = [pi.id]

        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        self.IDS['Person'] = [login.person.id]
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

        basics = API.getBasicsByLogin(login=login.username)
        self.assertTrue(basics[0].username == login.username, 'Incorrect username: %s' % str(basics))
        self.assertTrue(basics[0].pi_full_name == data.PEOPLE[1]['full_name'], 'Incorrect PI name %s' % str(basics))
        self.assertTrue(basics[0].department_name == 'Derp', 'Incorrect department name %s' % str(basics))


if __name__ == '__main__':
    unittest.main()
