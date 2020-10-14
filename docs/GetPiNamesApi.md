# nanites.client.swagger.GetPiNamesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pi_names_list**](GetPiNamesApi.md#get_pi_names_list) | **GET** /get-pi-names/ | 


# **get_pi_names_list**
> list[GetPiNames] get_pi_names_list(search=search)



Return PI first name last name for autocomplete list.  Only active user records returned.

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
api_instance = nanites.client.swagger.GetPiNamesApi(nanites.client.swagger.ApiClient(configuration))
search = 'search_example' # str |  (optional)

try:
    api_response = api_instance.get_pi_names_list(search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPiNamesApi->get_pi_names_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**list[GetPiNames]**](GetPiNames.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

