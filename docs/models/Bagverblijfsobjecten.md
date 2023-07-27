# openapi_client.model.bagverblijfsobjecten.Bagverblijfsobjecten

verblijfsobjecten

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | verblijfsobjecten | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[gebruiksdoel](#gebruiksdoel)** | list, tuple,  | tuple,  |  | 
**[toegang](#toegang)** | list, tuple,  | tuple,  |  | 
**identificatie** | str,  | str,  | Landelijke identificerende sleutel. | 
**[_links](#_links)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**volgnummer** | decimal.Decimal, int,  | decimal.Decimal,  | Uniek volgnummer van de toestand van het object. | value must be a 64 bit integer
**heeftDossierId** | None, str,  | NoneClass, str,  | Het dossier op basis waarvan het object is toegevoegd aan de registratie. | 
**ligtInBuurtId** | None, str,  | NoneClass, str,  | Buurt waarin het verblijfsobject ligt. | 
**heeftHoofdadresId** | None, str,  | NoneClass, str,  | Het HOOFDadres dat het verblijfsobject heeft. | 
**registratiedatum** | None, str, datetime,  | NoneClass, str,  | De datum waarop de toestand is geregistreerd. | [optional] value must conform to RFC-3339 date-time
**cbsNummer** | None, str,  | NoneClass, str,  | CBS-nummer. | [optional] 
**indicatieWoningvoorraad** | None, str,  | NoneClass, str,  | Geeft aan of een verblijfsobject bij de woningvoorraad hoort. | [optional] 
**financieringscodeCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Geeft aan op welke wijze een woning gefinancierd is bij de bouw. code | [optional] value must be a 64 bit integer
**financieringscodeOmschrijving** | None, str,  | NoneClass, str,  | Geeft aan op welke wijze een woning gefinancierd is bij de bouw. omschrijving | [optional] 
**geconstateerd** | None, bool,  | NoneClass, BoolClass,  | Dit geeft aan dat een VERBLIJFSOBJECT in de registratie is opgenomen als gevolg van een feitelijke constatering en niet op basis van een regulier brondocument (J/N). | [optional] 
**geometrie** | [**Geometry**](Geometry.md) | [**Geometry**](Geometry.md) |  | [optional] 
**oppervlakte** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De gebruiksoppervlakte van het verblijfsobject conform hetgeen in NEN 2580 is vastgelegd omtrent gebruiksoppervlakte. | [optional] value must be a 64 bit integer
**statusCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | De fase van de levenscyclus van een verblijfsobject, waarin het betreffende VERBLIJFSOBJECT zich bevindt. code | [optional] value must be a 64 bit integer
**statusOmschrijving** | None, str,  | NoneClass, str,  | De fase van de levenscyclus van een verblijfsobject, waarin het betreffende VERBLIJFSOBJECT zich bevindt. omschrijving | [optional] 
**beginGeldigheid** | None, str, datetime,  | NoneClass, str,  | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een VERBLIJFSOBJECT. | [optional] value must conform to RFC-3339 date-time
**eindGeldigheid** | None, str, datetime,  | NoneClass, str,  | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een VERBLIJFSOBJECT. | [optional] value must conform to RFC-3339 date-time
**documentdatum** | None, str, date,  | NoneClass, str,  | De datum waarop het brondocument is vastgesteld. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**documentnummer** | None, str,  | NoneClass, str,  | Het unieke nummer van het brondocument. | [optional] 
**gebruiksdoelWoonfunctieCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Amsterdamse uitbreiding op Gebruiksdoel verblijfsobject. code | [optional] value must be a 64 bit integer
**gebruiksdoelWoonfunctieOmschrijving** | None, str,  | NoneClass, str,  | Amsterdamse uitbreiding op Gebruiksdoel verblijfsobject. omschrijving | [optional] 
**gebruiksdoelGezondheidszorgfunctieCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Amsterdamse uitbreiding op Gebruiksdoel verblijfsobject. code | [optional] value must be a 64 bit integer
**gebruiksdoelGezondheidszorgfunctieOmschrijving** | None, str,  | NoneClass, str,  | Amsterdamse uitbreiding op Gebruiksdoel verblijfsobject. omschrijving | [optional] 
**aantalEenhedenComplex** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Aantal eenheden complex per verblijfsobject (alléén bij een speciale  woonfunctie of gezondheidszorgfunctie; zie gebruiksdoel-plus). | [optional] value must be a 64 bit integer
**verdiepingToegang** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Aanduiding op welke verdieping zich de toegang tot het verblijfsobject bevindt. | [optional] value must be a 64 bit integer
**aantalBouwlagen** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Aantal bouwlagen van een verblijfsobject. | [optional] value must be a 64 bit integer
**hoogsteBouwlaag** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Hoogste bouwlaag van een verblijfsobject. | [optional] value must be a 64 bit integer
**laagsteBouwlaag** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Laagste bouwlaag van een verblijfsobject. | [optional] value must be a 64 bit integer
**aantalKamers** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Geeft het aantal kamers aan binnen het verblijfsobject. | [optional] value must be a 64 bit integer
**eigendomsverhoudingCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Geeft de eigendomsverhouding aan (huur of eigendom). code | [optional] value must be a 64 bit integer
**eigendomsverhoudingOmschrijving** | None, str,  | NoneClass, str,  | Geeft de eigendomsverhouding aan (huur of eigendom). omschrijving | [optional] 
**feitelijkGebruikCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Feitelijk gebruik van een verblijfsobject. code | [optional] value must be a 64 bit integer
**feitelijkGebruikOmschrijving** | None, str,  | NoneClass, str,  | Feitelijk gebruik van een verblijfsobject. omschrijving | [optional] 
**redenopvoerCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Reden van de opvoer van het verblijfsobject. code | [optional] value must be a 64 bit integer
**redenopvoerOmschrijving** | None, str,  | NoneClass, str,  | Reden van de opvoer van het verblijfsobject. omschrijving | [optional] 
**redenafvoerCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Reden van de afvoer van het verblijfsobject. code | [optional] value must be a 64 bit integer
**redenafvoerOmschrijving** | None, str,  | NoneClass, str,  | Reden van de afvoer van het verblijfsobject. omschrijving | [optional] 
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
[BagVerblijfsobjectenLinks](BagVerblijfsobjectenLinks.md) | [**BagVerblijfsobjectenLinks**](BagVerblijfsobjectenLinks.md) | [**BagVerblijfsobjectenLinks**](BagVerblijfsobjectenLinks.md) |  | 

# gebruiksdoel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagverblijfsobjectenGebruiksdoel**](BagverblijfsobjectenGebruiksdoel.md) | [**BagverblijfsobjectenGebruiksdoel**](BagverblijfsobjectenGebruiksdoel.md) | [**BagverblijfsobjectenGebruiksdoel**](BagverblijfsobjectenGebruiksdoel.md) |  | 

# toegang

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BagverblijfsobjectenToegang**](BagverblijfsobjectenToegang.md) | [**BagverblijfsobjectenToegang**](BagverblijfsobjectenToegang.md) | [**BagverblijfsobjectenToegang**](BagverblijfsobjectenToegang.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

