# coding: utf-8

'''
Test Source
'''


from __future__ import absolute_import

import unittest
import os
from copy import deepcopy
from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from test.client import data, ApiTest

DATABASE_LOGIN_TOTAL = 10202


class TestLoginsApi(ApiTest):

    def test_login_create(self):
        '''Create a login with a person attached using createLogin method
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)

        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

    def test_login_create_no_username(self):
        '''Ensure that login creation fails if there is no username
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        del logindata['username']
        try:
            login = API.createLogin(api_client=self.api_client, **logindata)
            self.assertTrue(False, 'Login created without username')
        except Exception as e:
            self.assertTrue('{"username":["This field is required."]' in str(e), 'Unexpected exception message %s' % str(e))

    @unittest.skipUnless(os.environ.get('ENABLE_LONG_TESTS'), "Must set ENABLE_LONG_TESTS")
    def test_logins_list(self):
        '''Ensure that all logins can be returned by listLogins.  Total depends on what's in the database :)
        '''
        logins = API.listLogins(api_client=self.api_client)
        self.assertTrue(len(logins) == DATABASE_LOGIN_TOTAL, 'Incorrect number of logins %d' % (len(logins)))

    def test_logins_list_by_primary_email(self):
        '''Ensure that a login can be fetched by primary email
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]

        logins = API.listLogins(api_client=self.api_client, primary_email=data.PEOPLE[0]['primary_email'])
        self.assertTrue(len(logins) == 1, 'Incorrect number of logins %d' % len(logins))
        self.assertTrue(logins[0].username == logindata['username'], 'Incorrect login returned %s' % str(logins[0]))

    def test_logins_list_by_username(self):
        '''Ensure that a login can be fetched by username
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]

        logins = API.listLogins(api_client=self.api_client, username=logindata['username'])
        self.assertTrue(len(logins) == 1, 'Incorrect number of logins %d' % len(logins))
        self.assertTrue(logins[0].username == logindata['username'], 'Incorrect login returned %s' % str(logins[0]))

    def test_logins_list_by_ifxid(self):
        '''Ensure that a login can be fetched by ifxid
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]

        logins = API.listLogins(api_client=self.api_client, ifxid=login.person.ifxid)
        self.assertTrue(len(logins) == 1, 'Incorrect number of logins %d' % len(logins))
        self.assertTrue(logins[0].username == logindata['username'], 'Incorrect login returned %s' % str(logins[0]))

    def test_logins_list_non_existent(self):
        '''Ensure listLogins returns an empty list if no match exists
        '''
        logins = API.listLogins(api_client=self.api_client, ifxid='bad value')
        self.assertTrue(len(logins) == 0, 'Incorrect number of logins %d' % len(logins))

    def test_login_update(self):
        '''Ensure that a login can be updated
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)

        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

        login.username = 'newusername'
        logindata = login.to_dict()
        login = API.updateLogin(api_client=self.api_client, **logindata)
        self.assertTrue(login.username == 'newusername', 'Incorrect username %s' % login.username)

    def test_add_login_to_person(self):
        '''Ensure that you can add a login to an existing person
        '''
        persondata = deepcopy(data.PEOPLE[0])
        person = API.createPerson(api_client=self.api_client, **persondata)
        self.IDS['Person'] = [person.id]
        logindata = deepcopy(data.LOGINS[0])
        logindata['ifxid'] = person.ifxid

        login = API.createLogin(**logindata)
        self.assertTrue(login.username == logindata['username'], 'Incorrect login username %s' % login.username)
        self.assertTrue(login.person.full_name == person.full_name, 'Incorrect person %s' % str(login.person))

    def test_read_login(self):
        '''Ensure that a single login can be fetched by id
        '''
        logindata = deepcopy(data.LOGINS[0])
        logindata['person'] = deepcopy(data.PEOPLE[0])
        login = API.createLogin(api_client=self.api_client, **logindata)
        # Should only need to get rid of the person and the login will cascade
        self.IDS['Person'] = [login.person.id]

        fetchedlogin = API.readLogin(api_client=self.api_client, id=login.id)
        self.assertTrue(fetchedlogin.username == login.username, 'Incorrect login returned %s' % str(fetchedlogin))

    def test_failed_read_login(self):
        '''Ensure that readLogin throws an exception for a non-existent value
        '''
        try:
            fetchedlogin = API.readLogin(api_client=self.api_client, id=99999999999)
            self.assertTrue(False, 'Actually fetched a login!')
        except Exception as e:
            self.assertTrue('Item not found' in str(e), 'Incorrect error message: %s' % str(e))


if __name__ == '__main__':
    unittest.main()
