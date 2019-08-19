# nanites.client.swagger.GetOrgNamesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_names_list**](GetOrgNamesApi.md#get_org_names_list) | **GET** /get-org-names/ | 


# **get_org_names_list**
> get_org_names_list()



Return org names for autocomplete list.  Department names are followed by Schools, Museums, Institutes, and Centers

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
api_instance = nanites.client.swagger.GetOrgNamesApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_instance.get_org_names_list()
except ApiException as e:
    print("Exception when calling GetOrgNamesApi->get_org_names_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

