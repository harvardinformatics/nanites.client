# nanites.client.swagger.ApplicationsApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_create**](ApplicationsApi.md#applications_create) | **POST** /applications/ | 
[**applications_delete**](ApplicationsApi.md#applications_delete) | **DELETE** /applications/{name}/ | 
[**applications_list**](ApplicationsApi.md#applications_list) | **GET** /applications/ | 
[**applications_partial_update**](ApplicationsApi.md#applications_partial_update) | **PATCH** /applications/{name}/ | 
[**applications_read**](ApplicationsApi.md#applications_read) | **GET** /applications/{name}/ | 
[**applications_update**](ApplicationsApi.md#applications_update) | **PUT** /applications/{name}/ | 


# **applications_create**
> Application applications_create(data)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Application() # Application | 

try:
    api_response = api_instance.applications_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Application**](Application.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_delete**
> applications_delete(name)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the application

try:
    api_instance.applications_delete(name)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the application | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_list**
> InlineResponse2001 applications_list(page=page, page_size=page_size)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.applications_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_partial_update**
> Application applications_partial_update(name, data)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the application
data = nanites.client.swagger.Application() # Application | 

try:
    api_response = api_instance.applications_partial_update(name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the application | 
 **data** | [**Application**](Application.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_read**
> Application applications_read(name)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the application

try:
    api_response = api_instance.applications_read(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the application | 

### Return type

[**Application**](Application.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_update**
> Application applications_update(name, data)



Application ViewSet

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
api_instance = nanites.client.swagger.ApplicationsApi(nanites.client.swagger.ApiClient(configuration))
name = 'name_example' # str | Name of the application
data = nanites.client.swagger.Application() # Application | 

try:
    api_response = api_instance.applications_update(name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the application | 
 **data** | [**Application**](Application.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

