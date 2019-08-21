# coding: utf-8

"""
Test Source
"""


from __future__ import absolute_import

import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from test.client import data


DATABASE_PEOPLE_TOTAL = 10
# Maintain ids of created items so we can clean them up later
IDS = {
    "Person": [],
}
class TestPersonApi(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        configuration = Configuration()
        configuration.debug = False
        self.api_client = ApiClient(configuration=configuration)

    def setUp(self):
        self.clean()

    def tearDown(self):
        self.clean()

    def clean(self):
        for model_name, ids in IDS.items():
            for i in range(len(ids)):
                id = IDS[model_name].pop(i)
                try:
                    API.apiFn('delete%s' % model_name, api_client=self.api_client, id=id)
                except Exception as e:
                    print('Error deleting id %s: %s' % (str(id), str(e)))

    def test_create_minimal_person(self):
        ''' Create a person with a minimal set of information
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[0]['full_name'], 'Incorrect person name: %s' % str(person))

    def test_create_full_person(self):
        ''' Create a person with a full set of information including addresses and contacts
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        IDS['Person'] = [person.id]

        for attr in ['full_name', 'gender', 'national_origin', 'citizenship', 'visa_details', 'first_name', 'last_name', 'race']:
            self.assertTrue(getattr(person, attr) == data.PEOPLE[1][attr], 'Incorrect person name: %s' % str(person))

        self.assertTrue(len(person.addresses) == 2, 'Incorrect number of addresses %d' % len(person.addresses))
        self.assertTrue(len(person.contacts) == 3, 'Incorrect number of contacts: %d' % len(person.contacts))
        self.assertTrue(len(person.affiliations) == 1, 'Incorrect number of contacts: %d' % len(person.affiliations))

    @unittest.skipUnless(os.environ.get('ENABLE_LONG_TESTS'), "Must set ENABLE_LONG_TESTs")
    def test_people_list(self):
        '''Ensure that all people can be returned by listPeople.  Total depends on what's in the database :)
        '''
        peoplelist = API.listPeople(api_client=self.api_client)
        self.assertTrue(len(peoplelist) == DATABASE_PEOPLE_TOTAL, 'Incorrect number of people %d' % (len(peoplelist)))

    def test_people_list_by_primary_email(self):
        '''Ensure that a person can be retrieved by primary email from listPeople
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[0]['full_name'], 'Incorrect person name: %s' % str(person))

        peoplelist = API.listPeople(api_client=self.api_client, primary_email=person.primary_email)
        self.assertTrue(len(peoplelist) == 1, 'Incorrect number of people %d' % (len(peoplelist)))
        self.assertTrue(peoplelist[0].full_name == person.full_name, 'Incorrect person returned %s' % str(peoplelist))

    def test_people_list_by_login_username(self):
        '''Ensure that a person can be retrieved by login and username from listPeople
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        # Should only need to get rid of the person and the login will cascade
        IDS['Person'] = [login.person.id]

        peoplelist = API.listPeople(api_client=self.api_client, username=login.username, login=login.application)
        self.assertTrue(len(peoplelist) == 1, 'Incorrect number of people %d' % (len(peoplelist)))
        self.assertTrue(peoplelist[0].full_name == logindata['person']['full_name'], 'Incorrect person returned %s' % str(peoplelist))

    def test_read_person(self):
        '''Ensure that a person can be read by id
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[0]['full_name'], 'Incorrect person name: %s' % str(person))

        fetchedperson = API.readPerson(api_client=self.api_client, id=person.id)
        self.assertTrue(fetchedperson.full_name == person.full_name, 'Incorrect person retrieved: %s' % str(fetchedperson))

    def test_update_person(self):
        '''Ensure that a person can be updated
        '''
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
        IDS['Person'] = [person.id]
        self.assertTrue(person.full_name == data.PEOPLE[0]['full_name'], 'Incorrect person name: %s' % str(person))

        person.full_name = 'A new full name'
        persondata = person.to_dict()
        updatedperson = API.updatePerson(api_client=self.api_client, **persondata)
        self.assertTrue(updatedperson.full_name == person.full_name, 'Incorrect person retrieved: %s' % str(updatedperson))

if __name__ == '__main__':
    unittest.main()
