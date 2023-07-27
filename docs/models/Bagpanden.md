# openapi_client.model.bagpanden.Bagpanden

panden

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | panden | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**identificatie** | str,  | str,  | Landelijke identificerende sleutel. | 
**ligtInBouwblokId** | None, str,  | NoneClass, str,  | Het bouwblok waarin het pand ligt. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**heeftDossierId** | None, str,  | NoneClass, str,  | Het dossier op basis waarvan het object is toegevoegd aan de registratie. | 
**ligtInBuurtId** | None, str,  | NoneClass, str,  | De buurt waarin het pand ligt. | 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**geconstateerd** | None, bool,  | NoneClass, BoolClass,  | Dit geeft aan dat een PAND in de registratie is opgenomen als gevolg van een feitelijke constatering en niet op basis van een regulier brondocument (J/N). | [optional] 
**geometrie** | [**Geometry**](Geometry.md) | [**Geometry**](Geometry.md) |  | [optional] 
**oorspronkelijkBouwjaar** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De aanduiding van het jaar waarin een pand oorspronkelijk als bouwkundig gereed is of wordt opgeleverd. | [optional] value must be a 64 bit integer
**statusCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De fase van de levenscyclus van een pand, waarin het betreffende pand zich bevindt. code | [optional] value must be a 64 bit integer
**statusOmschrijving** | None, str,  | NoneClass, str,  | De fase van de levenscyclus van een pand, waarin het betreffende pand zich bevindt. omschrijving | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een PAND. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een PAND. | [optional] value must conform to RFC-3339 date-time
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het brondocument is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het unieke nummer van het brondocument. | [optional] 
**naam** | None, str,  | NoneClass, str,  | Naamgeving van een pand (bv. naam van metrostation of bijzonder gebouw). | [optional] 
**liggingCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Situering pand met verblijfsobject (vrijstaand, tussenwoning, etc.). code | [optional] value must be a 64 bit integer
**liggingOmschrijving** | None, str,  | NoneClass, str,  | Situering pand met verblijfsobject (vrijstaand, tussenwoning, etc.). omschrijving | [optional] 
**typeWoonobject** | None, str,  | NoneClass, str,  | Eén woning, Meerdere woningen. | [optional] 
**aantalBouwlagen** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Aantal bouwlagen van een pand. | [optional] value must be a 64 bit integer
**hoogsteBouwlaag** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Hoogste bouwlaag van een pand. | [optional] value must be a 64 bit integer
**laagsteBouwlaag** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Laagste bouwlaag van een pand. | [optional] value must be a 64 bit integer
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
[BagPandenLinks](BagPandenLinks.md) | [**BagPandenLinks**](BagPandenLinks.md) | [**BagPandenLinks**](BagPandenLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

