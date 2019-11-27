# nanites.client.swagger.SourcesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sources_create**](SourcesApi.md#sources_create) | **POST** /sources/ | 
[**sources_delete**](SourcesApi.md#sources_delete) | **DELETE** /sources/{name}/ | 
[**sources_list**](SourcesApi.md#sources_list) | **GET** /sources/ | 
[**sources_partial_update**](SourcesApi.md#sources_partial_update) | **PATCH** /sources/{name}/ | 
[**sources_read**](SourcesApi.md#sources_read) | **GET** /sources/{name}/ | 
[**sources_update**](SourcesApi.md#sources_update) | **PUT** /sources/{name}/ | 


# **sources_create**
> Source sources_create(data)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Source() # Source | 

try:
    api_response = api_instance.sources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_delete**
> sources_delete(name)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the data source

try:
    api_instance.sources_delete(name)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the data source | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_list**
> InlineResponse2007 sources_list(page=page, page_size=page_size)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.sources_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_partial_update**
> Source sources_partial_update(name, data)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the data source
data = nanites.client.swagger.Source() # Source | 

try:
    api_response = api_instance.sources_partial_update(name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the data source | 
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_read**
> Source sources_read(name)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the data source

try:
    api_response = api_instance.sources_read(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the data source | 

### Return type

[**Source**](Source.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_update**
> Source sources_update(name, data)



Source ViewSet

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
api_instance = nanites.client.swagger.SourcesApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the data source
data = nanites.client.swagger.Source() # Source | 

try:
    api_response = api_instance.sources_update(name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the data source | 
 **data** | [**Source**](Source.md)|  | 

### Return type

[**Source**](Source.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

