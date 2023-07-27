# openapi_client.model.bag_ligplaatsen_links.BagLigplaatsenLinks

The contents of the `ligplaatsen._links` field. It contains all relationships with objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The contents of the &#x60;ligplaatsen._links&#x60; field. It contains all relationships with objects. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema** | str,  | str,  |  | 
**heeftDossier** | [**BagdossiersLink**](BagdossiersLink.md) | [**BagdossiersLink**](BagdossiersLink.md) |  | 
**[heeftNevenadres](#heeftNevenadres)** | list, tuple,  | tuple,  |  | 
**ligtInBuurt** | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) |  | 
**heeftHoofdadres** | [**BagNummeraanduidingenLink**](BagNummeraanduidingenLink.md) | [**BagNummeraanduidingenLink**](BagNummeraanduidingenLink.md) |  | 
**self** | [**BagLigplaatsenLink**](BagLigplaatsenLink.md) | [**BagLigplaatsenLink**](BagLigplaatsenLink.md) |  | 
**[heeftOnderzoeken](#heeftOnderzoeken)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# heeftNevenadres

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagligplaatsenHeeftNevenadresM2M**](BagligplaatsenHeeftNevenadresM2M.md) | [**BagligplaatsenHeeftNevenadresM2M**](BagligplaatsenHeeftNevenadresM2M.md) | [**BagligplaatsenHeeftNevenadresM2M**](BagligplaatsenHeeftNevenadresM2M.md) |  | 

# heeftOnderzoeken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagligplaatsenHeeftOnderzoekenM2M**](BagligplaatsenHeeftOnderzoekenM2M.md) | [**BagligplaatsenHeeftOnderzoekenM2M**](BagligplaatsenHeeftOnderzoekenM2M.md) | [**BagligplaatsenHeeftOnderzoekenM2M**](BagligplaatsenHeeftOnderzoekenM2M.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

