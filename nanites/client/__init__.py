# coding: utf-8

"""
    Nanites Client

    This code provides a layer of insulation between the Swagger generated code
    and a client.  Returns swagger models.

    Contact: ifx@fas.harvard.edu
"""

from nanites.client.swagger import api as swaggerApi
from nanites.client.swagger import models as swaggerModels


def createSource(**kwargs):
    '''
    Create a source
    '''
    api_client = kwargs.pop('api_client', None)
    data = {}
    for key in swaggerModels.Source.attribute_map.keys():
        if key != 'id' and key in kwargs:
            data[key] = kwargs.pop(key)

    api = swaggerApi.SourcesApi(api_client=api_client)
    source = api.sources_create(data, **kwargs)
    return source

def deleteSource(**kwargs):
    '''
    Remove a source
    '''
    pass