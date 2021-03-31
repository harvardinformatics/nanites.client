# nanites.client.swagger.GetOrgListApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_list_list**](GetOrgListApi.md#get_org_list_list) | **GET** /get-org-list/ | 


# **get_org_list_list**
> list[GetOrgList] get_org_list_list(member=member, member_role=member_role, org_tree=org_tree)



Return list of names and member counts for organizations. May be filtered by ifxid and role

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
api_instance = nanites.client.swagger.GetOrgListApi(nanites.client.swagger.ApiClient(configuration))
member = 'member_example' # str |  (optional)
member_role = 'member_role_example' # str |  (optional)
org_tree = 'org_tree_example' # str |  (optional)

try:
    api_response = api_instance.get_org_list_list(member=member, member_role=member_role, org_tree=org_tree)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetOrgListApi->get_org_list_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member** | **str**|  | [optional] 
 **member_role** | **str**|  | [optional] 
 **org_tree** | **str**|  | [optional] 

### Return type

[**list[GetOrgList]**](GetOrgList.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

