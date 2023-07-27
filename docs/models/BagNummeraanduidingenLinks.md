# openapi_client.model.bag_nummeraanduidingen_links.BagNummeraanduidingenLinks

The contents of the `nummeraanduidingen._links` field. It contains all relationships with objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The contents of the &#x60;nummeraanduidingen._links&#x60; field. It contains all relationships with objects. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema** | str,  | str,  |  | 
**heeftDossier** | [**BagdossiersLink**](BagdossiersLink.md) | [**BagdossiersLink**](BagdossiersLink.md) |  | 
**ligtAanOpenbareruimte** | [**BagOpenbareruimtesLink**](BagOpenbareruimtesLink.md) | [**BagOpenbareruimtesLink**](BagOpenbareruimtesLink.md) |  | 
**adresseertVerblijfsobject** | [**BagVerblijfsobjectenLink**](BagVerblijfsobjectenLink.md) | [**BagVerblijfsobjectenLink**](BagVerblijfsobjectenLink.md) |  | 
**self** | [**BagNummeraanduidingenLink**](BagNummeraanduidingenLink.md) | [**BagNummeraanduidingenLink**](BagNummeraanduidingenLink.md) |  | 
**adresseertStandplaats** | [**BagStandplaatsenLink**](BagStandplaatsenLink.md) | [**BagStandplaatsenLink**](BagStandplaatsenLink.md) |  | 
**[heeftOnderzoeken](#heeftOnderzoeken)** | list, tuple,  | tuple,  |  | 
**ligtInWoonplaats** | [**BagWoonplaatsenLink**](BagWoonplaatsenLink.md) | [**BagWoonplaatsenLink**](BagWoonplaatsenLink.md) |  | 
**adresseertLigplaats** | [**BagLigplaatsenLink**](BagLigplaatsenLink.md) | [**BagLigplaatsenLink**](BagLigplaatsenLink.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# heeftOnderzoeken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagnummeraanduidingenHeeftOnderzoekenM2M**](BagnummeraanduidingenHeeftOnderzoekenM2M.md) | [**BagnummeraanduidingenHeeftOnderzoekenM2M**](BagnummeraanduidingenHeeftOnderzoekenM2M.md) | [**BagnummeraanduidingenHeeftOnderzoekenM2M**](BagnummeraanduidingenHeeftOnderzoekenM2M.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

