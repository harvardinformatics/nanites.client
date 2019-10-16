# Person

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**ifxid** | **str** | Informatics user identifier.  Globally unique. | [optional] 
**first_name** | **str** | First name.  Can be None, but one of first name or last name should have something. | [optional] 
**last_name** | **str** | Last name.  Can be None, but one of first name or last name should have something. | [optional] 
**full_name** | **str** | Full name.  Usually first and last, but may include middle initial, etc. to ensure uniqueness | 
**primary_email** | **str** | Primary email address.  There may be more. | 
**race** | **str** | One or more race codes or text?? | [optional] 
**ethnicity** | **str** | Ethnicity.  Generally just Hispanic or not. | [optional] 
**gender** | **str** | Gender.  Using controlled-ish vocab. (Male, Female, Non-binary) | [optional] [default to 'Unknown']
**is_disabled** | **bool** |  | [optional] [default to False]
**disability** | **str** | Free text description of disability. | [optional] 
**citizenship** | **str** | Citizenship status (e.g. Permanent Resident) | [optional] 
**visa_details** | **str** | If citizenship is \&quot;Visa\&quot;, this gives further info. | [optional] 
**national_origin** | **str** | If citizenship is \&quot;Visa\&quot;, this is set to home country. | [optional] 
**primary_affiliation** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] [default to True]
**source** | **str** |  | [optional] 
**change_comment** | **str** | Most recent change comment | 
**created** | **datetime** |  | [optional] 
**author** | **str** |  | [optional] 
**addresses** | [**list[PersonAddress]**](PersonAddress.md) |  | [optional] 
**affiliations** | [**list[PersonAffiliation]**](PersonAffiliation.md) |  | [optional] 
**contacts** | [**list[Contact]**](Contact.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


