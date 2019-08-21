# coding: utf-8

'''
Test Source
'''


from __future__ import absolute_import

import unittest

from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from test.client import data


# Maintain ids of created items so we can clean them up later
IDS = {
    "Person": [],
    "Organization": [],
    "Login": [],
}
class TestLoginsApi(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        configuration = Configuration()
        configuration.debug = True
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


    def test_login_create(self):
        '''Create a login with a person attached using createLogin method
        '''
        logindata = data.LOGINS[0]
        logindata['person'] = data.PEOPLE[0]
        login = API.createLogin(api_client=self.api_client, **logindata)

        # Should only need to get rid of the person and the login will cascade
        IDS['Person'] = [login.person.id]
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

    def test_logins_list(self):
        '''Ensure that all logins can be returned by listLogins.  Total depends on what's in the database :)
        '''
        logins = API.listLogins(api_client=self.api_client)
        self.assertTrue(len(logins) == 100, 'Incorrect number of logins %d' % (len(logins)))

    def test_login_update(self):
        '''Ensure that a login can be updated
        '''
        logindata = data.LOGINS[0]
        logindata['person'] = data.PEOPLE[0]
        login = API.createLogin(api_client=self.api_client, **logindata)

        # Should only need to get rid of the person and the login will cascade
        IDS['Person'] = [login.person.id]
        self.assertTrue(login.username == logindata['username'], 'Incorrect username %s' % login.username)

        login.username = 'newusername'
        logindata = login.to_dict()
        login = API.updateLogin(api_client=self.api_client, **logindata)
        self.assertTrue(login.username == 'newusername', 'Incorrect username %s' % login.username)

    # def test_add_login_to_person(self):
    #     '''Ensure that you can add a login to an existing person
    #     '''
    #     person = API.createPerson(api_client=self.api_client, **data.PEOPLE[0])
    #     IDS['Person'] = [person.id]
    #     logindata = data.LOGINS[0]
    #     logindata['ifxid'] = person.ifxid

    #     # Double check
    #     newperson = API.readPerson(id=person.id)
    #     self.assertTrue(newperson.ifxid == person.ifxid)

    #     # login = API.createLogin(**logindata)
    #     # self.assertTrue(login.username == logindata['username'], 'Incorrect login username %s' % login.username)
    #     # self.assertTrue(login.person.full_name == person.full_name, 'Incorrect person %s' % str(login.person))

    # def test_sources_update_fail(self):
    #     '''Ensure that a source update will fail without a 'name'
    #     '''
    #     source = API.createSource(api_client=self.api_client, **SOURCES[0])
    #     self.assertTrue(source.name == SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
    #     updated_description = 'Updated description'
    #     try:
    #         source = API.updateSource(api_client=self.api_client, description=updated_description)
    #         self.assertTrue(False, 'Successfully updated without a name parameter')
    #     except Exception as e:
    #         self.assertTrue('Source update requires a name' in str(e), 'Incorrect error message %s' % str(e))

if __name__ == '__main__':
    unittest.main()
