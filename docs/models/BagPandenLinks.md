# openapi_client.model.bag_panden_links.BagPandenLinks

The contents of the `panden._links` field. It contains all relationships with objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The contents of the &#x60;panden._links&#x60; field. It contains all relationships with objects. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema** | str,  | str,  |  | 
**ligtInBouwblok** | [**GebiedenBouwblokkenLink**](GebiedenBouwblokkenLink.md) | [**GebiedenBouwblokkenLink**](GebiedenBouwblokkenLink.md) |  | 
**heeftDossier** | [**BagdossiersLink**](BagdossiersLink.md) | [**BagdossiersLink**](BagdossiersLink.md) |  | 
**ligtInBuurt** | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) |  | 
**self** | [**BagPandenLink**](BagPandenLink.md) | [**BagPandenLink**](BagPandenLink.md) |  | 
**[bevatVerblijfsobjecten](#bevatVerblijfsobjecten)** | list, tuple,  | tuple,  |  | 
**[heeftOnderzoeken](#heeftOnderzoeken)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bevatVerblijfsobjecten

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagVerblijfsobjectenLink**](BagVerblijfsobjectenLink.md) | [**BagVerblijfsobjectenLink**](BagVerblijfsobjectenLink.md) | [**BagVerblijfsobjectenLink**](BagVerblijfsobjectenLink.md) |  | 

# heeftOnderzoeken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagpandenHeeftOnderzoekenM2M**](BagpandenHeeftOnderzoekenM2M.md) | [**BagpandenHeeftOnderzoekenM2M**](BagpandenHeeftOnderzoekenM2M.md) | [**BagpandenHeeftOnderzoekenM2M**](BagpandenHeeftOnderzoekenM2M.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

