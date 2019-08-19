# nanites.client.swagger.GetBasicsByLoginApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basics_by_login_list**](GetBasicsByLoginApi.md#get_basics_by_login_list) | **GET** /get-basics-by-login/ | 


# **get_basics_by_login_list**
> get_basics_by_login_list()



Retrieve basic information by login.  Used in p3 OfficeHoursSignIn.

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
api_instance = nanites.client.swagger.GetBasicsByLoginApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_instance.get_basics_by_login_list()
except ApiException as e:
    print("Exception when calling GetBasicsByLoginApi->get_basics_by_login_list: %s\n" % e)
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

