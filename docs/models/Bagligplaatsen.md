# openapi_client.model.bagligplaatsen.Bagligplaatsen

ligplaatsen

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ligplaatsen | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[gebruiksdoel](#gebruiksdoel)** | list, tuple,  | tuple,  |  | 
**identificatie** | str,  | str,  | Landelijke identificerende sleutel. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**heeftDossierId** | None, str,  | NoneClass, str,  | Het dossier op basis waarvan het object is toegevoegd aan de registratie. | 
**ligtInBuurtId** | None, str,  | NoneClass, str,  | De buurt waarin een ligplaats ligt. | 
**heeftHoofdadresId** | None, str,  | NoneClass, str,  | Het HOOFDadres dat de ligplaats heeft. | 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**geconstateerd** | None, bool,  | NoneClass, BoolClass,  | Dit geeft aan dat een LIGPLAATS in de registratie is opgenomen als gevolg van een feitelijke constatering en niet op basis van een regulier brondocument. | [optional] 
**statusCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De fase van de levenscyclus van een ligplaats, waarin de betreffende ligplaats zich bevindt, Plaats aangewezen, plaats ingetrokken. code | [optional] value must be a 64 bit integer
**statusOmschrijving** | None, str,  | NoneClass, str,  | De fase van de levenscyclus van een ligplaats, waarin de betreffende ligplaats zich bevindt, Plaats aangewezen, plaats ingetrokken. omschrijving | [optional] 
**geometrie** | [**Geometry**](Geometry.md) | [**Geometry**](Geometry.md) |  | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De begindatum van een periode waarin een of meer gegevens die worden bijgehouden over een ligplaats een wijziging hebben ondergaan. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De einddatum van een periode waarin een of meer gegevens die worden bijgehouden over een ligplaats een wijziging hebben ondergaan. | [optional] value must conform to RFC-3339 date-time
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het brondocument is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het unieke nummer van het brondocument. | [optional] 
**bagprocesCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Functionele handeling die ten grondslag ligt aan de gebeurtenis. code | [optional] value must be a 64 bit integer
**bagprocesOmschrijving** | None, str,  | NoneClass, str,  | Functionele handeling die ten grondslag ligt aan de gebeurtenis. omschrijving | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# _links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BagLigplaatsenLinks](BagLigplaatsenLinks.md) | [**BagLigplaatsenLinks**](BagLigplaatsenLinks.md) | [**BagLigplaatsenLinks**](BagLigplaatsenLinks.md) |  | 

# gebruiksdoel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagligplaatsenGebruiksdoel**](BagligplaatsenGebruiksdoel.md) | [**BagligplaatsenGebruiksdoel**](BagligplaatsenGebruiksdoel.md) | [**BagligplaatsenGebruiksdoel**](BagligplaatsenGebruiksdoel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

