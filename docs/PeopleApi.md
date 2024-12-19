# nanites.client.swagger.PeopleApi

All URIs are relative to *https://nanites.rc.fas.harvard.edu/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**people_create**](PeopleApi.md#people_create) | **POST** /people/ | 
[**people_delete**](PeopleApi.md#people_delete) | **DELETE** /people/{ifxid}/ | 
[**people_list**](PeopleApi.md#people_list) | **GET** /people/ | 
[**people_partial_update**](PeopleApi.md#people_partial_update) | **PATCH** /people/{ifxid}/ | 
[**people_read**](PeopleApi.md#people_read) | **GET** /people/{ifxid}/ | 
[**people_update**](PeopleApi.md#people_update) | **PUT** /people/{ifxid}/ | 


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

# Configure API key authorization: token
configuration = nanites.client.swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

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

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_delete**
> people_delete(ifxid)



Viewset for the Person object

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
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
ifxid = 'ifxid_example' # str | 

try:
    api_instance.people_delete(ifxid)
except ApiException as e:
    print("Exception when calling PeopleApi->people_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifxid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_list**
> InlineResponse2005 people_list(ordering=ordering, page=page, page_size=page_size, login=login, username=username, primary_email=primary_email, full_name=full_name, email=email)



Viewset for the Person object

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
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
login = 'login_example' # str |  (optional)
username = 'username_example' # str |  (optional)
primary_email = 'primary_email_example' # str |  (optional)
full_name = 'full_name_example' # str |  (optional)
email = 'email_example' # str |  (optional)

try:
    api_response = api_instance.people_list(ordering=ordering, page=page, page_size=page_size, login=login, username=username, primary_email=primary_email, full_name=full_name, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **login** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **primary_email** | **str**|  | [optional] 
 **full_name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_partial_update**
> Person people_partial_update(ifxid, data)



Viewset for the Person object

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
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
ifxid = 'ifxid_example' # str | 
data = nanites.client.swagger.Person() # Person | 

try:
    api_response = api_instance.people_partial_update(ifxid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifxid** | **str**|  | 
 **data** | [**Person**](Person.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_read**
> Person people_read(ifxid)



Viewset for the Person object

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
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
ifxid = 'ifxid_example' # str | 

try:
    api_response = api_instance.people_read(ifxid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifxid** | **str**|  | 

### Return type

[**Person**](Person.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_update**
> Person people_update(ifxid, data)



Viewset for the Person object

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
api_instance = nanites.client.swagger.PeopleApi(nanites.client.swagger.ApiClient(configuration))
ifxid = 'ifxid_example' # str | 
data = nanites.client.swagger.Person() # Person | 

try:
    api_response = api_instance.people_update(ifxid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifxid** | **str**|  | 
 **data** | [**Person**](Person.md)|  | 

### Return type

[**Person**](Person.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

