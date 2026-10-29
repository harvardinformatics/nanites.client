# nanites.client.swagger.RedirectUriApi

All URIs are relative to *https://nanites.rc.fas.harvard.edu/nanites*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redirect_uri_list**](RedirectUriApi.md#redirect_uri_list) | **GET** /redirect-uri/ | 


# **redirect_uri_list**
> redirect_uri_list()



Redirect to the BauerCat home page

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
api_instance = nanites.client.swagger.RedirectUriApi(nanites.client.swagger.ApiClient(configuration))

try:
    api_instance.redirect_uri_list()
except ApiException as e:
    print("Exception when calling RedirectUriApi->redirect_uri_list: %s\n" % e)
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

