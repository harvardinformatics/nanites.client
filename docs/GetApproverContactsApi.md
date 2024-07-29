# nanites.client.swagger.GetApproverContactsApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_approver_contacts_list**](GetApproverContactsApi.md#get_approver_contacts_list) | **GET** /get-approver-contacts/ | 


# **get_approver_contacts_list**
> list[GetApproverContacts] get_approver_contacts_list()



Given one or more organization slugs, return a list of possible approvers and their email addresses. If role_filters are provided, only return approvers with those roles, otherwise PI and Lab Manager are used.

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
api_instance = nanites.client.swagger.GetApproverContactsApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_response = api_instance.get_approver_contacts_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApproverContactsApi->get_approver_contacts_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetApproverContacts]**](GetApproverContacts.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

