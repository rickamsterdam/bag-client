# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import brondocumenten_api
from openapi_client.model.bagbrondocumenten import Bagbrondocumenten
from openapi_client.model.paginated_bagbrondocumenten_list import PaginatedBagbrondocumentenList
# Defining the host is optional and defaults to https://api.data.amsterdam.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.data.amsterdam.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = openapi_client.Configuration(
    host = "https://api.data.amsterdam.nl",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brondocumenten_api.BrondocumentenApi(api_client)
    accept_crs = "Accept-Crs_example" # str | Accept-Crs header for Geo queries (optional)
content_crs = "Content-Crs_example" # str | Content-Crs header for Geo queries (optional)
count = True # bool | Include a count of the total result set and the number of pages.Only works for responses that return a page. (optional)
expand = True # bool | Allow to expand relations. (optional)
expand_scope = "_expandScope_example" # str | Comma separated list of named relations to expand. (optional)
fields = "_fields_example" # str | Comma-separated list of fields to display (optional)
format = "json" # str | Select the export format (optional)
page_size = 1 # int | Number of results to return per page. (optional)
sort = "_sort_example" # str | Which field to use when ordering the results. (optional)
bronleverancier_code = "bronleverancierCode_example" # str | Verstrekker van brondocumenten en/​of gegevens voortkomend uit het uitoefenen of voorbereiden van een gemeentelijke bevoegdheid, die nodig zijn voor een registratie aan de bronhouder, conform vastgestelde aanleverspecificaties. code (optional)
bronleverancier_code_in = [
        "bronleverancierCode[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
bronleverancier_code_isempty = True # bool | Whether the field is empty or not. (optional)
bronleverancier_code_isnull = True # bool | Whether the field has a NULL value or not. (optional)
bronleverancier_code_like = "bronleverancierCode[like]_example" # str | Matches text using wildcards (? and *). (optional)
bronleverancier_code_not = [
        "bronleverancierCode[not]_example"
    ] # [str] | Exclude matches; text (optional)
bronleverancier_omschrijving = "bronleverancierOmschrijving_example" # str | Verstrekker van brondocumenten en/​of gegevens voortkomend uit het uitoefenen of voorbereiden van een gemeentelijke bevoegdheid, die nodig zijn voor een registratie aan de bronhouder, conform vastgestelde aanleverspecificaties. omschrijving (optional)
bronleverancier_omschrijving_in = [
        "bronleverancierOmschrijving[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
bronleverancier_omschrijving_isempty = True # bool | Whether the field is empty or not. (optional)
bronleverancier_omschrijving_isnull = True # bool | Whether the field has a NULL value or not. (optional)
bronleverancier_omschrijving_like = "bronleverancierOmschrijving[like]_example" # str | Matches text using wildcards (? and *). (optional)
bronleverancier_omschrijving_not = [
        "bronleverancierOmschrijving[not]_example"
    ] # [str] | Exclude matches; text (optional)
documentnummer = "documentnummer_example" # str | Identificerende nummer van het document. (optional)
documentnummer_in = [
        "documentnummer[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
documentnummer_isempty = True # bool | Whether the field is empty or not. (optional)
documentnummer_isnull = True # bool | Whether the field has a NULL value or not. (optional)
documentnummer_like = "documentnummer[like]_example" # str | Matches text using wildcards (? and *). (optional)
documentnummer_not = [
        "documentnummer[not]_example"
    ] # [str] | Exclude matches; text (optional)
page = 1 # int | A page number within the paginated result set. (optional)
registratiedatum = "1970-01-01T00:00:00.00Z" # datetime | De datum waarop het brondocument is opgeslagen in het register. (optional)
registratiedatum_gt = "1970-01-01T00:00:00.00Z" # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
registratiedatum_gte = "1970-01-01T00:00:00.00Z" # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
registratiedatum_in = [
        "1970-01-01T00:00:00.00Z"
    ] # [datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
registratiedatum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
registratiedatum_lt = "1970-01-01T00:00:00.00Z" # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
registratiedatum_lte = "1970-01-01T00:00:00.00Z" # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
registratiedatum_not = [
        "1970-01-01T00:00:00.00Z"
    ] # [datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
type_brondocument_code = "typeBrondocumentCode_example" # str | Het type brondocument. code (optional)
type_brondocument_code_in = [
        "typeBrondocumentCode[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
type_brondocument_code_isempty = True # bool | Whether the field is empty or not. (optional)
type_brondocument_code_isnull = True # bool | Whether the field has a NULL value or not. (optional)
type_brondocument_code_like = "typeBrondocumentCode[like]_example" # str | Matches text using wildcards (? and *). (optional)
type_brondocument_code_not = [
        "typeBrondocumentCode[not]_example"
    ] # [str] | Exclude matches; text (optional)
type_brondocument_omschrijving = "typeBrondocumentOmschrijving_example" # str | Het type brondocument. omschrijving (optional)
type_brondocument_omschrijving_in = [
        "typeBrondocumentOmschrijving[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
type_brondocument_omschrijving_isempty = True # bool | Whether the field is empty or not. (optional)
type_brondocument_omschrijving_isnull = True # bool | Whether the field has a NULL value or not. (optional)
type_brondocument_omschrijving_like = "typeBrondocumentOmschrijving[like]_example" # str | Matches text using wildcards (? and *). (optional)
type_brondocument_omschrijving_not = [
        "typeBrondocumentOmschrijving[not]_example"
    ] # [str] | Exclude matches; text (optional)
type_dossier_code = "typeDossierCode_example" # str | Het type dossier. code (optional)
type_dossier_code_in = [
        "typeDossierCode[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
type_dossier_code_isempty = True # bool | Whether the field is empty or not. (optional)
type_dossier_code_isnull = True # bool | Whether the field has a NULL value or not. (optional)
type_dossier_code_like = "typeDossierCode[like]_example" # str | Matches text using wildcards (? and *). (optional)
type_dossier_code_not = [
        "typeDossierCode[not]_example"
    ] # [str] | Exclude matches; text (optional)
type_dossier_omschrijving = "typeDossierOmschrijving_example" # str | Het type dossier. omschrijving (optional)
type_dossier_omschrijving_in = [
        "typeDossierOmschrijving[in]_example"
    ] # [str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
type_dossier_omschrijving_isempty = True # bool | Whether the field is empty or not. (optional)
type_dossier_omschrijving_isnull = True # bool | Whether the field has a NULL value or not. (optional)
type_dossier_omschrijving_like = "typeDossierOmschrijving[like]_example" # str | Matches text using wildcards (? and *). (optional)
type_dossier_omschrijving_not = [
        "typeDossierOmschrijving[not]_example"
    ] # [str] | Exclude matches; text (optional)

    try:
        api_response = api_instance.bag_brondocumenten_list(accept_crs=accept_crscontent_crs=content_crscount=countexpand=expandexpand_scope=expand_scopefields=fieldsformat=formatpage_size=page_sizesort=sortbronleverancier_code=bronleverancier_codebronleverancier_code_in=bronleverancier_code_inbronleverancier_code_isempty=bronleverancier_code_isemptybronleverancier_code_isnull=bronleverancier_code_isnullbronleverancier_code_like=bronleverancier_code_likebronleverancier_code_not=bronleverancier_code_notbronleverancier_omschrijving=bronleverancier_omschrijvingbronleverancier_omschrijving_in=bronleverancier_omschrijving_inbronleverancier_omschrijving_isempty=bronleverancier_omschrijving_isemptybronleverancier_omschrijving_isnull=bronleverancier_omschrijving_isnullbronleverancier_omschrijving_like=bronleverancier_omschrijving_likebronleverancier_omschrijving_not=bronleverancier_omschrijving_notdocumentnummer=documentnummerdocumentnummer_in=documentnummer_indocumentnummer_isempty=documentnummer_isemptydocumentnummer_isnull=documentnummer_isnulldocumentnummer_like=documentnummer_likedocumentnummer_not=documentnummer_notpage=pageregistratiedatum=registratiedatumregistratiedatum_gt=registratiedatum_gtregistratiedatum_gte=registratiedatum_gteregistratiedatum_in=registratiedatum_inregistratiedatum_isnull=registratiedatum_isnullregistratiedatum_lt=registratiedatum_ltregistratiedatum_lte=registratiedatum_lteregistratiedatum_not=registratiedatum_nottype_brondocument_code=type_brondocument_codetype_brondocument_code_in=type_brondocument_code_intype_brondocument_code_isempty=type_brondocument_code_isemptytype_brondocument_code_isnull=type_brondocument_code_isnulltype_brondocument_code_like=type_brondocument_code_liketype_brondocument_code_not=type_brondocument_code_nottype_brondocument_omschrijving=type_brondocument_omschrijvingtype_brondocument_omschrijving_in=type_brondocument_omschrijving_intype_brondocument_omschrijving_isempty=type_brondocument_omschrijving_isemptytype_brondocument_omschrijving_isnull=type_brondocument_omschrijving_isnulltype_brondocument_omschrijving_like=type_brondocument_omschrijving_liketype_brondocument_omschrijving_not=type_brondocument_omschrijving_nottype_dossier_code=type_dossier_codetype_dossier_code_in=type_dossier_code_intype_dossier_code_isempty=type_dossier_code_isemptytype_dossier_code_isnull=type_dossier_code_isnulltype_dossier_code_like=type_dossier_code_liketype_dossier_code_not=type_dossier_code_nottype_dossier_omschrijving=type_dossier_omschrijvingtype_dossier_omschrijving_in=type_dossier_omschrijving_intype_dossier_omschrijving_isempty=type_dossier_omschrijving_isemptytype_dossier_omschrijving_isnull=type_dossier_omschrijving_isnulltype_dossier_omschrijving_like=type_dossier_omschrijving_liketype_dossier_omschrijving_not=type_dossier_omschrijving_not)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrondocumentenApi->bag_brondocumenten_list: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.data.amsterdam.nl*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrondocumentenApi* | [**bag_brondocumenten_list**](docs/apis/tags/BrondocumentenApi.md#bag_brondocumenten_list) | **get** /v1/bag/brondocumenten/ | 
*BrondocumentenApi* | [**bag_brondocumenten_retrieve**](docs/apis/tags/BrondocumentenApi.md#bag_brondocumenten_retrieve) | **get** /v1/bag/brondocumenten/{documentnummer}/ | 
*DossiersApi* | [**bag_dossiers_list**](docs/apis/tags/DossiersApi.md#bag_dossiers_list) | **get** /v1/bag/dossiers/ | 
*DossiersApi* | [**bag_dossiers_retrieve**](docs/apis/tags/DossiersApi.md#bag_dossiers_retrieve) | **get** /v1/bag/dossiers/{dossier}/ | 
*LigplaatsenApi* | [**bag_ligplaatsen_list**](docs/apis/tags/LigplaatsenApi.md#bag_ligplaatsen_list) | **get** /v1/bag/ligplaatsen/ | 
*LigplaatsenApi* | [**bag_ligplaatsen_retrieve**](docs/apis/tags/LigplaatsenApi.md#bag_ligplaatsen_retrieve) | **get** /v1/bag/ligplaatsen/{id}/ | 
*NummeraanduidingenApi* | [**bag_nummeraanduidingen_list**](docs/apis/tags/NummeraanduidingenApi.md#bag_nummeraanduidingen_list) | **get** /v1/bag/nummeraanduidingen/ | 
*NummeraanduidingenApi* | [**bag_nummeraanduidingen_retrieve**](docs/apis/tags/NummeraanduidingenApi.md#bag_nummeraanduidingen_retrieve) | **get** /v1/bag/nummeraanduidingen/{id}/ | 
*OnderzoekenApi* | [**bag_onderzoeken_list**](docs/apis/tags/OnderzoekenApi.md#bag_onderzoeken_list) | **get** /v1/bag/onderzoeken/ | 
*OnderzoekenApi* | [**bag_onderzoeken_retrieve**](docs/apis/tags/OnderzoekenApi.md#bag_onderzoeken_retrieve) | **get** /v1/bag/onderzoeken/{id}/ | 
*OpenbareruimtesApi* | [**bag_openbareruimtes_list**](docs/apis/tags/OpenbareruimtesApi.md#bag_openbareruimtes_list) | **get** /v1/bag/openbareruimtes/ | 
*OpenbareruimtesApi* | [**bag_openbareruimtes_retrieve**](docs/apis/tags/OpenbareruimtesApi.md#bag_openbareruimtes_retrieve) | **get** /v1/bag/openbareruimtes/{id}/ | 
*PandenApi* | [**bag_panden_list**](docs/apis/tags/PandenApi.md#bag_panden_list) | **get** /v1/bag/panden/ | 
*PandenApi* | [**bag_panden_retrieve**](docs/apis/tags/PandenApi.md#bag_panden_retrieve) | **get** /v1/bag/panden/{id}/ | 
*StandplaatsenApi* | [**bag_standplaatsen_list**](docs/apis/tags/StandplaatsenApi.md#bag_standplaatsen_list) | **get** /v1/bag/standplaatsen/ | 
*StandplaatsenApi* | [**bag_standplaatsen_retrieve**](docs/apis/tags/StandplaatsenApi.md#bag_standplaatsen_retrieve) | **get** /v1/bag/standplaatsen/{id}/ | 
*VerblijfsobjectenApi* | [**bag_verblijfsobjecten_list**](docs/apis/tags/VerblijfsobjectenApi.md#bag_verblijfsobjecten_list) | **get** /v1/bag/verblijfsobjecten/ | 
*VerblijfsobjectenApi* | [**bag_verblijfsobjecten_retrieve**](docs/apis/tags/VerblijfsobjectenApi.md#bag_verblijfsobjecten_retrieve) | **get** /v1/bag/verblijfsobjecten/{id}/ | 
*WoonplaatsenApi* | [**bag_woonplaatsen_list**](docs/apis/tags/WoonplaatsenApi.md#bag_woonplaatsen_list) | **get** /v1/bag/woonplaatsen/ | 
*WoonplaatsenApi* | [**bag_woonplaatsen_retrieve**](docs/apis/tags/WoonplaatsenApi.md#bag_woonplaatsen_retrieve) | **get** /v1/bag/woonplaatsen/{id}/ | 

## Documentation For Models

 - [BagBrondocumentenLinks](docs/models/BagBrondocumentenLinks.md)
 - [BagDossiersLinks](docs/models/BagDossiersLinks.md)
 - [BagLigplaatsenLink](docs/models/BagLigplaatsenLink.md)
 - [BagLigplaatsenLinks](docs/models/BagLigplaatsenLinks.md)
 - [BagNummeraanduidingenLink](docs/models/BagNummeraanduidingenLink.md)
 - [BagNummeraanduidingenLinks](docs/models/BagNummeraanduidingenLinks.md)
 - [BagOnderzoekenLink](docs/models/BagOnderzoekenLink.md)
 - [BagOnderzoekenLinks](docs/models/BagOnderzoekenLinks.md)
 - [BagOpenbareruimtesLink](docs/models/BagOpenbareruimtesLink.md)
 - [BagOpenbareruimtesLinks](docs/models/BagOpenbareruimtesLinks.md)
 - [BagPandenLink](docs/models/BagPandenLink.md)
 - [BagPandenLinks](docs/models/BagPandenLinks.md)
 - [BagStandplaatsenLink](docs/models/BagStandplaatsenLink.md)
 - [BagStandplaatsenLinks](docs/models/BagStandplaatsenLinks.md)
 - [BagVerblijfsobjectenLink](docs/models/BagVerblijfsobjectenLink.md)
 - [BagVerblijfsobjectenLinks](docs/models/BagVerblijfsobjectenLinks.md)
 - [BagWoonplaatsenLink](docs/models/BagWoonplaatsenLink.md)
 - [BagWoonplaatsenLinks](docs/models/BagWoonplaatsenLinks.md)
 - [Bagbrondocumenten](docs/models/Bagbrondocumenten.md)
 - [BagbrondocumentenLink](docs/models/BagbrondocumentenLink.md)
 - [Bagdossiers](docs/models/Bagdossiers.md)
 - [BagdossiersHeeftBrondocumentenM2M](docs/models/BagdossiersHeeftBrondocumentenM2M.md)
 - [BagdossiersLink](docs/models/BagdossiersLink.md)
 - [Bagligplaatsen](docs/models/Bagligplaatsen.md)
 - [BagligplaatsenGebruiksdoel](docs/models/BagligplaatsenGebruiksdoel.md)
 - [BagligplaatsenHeeftNevenadresM2M](docs/models/BagligplaatsenHeeftNevenadresM2M.md)
 - [BagligplaatsenHeeftOnderzoekenM2M](docs/models/BagligplaatsenHeeftOnderzoekenM2M.md)
 - [Bagnummeraanduidingen](docs/models/Bagnummeraanduidingen.md)
 - [BagnummeraanduidingenHeeftOnderzoekenM2M](docs/models/BagnummeraanduidingenHeeftOnderzoekenM2M.md)
 - [Bagonderzoeken](docs/models/Bagonderzoeken.md)
 - [Bagopenbareruimtes](docs/models/Bagopenbareruimtes.md)
 - [BagopenbareruimtesHeeftOnderzoekenM2M](docs/models/BagopenbareruimtesHeeftOnderzoekenM2M.md)
 - [Bagpanden](docs/models/Bagpanden.md)
 - [BagpandenHeeftOnderzoekenM2M](docs/models/BagpandenHeeftOnderzoekenM2M.md)
 - [Bagstandplaatsen](docs/models/Bagstandplaatsen.md)
 - [BagstandplaatsenGebruiksdoel](docs/models/BagstandplaatsenGebruiksdoel.md)
 - [BagstandplaatsenHeeftNevenadresM2M](docs/models/BagstandplaatsenHeeftNevenadresM2M.md)
 - [BagstandplaatsenHeeftOnderzoekenM2M](docs/models/BagstandplaatsenHeeftOnderzoekenM2M.md)
 - [Bagverblijfsobjecten](docs/models/Bagverblijfsobjecten.md)
 - [BagverblijfsobjectenGebruiksdoel](docs/models/BagverblijfsobjectenGebruiksdoel.md)
 - [BagverblijfsobjectenHeeftNevenadresM2M](docs/models/BagverblijfsobjectenHeeftNevenadresM2M.md)
 - [BagverblijfsobjectenHeeftOnderzoekenM2M](docs/models/BagverblijfsobjectenHeeftOnderzoekenM2M.md)
 - [BagverblijfsobjectenLigtInPandenM2M](docs/models/BagverblijfsobjectenLigtInPandenM2M.md)
 - [BagverblijfsobjectenToegang](docs/models/BagverblijfsobjectenToegang.md)
 - [Bagwoonplaatsen](docs/models/Bagwoonplaatsen.md)
 - [BagwoonplaatsenHeeftOnderzoekenM2M](docs/models/BagwoonplaatsenHeeftOnderzoekenM2M.md)
 - [BrkGemeentesLink](docs/models/BrkGemeentesLink.md)
 - [GebiedenBouwblokkenLink](docs/models/GebiedenBouwblokkenLink.md)
 - [GebiedenBuurtenLink](docs/models/GebiedenBuurtenLink.md)
 - [Geometry](docs/models/Geometry.md)
 - [GeometryCollection](docs/models/GeometryCollection.md)
 - [LineString](docs/models/LineString.md)
 - [MultiLineString](docs/models/MultiLineString.md)
 - [MultiPoint](docs/models/MultiPoint.md)
 - [MultiPolygon](docs/models/MultiPolygon.md)
 - [PaginatedBagbrondocumentenList](docs/models/PaginatedBagbrondocumentenList.md)
 - [PaginatedBagdossiersList](docs/models/PaginatedBagdossiersList.md)
 - [PaginatedBagligplaatsenList](docs/models/PaginatedBagligplaatsenList.md)
 - [PaginatedBagnummeraanduidingenList](docs/models/PaginatedBagnummeraanduidingenList.md)
 - [PaginatedBagonderzoekenList](docs/models/PaginatedBagonderzoekenList.md)
 - [PaginatedBagopenbareruimtesList](docs/models/PaginatedBagopenbareruimtesList.md)
 - [PaginatedBagpandenList](docs/models/PaginatedBagpandenList.md)
 - [PaginatedBagstandplaatsenList](docs/models/PaginatedBagstandplaatsenList.md)
 - [PaginatedBagverblijfsobjectenList](docs/models/PaginatedBagverblijfsobjectenList.md)
 - [PaginatedBagwoonplaatsenList](docs/models/PaginatedBagwoonplaatsenList.md)
 - [Point](docs/models/Point.md)
 - [Point3D](docs/models/Point3D.md)
 - [Polygon](docs/models/Polygon.md)
 - [RelatedSummary](docs/models/RelatedSummary.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://iam.amsterdam.nl/auth/realms/datapunt-ad/protocol/openid-connect/auth
- **Scopes**: N/A


## Author

datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl
datapunt@amsterdam.nl

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```