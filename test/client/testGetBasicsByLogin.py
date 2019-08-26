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
from test.client import data


# Maintain ids of created items so we can clean them up later
IDS = {
    "Person": [],
    "Organization": [],
    "Login": [],
}
class TestGetBasicsByLoginApi(unittest.TestCase):

    def test_get_basics_by_login(self):
        '''Create a login with a person attached using createLogin method
        '''
        pass


if __name__ == '__main__':
    unittest.main()
