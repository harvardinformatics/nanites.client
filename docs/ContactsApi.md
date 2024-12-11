# nanites.client.swagger.ContactsApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_create**](ContactsApi.md#contacts_create) | **POST** /contacts/ | 
[**contacts_delete**](ContactsApi.md#contacts_delete) | **DELETE** /contacts/{id}/ | 
[**contacts_list**](ContactsApi.md#contacts_list) | **GET** /contacts/ | 
[**contacts_partial_update**](ContactsApi.md#contacts_partial_update) | **PATCH** /contacts/{id}/ | 
[**contacts_read**](ContactsApi.md#contacts_read) | **GET** /contacts/{id}/ | 
[**contacts_update**](ContactsApi.md#contacts_update) | **PUT** /contacts/{id}/ | 


# **contacts_create**
> Contact contacts_create(data)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Contact() # Contact | 

try:
    api_response = api_instance.contacts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_delete**
> contacts_delete(id)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.contacts_delete(id)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_delete: %s\n" % e)
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

# **contacts_list**
> InlineResponse2002 contacts_list(page=page, page_size=page_size, type=type, detail=detail, email=email, name=name, application_key=application_key)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
type = 'type_example' # str | Contact type (e.g. email) (optional)
detail = 'detail_example' # str | Contact detail (e.g dderpiston@gmail.com) (optional)
email = 'email_example' # str | Short cut for searching by email (optional)
name = 'name_example' # str | Search by name (full name for primary contact records) (optional)
application_key = 'application_key_example' # str | Search by application key (optional)

try:
    api_response = api_instance.contacts_list(page=page, page_size=page_size, type=type, detail=detail, email=email, name=name, application_key=application_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | **str**| Contact type (e.g. email) | [optional] 
 **detail** | **str**| Contact detail (e.g dderpiston@gmail.com) | [optional] 
 **email** | **str**| Short cut for searching by email | [optional] 
 **name** | **str**| Search by name (full name for primary contact records) | [optional] 
 **application_key** | **str**| Search by application key | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_partial_update**
> Contact contacts_partial_update(id, data)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Contact() # Contact | 

try:
    api_response = api_instance.contacts_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_read**
> Contact contacts_read(id)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.contacts_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_update**
> Contact contacts_update(id, data)



ViewSet for contact objects

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
api_instance = nanites.client.swagger.ContactsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Contact() # Contact | 

try:
    api_response = api_instance.contacts_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contacts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

