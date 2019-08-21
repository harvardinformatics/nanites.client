# coding: utf-8

"""
Test the Address API
"""


from __future__ import absolute_import

import unittest

from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API


ADDRESSES = [
    {
        'name': 'test source',
        'description': 'test source description'
    },
    {
        'name': 'test2',
        'description': 'another test'
    }
]
class TestAddressesApi(unittest.TestCase):

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
        for address in ADDRESSES:
            try:
                API.deleteAddress(api_client=self.api_client, name=address['name'])
            except Exception as e:
                pass


    # def test_sources_create(self):
    #     """Test case for sources_create

    #     """
    #     source = API.createSource(api_client=self.api_client, **SOURCES[0])
    #     self.assertTrue(source.name == SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))

    # def test_sources_delete(self):
    #     """Ensure that deleteSource works
    #     """
    #     source = API.createSource(api_client=self.api_client, **SOURCES[0])
    #     self.assertTrue(source.name == SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
    #     API.deleteSource(api_client=self.api_client, name=SOURCES[0]['name'])
    #     try:
    #         source = API.readSource(api_client=self.api_client, name=SOURCES[0]['name'])
    #     except Exception as e:
    #         self.assertTrue('Item not found' in str(e), 'Incorrect exception %s' % str(e))

    # def test_sources_list(self):
    #     """Ensure that all sources can be returned by listSources.  Total depends on what's in the database :)
    #     """
    #     sources = API.listSources(api_client=self.api_client)
    #     self.assertTrue(len(sources) == 7, 'Incorrect number of sources %d: %s' % (len(sources), str(sources)))

    # def test_sources_update(self):
    #     """Ensure that a source can be updated
    #     """
    #     source = API.createSource(api_client=self.api_client, **SOURCES[0])
    #     self.assertTrue(source.name == SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
    #     updated_description = 'Updated description'
    #     source = API.updateSource(api_client=self.api_client, name=SOURCES[0]['name'], description=updated_description)
    #     self.assertTrue(source.description == updated_description, 'Incorrect description upon update %s' % source.description)

    # def test_sources_update_fail(self):
    #     """Ensure that a source update will fail without a 'name'
    #     """
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
