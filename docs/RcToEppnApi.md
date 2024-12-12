# nanites.client.swagger.RcToEppnApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rc_to_eppn_list**](RcToEppnApi.md#rc_to_eppn_list) | **GET** /rc-to-eppn/ | 


# **rc_to_eppn_list**
> rc_to_eppn_list()



Return all of the RC logins mapped to Harvard Key eppns.

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
api_instance = nanites.client.swagger.RcToEppnApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_instance.rc_to_eppn_list()
except ApiException as e:
    print("Exception when calling RcToEppnApi->rc_to_eppn_list: %s\n" % e)
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

