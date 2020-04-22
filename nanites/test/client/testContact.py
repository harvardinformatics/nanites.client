# coding: utf-8

"""
Test Contact
"""


from __future__ import absolute_import

import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestContactApi(ApiTest):

    def test_list_contact_by_email(self):
        ''' Create a person with a minimal set of information and retrieve the primary email contact
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        self.IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[1]['full_name'], 'Incorrect person name: %s' % str(person))

        contacts = API.listContacts(api_client=self.api_client, email=data.PEOPLE[0]['primary_email'])
        self.assertTrue(len(contacts) == 1, 'Incorrect number of contacts returned')
        self.assertTrue(contacts[0].detail == data.PEOPLE[0]['primary_email'], 'Incorrect data returned %s' % str(contacts[0]))

    def test_list_contact_by_name(self):
        ''' Create a person with a minimal set of information and retrieve the primary email contact by full name
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        self.IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[1]['full_name'], 'Incorrect person name: %s' % str(person))

        contacts = API.listContacts(api_client=self.api_client, name=data.PEOPLE[0]['full_name'])
        self.assertTrue(len(contacts) == 1, 'Incorrect number of contacts returned')
        self.assertTrue(contacts[0].name == data.PEOPLE[0]['full_name'], 'Incorrect data returned %s' % str(contacts[0]))

    def test_list_contact_by_type_detail(self):
        ''' Create a person with a minimal set of information and retrieve the primary email contact by type and detail
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        self.IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[1]['full_name'], 'Incorrect person name: %s' % str(person))

        contacts = API.listContacts(api_client=self.api_client, type='Email', detail=data.PEOPLE[0]['primary_email'])
        self.assertTrue(len(contacts) == 1, 'Incorrect number of contacts returned')
        self.assertTrue(contacts[0].detail == data.PEOPLE[0]['primary_email'], 'Incorrect data returned %s' % str(contacts[0]))
