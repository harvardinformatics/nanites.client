# nanites.client.swagger.AddressesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addresses_create**](AddressesApi.md#addresses_create) | **POST** /addresses/ | 
[**addresses_delete**](AddressesApi.md#addresses_delete) | **DELETE** /addresses/{id}/ | 
[**addresses_list**](AddressesApi.md#addresses_list) | **GET** /addresses/ | 
[**addresses_partial_update**](AddressesApi.md#addresses_partial_update) | **PATCH** /addresses/{id}/ | 
[**addresses_read**](AddressesApi.md#addresses_read) | **GET** /addresses/{id}/ | 
[**addresses_update**](AddressesApi.md#addresses_update) | **PUT** /addresses/{id}/ | 


# **addresses_create**
> Address addresses_create(data)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Address() # Address | 

try:
    api_response = api_instance.addresses_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_delete**
> addresses_delete(id)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this address.

try:
    api_instance.addresses_delete(id)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this address. | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_list**
> InlineResponse200 addresses_list(page=page, page_size=page_size)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.addresses_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_partial_update**
> Address addresses_partial_update(id, data)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this address.
data = nanites.client.swagger.Address() # Address | 

try:
    api_response = api_instance.addresses_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this address. | 
 **data** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_read**
> Address addresses_read(id)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this address.

try:
    api_response = api_instance.addresses_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this address. | 

### Return type

[**Address**](Address.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addresses_update**
> Address addresses_update(id, data)



Viewset for Addresses

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
api_instance = nanites.client.swagger.AddressesApi(nanites.client.swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this address.
data = nanites.client.swagger.Address() # Address | 

try:
    api_response = api_instance.addresses_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->addresses_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this address. | 
 **data** | [**Address**](Address.md)|  | 

### Return type

[**Address**](Address.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

