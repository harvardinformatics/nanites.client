# nanites.client.swagger.LoginsApi

All URIs are relative to *https://nanites.rc.fas.harvard.edu/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logins_create**](LoginsApi.md#logins_create) | **POST** /logins/ | 
[**logins_delete**](LoginsApi.md#logins_delete) | **DELETE** /logins/{id}/ | 
[**logins_list**](LoginsApi.md#logins_list) | **GET** /logins/ | 
[**logins_partial_update**](LoginsApi.md#logins_partial_update) | **PATCH** /logins/{id}/ | 
[**logins_read**](LoginsApi.md#logins_read) | **GET** /logins/{id}/ | 
[**logins_update**](LoginsApi.md#logins_update) | **PUT** /logins/{id}/ | 


# **logins_create**
> Login logins_create(data)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Login() # Login | 

try:
    api_response = api_instance.logins_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Login**](Login.md)|  | 

### Return type

[**Login**](Login.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logins_delete**
> logins_delete(id)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.logins_delete(id)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_delete: %s\n" % e)
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

# **logins_list**
> InlineResponse2003 logins_list(ordering=ordering, page=page, page_size=page_size, login=login, username=username, ifxid=ifxid, primary_email=primary_email)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
login = 'login_example' # str |  (optional)
username = 'username_example' # str |  (optional)
ifxid = 'ifxid_example' # str |  (optional)
primary_email = 'primary_email_example' # str |  (optional)

try:
    api_response = api_instance.logins_list(ordering=ordering, page=page, page_size=page_size, login=login, username=username, ifxid=ifxid, primary_email=primary_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **login** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **ifxid** | **str**|  | [optional] 
 **primary_email** | **str**|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logins_partial_update**
> Login logins_partial_update(id, data)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Login() # Login | 

try:
    api_response = api_instance.logins_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Login**](Login.md)|  | 

### Return type

[**Login**](Login.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logins_read**
> Login logins_read(id)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.logins_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Login**](Login.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logins_update**
> Login logins_update(id, data)



Viewset for Logins

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
api_instance = nanites.client.swagger.LoginsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Login() # Login | 

try:
    api_response = api_instance.logins_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginsApi->logins_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Login**](Login.md)|  | 

### Return type

[**Login**](Login.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

