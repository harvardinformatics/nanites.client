# nanites.client.swagger.PeopleApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**people_create**](PeopleApi.md#people_create) | **POST** /people/ | 
[**people_delete**](PeopleApi.md#people_delete) | **DELETE** /people/{id}/ | 
[**people_list**](PeopleApi.md#people_list) | **GET** /people/ | 
[**people_partial_update**](PeopleApi.md#people_partial_update) | **PATCH** /people/{id}/ | 
[**people_read**](PeopleApi.md#people_read) | **GET** /people/{id}/ | 
[**people_update**](PeopleApi.md#people_update) | **PUT** /people/{id}/ | 


# **people_create**
> Person people_create(data)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Person() # Person | 

try:
    api_response = api_instance.people_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Person**](Person.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_delete**
> people_delete(id)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.people_delete(id)
except ApiException as e:
    print("Exception when calling PeopleApi->people_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_list**
> InlineResponse2005 people_list(page=page, page_size=page_size)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.people_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_partial_update**
> Person people_partial_update(id, data)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Person() # Person | 

try:
    api_response = api_instance.people_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Person**](Person.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_read**
> Person people_read(id)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.people_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Person**](Person.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_update**
> Person people_update(id, data)



Viewset for the Person object

### Example
```python
from __future__ import print_function
import time
import nanites.client.swagger
from nanites.client.swagger.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = nanites.client.swagger.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Person() # Person | 

try:
    api_response = api_instance.people_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Person**](Person.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

