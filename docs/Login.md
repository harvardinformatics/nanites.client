# Login

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**ifxid** | **str** |  | [optional] 
**application** | **str** |  | 
**application_key** | **str** | Alternate key for the application login (e.g. objectSid). | [optional] 
**username** | **str** | Identity required for this login. | 
**role** | **str** | Role in the application (e.g. superuser) | [optional] [default to 'user']
**is_enabled** | **bool** |  | [optional] [default to True]
**created** | **datetime** |  | [optional] 
**author** | **str** |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**contacts** | **list[int]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


