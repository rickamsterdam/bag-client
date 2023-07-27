# openapi_client.model.bagbrondocumenten.Bagbrondocumenten

brondocumenten

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | brondocumenten | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentnummer** | str,  | str,  | Identificerende nummer van het document. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**bronleverancierCode** | None, str,  | NoneClass, str,  | Verstrekker van brondocumenten en/​of gegevens voortkomend uit het uitoefenen of voorbereiden van een gemeentelijke bevoegdheid, die nodig zijn voor een registratie aan de bronhouder, conform vastgestelde aanleverspecificaties. code | [optional] 
**bronleverancierOmschrijving** | None, str,  | NoneClass, str,  | Verstrekker van brondocumenten en/​of gegevens voortkomend uit het uitoefenen of voorbereiden van een gemeentelijke bevoegdheid, die nodig zijn voor een registratie aan de bronhouder, conform vastgestelde aanleverspecificaties. omschrijving | [optional] 
**typeDossierCode** | None, str,  | NoneClass, str,  | Het type dossier. code | [optional] 
**typeDossierOmschrijving** | None, str,  | NoneClass, str,  | Het type dossier. omschrijving | [optional] 
**typeBrondocumentCode** | None, str,  | NoneClass, str,  | Het type brondocument. code | [optional] 
**typeBrondocumentOmschrijving** | None, str,  | NoneClass, str,  | Het type brondocument. omschrijving | [optional] 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop het brondocument is opgeslagen in het register. | [optional] value must conform to RFC-3339 date-time
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
[BagBrondocumentenLinks](BagBrondocumentenLinks.md) | [**BagBrondocumentenLinks**](BagBrondocumentenLinks.md) | [**BagBrondocumentenLinks**](BagBrondocumentenLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

