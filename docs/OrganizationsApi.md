# nanites.client.swagger.OrganizationsApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_create**](OrganizationsApi.md#organizations_create) | **POST** /organizations/ | 
[**organizations_delete**](OrganizationsApi.md#organizations_delete) | **DELETE** /organizations/{id}/ | 
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /organizations/ | 
[**organizations_partial_update**](OrganizationsApi.md#organizations_partial_update) | **PATCH** /organizations/{id}/ | 
[**organizations_read**](OrganizationsApi.md#organizations_read) | **GET** /organizations/{id}/ | 
[**organizations_update**](OrganizationsApi.md#organizations_update) | **PUT** /organizations/{id}/ | 


# **organizations_create**
> Organization organizations_create(data)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
data = nanites.client.swagger.Organization() # Organization | 

try:
    api_response = api_instance.organizations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Organization**](Organization.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_delete**
> organizations_delete(id)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.organizations_delete(id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_delete: %s\n" % e)
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

# **organizations_list**
> InlineResponse2004 organizations_list(page=page, page_size=page_size, org_tree=org_tree, rank=rank, name=name)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
org_tree = 'org_tree_example' # str | Organization tree (e.g. Research Computing AD) (optional)
rank = 'rank_example' # str | Organization unit rank (e.g. Department) (optional)
name = 'name_example' # str | Organization name (e.g. Informatics) (optional)

try:
    api_response = api_instance.organizations_list(page=page, page_size=page_size, org_tree=org_tree, rank=rank, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **org_tree** | **str**| Organization tree (e.g. Research Computing AD) | [optional] 
 **rank** | **str**| Organization unit rank (e.g. Department) | [optional] 
 **name** | **str**| Organization name (e.g. Informatics) | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_partial_update**
> Organization organizations_partial_update(id, data)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Organization() # Organization | 

try:
    api_response = api_instance.organizations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Organization**](Organization.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_read**
> Organization organizations_read(id)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.organizations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> Organization organizations_update(id, data)



Organization ViewSet

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
api_instance = nanites.client.swagger.OrganizationsApi(nanites.client.swagger.ApiClient(configuration))
id = 'id_example' # str | 
data = nanites.client.swagger.Organization() # Organization | 

try:
    api_response = api_instance.organizations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Organization**](Organization.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

