# nanites.client.swagger.GetLocationInfoApi

All URIs are relative to *http://localhost:8765/nanites/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_info_list**](GetLocationInfoApi.md#get_location_info_list) | **GET** /get-location-info/ | 


# **get_location_info_list**
> GetLocationInfo get_location_info_list(target=target, country=country, state=state, city=city, postal_code=postal_code)



Get location info for addresses. The \"target\" parameter determines the field returned (country, state, city, postal_code) The values for the target can be filtered by other fields.  For example, setting target to city and filtering by state will get you all of the cities in a particular state  A \"location_info\" object is returned. If target was \"state\" and country was \"United States\". {     \"location_info\": [         \"Alabama\",         \"Arkansas\",         ...     ] }  When \"United States\" is in the results (ie a \"country\" target), it is placed at the top of the list.

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
api_instance = nanites.client.swagger.GetLocationInfoApi(nanites.client.swagger.ApiClient(configuration))
target = 'target_example' # str |  (optional)
country = 'country_example' # str |  (optional)
state = 'state_example' # str |  (optional)
city = 'city_example' # str |  (optional)
postal_code = 'postal_code_example' # str |  (optional)

try:
    api_response = api_instance.get_location_info_list(target=target, country=country, state=state, city=city, postal_code=postal_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetLocationInfoApi->get_location_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **city** | **str**|  | [optional] 
 **postal_code** | **str**|  | [optional] 

### Return type

[**GetLocationInfo**](GetLocationInfo.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

