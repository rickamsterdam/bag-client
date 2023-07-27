# openapi_client.model.bagopenbareruimtes.Bagopenbareruimtes

openbareruimtes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | openbareruimtes | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ligtInWoonplaatsId** | None, str,  | NoneClass, str,  | De woonplaats (landelijke identificatie) waarin de openbare ruimte ligt. | 
**identificatie** | str,  | str,  | Landelijke identificerende sleutel. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**heeftDossierId** | None, str,  | NoneClass, str,  | Het dossier op basis waarvan het object is toegevoegd aan de registratie. | 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**straatcode** | None, str,  | NoneClass, str,  | Straatcode. | [optional] 
**straatnaamPtt** | None, str,  | NoneClass, str,  | Straatnaam volgens de schrijfwijze van PostNL (17 tekens). | [optional] 
**statusCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De status van de levenscyclus van een openbare ruimte (Naamgeving uitgegeven, Naamgeving ingetrokken). code | [optional] value must be a 64 bit integer
**statusOmschrijving** | None, str,  | NoneClass, str,  | De status van de levenscyclus van een openbare ruimte (Naamgeving uitgegeven, Naamgeving ingetrokken). omschrijving | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een OPENBARE RUIMTE. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een OPENBARE RUIMTE. | [optional] value must conform to RFC-3339 date-time
**geconstateerd** | None, bool,  | NoneClass, BoolClass,  | Dit geeft aan dat een OPENBARE RUIMTE in de registratie is opgenomen als gevolg van een feitelijke constatering en niet op basis van een regulier brondocument (J/N) | [optional] 
**typeCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De aard van de zodanig benoemde openbare ruimte (01 Weg, 02 Water, 03 Spoorbaan, 04 Terrein, 05 Kunstwerk, 06 Landschappelijk gebied, 07 Administratief gebied) code | [optional] value must be a 64 bit integer
**typeOmschrijving** | None, str,  | NoneClass, str,  | De aard van de zodanig benoemde openbare ruimte (01 Weg, 02 Water, 03 Spoorbaan, 04 Terrein, 05 Kunstwerk, 06 Landschappelijk gebied, 07 Administratief gebied) omschrijving | [optional] 
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het brondocument is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het unieke nummer van het brondocument. | [optional] 
**naam** | None, str,  | NoneClass, str,  | Officiële naam openbare ruimte (80 tekens). | [optional] 
**naamNen** | None, str,  | NoneClass, str,  | Straatnaam volgens de inkortingsregels van NEN 5825 (24 tekens). | [optional] 
**beschrijvingNaam** | None, str,  | NoneClass, str,  | Beschrijving van de openbare ruimte bijvoorbeeld: Vogel. Wereldwijd komen 24 soorten albatrossen voor. De meeste leven op het zuidelijk halfrond. De grootste albatros heeft een spanwijdte van meer dan drie meter en is daarmee de grootste zeevogel ter wereld. | [optional] 
**bagprocesCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Functionele handeling die ten grondslag ligt aan de gebeurtenis. code | [optional] value must be a 64 bit integer
**bagprocesOmschrijving** | None, str,  | NoneClass, str,  | Functionele handeling die ten grondslag ligt aan de gebeurtenis. omschrijving | [optional] 
**geometrie** | [**Geometry**](Geometry.md) | [**Geometry**](Geometry.md) |  | [optional] 
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
[BagOpenbareruimtesLinks](BagOpenbareruimtesLinks.md) | [**BagOpenbareruimtesLinks**](BagOpenbareruimtesLinks.md) | [**BagOpenbareruimtesLinks**](BagOpenbareruimtesLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

