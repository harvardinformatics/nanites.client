# coding: utf-8

"""
Test Source
"""


from __future__ import absolute_import

import unittest

from nanites.client.swagger import ApiClient, Configuration
from nanites import client


SOURCES = {
    'good': {
        'name': 'test source',
        'description': 'test source description'
    }
}
class TestSourcesApi(unittest.TestCase):
    """SourcesApi unit test stubs"""

    def setUp(self):
        configuration = Configuration()
        configuration.debug = True
        self.api_client = ApiClient(configuration=configuration)


    def tearDown(self):
        pass

    def test_sources_create(self):
        """Test case for sources_create

        """
        source = client.createSource(api_client=self.api_client, **SOURCES['good'])
        self.assertTrue(source.name == SOURCES['good']['name'], 'Incorrect source name: %s' % str(source))

    def test_sources_delete(self):
        """Test case for sources_delete

        """
        pass

    def test_sources_list(self):
        """Test case for sources_list

        """
        pass

    def test_sources_partial_update(self):
        """Test case for sources_partial_update

        """
        pass

    def test_sources_read(self):
        """Test case for sources_read

        """
        pass

    def test_sources_update(self):
        """Test case for sources_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
