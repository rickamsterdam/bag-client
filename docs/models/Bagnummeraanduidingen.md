# openapi_client.model.bagnummeraanduidingen.Bagnummeraanduidingen

nummeraanduidingen

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | nummeraanduidingen | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ligtInWoonplaatsId** | None, str,  | NoneClass, str,  | De woonplaats (landelijke identificatie) waarin de nummeraanduiding ligt. | 
**identificatie** | str,  | str,  | Landelijke identificerende sleutel. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**adresseertLigplaatsId** | None, str,  | NoneClass, str,  | De ligplaats (landelijke identificatie) die door de nummeraanduiding wordt aangeduid. | 
**ligtAanOpenbareruimteId** | None, str,  | NoneClass, str,  | De openbare ruimte (landelijke identificatie) waaraan het betreffende adresseerbare object ligt. | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**heeftDossierId** | None, str,  | NoneClass, str,  | Het dossier op basis waarvan het object is toegevoegd aan de registratie. | 
**adresseertVerblijfsobjectId** | None, str,  | NoneClass, str,  | Het verblijfsobject (landelijke identificatie) dat door de nummeraanduiding wordt aangeduid. | 
**adresseertStandplaatsId** | None, str,  | NoneClass, str,  | De standplaats (landelijke identificatie) die door de nummeraanduiding wordt aangeduid. | 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**huisnummer** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Een door het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende nummering. | [optional] value must be a 64 bit integer
**geconstateerd** | None, bool,  | NoneClass, BoolClass,  | Dit geeft aan dat een gegeven in de registratie is opgenomen als gevolg van een feitelijke constatering en niet op basis van een regulier brondocument (J/N). | [optional] 
**huisletter** | None, str,  | NoneClass, str,  | Een door het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende toevoeging aan een huisnummer in de vorm van een alfanumeriek teken. | [optional] 
**huisnummertoevoeging** | None, str,  | NoneClass, str,  | Een door het bevoegde gemeentelijke orgaan ten aanzien van een adresseerbaar object toegekende nadere toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter. | [optional] 
**postcode** | None, str,  | NoneClass, str,  | De door PostNL vastgestelde code bestaande uit 4 cijfers en 2 letters (1234AB). | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een NUMMERAANDUIDING. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een NUMMERAANDUIDING. | [optional] value must conform to RFC-3339 date-time
**typeAdresseerbaarObjectCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Het type adresseerbaar object waaraan een nummeraanduiding is toegekend. code | [optional] value must be a 64 bit integer
**typeAdresseerbaarObjectOmschrijving** | None, str,  | NoneClass, str,  | Het type adresseerbaar object waaraan een nummeraanduiding is toegekend. omschrijving | [optional] 
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het brondocument is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het unieke nummer van het brondocument. | [optional] 
**statusCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De fase van de levenscyclus van een nummeraanduiding,waarin de betreffende nummeraanduiding zich bevindt. (Naamgeving uitgegeven, Naamgeving ingetrokken). code | [optional] value must be a 64 bit integer
**statusOmschrijving** | None, str,  | NoneClass, str,  | De fase van de levenscyclus van een nummeraanduiding,waarin de betreffende nummeraanduiding zich bevindt. (Naamgeving uitgegeven, Naamgeving ingetrokken). omschrijving | [optional] 
**typeAdres** | None, str,  | NoneClass, str,  | Hiermee wordt aangegeven of het een relatie betreft vanuit een hoofdadres. Anders is er sprake van een nevenadres (Hoofdadres, Nevenadres). | [optional] 
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
[BagNummeraanduidingenLinks](BagNummeraanduidingenLinks.md) | [**BagNummeraanduidingenLinks**](BagNummeraanduidingenLinks.md) | [**BagNummeraanduidingenLinks**](BagNummeraanduidingenLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

