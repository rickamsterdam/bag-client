# openapi_client.model.bag_woonplaatsen_links.BagWoonplaatsenLinks

The contents of the `woonplaatsen._links` field. It contains all relationships with objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The contents of the &#x60;woonplaatsen._links&#x60; field. It contains all relationships with objects. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema** | str,  | str,  |  | 
**heeftDossier** | [**BagdossiersLink**](BagdossiersLink.md) | [**BagdossiersLink**](BagdossiersLink.md) |  | 
**ligtInGemeente** | [**BrkGemeentesLink**](BrkGemeentesLink.md) | [**BrkGemeentesLink**](BrkGemeentesLink.md) |  | 
**openbareruimtes** | [**RelatedSummary**](RelatedSummary.md) | [**RelatedSummary**](RelatedSummary.md) |  | 
**self** | [**BagWoonplaatsenLink**](BagWoonplaatsenLink.md) | [**BagWoonplaatsenLink**](BagWoonplaatsenLink.md) |  | 
**[heeftOnderzoeken](#heeftOnderzoeken)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# heeftOnderzoeken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagwoonplaatsenHeeftOnderzoekenM2M**](BagwoonplaatsenHeeftOnderzoekenM2M.md) | [**BagwoonplaatsenHeeftOnderzoekenM2M**](BagwoonplaatsenHeeftOnderzoekenM2M.md) | [**BagwoonplaatsenHeeftOnderzoekenM2M**](BagwoonplaatsenHeeftOnderzoekenM2M.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

