# nanites.client.swagger.GetPiNamesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pi_names_list**](GetPiNamesApi.md#get_pi_names_list) | **GET** /get-pi-names/ | 


# **get_pi_names_list**
> get_pi_names_list()



Return PI first name last name for autocomplete list.  Only active user records returned.

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.GetPiNamesApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_instance.get_pi_names_list()
except ApiException as e:
    print("Exception when calling GetPiNamesApi->get_pi_names_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

