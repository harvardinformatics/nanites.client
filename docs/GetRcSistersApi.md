# nanites.client.swagger.GetRcSistersApi

All URIs are relative to *https://nanites.rc.fas.harvard.edu/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rc_sisters_list**](GetRcSistersApi.md#get_rc_sisters_list) | **GET** /get-rc-sisters/ | 


# **get_rc_sisters_list**
> list[GetRcSisters] get_rc_sisters_list()



Return RC organization \"codes\" mapped to Harvard org tree organization ifxorgs. Used in coldfront to make sure \"projects\" are mapped to Harvard orgs

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = nanites.client.swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = nanites.client.swagger.GetRcSistersApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_response = api_instance.get_rc_sisters_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetRcSistersApi->get_rc_sisters_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetRcSisters]**](GetRcSisters.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

