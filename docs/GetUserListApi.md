# nanites.client.swagger.GetUserListApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_list_list**](GetUserListApi.md#get_user_list_list) | **GET** /get-user-list/ | 


# **get_user_list_list**
> list[GetUserList] get_user_list_list(search=search, org_tree=org_tree, offset=offset, limit=limit, order_by=order_by)



Similar to get_basics_by_login, but includes grouped by logins and is_enabled status. Takes a generic 'search' term that is tested against username, full_name, lab name, pi name and department name.  Meant for p3 user listing.

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
api_instance = nanites.client.swagger.GetUserListApi(nanites.client.swagger.ApiClient(configuration))
search = 'search_example' # str |  (optional)
org_tree = 'org_tree_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.get_user_list_list(search=search, org_tree=org_tree, offset=offset, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetUserListApi->get_user_list_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **org_tree** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[GetUserList]**](GetUserList.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

