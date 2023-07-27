<a id="__pageTop"></a>
# openapi_client.apis.tags.nummeraanduidingen_api.NummeraanduidingenApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bag_nummeraanduidingen_list**](#bag_nummeraanduidingen_list) | **get** /v1/bag/nummeraanduidingen/ | 
[**bag_nummeraanduidingen_retrieve**](#bag_nummeraanduidingen_retrieve) | **get** /v1/bag/nummeraanduidingen/{id}/ | 

# **bag_nummeraanduidingen_list**
<a id="bag_nummeraanduidingen_list"></a>
> PaginatedBagnummeraanduidingenList bag_nummeraanduidingen_list()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import nummeraanduidingen_api
from openapi_client.model.paginated_bagnummeraanduidingen_list import PaginatedBagnummeraanduidingenList
from pprint import pprint
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
    api_instance = nummeraanduidingen_api.NummeraanduidingenApi(api_client)

    # example passing only optional values
    query_params = {
        '_count': True,
        '_expand': True,
        '_expandScope': "adresseertLigplaats",
        '_fields': "_fields_example",
        '_format': "json",
        '_pageSize': 1,
        '_sort': "_sort_example",
        'adresseertLigplaats.identificatie': "adresseertLigplaats.identificatie_example",
        'adresseertLigplaats.identificatie[in]': [
        "adresseertLigplaats.identificatie[in]_example"
    ],
        'adresseertLigplaats.identificatie[isempty]': True,
        'adresseertLigplaats.identificatie[isnull]': True,
        'adresseertLigplaats.identificatie[like]': "adresseertLigplaats.identificatie[like]_example",
        'adresseertLigplaats.identificatie[not]': [
        "adresseertLigplaats.identificatie[not]_example"
    ],
        'adresseertLigplaats.volgnummer': 1,
        'adresseertLigplaats.volgnummer[gt]': 1,
        'adresseertLigplaats.volgnummer[gte]': 1,
        'adresseertLigplaats.volgnummer[in]': [
        1
    ],
        'adresseertLigplaats.volgnummer[isnull]': True,
        'adresseertLigplaats.volgnummer[lt]': 1,
        'adresseertLigplaats.volgnummer[lte]': 1,
        'adresseertLigplaats.volgnummer[not]': [
        1
    ],
        'adresseertStandplaats.identificatie': "adresseertStandplaats.identificatie_example",
        'adresseertStandplaats.identificatie[in]': [
        "adresseertStandplaats.identificatie[in]_example"
    ],
        'adresseertStandplaats.identificatie[isempty]': True,
        'adresseertStandplaats.identificatie[isnull]': True,
        'adresseertStandplaats.identificatie[like]': "adresseertStandplaats.identificatie[like]_example",
        'adresseertStandplaats.identificatie[not]': [
        "adresseertStandplaats.identificatie[not]_example"
    ],
        'adresseertStandplaats.volgnummer': 1,
        'adresseertStandplaats.volgnummer[gt]': 1,
        'adresseertStandplaats.volgnummer[gte]': 1,
        'adresseertStandplaats.volgnummer[in]': [
        1
    ],
        'adresseertStandplaats.volgnummer[isnull]': True,
        'adresseertStandplaats.volgnummer[lt]': 1,
        'adresseertStandplaats.volgnummer[lte]': 1,
        'adresseertStandplaats.volgnummer[not]': [
        1
    ],
        'adresseertVerblijfsobject.identificatie': "adresseertVerblijfsobject.identificatie_example",
        'adresseertVerblijfsobject.identificatie[in]': [
        "adresseertVerblijfsobject.identificatie[in]_example"
    ],
        'adresseertVerblijfsobject.identificatie[isempty]': True,
        'adresseertVerblijfsobject.identificatie[isnull]': True,
        'adresseertVerblijfsobject.identificatie[like]': "adresseertVerblijfsobject.identificatie[like]_example",
        'adresseertVerblijfsobject.identificatie[not]': [
        "adresseertVerblijfsobject.identificatie[not]_example"
    ],
        'adresseertVerblijfsobject.volgnummer': 1,
        'adresseertVerblijfsobject.volgnummer[gt]': 1,
        'adresseertVerblijfsobject.volgnummer[gte]': 1,
        'adresseertVerblijfsobject.volgnummer[in]': [
        1
    ],
        'adresseertVerblijfsobject.volgnummer[isnull]': True,
        'adresseertVerblijfsobject.volgnummer[lt]': 1,
        'adresseertVerblijfsobject.volgnummer[lte]': 1,
        'adresseertVerblijfsobject.volgnummer[not]': [
        1
    ],
        'bagprocesCode': 1,
        'bagprocesCode[gt]': 1,
        'bagprocesCode[gte]': 1,
        'bagprocesCode[in]': [
        1
    ],
        'bagprocesCode[isnull]': True,
        'bagprocesCode[lt]': 1,
        'bagprocesCode[lte]': 1,
        'bagprocesCode[not]': [
        1
    ],
        'bagprocesOmschrijving': "bagprocesOmschrijving_example",
        'bagprocesOmschrijving[in]': [
        "bagprocesOmschrijving[in]_example"
    ],
        'bagprocesOmschrijving[isempty]': True,
        'bagprocesOmschrijving[isnull]': True,
        'bagprocesOmschrijving[like]': "bagprocesOmschrijving[like]_example",
        'bagprocesOmschrijving[not]': [
        "bagprocesOmschrijving[not]_example"
    ],
        'beginGeldigheid': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[gt]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[gte]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'beginGeldigheid[isnull]': True,
        'beginGeldigheid[lt]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[lte]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'documentdatum': "1970-01-01",
        'documentdatum[gt]': "1970-01-01",
        'documentdatum[gte]': "1970-01-01",
        'documentdatum[in]': [
        "1970-01-01"
    ],
        'documentdatum[isnull]': True,
        'documentdatum[lt]': "1970-01-01",
        'documentdatum[lte]': "1970-01-01",
        'documentdatum[not]': [
        "1970-01-01"
    ],
        'documentnummer': "documentnummer_example",
        'documentnummer[in]': [
        "documentnummer[in]_example"
    ],
        'documentnummer[isempty]': True,
        'documentnummer[isnull]': True,
        'documentnummer[like]': "documentnummer[like]_example",
        'documentnummer[not]': [
        "documentnummer[not]_example"
    ],
        'eindGeldigheid': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[gt]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[gte]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'eindGeldigheid[isnull]': True,
        'eindGeldigheid[lt]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[lte]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'geconstateerd': True,
        'geconstateerd[isnull]': True,
        'geldigOp': "1970-01-01T00:00:00.00Z",
        'geldigOp[gt]': "1970-01-01T00:00:00.00Z",
        'geldigOp[gte]': "1970-01-01T00:00:00.00Z",
        'geldigOp[in]': "1970-01-01T00:00:00.00Z",
        'geldigOp[isnull]': "1970-01-01T00:00:00.00Z",
        'geldigOp[lt]': "1970-01-01T00:00:00.00Z",
        'geldigOp[lte]': "1970-01-01T00:00:00.00Z",
        'geldigOp[not]': "1970-01-01T00:00:00.00Z",
        'heeftDossier.dossier': "heeftDossier.dossier_example",
        'heeftDossier.dossier[in]': [
        "heeftDossier.dossier[in]_example"
    ],
        'heeftDossier.dossier[isempty]': True,
        'heeftDossier.dossier[isnull]': True,
        'heeftDossier.dossier[like]': "heeftDossier.dossier[like]_example",
        'heeftDossier.dossier[not]': [
        "heeftDossier.dossier[not]_example"
    ],
        'heeftOnderzoeken.identificatie': "heeftOnderzoeken.identificatie_example",
        'heeftOnderzoeken.identificatie[in]': [
        "heeftOnderzoeken.identificatie[in]_example"
    ],
        'heeftOnderzoeken.identificatie[isempty]': True,
        'heeftOnderzoeken.identificatie[isnull]': True,
        'heeftOnderzoeken.identificatie[like]': "heeftOnderzoeken.identificatie[like]_example",
        'heeftOnderzoeken.identificatie[not]': [
        "heeftOnderzoeken.identificatie[not]_example"
    ],
        'heeftOnderzoeken.volgnummer': 1,
        'heeftOnderzoeken.volgnummer[gt]': 1,
        'heeftOnderzoeken.volgnummer[gte]': 1,
        'heeftOnderzoeken.volgnummer[in]': [
        1
    ],
        'heeftOnderzoeken.volgnummer[isnull]': True,
        'heeftOnderzoeken.volgnummer[lt]': 1,
        'heeftOnderzoeken.volgnummer[lte]': 1,
        'heeftOnderzoeken.volgnummer[not]': [
        1
    ],
        'huisletter': "huisletter_example",
        'huisletter[in]': [
        "huisletter[in]_example"
    ],
        'huisletter[isempty]': True,
        'huisletter[isnull]': True,
        'huisletter[like]': "huisletter[like]_example",
        'huisletter[not]': [
        "huisletter[not]_example"
    ],
        'huisnummer': 1,
        'huisnummer[gt]': 1,
        'huisnummer[gte]': 1,
        'huisnummer[in]': [
        1
    ],
        'huisnummer[isnull]': True,
        'huisnummer[lt]': 1,
        'huisnummer[lte]': 1,
        'huisnummer[not]': [
        1
    ],
        'huisnummertoevoeging': "huisnummertoevoeging_example",
        'huisnummertoevoeging[in]': [
        "huisnummertoevoeging[in]_example"
    ],
        'huisnummertoevoeging[isempty]': True,
        'huisnummertoevoeging[isnull]': True,
        'huisnummertoevoeging[like]': "huisnummertoevoeging[like]_example",
        'huisnummertoevoeging[not]': [
        "huisnummertoevoeging[not]_example"
    ],
        'id': "id_example",
        'id[in]': [
        "id[in]_example"
    ],
        'id[isempty]': True,
        'id[isnull]': True,
        'id[like]': "id[like]_example",
        'id[not]': [
        "id[not]_example"
    ],
        'identificatie': "identificatie_example",
        'identificatie[in]': [
        "identificatie[in]_example"
    ],
        'identificatie[isempty]': True,
        'identificatie[isnull]': True,
        'identificatie[like]': "identificatie[like]_example",
        'identificatie[not]': [
        "identificatie[not]_example"
    ],
        'ligtAanOpenbareruimte.identificatie': "ligtAanOpenbareruimte.identificatie_example",
        'ligtAanOpenbareruimte.identificatie[in]': [
        "ligtAanOpenbareruimte.identificatie[in]_example"
    ],
        'ligtAanOpenbareruimte.identificatie[isempty]': True,
        'ligtAanOpenbareruimte.identificatie[isnull]': True,
        'ligtAanOpenbareruimte.identificatie[like]': "ligtAanOpenbareruimte.identificatie[like]_example",
        'ligtAanOpenbareruimte.identificatie[not]': [
        "ligtAanOpenbareruimte.identificatie[not]_example"
    ],
        'ligtAanOpenbareruimte.volgnummer': 1,
        'ligtAanOpenbareruimte.volgnummer[gt]': 1,
        'ligtAanOpenbareruimte.volgnummer[gte]': 1,
        'ligtAanOpenbareruimte.volgnummer[in]': [
        1
    ],
        'ligtAanOpenbareruimte.volgnummer[isnull]': True,
        'ligtAanOpenbareruimte.volgnummer[lt]': 1,
        'ligtAanOpenbareruimte.volgnummer[lte]': 1,
        'ligtAanOpenbareruimte.volgnummer[not]': [
        1
    ],
        'ligtInWoonplaats.identificatie': "ligtInWoonplaats.identificatie_example",
        'ligtInWoonplaats.identificatie[in]': [
        "ligtInWoonplaats.identificatie[in]_example"
    ],
        'ligtInWoonplaats.identificatie[isempty]': True,
        'ligtInWoonplaats.identificatie[isnull]': True,
        'ligtInWoonplaats.identificatie[like]': "ligtInWoonplaats.identificatie[like]_example",
        'ligtInWoonplaats.identificatie[not]': [
        "ligtInWoonplaats.identificatie[not]_example"
    ],
        'ligtInWoonplaats.volgnummer': 1,
        'ligtInWoonplaats.volgnummer[gt]': 1,
        'ligtInWoonplaats.volgnummer[gte]': 1,
        'ligtInWoonplaats.volgnummer[in]': [
        1
    ],
        'ligtInWoonplaats.volgnummer[isnull]': True,
        'ligtInWoonplaats.volgnummer[lt]': 1,
        'ligtInWoonplaats.volgnummer[lte]': 1,
        'ligtInWoonplaats.volgnummer[not]': [
        1
    ],
        'page': 1,
        'postcode': "postcode_example",
        'postcode[in]': [
        "postcode[in]_example"
    ],
        'postcode[isempty]': True,
        'postcode[isnull]': True,
        'postcode[like]': "postcode[like]_example",
        'postcode[not]': [
        "postcode[not]_example"
    ],
        'registratiedatum': "1970-01-01T00:00:00.00Z",
        'registratiedatum[gt]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[gte]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'registratiedatum[isnull]': True,
        'registratiedatum[lt]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[lte]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'statusCode': 1,
        'statusCode[gt]': 1,
        'statusCode[gte]': 1,
        'statusCode[in]': [
        1
    ],
        'statusCode[isnull]': True,
        'statusCode[lt]': 1,
        'statusCode[lte]': 1,
        'statusCode[not]': [
        1
    ],
        'statusOmschrijving': "statusOmschrijving_example",
        'statusOmschrijving[in]': [
        "statusOmschrijving[in]_example"
    ],
        'statusOmschrijving[isempty]': True,
        'statusOmschrijving[isnull]': True,
        'statusOmschrijving[like]': "statusOmschrijving[like]_example",
        'statusOmschrijving[not]': [
        "statusOmschrijving[not]_example"
    ],
        'typeAdres': "typeAdres_example",
        'typeAdres[in]': [
        "typeAdres[in]_example"
    ],
        'typeAdres[isempty]': True,
        'typeAdres[isnull]': True,
        'typeAdres[like]': "typeAdres[like]_example",
        'typeAdres[not]': [
        "typeAdres[not]_example"
    ],
        'typeAdresseerbaarObjectCode': 1,
        'typeAdresseerbaarObjectCode[gt]': 1,
        'typeAdresseerbaarObjectCode[gte]': 1,
        'typeAdresseerbaarObjectCode[in]': [
        1
    ],
        'typeAdresseerbaarObjectCode[isnull]': True,
        'typeAdresseerbaarObjectCode[lt]': 1,
        'typeAdresseerbaarObjectCode[lte]': 1,
        'typeAdresseerbaarObjectCode[not]': [
        1
    ],
        'typeAdresseerbaarObjectOmschrijving': "typeAdresseerbaarObjectOmschrijving_example",
        'typeAdresseerbaarObjectOmschrijving[in]': [
        "typeAdresseerbaarObjectOmschrijving[in]_example"
    ],
        'typeAdresseerbaarObjectOmschrijving[isempty]': True,
        'typeAdresseerbaarObjectOmschrijving[isnull]': True,
        'typeAdresseerbaarObjectOmschrijving[like]': "typeAdresseerbaarObjectOmschrijving[like]_example",
        'typeAdresseerbaarObjectOmschrijving[not]': [
        "typeAdresseerbaarObjectOmschrijving[not]_example"
    ],
        'volgnummer': 1,
        'volgnummer[gt]': 1,
        'volgnummer[gte]': 1,
        'volgnummer[in]': [
        1
    ],
        'volgnummer[isnull]': True,
        'volgnummer[lt]': 1,
        'volgnummer[lte]': 1,
        'volgnummer[not]': [
        1
    ],
    }
    header_params = {
        'Accept-Crs': "Accept-Crs_example",
        'Content-Crs': "Content-Crs_example",
    }
    try:
        api_response = api_instance.bag_nummeraanduidingen_list(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NummeraanduidingenApi->bag_nummeraanduidingen_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/hal+json', 'text/csv', 'application/geo+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
_count | CountSchema | | optional
_expand | ExpandSchema | | optional
_expandScope | ExpandScopeSchema | | optional
_fields | FieldsSchema | | optional
_format | FormatSchema | | optional
_pageSize | PageSizeSchema | | optional
_sort | SortSchema | | optional
adresseertLigplaats.identificatie | AdresseertLigplaatsIdentificatieSchema | | optional
adresseertLigplaats.identificatie[in] | AdresseertLigplaatsIdentificatieInSchema | | optional
adresseertLigplaats.identificatie[isempty] | AdresseertLigplaatsIdentificatieIsemptySchema | | optional
adresseertLigplaats.identificatie[isnull] | AdresseertLigplaatsIdentificatieIsnullSchema | | optional
adresseertLigplaats.identificatie[like] | AdresseertLigplaatsIdentificatieLikeSchema | | optional
adresseertLigplaats.identificatie[not] | AdresseertLigplaatsIdentificatieNotSchema | | optional
adresseertLigplaats.volgnummer | AdresseertLigplaatsVolgnummerSchema | | optional
adresseertLigplaats.volgnummer[gt] | AdresseertLigplaatsVolgnummerGtSchema | | optional
adresseertLigplaats.volgnummer[gte] | AdresseertLigplaatsVolgnummerGteSchema | | optional
adresseertLigplaats.volgnummer[in] | AdresseertLigplaatsVolgnummerInSchema | | optional
adresseertLigplaats.volgnummer[isnull] | AdresseertLigplaatsVolgnummerIsnullSchema | | optional
adresseertLigplaats.volgnummer[lt] | AdresseertLigplaatsVolgnummerLtSchema | | optional
adresseertLigplaats.volgnummer[lte] | AdresseertLigplaatsVolgnummerLteSchema | | optional
adresseertLigplaats.volgnummer[not] | AdresseertLigplaatsVolgnummerNotSchema | | optional
adresseertStandplaats.identificatie | AdresseertStandplaatsIdentificatieSchema | | optional
adresseertStandplaats.identificatie[in] | AdresseertStandplaatsIdentificatieInSchema | | optional
adresseertStandplaats.identificatie[isempty] | AdresseertStandplaatsIdentificatieIsemptySchema | | optional
adresseertStandplaats.identificatie[isnull] | AdresseertStandplaatsIdentificatieIsnullSchema | | optional
adresseertStandplaats.identificatie[like] | AdresseertStandplaatsIdentificatieLikeSchema | | optional
adresseertStandplaats.identificatie[not] | AdresseertStandplaatsIdentificatieNotSchema | | optional
adresseertStandplaats.volgnummer | AdresseertStandplaatsVolgnummerSchema | | optional
adresseertStandplaats.volgnummer[gt] | AdresseertStandplaatsVolgnummerGtSchema | | optional
adresseertStandplaats.volgnummer[gte] | AdresseertStandplaatsVolgnummerGteSchema | | optional
adresseertStandplaats.volgnummer[in] | AdresseertStandplaatsVolgnummerInSchema | | optional
adresseertStandplaats.volgnummer[isnull] | AdresseertStandplaatsVolgnummerIsnullSchema | | optional
adresseertStandplaats.volgnummer[lt] | AdresseertStandplaatsVolgnummerLtSchema | | optional
adresseertStandplaats.volgnummer[lte] | AdresseertStandplaatsVolgnummerLteSchema | | optional
adresseertStandplaats.volgnummer[not] | AdresseertStandplaatsVolgnummerNotSchema | | optional
adresseertVerblijfsobject.identificatie | AdresseertVerblijfsobjectIdentificatieSchema | | optional
adresseertVerblijfsobject.identificatie[in] | AdresseertVerblijfsobjectIdentificatieInSchema | | optional
adresseertVerblijfsobject.identificatie[isempty] | AdresseertVerblijfsobjectIdentificatieIsemptySchema | | optional
adresseertVerblijfsobject.identificatie[isnull] | AdresseertVerblijfsobjectIdentificatieIsnullSchema | | optional
adresseertVerblijfsobject.identificatie[like] | AdresseertVerblijfsobjectIdentificatieLikeSchema | | optional
adresseertVerblijfsobject.identificatie[not] | AdresseertVerblijfsobjectIdentificatieNotSchema | | optional
adresseertVerblijfsobject.volgnummer | AdresseertVerblijfsobjectVolgnummerSchema | | optional
adresseertVerblijfsobject.volgnummer[gt] | AdresseertVerblijfsobjectVolgnummerGtSchema | | optional
adresseertVerblijfsobject.volgnummer[gte] | AdresseertVerblijfsobjectVolgnummerGteSchema | | optional
adresseertVerblijfsobject.volgnummer[in] | AdresseertVerblijfsobjectVolgnummerInSchema | | optional
adresseertVerblijfsobject.volgnummer[isnull] | AdresseertVerblijfsobjectVolgnummerIsnullSchema | | optional
adresseertVerblijfsobject.volgnummer[lt] | AdresseertVerblijfsobjectVolgnummerLtSchema | | optional
adresseertVerblijfsobject.volgnummer[lte] | AdresseertVerblijfsobjectVolgnummerLteSchema | | optional
adresseertVerblijfsobject.volgnummer[not] | AdresseertVerblijfsobjectVolgnummerNotSchema | | optional
bagprocesCode | BagprocesCodeSchema | | optional
bagprocesCode[gt] | BagprocesCodeGtSchema | | optional
bagprocesCode[gte] | BagprocesCodeGteSchema | | optional
bagprocesCode[in] | BagprocesCodeInSchema | | optional
bagprocesCode[isnull] | BagprocesCodeIsnullSchema | | optional
bagprocesCode[lt] | BagprocesCodeLtSchema | | optional
bagprocesCode[lte] | BagprocesCodeLteSchema | | optional
bagprocesCode[not] | BagprocesCodeNotSchema | | optional
bagprocesOmschrijving | BagprocesOmschrijvingSchema | | optional
bagprocesOmschrijving[in] | BagprocesOmschrijvingInSchema | | optional
bagprocesOmschrijving[isempty] | BagprocesOmschrijvingIsemptySchema | | optional
bagprocesOmschrijving[isnull] | BagprocesOmschrijvingIsnullSchema | | optional
bagprocesOmschrijving[like] | BagprocesOmschrijvingLikeSchema | | optional
bagprocesOmschrijving[not] | BagprocesOmschrijvingNotSchema | | optional
beginGeldigheid | BeginGeldigheidSchema | | optional
beginGeldigheid[gt] | BeginGeldigheidGtSchema | | optional
beginGeldigheid[gte] | BeginGeldigheidGteSchema | | optional
beginGeldigheid[in] | BeginGeldigheidInSchema | | optional
beginGeldigheid[isnull] | BeginGeldigheidIsnullSchema | | optional
beginGeldigheid[lt] | BeginGeldigheidLtSchema | | optional
beginGeldigheid[lte] | BeginGeldigheidLteSchema | | optional
beginGeldigheid[not] | BeginGeldigheidNotSchema | | optional
documentdatum | DocumentdatumSchema | | optional
documentdatum[gt] | DocumentdatumGtSchema | | optional
documentdatum[gte] | DocumentdatumGteSchema | | optional
documentdatum[in] | DocumentdatumInSchema | | optional
documentdatum[isnull] | DocumentdatumIsnullSchema | | optional
documentdatum[lt] | DocumentdatumLtSchema | | optional
documentdatum[lte] | DocumentdatumLteSchema | | optional
documentdatum[not] | DocumentdatumNotSchema | | optional
documentnummer | DocumentnummerSchema | | optional
documentnummer[in] | DocumentnummerInSchema | | optional
documentnummer[isempty] | DocumentnummerIsemptySchema | | optional
documentnummer[isnull] | DocumentnummerIsnullSchema | | optional
documentnummer[like] | DocumentnummerLikeSchema | | optional
documentnummer[not] | DocumentnummerNotSchema | | optional
eindGeldigheid | EindGeldigheidSchema | | optional
eindGeldigheid[gt] | EindGeldigheidGtSchema | | optional
eindGeldigheid[gte] | EindGeldigheidGteSchema | | optional
eindGeldigheid[in] | EindGeldigheidInSchema | | optional
eindGeldigheid[isnull] | EindGeldigheidIsnullSchema | | optional
eindGeldigheid[lt] | EindGeldigheidLtSchema | | optional
eindGeldigheid[lte] | EindGeldigheidLteSchema | | optional
eindGeldigheid[not] | EindGeldigheidNotSchema | | optional
geconstateerd | GeconstateerdSchema | | optional
geconstateerd[isnull] | GeconstateerdIsnullSchema | | optional
geldigOp | GeldigOpSchema | | optional
geldigOp[gt] | GeldigOpGtSchema | | optional
geldigOp[gte] | GeldigOpGteSchema | | optional
geldigOp[in] | GeldigOpInSchema | | optional
geldigOp[isnull] | GeldigOpIsnullSchema | | optional
geldigOp[lt] | GeldigOpLtSchema | | optional
geldigOp[lte] | GeldigOpLteSchema | | optional
geldigOp[not] | GeldigOpNotSchema | | optional
heeftDossier.dossier | HeeftDossierDossierSchema | | optional
heeftDossier.dossier[in] | HeeftDossierDossierInSchema | | optional
heeftDossier.dossier[isempty] | HeeftDossierDossierIsemptySchema | | optional
heeftDossier.dossier[isnull] | HeeftDossierDossierIsnullSchema | | optional
heeftDossier.dossier[like] | HeeftDossierDossierLikeSchema | | optional
heeftDossier.dossier[not] | HeeftDossierDossierNotSchema | | optional
heeftOnderzoeken.identificatie | HeeftOnderzoekenIdentificatieSchema | | optional
heeftOnderzoeken.identificatie[in] | HeeftOnderzoekenIdentificatieInSchema | | optional
heeftOnderzoeken.identificatie[isempty] | HeeftOnderzoekenIdentificatieIsemptySchema | | optional
heeftOnderzoeken.identificatie[isnull] | HeeftOnderzoekenIdentificatieIsnullSchema | | optional
heeftOnderzoeken.identificatie[like] | HeeftOnderzoekenIdentificatieLikeSchema | | optional
heeftOnderzoeken.identificatie[not] | HeeftOnderzoekenIdentificatieNotSchema | | optional
heeftOnderzoeken.volgnummer | HeeftOnderzoekenVolgnummerSchema | | optional
heeftOnderzoeken.volgnummer[gt] | HeeftOnderzoekenVolgnummerGtSchema | | optional
heeftOnderzoeken.volgnummer[gte] | HeeftOnderzoekenVolgnummerGteSchema | | optional
heeftOnderzoeken.volgnummer[in] | HeeftOnderzoekenVolgnummerInSchema | | optional
heeftOnderzoeken.volgnummer[isnull] | HeeftOnderzoekenVolgnummerIsnullSchema | | optional
heeftOnderzoeken.volgnummer[lt] | HeeftOnderzoekenVolgnummerLtSchema | | optional
heeftOnderzoeken.volgnummer[lte] | HeeftOnderzoekenVolgnummerLteSchema | | optional
heeftOnderzoeken.volgnummer[not] | HeeftOnderzoekenVolgnummerNotSchema | | optional
huisletter | HuisletterSchema | | optional
huisletter[in] | HuisletterInSchema | | optional
huisletter[isempty] | HuisletterIsemptySchema | | optional
huisletter[isnull] | HuisletterIsnullSchema | | optional
huisletter[like] | HuisletterLikeSchema | | optional
huisletter[not] | HuisletterNotSchema | | optional
huisnummer | HuisnummerSchema | | optional
huisnummer[gt] | HuisnummerGtSchema | | optional
huisnummer[gte] | HuisnummerGteSchema | | optional
huisnummer[in] | HuisnummerInSchema | | optional
huisnummer[isnull] | HuisnummerIsnullSchema | | optional
huisnummer[lt] | HuisnummerLtSchema | | optional
huisnummer[lte] | HuisnummerLteSchema | | optional
huisnummer[not] | HuisnummerNotSchema | | optional
huisnummertoevoeging | HuisnummertoevoegingSchema | | optional
huisnummertoevoeging[in] | HuisnummertoevoegingInSchema | | optional
huisnummertoevoeging[isempty] | HuisnummertoevoegingIsemptySchema | | optional
huisnummertoevoeging[isnull] | HuisnummertoevoegingIsnullSchema | | optional
huisnummertoevoeging[like] | HuisnummertoevoegingLikeSchema | | optional
huisnummertoevoeging[not] | HuisnummertoevoegingNotSchema | | optional
id | IdSchema | | optional
id[in] | IdInSchema | | optional
id[isempty] | IdIsemptySchema | | optional
id[isnull] | IdIsnullSchema | | optional
id[like] | IdLikeSchema | | optional
id[not] | IdNotSchema | | optional
identificatie | IdentificatieSchema | | optional
identificatie[in] | IdentificatieInSchema | | optional
identificatie[isempty] | IdentificatieIsemptySchema | | optional
identificatie[isnull] | IdentificatieIsnullSchema | | optional
identificatie[like] | IdentificatieLikeSchema | | optional
identificatie[not] | IdentificatieNotSchema | | optional
ligtAanOpenbareruimte.identificatie | LigtAanOpenbareruimteIdentificatieSchema | | optional
ligtAanOpenbareruimte.identificatie[in] | LigtAanOpenbareruimteIdentificatieInSchema | | optional
ligtAanOpenbareruimte.identificatie[isempty] | LigtAanOpenbareruimteIdentificatieIsemptySchema | | optional
ligtAanOpenbareruimte.identificatie[isnull] | LigtAanOpenbareruimteIdentificatieIsnullSchema | | optional
ligtAanOpenbareruimte.identificatie[like] | LigtAanOpenbareruimteIdentificatieLikeSchema | | optional
ligtAanOpenbareruimte.identificatie[not] | LigtAanOpenbareruimteIdentificatieNotSchema | | optional
ligtAanOpenbareruimte.volgnummer | LigtAanOpenbareruimteVolgnummerSchema | | optional
ligtAanOpenbareruimte.volgnummer[gt] | LigtAanOpenbareruimteVolgnummerGtSchema | | optional
ligtAanOpenbareruimte.volgnummer[gte] | LigtAanOpenbareruimteVolgnummerGteSchema | | optional
ligtAanOpenbareruimte.volgnummer[in] | LigtAanOpenbareruimteVolgnummerInSchema | | optional
ligtAanOpenbareruimte.volgnummer[isnull] | LigtAanOpenbareruimteVolgnummerIsnullSchema | | optional
ligtAanOpenbareruimte.volgnummer[lt] | LigtAanOpenbareruimteVolgnummerLtSchema | | optional
ligtAanOpenbareruimte.volgnummer[lte] | LigtAanOpenbareruimteVolgnummerLteSchema | | optional
ligtAanOpenbareruimte.volgnummer[not] | LigtAanOpenbareruimteVolgnummerNotSchema | | optional
ligtInWoonplaats.identificatie | LigtInWoonplaatsIdentificatieSchema | | optional
ligtInWoonplaats.identificatie[in] | LigtInWoonplaatsIdentificatieInSchema | | optional
ligtInWoonplaats.identificatie[isempty] | LigtInWoonplaatsIdentificatieIsemptySchema | | optional
ligtInWoonplaats.identificatie[isnull] | LigtInWoonplaatsIdentificatieIsnullSchema | | optional
ligtInWoonplaats.identificatie[like] | LigtInWoonplaatsIdentificatieLikeSchema | | optional
ligtInWoonplaats.identificatie[not] | LigtInWoonplaatsIdentificatieNotSchema | | optional
ligtInWoonplaats.volgnummer | LigtInWoonplaatsVolgnummerSchema | | optional
ligtInWoonplaats.volgnummer[gt] | LigtInWoonplaatsVolgnummerGtSchema | | optional
ligtInWoonplaats.volgnummer[gte] | LigtInWoonplaatsVolgnummerGteSchema | | optional
ligtInWoonplaats.volgnummer[in] | LigtInWoonplaatsVolgnummerInSchema | | optional
ligtInWoonplaats.volgnummer[isnull] | LigtInWoonplaatsVolgnummerIsnullSchema | | optional
ligtInWoonplaats.volgnummer[lt] | LigtInWoonplaatsVolgnummerLtSchema | | optional
ligtInWoonplaats.volgnummer[lte] | LigtInWoonplaatsVolgnummerLteSchema | | optional
ligtInWoonplaats.volgnummer[not] | LigtInWoonplaatsVolgnummerNotSchema | | optional
page | PageSchema | | optional
postcode | PostcodeSchema | | optional
postcode[in] | PostcodeInSchema | | optional
postcode[isempty] | PostcodeIsemptySchema | | optional
postcode[isnull] | PostcodeIsnullSchema | | optional
postcode[like] | PostcodeLikeSchema | | optional
postcode[not] | PostcodeNotSchema | | optional
registratiedatum | RegistratiedatumSchema | | optional
registratiedatum[gt] | RegistratiedatumGtSchema | | optional
registratiedatum[gte] | RegistratiedatumGteSchema | | optional
registratiedatum[in] | RegistratiedatumInSchema | | optional
registratiedatum[isnull] | RegistratiedatumIsnullSchema | | optional
registratiedatum[lt] | RegistratiedatumLtSchema | | optional
registratiedatum[lte] | RegistratiedatumLteSchema | | optional
registratiedatum[not] | RegistratiedatumNotSchema | | optional
statusCode | StatusCodeSchema | | optional
statusCode[gt] | StatusCodeGtSchema | | optional
statusCode[gte] | StatusCodeGteSchema | | optional
statusCode[in] | StatusCodeInSchema | | optional
statusCode[isnull] | StatusCodeIsnullSchema | | optional
statusCode[lt] | StatusCodeLtSchema | | optional
statusCode[lte] | StatusCodeLteSchema | | optional
statusCode[not] | StatusCodeNotSchema | | optional
statusOmschrijving | StatusOmschrijvingSchema | | optional
statusOmschrijving[in] | StatusOmschrijvingInSchema | | optional
statusOmschrijving[isempty] | StatusOmschrijvingIsemptySchema | | optional
statusOmschrijving[isnull] | StatusOmschrijvingIsnullSchema | | optional
statusOmschrijving[like] | StatusOmschrijvingLikeSchema | | optional
statusOmschrijving[not] | StatusOmschrijvingNotSchema | | optional
typeAdres | TypeAdresSchema | | optional
typeAdres[in] | TypeAdresInSchema | | optional
typeAdres[isempty] | TypeAdresIsemptySchema | | optional
typeAdres[isnull] | TypeAdresIsnullSchema | | optional
typeAdres[like] | TypeAdresLikeSchema | | optional
typeAdres[not] | TypeAdresNotSchema | | optional
typeAdresseerbaarObjectCode | TypeAdresseerbaarObjectCodeSchema | | optional
typeAdresseerbaarObjectCode[gt] | TypeAdresseerbaarObjectCodeGtSchema | | optional
typeAdresseerbaarObjectCode[gte] | TypeAdresseerbaarObjectCodeGteSchema | | optional
typeAdresseerbaarObjectCode[in] | TypeAdresseerbaarObjectCodeInSchema | | optional
typeAdresseerbaarObjectCode[isnull] | TypeAdresseerbaarObjectCodeIsnullSchema | | optional
typeAdresseerbaarObjectCode[lt] | TypeAdresseerbaarObjectCodeLtSchema | | optional
typeAdresseerbaarObjectCode[lte] | TypeAdresseerbaarObjectCodeLteSchema | | optional
typeAdresseerbaarObjectCode[not] | TypeAdresseerbaarObjectCodeNotSchema | | optional
typeAdresseerbaarObjectOmschrijving | TypeAdresseerbaarObjectOmschrijvingSchema | | optional
typeAdresseerbaarObjectOmschrijving[in] | TypeAdresseerbaarObjectOmschrijvingInSchema | | optional
typeAdresseerbaarObjectOmschrijving[isempty] | TypeAdresseerbaarObjectOmschrijvingIsemptySchema | | optional
typeAdresseerbaarObjectOmschrijving[isnull] | TypeAdresseerbaarObjectOmschrijvingIsnullSchema | | optional
typeAdresseerbaarObjectOmschrijving[like] | TypeAdresseerbaarObjectOmschrijvingLikeSchema | | optional
typeAdresseerbaarObjectOmschrijving[not] | TypeAdresseerbaarObjectOmschrijvingNotSchema | | optional
volgnummer | VolgnummerSchema | | optional
volgnummer[gt] | VolgnummerGtSchema | | optional
volgnummer[gte] | VolgnummerGteSchema | | optional
volgnummer[in] | VolgnummerInSchema | | optional
volgnummer[isnull] | VolgnummerIsnullSchema | | optional
volgnummer[lt] | VolgnummerLtSchema | | optional
volgnummer[lte] | VolgnummerLteSchema | | optional
volgnummer[not] | VolgnummerNotSchema | | optional


# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ExpandSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ExpandScopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "csv", "geojson", ] 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertLigplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertStandplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertVerblijfsobjectVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BagprocesOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BagprocesOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BagprocesOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BeginGeldigheidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeginGeldigheidLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# DocumentdatumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentdatumLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DocumentnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DocumentnummerIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentnummerLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DocumentnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# EindGeldigheidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EindGeldigheidLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeconstateerdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GeconstateerdIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GeldigOpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# HeeftDossierDossierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftDossierDossierInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftDossierDossierIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftDossierDossierIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftDossierDossierLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftDossierDossierNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisletterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisletterInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisletterIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisletterIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisletterLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisletterNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummertoevoegingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisnummertoevoegingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisnummertoevoegingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummertoevoegingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummertoevoegingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisnummertoevoegingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInWoonplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PostcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PostcodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PostcodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PostcodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PostcodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PostcodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RegistratiedatumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RegistratiedatumLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# StatusCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StatusOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresseerbaarObjectCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# VolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# VolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Crs | AcceptCrsSchema | | optional
Content-Crs | ContentCrsSchema | | optional

# AcceptCrsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentCrsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bag_nummeraanduidingen_list.ApiResponseFor200) | 

#### bag_nummeraanduidingen_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagnummeraanduidingenList**](../../models/PaginatedBagnummeraanduidingenList.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagnummeraanduidingenList**](../../models/PaginatedBagnummeraanduidingenList.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagnummeraanduidingenList**](../../models/PaginatedBagnummeraanduidingenList.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bag_nummeraanduidingen_retrieve**
<a id="bag_nummeraanduidingen_retrieve"></a>
> Bagnummeraanduidingen bag_nummeraanduidingen_retrieve(id)



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import nummeraanduidingen_api
from openapi_client.model.bagnummeraanduidingen import Bagnummeraanduidingen
from pprint import pprint
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
    api_instance = nummeraanduidingen_api.NummeraanduidingenApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "k",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.bag_nummeraanduidingen_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NummeraanduidingenApi->bag_nummeraanduidingen_retrieve: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "k",
    }
    query_params = {
        '_expand': True,
        '_expandScope': "adresseertLigplaats",
        '_fields': "_fields_example",
        '_format': "json",
        '_sort': "_sort_example",
        'adresseertLigplaats.identificatie': "adresseertLigplaats.identificatie_example",
        'adresseertLigplaats.identificatie[in]': [
        "adresseertLigplaats.identificatie[in]_example"
    ],
        'adresseertLigplaats.identificatie[isempty]': True,
        'adresseertLigplaats.identificatie[isnull]': True,
        'adresseertLigplaats.identificatie[like]': "adresseertLigplaats.identificatie[like]_example",
        'adresseertLigplaats.identificatie[not]': [
        "adresseertLigplaats.identificatie[not]_example"
    ],
        'adresseertLigplaats.volgnummer': 1,
        'adresseertLigplaats.volgnummer[gt]': 1,
        'adresseertLigplaats.volgnummer[gte]': 1,
        'adresseertLigplaats.volgnummer[in]': [
        1
    ],
        'adresseertLigplaats.volgnummer[isnull]': True,
        'adresseertLigplaats.volgnummer[lt]': 1,
        'adresseertLigplaats.volgnummer[lte]': 1,
        'adresseertLigplaats.volgnummer[not]': [
        1
    ],
        'adresseertStandplaats.identificatie': "adresseertStandplaats.identificatie_example",
        'adresseertStandplaats.identificatie[in]': [
        "adresseertStandplaats.identificatie[in]_example"
    ],
        'adresseertStandplaats.identificatie[isempty]': True,
        'adresseertStandplaats.identificatie[isnull]': True,
        'adresseertStandplaats.identificatie[like]': "adresseertStandplaats.identificatie[like]_example",
        'adresseertStandplaats.identificatie[not]': [
        "adresseertStandplaats.identificatie[not]_example"
    ],
        'adresseertStandplaats.volgnummer': 1,
        'adresseertStandplaats.volgnummer[gt]': 1,
        'adresseertStandplaats.volgnummer[gte]': 1,
        'adresseertStandplaats.volgnummer[in]': [
        1
    ],
        'adresseertStandplaats.volgnummer[isnull]': True,
        'adresseertStandplaats.volgnummer[lt]': 1,
        'adresseertStandplaats.volgnummer[lte]': 1,
        'adresseertStandplaats.volgnummer[not]': [
        1
    ],
        'adresseertVerblijfsobject.identificatie': "adresseertVerblijfsobject.identificatie_example",
        'adresseertVerblijfsobject.identificatie[in]': [
        "adresseertVerblijfsobject.identificatie[in]_example"
    ],
        'adresseertVerblijfsobject.identificatie[isempty]': True,
        'adresseertVerblijfsobject.identificatie[isnull]': True,
        'adresseertVerblijfsobject.identificatie[like]': "adresseertVerblijfsobject.identificatie[like]_example",
        'adresseertVerblijfsobject.identificatie[not]': [
        "adresseertVerblijfsobject.identificatie[not]_example"
    ],
        'adresseertVerblijfsobject.volgnummer': 1,
        'adresseertVerblijfsobject.volgnummer[gt]': 1,
        'adresseertVerblijfsobject.volgnummer[gte]': 1,
        'adresseertVerblijfsobject.volgnummer[in]': [
        1
    ],
        'adresseertVerblijfsobject.volgnummer[isnull]': True,
        'adresseertVerblijfsobject.volgnummer[lt]': 1,
        'adresseertVerblijfsobject.volgnummer[lte]': 1,
        'adresseertVerblijfsobject.volgnummer[not]': [
        1
    ],
        'bagprocesCode': 1,
        'bagprocesCode[gt]': 1,
        'bagprocesCode[gte]': 1,
        'bagprocesCode[in]': [
        1
    ],
        'bagprocesCode[isnull]': True,
        'bagprocesCode[lt]': 1,
        'bagprocesCode[lte]': 1,
        'bagprocesCode[not]': [
        1
    ],
        'bagprocesOmschrijving': "bagprocesOmschrijving_example",
        'bagprocesOmschrijving[in]': [
        "bagprocesOmschrijving[in]_example"
    ],
        'bagprocesOmschrijving[isempty]': True,
        'bagprocesOmschrijving[isnull]': True,
        'bagprocesOmschrijving[like]': "bagprocesOmschrijving[like]_example",
        'bagprocesOmschrijving[not]': [
        "bagprocesOmschrijving[not]_example"
    ],
        'beginGeldigheid': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[gt]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[gte]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'beginGeldigheid[isnull]': True,
        'beginGeldigheid[lt]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[lte]': "1970-01-01T00:00:00.00Z",
        'beginGeldigheid[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'documentdatum': "1970-01-01",
        'documentdatum[gt]': "1970-01-01",
        'documentdatum[gte]': "1970-01-01",
        'documentdatum[in]': [
        "1970-01-01"
    ],
        'documentdatum[isnull]': True,
        'documentdatum[lt]': "1970-01-01",
        'documentdatum[lte]': "1970-01-01",
        'documentdatum[not]': [
        "1970-01-01"
    ],
        'documentnummer': "documentnummer_example",
        'documentnummer[in]': [
        "documentnummer[in]_example"
    ],
        'documentnummer[isempty]': True,
        'documentnummer[isnull]': True,
        'documentnummer[like]': "documentnummer[like]_example",
        'documentnummer[not]': [
        "documentnummer[not]_example"
    ],
        'eindGeldigheid': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[gt]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[gte]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'eindGeldigheid[isnull]': True,
        'eindGeldigheid[lt]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[lte]': "1970-01-01T00:00:00.00Z",
        'eindGeldigheid[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'geconstateerd': True,
        'geconstateerd[isnull]': True,
        'geldigOp': "1970-01-01T00:00:00.00Z",
        'geldigOp[gt]': "1970-01-01T00:00:00.00Z",
        'geldigOp[gte]': "1970-01-01T00:00:00.00Z",
        'geldigOp[in]': "1970-01-01T00:00:00.00Z",
        'geldigOp[isnull]': "1970-01-01T00:00:00.00Z",
        'geldigOp[lt]': "1970-01-01T00:00:00.00Z",
        'geldigOp[lte]': "1970-01-01T00:00:00.00Z",
        'geldigOp[not]': "1970-01-01T00:00:00.00Z",
        'heeftDossier.dossier': "heeftDossier.dossier_example",
        'heeftDossier.dossier[in]': [
        "heeftDossier.dossier[in]_example"
    ],
        'heeftDossier.dossier[isempty]': True,
        'heeftDossier.dossier[isnull]': True,
        'heeftDossier.dossier[like]': "heeftDossier.dossier[like]_example",
        'heeftDossier.dossier[not]': [
        "heeftDossier.dossier[not]_example"
    ],
        'heeftOnderzoeken.identificatie': "heeftOnderzoeken.identificatie_example",
        'heeftOnderzoeken.identificatie[in]': [
        "heeftOnderzoeken.identificatie[in]_example"
    ],
        'heeftOnderzoeken.identificatie[isempty]': True,
        'heeftOnderzoeken.identificatie[isnull]': True,
        'heeftOnderzoeken.identificatie[like]': "heeftOnderzoeken.identificatie[like]_example",
        'heeftOnderzoeken.identificatie[not]': [
        "heeftOnderzoeken.identificatie[not]_example"
    ],
        'heeftOnderzoeken.volgnummer': 1,
        'heeftOnderzoeken.volgnummer[gt]': 1,
        'heeftOnderzoeken.volgnummer[gte]': 1,
        'heeftOnderzoeken.volgnummer[in]': [
        1
    ],
        'heeftOnderzoeken.volgnummer[isnull]': True,
        'heeftOnderzoeken.volgnummer[lt]': 1,
        'heeftOnderzoeken.volgnummer[lte]': 1,
        'heeftOnderzoeken.volgnummer[not]': [
        1
    ],
        'huisletter': "huisletter_example",
        'huisletter[in]': [
        "huisletter[in]_example"
    ],
        'huisletter[isempty]': True,
        'huisletter[isnull]': True,
        'huisletter[like]': "huisletter[like]_example",
        'huisletter[not]': [
        "huisletter[not]_example"
    ],
        'huisnummer': 1,
        'huisnummer[gt]': 1,
        'huisnummer[gte]': 1,
        'huisnummer[in]': [
        1
    ],
        'huisnummer[isnull]': True,
        'huisnummer[lt]': 1,
        'huisnummer[lte]': 1,
        'huisnummer[not]': [
        1
    ],
        'huisnummertoevoeging': "huisnummertoevoeging_example",
        'huisnummertoevoeging[in]': [
        "huisnummertoevoeging[in]_example"
    ],
        'huisnummertoevoeging[isempty]': True,
        'huisnummertoevoeging[isnull]': True,
        'huisnummertoevoeging[like]': "huisnummertoevoeging[like]_example",
        'huisnummertoevoeging[not]': [
        "huisnummertoevoeging[not]_example"
    ],
        'id': "id_example",
        'id[in]': [
        "id[in]_example"
    ],
        'id[isempty]': True,
        'id[isnull]': True,
        'id[like]': "id[like]_example",
        'id[not]': [
        "id[not]_example"
    ],
        'identificatie': "identificatie_example",
        'identificatie[in]': [
        "identificatie[in]_example"
    ],
        'identificatie[isempty]': True,
        'identificatie[isnull]': True,
        'identificatie[like]': "identificatie[like]_example",
        'identificatie[not]': [
        "identificatie[not]_example"
    ],
        'ligtAanOpenbareruimte.identificatie': "ligtAanOpenbareruimte.identificatie_example",
        'ligtAanOpenbareruimte.identificatie[in]': [
        "ligtAanOpenbareruimte.identificatie[in]_example"
    ],
        'ligtAanOpenbareruimte.identificatie[isempty]': True,
        'ligtAanOpenbareruimte.identificatie[isnull]': True,
        'ligtAanOpenbareruimte.identificatie[like]': "ligtAanOpenbareruimte.identificatie[like]_example",
        'ligtAanOpenbareruimte.identificatie[not]': [
        "ligtAanOpenbareruimte.identificatie[not]_example"
    ],
        'ligtAanOpenbareruimte.volgnummer': 1,
        'ligtAanOpenbareruimte.volgnummer[gt]': 1,
        'ligtAanOpenbareruimte.volgnummer[gte]': 1,
        'ligtAanOpenbareruimte.volgnummer[in]': [
        1
    ],
        'ligtAanOpenbareruimte.volgnummer[isnull]': True,
        'ligtAanOpenbareruimte.volgnummer[lt]': 1,
        'ligtAanOpenbareruimte.volgnummer[lte]': 1,
        'ligtAanOpenbareruimte.volgnummer[not]': [
        1
    ],
        'ligtInWoonplaats.identificatie': "ligtInWoonplaats.identificatie_example",
        'ligtInWoonplaats.identificatie[in]': [
        "ligtInWoonplaats.identificatie[in]_example"
    ],
        'ligtInWoonplaats.identificatie[isempty]': True,
        'ligtInWoonplaats.identificatie[isnull]': True,
        'ligtInWoonplaats.identificatie[like]': "ligtInWoonplaats.identificatie[like]_example",
        'ligtInWoonplaats.identificatie[not]': [
        "ligtInWoonplaats.identificatie[not]_example"
    ],
        'ligtInWoonplaats.volgnummer': 1,
        'ligtInWoonplaats.volgnummer[gt]': 1,
        'ligtInWoonplaats.volgnummer[gte]': 1,
        'ligtInWoonplaats.volgnummer[in]': [
        1
    ],
        'ligtInWoonplaats.volgnummer[isnull]': True,
        'ligtInWoonplaats.volgnummer[lt]': 1,
        'ligtInWoonplaats.volgnummer[lte]': 1,
        'ligtInWoonplaats.volgnummer[not]': [
        1
    ],
        'postcode': "postcode_example",
        'postcode[in]': [
        "postcode[in]_example"
    ],
        'postcode[isempty]': True,
        'postcode[isnull]': True,
        'postcode[like]': "postcode[like]_example",
        'postcode[not]': [
        "postcode[not]_example"
    ],
        'registratiedatum': "1970-01-01T00:00:00.00Z",
        'registratiedatum[gt]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[gte]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[in]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'registratiedatum[isnull]': True,
        'registratiedatum[lt]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[lte]': "1970-01-01T00:00:00.00Z",
        'registratiedatum[not]': [
        "1970-01-01T00:00:00.00Z"
    ],
        'statusCode': 1,
        'statusCode[gt]': 1,
        'statusCode[gte]': 1,
        'statusCode[in]': [
        1
    ],
        'statusCode[isnull]': True,
        'statusCode[lt]': 1,
        'statusCode[lte]': 1,
        'statusCode[not]': [
        1
    ],
        'statusOmschrijving': "statusOmschrijving_example",
        'statusOmschrijving[in]': [
        "statusOmschrijving[in]_example"
    ],
        'statusOmschrijving[isempty]': True,
        'statusOmschrijving[isnull]': True,
        'statusOmschrijving[like]': "statusOmschrijving[like]_example",
        'statusOmschrijving[not]': [
        "statusOmschrijving[not]_example"
    ],
        'typeAdres': "typeAdres_example",
        'typeAdres[in]': [
        "typeAdres[in]_example"
    ],
        'typeAdres[isempty]': True,
        'typeAdres[isnull]': True,
        'typeAdres[like]': "typeAdres[like]_example",
        'typeAdres[not]': [
        "typeAdres[not]_example"
    ],
        'typeAdresseerbaarObjectCode': 1,
        'typeAdresseerbaarObjectCode[gt]': 1,
        'typeAdresseerbaarObjectCode[gte]': 1,
        'typeAdresseerbaarObjectCode[in]': [
        1
    ],
        'typeAdresseerbaarObjectCode[isnull]': True,
        'typeAdresseerbaarObjectCode[lt]': 1,
        'typeAdresseerbaarObjectCode[lte]': 1,
        'typeAdresseerbaarObjectCode[not]': [
        1
    ],
        'typeAdresseerbaarObjectOmschrijving': "typeAdresseerbaarObjectOmschrijving_example",
        'typeAdresseerbaarObjectOmschrijving[in]': [
        "typeAdresseerbaarObjectOmschrijving[in]_example"
    ],
        'typeAdresseerbaarObjectOmschrijving[isempty]': True,
        'typeAdresseerbaarObjectOmschrijving[isnull]': True,
        'typeAdresseerbaarObjectOmschrijving[like]': "typeAdresseerbaarObjectOmschrijving[like]_example",
        'typeAdresseerbaarObjectOmschrijving[not]': [
        "typeAdresseerbaarObjectOmschrijving[not]_example"
    ],
        'volgnummer': 1,
        'volgnummer[gt]': 1,
        'volgnummer[gte]': 1,
        'volgnummer[in]': [
        1
    ],
        'volgnummer[isnull]': True,
        'volgnummer[lt]': 1,
        'volgnummer[lte]': 1,
        'volgnummer[not]': [
        1
    ],
    }
    header_params = {
        'Accept-Crs': "Accept-Crs_example",
        'Content-Crs': "Content-Crs_example",
    }
    try:
        api_response = api_instance.bag_nummeraanduidingen_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NummeraanduidingenApi->bag_nummeraanduidingen_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/hal+json', 'text/csv', 'application/geo+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
_expand | ExpandSchema | | optional
_expandScope | ExpandScopeSchema | | optional
_fields | FieldsSchema | | optional
_format | FormatSchema | | optional
_sort | SortSchema | | optional
adresseertLigplaats.identificatie | AdresseertLigplaatsIdentificatieSchema | | optional
adresseertLigplaats.identificatie[in] | AdresseertLigplaatsIdentificatieInSchema | | optional
adresseertLigplaats.identificatie[isempty] | AdresseertLigplaatsIdentificatieIsemptySchema | | optional
adresseertLigplaats.identificatie[isnull] | AdresseertLigplaatsIdentificatieIsnullSchema | | optional
adresseertLigplaats.identificatie[like] | AdresseertLigplaatsIdentificatieLikeSchema | | optional
adresseertLigplaats.identificatie[not] | AdresseertLigplaatsIdentificatieNotSchema | | optional
adresseertLigplaats.volgnummer | AdresseertLigplaatsVolgnummerSchema | | optional
adresseertLigplaats.volgnummer[gt] | AdresseertLigplaatsVolgnummerGtSchema | | optional
adresseertLigplaats.volgnummer[gte] | AdresseertLigplaatsVolgnummerGteSchema | | optional
adresseertLigplaats.volgnummer[in] | AdresseertLigplaatsVolgnummerInSchema | | optional
adresseertLigplaats.volgnummer[isnull] | AdresseertLigplaatsVolgnummerIsnullSchema | | optional
adresseertLigplaats.volgnummer[lt] | AdresseertLigplaatsVolgnummerLtSchema | | optional
adresseertLigplaats.volgnummer[lte] | AdresseertLigplaatsVolgnummerLteSchema | | optional
adresseertLigplaats.volgnummer[not] | AdresseertLigplaatsVolgnummerNotSchema | | optional
adresseertStandplaats.identificatie | AdresseertStandplaatsIdentificatieSchema | | optional
adresseertStandplaats.identificatie[in] | AdresseertStandplaatsIdentificatieInSchema | | optional
adresseertStandplaats.identificatie[isempty] | AdresseertStandplaatsIdentificatieIsemptySchema | | optional
adresseertStandplaats.identificatie[isnull] | AdresseertStandplaatsIdentificatieIsnullSchema | | optional
adresseertStandplaats.identificatie[like] | AdresseertStandplaatsIdentificatieLikeSchema | | optional
adresseertStandplaats.identificatie[not] | AdresseertStandplaatsIdentificatieNotSchema | | optional
adresseertStandplaats.volgnummer | AdresseertStandplaatsVolgnummerSchema | | optional
adresseertStandplaats.volgnummer[gt] | AdresseertStandplaatsVolgnummerGtSchema | | optional
adresseertStandplaats.volgnummer[gte] | AdresseertStandplaatsVolgnummerGteSchema | | optional
adresseertStandplaats.volgnummer[in] | AdresseertStandplaatsVolgnummerInSchema | | optional
adresseertStandplaats.volgnummer[isnull] | AdresseertStandplaatsVolgnummerIsnullSchema | | optional
adresseertStandplaats.volgnummer[lt] | AdresseertStandplaatsVolgnummerLtSchema | | optional
adresseertStandplaats.volgnummer[lte] | AdresseertStandplaatsVolgnummerLteSchema | | optional
adresseertStandplaats.volgnummer[not] | AdresseertStandplaatsVolgnummerNotSchema | | optional
adresseertVerblijfsobject.identificatie | AdresseertVerblijfsobjectIdentificatieSchema | | optional
adresseertVerblijfsobject.identificatie[in] | AdresseertVerblijfsobjectIdentificatieInSchema | | optional
adresseertVerblijfsobject.identificatie[isempty] | AdresseertVerblijfsobjectIdentificatieIsemptySchema | | optional
adresseertVerblijfsobject.identificatie[isnull] | AdresseertVerblijfsobjectIdentificatieIsnullSchema | | optional
adresseertVerblijfsobject.identificatie[like] | AdresseertVerblijfsobjectIdentificatieLikeSchema | | optional
adresseertVerblijfsobject.identificatie[not] | AdresseertVerblijfsobjectIdentificatieNotSchema | | optional
adresseertVerblijfsobject.volgnummer | AdresseertVerblijfsobjectVolgnummerSchema | | optional
adresseertVerblijfsobject.volgnummer[gt] | AdresseertVerblijfsobjectVolgnummerGtSchema | | optional
adresseertVerblijfsobject.volgnummer[gte] | AdresseertVerblijfsobjectVolgnummerGteSchema | | optional
adresseertVerblijfsobject.volgnummer[in] | AdresseertVerblijfsobjectVolgnummerInSchema | | optional
adresseertVerblijfsobject.volgnummer[isnull] | AdresseertVerblijfsobjectVolgnummerIsnullSchema | | optional
adresseertVerblijfsobject.volgnummer[lt] | AdresseertVerblijfsobjectVolgnummerLtSchema | | optional
adresseertVerblijfsobject.volgnummer[lte] | AdresseertVerblijfsobjectVolgnummerLteSchema | | optional
adresseertVerblijfsobject.volgnummer[not] | AdresseertVerblijfsobjectVolgnummerNotSchema | | optional
bagprocesCode | BagprocesCodeSchema | | optional
bagprocesCode[gt] | BagprocesCodeGtSchema | | optional
bagprocesCode[gte] | BagprocesCodeGteSchema | | optional
bagprocesCode[in] | BagprocesCodeInSchema | | optional
bagprocesCode[isnull] | BagprocesCodeIsnullSchema | | optional
bagprocesCode[lt] | BagprocesCodeLtSchema | | optional
bagprocesCode[lte] | BagprocesCodeLteSchema | | optional
bagprocesCode[not] | BagprocesCodeNotSchema | | optional
bagprocesOmschrijving | BagprocesOmschrijvingSchema | | optional
bagprocesOmschrijving[in] | BagprocesOmschrijvingInSchema | | optional
bagprocesOmschrijving[isempty] | BagprocesOmschrijvingIsemptySchema | | optional
bagprocesOmschrijving[isnull] | BagprocesOmschrijvingIsnullSchema | | optional
bagprocesOmschrijving[like] | BagprocesOmschrijvingLikeSchema | | optional
bagprocesOmschrijving[not] | BagprocesOmschrijvingNotSchema | | optional
beginGeldigheid | BeginGeldigheidSchema | | optional
beginGeldigheid[gt] | BeginGeldigheidGtSchema | | optional
beginGeldigheid[gte] | BeginGeldigheidGteSchema | | optional
beginGeldigheid[in] | BeginGeldigheidInSchema | | optional
beginGeldigheid[isnull] | BeginGeldigheidIsnullSchema | | optional
beginGeldigheid[lt] | BeginGeldigheidLtSchema | | optional
beginGeldigheid[lte] | BeginGeldigheidLteSchema | | optional
beginGeldigheid[not] | BeginGeldigheidNotSchema | | optional
documentdatum | DocumentdatumSchema | | optional
documentdatum[gt] | DocumentdatumGtSchema | | optional
documentdatum[gte] | DocumentdatumGteSchema | | optional
documentdatum[in] | DocumentdatumInSchema | | optional
documentdatum[isnull] | DocumentdatumIsnullSchema | | optional
documentdatum[lt] | DocumentdatumLtSchema | | optional
documentdatum[lte] | DocumentdatumLteSchema | | optional
documentdatum[not] | DocumentdatumNotSchema | | optional
documentnummer | DocumentnummerSchema | | optional
documentnummer[in] | DocumentnummerInSchema | | optional
documentnummer[isempty] | DocumentnummerIsemptySchema | | optional
documentnummer[isnull] | DocumentnummerIsnullSchema | | optional
documentnummer[like] | DocumentnummerLikeSchema | | optional
documentnummer[not] | DocumentnummerNotSchema | | optional
eindGeldigheid | EindGeldigheidSchema | | optional
eindGeldigheid[gt] | EindGeldigheidGtSchema | | optional
eindGeldigheid[gte] | EindGeldigheidGteSchema | | optional
eindGeldigheid[in] | EindGeldigheidInSchema | | optional
eindGeldigheid[isnull] | EindGeldigheidIsnullSchema | | optional
eindGeldigheid[lt] | EindGeldigheidLtSchema | | optional
eindGeldigheid[lte] | EindGeldigheidLteSchema | | optional
eindGeldigheid[not] | EindGeldigheidNotSchema | | optional
geconstateerd | GeconstateerdSchema | | optional
geconstateerd[isnull] | GeconstateerdIsnullSchema | | optional
geldigOp | GeldigOpSchema | | optional
geldigOp[gt] | GeldigOpGtSchema | | optional
geldigOp[gte] | GeldigOpGteSchema | | optional
geldigOp[in] | GeldigOpInSchema | | optional
geldigOp[isnull] | GeldigOpIsnullSchema | | optional
geldigOp[lt] | GeldigOpLtSchema | | optional
geldigOp[lte] | GeldigOpLteSchema | | optional
geldigOp[not] | GeldigOpNotSchema | | optional
heeftDossier.dossier | HeeftDossierDossierSchema | | optional
heeftDossier.dossier[in] | HeeftDossierDossierInSchema | | optional
heeftDossier.dossier[isempty] | HeeftDossierDossierIsemptySchema | | optional
heeftDossier.dossier[isnull] | HeeftDossierDossierIsnullSchema | | optional
heeftDossier.dossier[like] | HeeftDossierDossierLikeSchema | | optional
heeftDossier.dossier[not] | HeeftDossierDossierNotSchema | | optional
heeftOnderzoeken.identificatie | HeeftOnderzoekenIdentificatieSchema | | optional
heeftOnderzoeken.identificatie[in] | HeeftOnderzoekenIdentificatieInSchema | | optional
heeftOnderzoeken.identificatie[isempty] | HeeftOnderzoekenIdentificatieIsemptySchema | | optional
heeftOnderzoeken.identificatie[isnull] | HeeftOnderzoekenIdentificatieIsnullSchema | | optional
heeftOnderzoeken.identificatie[like] | HeeftOnderzoekenIdentificatieLikeSchema | | optional
heeftOnderzoeken.identificatie[not] | HeeftOnderzoekenIdentificatieNotSchema | | optional
heeftOnderzoeken.volgnummer | HeeftOnderzoekenVolgnummerSchema | | optional
heeftOnderzoeken.volgnummer[gt] | HeeftOnderzoekenVolgnummerGtSchema | | optional
heeftOnderzoeken.volgnummer[gte] | HeeftOnderzoekenVolgnummerGteSchema | | optional
heeftOnderzoeken.volgnummer[in] | HeeftOnderzoekenVolgnummerInSchema | | optional
heeftOnderzoeken.volgnummer[isnull] | HeeftOnderzoekenVolgnummerIsnullSchema | | optional
heeftOnderzoeken.volgnummer[lt] | HeeftOnderzoekenVolgnummerLtSchema | | optional
heeftOnderzoeken.volgnummer[lte] | HeeftOnderzoekenVolgnummerLteSchema | | optional
heeftOnderzoeken.volgnummer[not] | HeeftOnderzoekenVolgnummerNotSchema | | optional
huisletter | HuisletterSchema | | optional
huisletter[in] | HuisletterInSchema | | optional
huisletter[isempty] | HuisletterIsemptySchema | | optional
huisletter[isnull] | HuisletterIsnullSchema | | optional
huisletter[like] | HuisletterLikeSchema | | optional
huisletter[not] | HuisletterNotSchema | | optional
huisnummer | HuisnummerSchema | | optional
huisnummer[gt] | HuisnummerGtSchema | | optional
huisnummer[gte] | HuisnummerGteSchema | | optional
huisnummer[in] | HuisnummerInSchema | | optional
huisnummer[isnull] | HuisnummerIsnullSchema | | optional
huisnummer[lt] | HuisnummerLtSchema | | optional
huisnummer[lte] | HuisnummerLteSchema | | optional
huisnummer[not] | HuisnummerNotSchema | | optional
huisnummertoevoeging | HuisnummertoevoegingSchema | | optional
huisnummertoevoeging[in] | HuisnummertoevoegingInSchema | | optional
huisnummertoevoeging[isempty] | HuisnummertoevoegingIsemptySchema | | optional
huisnummertoevoeging[isnull] | HuisnummertoevoegingIsnullSchema | | optional
huisnummertoevoeging[like] | HuisnummertoevoegingLikeSchema | | optional
huisnummertoevoeging[not] | HuisnummertoevoegingNotSchema | | optional
id | IdSchema | | optional
id[in] | IdInSchema | | optional
id[isempty] | IdIsemptySchema | | optional
id[isnull] | IdIsnullSchema | | optional
id[like] | IdLikeSchema | | optional
id[not] | IdNotSchema | | optional
identificatie | IdentificatieSchema | | optional
identificatie[in] | IdentificatieInSchema | | optional
identificatie[isempty] | IdentificatieIsemptySchema | | optional
identificatie[isnull] | IdentificatieIsnullSchema | | optional
identificatie[like] | IdentificatieLikeSchema | | optional
identificatie[not] | IdentificatieNotSchema | | optional
ligtAanOpenbareruimte.identificatie | LigtAanOpenbareruimteIdentificatieSchema | | optional
ligtAanOpenbareruimte.identificatie[in] | LigtAanOpenbareruimteIdentificatieInSchema | | optional
ligtAanOpenbareruimte.identificatie[isempty] | LigtAanOpenbareruimteIdentificatieIsemptySchema | | optional
ligtAanOpenbareruimte.identificatie[isnull] | LigtAanOpenbareruimteIdentificatieIsnullSchema | | optional
ligtAanOpenbareruimte.identificatie[like] | LigtAanOpenbareruimteIdentificatieLikeSchema | | optional
ligtAanOpenbareruimte.identificatie[not] | LigtAanOpenbareruimteIdentificatieNotSchema | | optional
ligtAanOpenbareruimte.volgnummer | LigtAanOpenbareruimteVolgnummerSchema | | optional
ligtAanOpenbareruimte.volgnummer[gt] | LigtAanOpenbareruimteVolgnummerGtSchema | | optional
ligtAanOpenbareruimte.volgnummer[gte] | LigtAanOpenbareruimteVolgnummerGteSchema | | optional
ligtAanOpenbareruimte.volgnummer[in] | LigtAanOpenbareruimteVolgnummerInSchema | | optional
ligtAanOpenbareruimte.volgnummer[isnull] | LigtAanOpenbareruimteVolgnummerIsnullSchema | | optional
ligtAanOpenbareruimte.volgnummer[lt] | LigtAanOpenbareruimteVolgnummerLtSchema | | optional
ligtAanOpenbareruimte.volgnummer[lte] | LigtAanOpenbareruimteVolgnummerLteSchema | | optional
ligtAanOpenbareruimte.volgnummer[not] | LigtAanOpenbareruimteVolgnummerNotSchema | | optional
ligtInWoonplaats.identificatie | LigtInWoonplaatsIdentificatieSchema | | optional
ligtInWoonplaats.identificatie[in] | LigtInWoonplaatsIdentificatieInSchema | | optional
ligtInWoonplaats.identificatie[isempty] | LigtInWoonplaatsIdentificatieIsemptySchema | | optional
ligtInWoonplaats.identificatie[isnull] | LigtInWoonplaatsIdentificatieIsnullSchema | | optional
ligtInWoonplaats.identificatie[like] | LigtInWoonplaatsIdentificatieLikeSchema | | optional
ligtInWoonplaats.identificatie[not] | LigtInWoonplaatsIdentificatieNotSchema | | optional
ligtInWoonplaats.volgnummer | LigtInWoonplaatsVolgnummerSchema | | optional
ligtInWoonplaats.volgnummer[gt] | LigtInWoonplaatsVolgnummerGtSchema | | optional
ligtInWoonplaats.volgnummer[gte] | LigtInWoonplaatsVolgnummerGteSchema | | optional
ligtInWoonplaats.volgnummer[in] | LigtInWoonplaatsVolgnummerInSchema | | optional
ligtInWoonplaats.volgnummer[isnull] | LigtInWoonplaatsVolgnummerIsnullSchema | | optional
ligtInWoonplaats.volgnummer[lt] | LigtInWoonplaatsVolgnummerLtSchema | | optional
ligtInWoonplaats.volgnummer[lte] | LigtInWoonplaatsVolgnummerLteSchema | | optional
ligtInWoonplaats.volgnummer[not] | LigtInWoonplaatsVolgnummerNotSchema | | optional
postcode | PostcodeSchema | | optional
postcode[in] | PostcodeInSchema | | optional
postcode[isempty] | PostcodeIsemptySchema | | optional
postcode[isnull] | PostcodeIsnullSchema | | optional
postcode[like] | PostcodeLikeSchema | | optional
postcode[not] | PostcodeNotSchema | | optional
registratiedatum | RegistratiedatumSchema | | optional
registratiedatum[gt] | RegistratiedatumGtSchema | | optional
registratiedatum[gte] | RegistratiedatumGteSchema | | optional
registratiedatum[in] | RegistratiedatumInSchema | | optional
registratiedatum[isnull] | RegistratiedatumIsnullSchema | | optional
registratiedatum[lt] | RegistratiedatumLtSchema | | optional
registratiedatum[lte] | RegistratiedatumLteSchema | | optional
registratiedatum[not] | RegistratiedatumNotSchema | | optional
statusCode | StatusCodeSchema | | optional
statusCode[gt] | StatusCodeGtSchema | | optional
statusCode[gte] | StatusCodeGteSchema | | optional
statusCode[in] | StatusCodeInSchema | | optional
statusCode[isnull] | StatusCodeIsnullSchema | | optional
statusCode[lt] | StatusCodeLtSchema | | optional
statusCode[lte] | StatusCodeLteSchema | | optional
statusCode[not] | StatusCodeNotSchema | | optional
statusOmschrijving | StatusOmschrijvingSchema | | optional
statusOmschrijving[in] | StatusOmschrijvingInSchema | | optional
statusOmschrijving[isempty] | StatusOmschrijvingIsemptySchema | | optional
statusOmschrijving[isnull] | StatusOmschrijvingIsnullSchema | | optional
statusOmschrijving[like] | StatusOmschrijvingLikeSchema | | optional
statusOmschrijving[not] | StatusOmschrijvingNotSchema | | optional
typeAdres | TypeAdresSchema | | optional
typeAdres[in] | TypeAdresInSchema | | optional
typeAdres[isempty] | TypeAdresIsemptySchema | | optional
typeAdres[isnull] | TypeAdresIsnullSchema | | optional
typeAdres[like] | TypeAdresLikeSchema | | optional
typeAdres[not] | TypeAdresNotSchema | | optional
typeAdresseerbaarObjectCode | TypeAdresseerbaarObjectCodeSchema | | optional
typeAdresseerbaarObjectCode[gt] | TypeAdresseerbaarObjectCodeGtSchema | | optional
typeAdresseerbaarObjectCode[gte] | TypeAdresseerbaarObjectCodeGteSchema | | optional
typeAdresseerbaarObjectCode[in] | TypeAdresseerbaarObjectCodeInSchema | | optional
typeAdresseerbaarObjectCode[isnull] | TypeAdresseerbaarObjectCodeIsnullSchema | | optional
typeAdresseerbaarObjectCode[lt] | TypeAdresseerbaarObjectCodeLtSchema | | optional
typeAdresseerbaarObjectCode[lte] | TypeAdresseerbaarObjectCodeLteSchema | | optional
typeAdresseerbaarObjectCode[not] | TypeAdresseerbaarObjectCodeNotSchema | | optional
typeAdresseerbaarObjectOmschrijving | TypeAdresseerbaarObjectOmschrijvingSchema | | optional
typeAdresseerbaarObjectOmschrijving[in] | TypeAdresseerbaarObjectOmschrijvingInSchema | | optional
typeAdresseerbaarObjectOmschrijving[isempty] | TypeAdresseerbaarObjectOmschrijvingIsemptySchema | | optional
typeAdresseerbaarObjectOmschrijving[isnull] | TypeAdresseerbaarObjectOmschrijvingIsnullSchema | | optional
typeAdresseerbaarObjectOmschrijving[like] | TypeAdresseerbaarObjectOmschrijvingLikeSchema | | optional
typeAdresseerbaarObjectOmschrijving[not] | TypeAdresseerbaarObjectOmschrijvingNotSchema | | optional
volgnummer | VolgnummerSchema | | optional
volgnummer[gt] | VolgnummerGtSchema | | optional
volgnummer[gte] | VolgnummerGteSchema | | optional
volgnummer[in] | VolgnummerInSchema | | optional
volgnummer[isnull] | VolgnummerIsnullSchema | | optional
volgnummer[lt] | VolgnummerLtSchema | | optional
volgnummer[lte] | VolgnummerLteSchema | | optional
volgnummer[not] | VolgnummerNotSchema | | optional


# ExpandSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ExpandScopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "csv", "geojson", ] 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertLigplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertLigplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertLigplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertLigplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertStandplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertStandplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertStandplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertStandplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdresseertVerblijfsobjectIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AdresseertVerblijfsobjectVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AdresseertVerblijfsobjectVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AdresseertVerblijfsobjectVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BagprocesOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BagprocesOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BagprocesOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BagprocesOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BagprocesOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BeginGeldigheidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeginGeldigheidLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# BeginGeldigheidNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# DocumentdatumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentdatumLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentdatumNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# DocumentnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DocumentnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DocumentnummerIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DocumentnummerLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DocumentnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# EindGeldigheidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EindGeldigheidLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EindGeldigheidNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeconstateerdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GeconstateerdIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GeldigOpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# GeldigOpNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# HeeftDossierDossierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftDossierDossierInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftDossierDossierIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftDossierDossierIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftDossierDossierLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftDossierDossierNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftOnderzoekenIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftOnderzoekenVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftOnderzoekenVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftOnderzoekenVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisletterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisletterInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisletterIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisletterIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisletterLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisletterNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HuisnummertoevoegingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisnummertoevoegingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HuisnummertoevoegingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummertoevoegingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HuisnummertoevoegingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HuisnummertoevoegingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtAanOpenbareruimteIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtAanOpenbareruimteVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtAanOpenbareruimteVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtAanOpenbareruimteVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInWoonplaatsIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInWoonplaatsVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInWoonplaatsVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInWoonplaatsVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PostcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PostcodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PostcodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PostcodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PostcodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PostcodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RegistratiedatumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RegistratiedatumLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# RegistratiedatumNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# StatusCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StatusOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StatusOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StatusOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresseerbaarObjectCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeAdresseerbaarObjectOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeAdresseerbaarObjectOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeAdresseerbaarObjectOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# VolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# VolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Crs | AcceptCrsSchema | | optional
Content-Crs | ContentCrsSchema | | optional

# AcceptCrsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentCrsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bag_nummeraanduidingen_retrieve.ApiResponseFor200) | 

#### bag_nummeraanduidingen_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagnummeraanduidingen**](../../models/Bagnummeraanduidingen.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagnummeraanduidingen**](../../models/Bagnummeraanduidingen.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagnummeraanduidingen**](../../models/Bagnummeraanduidingen.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

