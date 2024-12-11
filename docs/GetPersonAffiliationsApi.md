# nanites.client.swagger.GetPersonAffiliationsApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_person_affiliations_list**](GetPersonAffiliationsApi.md#get_person_affiliations_list) | **GET** /get-person-affiliations/ | 


# **get_person_affiliations_list**
> list[GetPersonAffiliations] get_person_affiliations_list(ifxid=ifxid, org_tree=org_tree, ifxorg=ifxorg)



Return a row for each PersonAffiliation record including the Person's full name and ifxid as well as the ifxorg and the organization slug. Used in org synchronization

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
api_instance = nanites.client.swagger.GetPersonAffiliationsApi(nanites.client.swagger.ApiClient(configuration))
ifxid = 'ifxid_example' # str |  (optional)
org_tree = 'org_tree_example' # str |  (optional)
ifxorg = 'ifxorg_example' # str |  (optional)

try:
    api_response = api_instance.get_person_affiliations_list(ifxid=ifxid, org_tree=org_tree, ifxorg=ifxorg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPersonAffiliationsApi->get_person_affiliations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifxid** | **str**|  | [optional] 
 **org_tree** | **str**|  | [optional] 
 **ifxorg** | **str**|  | [optional] 

### Return type

[**list[GetPersonAffiliations]**](GetPersonAffiliations.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

