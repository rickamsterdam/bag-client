# openapi_client.model.bagonderzoeken.Bagonderzoeken

onderzoeken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | onderzoeken | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**identificatie** | str,  | str,  | Identificatie van de objectklasse Onderzoek voor intern gebruik. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**objectIdentificatie** | None, str,  | NoneClass, str,  | Identificerende nummer van het object dat in onderzoek is geplaatst. | [optional] 
**objecttype** | None, str,  | NoneClass, str,  | Geeft aan welk objectklasse in onderzoek staat. | [optional] 
**kenmerk** | None, str,  | NoneClass, str,  | De naam van het kenmerk van het object dat in onderzoek is geplaatst. Het kenmerk kan ook een relatie zijn met een ander object. | [optional] 
**inOnderzoek** | None, str,  | NoneClass, str,  | Indicatie of het kenmerk wel of niet in onderzoek staat. | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De datum waarop het kenmerk of de relatie van een object bij de bronhouder in onderzoek is geplaatst. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De datum waarop het onderzoek naar het kenmerk of de relatie van een object door de bronhouder is afgerond. | [optional] value must conform to RFC-3339 date-time
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het document, waarin de grondslag van het onderzoek wordt vastgelegd, is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het nummer van het document waarin de grondslag van het onderzoek wordt vastgelegd. | [optional] 
**tijdstipRegistratie** | None, str, datetime,  | NoneClass, str,  | Het tijdstip waarop het onderzoek is geregistreerd bij de bronhouder. | [optional] value must conform to RFC-3339 date-time
**eindRegistratie** | None, str, datetime,  | NoneClass, str,  | Het tijdstip waarop de registratie van het onderzoek is beëindigd bij de bronhouder. | [optional] value must conform to RFC-3339 date-time
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
[BagOnderzoekenLinks](BagOnderzoekenLinks.md) | [**BagOnderzoekenLinks**](BagOnderzoekenLinks.md) | [**BagOnderzoekenLinks**](BagOnderzoekenLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

