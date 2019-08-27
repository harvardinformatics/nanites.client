# coding: utf-8

"""
Test Source
"""


from nanites.client.swagger import ApiClient, Configuration
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestSourcesApi(ApiTest):
    """SourcesApi unit test stubs"""



    def test_sources_delete(self):
        """Ensure that deleteSource works
        """

        # Create it if necessary, but it should already be there
        try:
            source = API.createSource(api_client=self.api_client, **data.SOURCES[0])
            self.assertTrue(source.name == data.SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
        except Exception:
            pass

        API.deleteSource(api_client=self.api_client, name=data.SOURCES[0]['name'])
        try:
            source = API.readSource(api_client=self.api_client, name=data.SOURCES[0]['name'])
        except Exception as e:
            self.assertTrue('Item not found' in str(e), 'Incorrect exception %s' % str(e))

    def test_sources_list(self):
        """Ensure that all sources can be returned by listSources.  Total depends on what's in the database :)
        """
        sources = API.listSources(api_client=self.api_client)
        self.assertTrue(len(sources) == 2, 'Incorrect number of sources %d: %s' % (len(sources), str(sources)))

    def test_sources_update(self):
        """Ensure that a source can be updated
        """
        source = API.readSource(api_client=self.api_client, name=data.SOURCES[0]['name'])
        self.assertTrue(source.name == data.SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
        updated_description = 'Updated description'
        source = API.updateSource(api_client=self.api_client, name=data.SOURCES[0]['name'], description=updated_description)
        self.assertTrue(source.description == updated_description, 'Incorrect description upon update %s' % source.description)

    def test_sources_update_fail(self):
        """Ensure that a source update will fail without a 'name'
        """
        source = API.readSource(api_client=self.api_client, name=data.SOURCES[0]['name'])
        self.assertTrue(source.name == data.SOURCES[0]['name'], 'Incorrect source name: %s' % str(source))
        updated_description = 'Updated description'
        try:
            source = API.updateSource(api_client=self.api_client, description=updated_description)
            self.assertTrue(False, 'Successfully updated without a name parameter')
        except Exception as e:
            self.assertTrue('Source update requires a name' in str(e), 'Incorrect error message %s' % str(e))

if __name__ == '__main__':
    unittest.main()
