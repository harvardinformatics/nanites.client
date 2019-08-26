# nanites.client.swagger.GetBasicsByLoginApi

All URIs are relative to *https://nanites.rc.fas.harvard.edu/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basics_by_login_list**](GetBasicsByLoginApi.md#get_basics_by_login_list) | **GET** /get-basics-by-login/ | 


# **get_basics_by_login_list**
> get_basics_by_login_list(login=login)



Retrieve basic information by login.  Used in p3 OfficeHoursSignIn.

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
api_instance = nanites.client.swagger.GetBasicsByLoginApi(nanites.client.swagger.ApiClient(configuration))
login = 'login_example' # str |  (optional)

try:
    api_instance.get_basics_by_login_list(login=login)
except ApiException as e:
    print("Exception when calling GetBasicsByLoginApi->get_basics_by_login_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

