# nanites.client.swagger.PersonChangesApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**person_changes_create**](PersonChangesApi.md#person_changes_create) | **POST** /person_changes/ | 
[**person_changes_delete**](PersonChangesApi.md#person_changes_delete) | **DELETE** /person_changes/{id}/ | 
[**person_changes_list**](PersonChangesApi.md#person_changes_list) | **GET** /person_changes/ | 
[**person_changes_partial_update**](PersonChangesApi.md#person_changes_partial_update) | **PATCH** /person_changes/{id}/ | 
[**person_changes_read**](PersonChangesApi.md#person_changes_read) | **GET** /person_changes/{id}/ | 
[**person_changes_update**](PersonChangesApi.md#person_changes_update) | **PUT** /person_changes/{id}/ | 


# **person_changes_create**
> PersonChange person_changes_create(data)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.PersonChange() # PersonChange | 

try:
    api_response = api_instance.person_changes_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PersonChange**](PersonChange.md)|  | 

### Return type

[**PersonChange**](PersonChange.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes_delete**
> person_changes_delete(id)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.person_changes_delete(id)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes_list**
> InlineResponse2006 person_changes_list(page=page, page_size=page_size, ifxid=ifxid)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
ifxid = 'ifxid_example' # str |  (optional)

try:
    api_response = api_instance.person_changes_list(page=page, page_size=page_size, ifxid=ifxid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **ifxid** | **str**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes_partial_update**
> PersonChange person_changes_partial_update(id, data)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.PersonChange() # PersonChange | 

try:
    api_response = api_instance.person_changes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**PersonChange**](PersonChange.md)|  | 

### Return type

[**PersonChange**](PersonChange.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes_read**
> PersonChange person_changes_read(id)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.person_changes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PersonChange**](PersonChange.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes_update**
> PersonChange person_changes_update(id, data)



Viewset for PersonChange

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
api_instance = nanites.client.swagger.PersonChangesApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.PersonChange() # PersonChange | 

try:
    api_response = api_instance.person_changes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonChangesApi->person_changes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**PersonChange**](PersonChange.md)|  | 

### Return type

[**PersonChange**](PersonChange.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

