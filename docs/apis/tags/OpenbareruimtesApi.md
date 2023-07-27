<a id="__pageTop"></a>
# openapi_client.apis.tags.openbareruimtes_api.OpenbareruimtesApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bag_openbareruimtes_list**](#bag_openbareruimtes_list) | **get** /v1/bag/openbareruimtes/ | 
[**bag_openbareruimtes_retrieve**](#bag_openbareruimtes_retrieve) | **get** /v1/bag/openbareruimtes/{id}/ | 

# **bag_openbareruimtes_list**
<a id="bag_openbareruimtes_list"></a>
> PaginatedBagopenbareruimtesList bag_openbareruimtes_list()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import openbareruimtes_api
from openapi_client.model.paginated_bagopenbareruimtes_list import PaginatedBagopenbareruimtesList
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
    api_instance = openbareruimtes_api.OpenbareruimtesApi(api_client)

    # example passing only optional values
    query_params = {
        '_count': True,
        '_expand': True,
        '_expandScope': "heeftDossier",
        '_fields': "_fields_example",
        '_format': "json",
        '_pageSize': 1,
        '_sort': "_sort_example",
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
        'beschrijvingNaam': "beschrijvingNaam_example",
        'beschrijvingNaam[in]': [
        "beschrijvingNaam[in]_example"
    ],
        'beschrijvingNaam[isempty]': True,
        'beschrijvingNaam[isnull]': True,
        'beschrijvingNaam[like]': "beschrijvingNaam[like]_example",
        'beschrijvingNaam[not]': [
        "beschrijvingNaam[not]_example"
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
        'geometrie': "geometrie_example",
        'geometrie[contains]': "geometrie[contains]_example",
        'geometrie[isnull]': "geometrie[isnull]_example",
        'geometrie[not]': "geometrie[not]_example",
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
        'naam': "naam_example",
        'naamNen': "naamNen_example",
        'naamNen[in]': [
        "naamNen[in]_example"
    ],
        'naamNen[isempty]': True,
        'naamNen[isnull]': True,
        'naamNen[like]': "naamNen[like]_example",
        'naamNen[not]': [
        "naamNen[not]_example"
    ],
        'naam[in]': [
        "naam[in]_example"
    ],
        'naam[isempty]': True,
        'naam[isnull]': True,
        'naam[like]': "naam[like]_example",
        'naam[not]': [
        "naam[not]_example"
    ],
        'page': 1,
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
        'straatcode': "straatcode_example",
        'straatcode[in]': [
        "straatcode[in]_example"
    ],
        'straatcode[isempty]': True,
        'straatcode[isnull]': True,
        'straatcode[like]': "straatcode[like]_example",
        'straatcode[not]': [
        "straatcode[not]_example"
    ],
        'straatnaamPtt': "straatnaamPtt_example",
        'straatnaamPtt[in]': [
        "straatnaamPtt[in]_example"
    ],
        'straatnaamPtt[isempty]': True,
        'straatnaamPtt[isnull]': True,
        'straatnaamPtt[like]': "straatnaamPtt[like]_example",
        'straatnaamPtt[not]': [
        "straatnaamPtt[not]_example"
    ],
        'typeCode': 1,
        'typeCode[gt]': 1,
        'typeCode[gte]': 1,
        'typeCode[in]': [
        1
    ],
        'typeCode[isnull]': True,
        'typeCode[lt]': 1,
        'typeCode[lte]': 1,
        'typeCode[not]': [
        1
    ],
        'typeOmschrijving': "typeOmschrijving_example",
        'typeOmschrijving[in]': [
        "typeOmschrijving[in]_example"
    ],
        'typeOmschrijving[isempty]': True,
        'typeOmschrijving[isnull]': True,
        'typeOmschrijving[like]': "typeOmschrijving[like]_example",
        'typeOmschrijving[not]': [
        "typeOmschrijving[not]_example"
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
        api_response = api_instance.bag_openbareruimtes_list(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenbareruimtesApi->bag_openbareruimtes_list: %s\n" % e)
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
beschrijvingNaam | BeschrijvingNaamSchema | | optional
beschrijvingNaam[in] | BeschrijvingNaamInSchema | | optional
beschrijvingNaam[isempty] | BeschrijvingNaamIsemptySchema | | optional
beschrijvingNaam[isnull] | BeschrijvingNaamIsnullSchema | | optional
beschrijvingNaam[like] | BeschrijvingNaamLikeSchema | | optional
beschrijvingNaam[not] | BeschrijvingNaamNotSchema | | optional
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
geometrie | GeometrieSchema | | optional
geometrie[contains] | GeometrieContainsSchema | | optional
geometrie[isnull] | GeometrieIsnullSchema | | optional
geometrie[not] | GeometrieNotSchema | | optional
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
naam | NaamSchema | | optional
naamNen | NaamNenSchema | | optional
naamNen[in] | NaamNenInSchema | | optional
naamNen[isempty] | NaamNenIsemptySchema | | optional
naamNen[isnull] | NaamNenIsnullSchema | | optional
naamNen[like] | NaamNenLikeSchema | | optional
naamNen[not] | NaamNenNotSchema | | optional
naam[in] | NaamInSchema | | optional
naam[isempty] | NaamIsemptySchema | | optional
naam[isnull] | NaamIsnullSchema | | optional
naam[like] | NaamLikeSchema | | optional
naam[not] | NaamNotSchema | | optional
page | PageSchema | | optional
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
straatcode | StraatcodeSchema | | optional
straatcode[in] | StraatcodeInSchema | | optional
straatcode[isempty] | StraatcodeIsemptySchema | | optional
straatcode[isnull] | StraatcodeIsnullSchema | | optional
straatcode[like] | StraatcodeLikeSchema | | optional
straatcode[not] | StraatcodeNotSchema | | optional
straatnaamPtt | StraatnaamPttSchema | | optional
straatnaamPtt[in] | StraatnaamPttInSchema | | optional
straatnaamPtt[isempty] | StraatnaamPttIsemptySchema | | optional
straatnaamPtt[isnull] | StraatnaamPttIsnullSchema | | optional
straatnaamPtt[like] | StraatnaamPttLikeSchema | | optional
straatnaamPtt[not] | StraatnaamPttNotSchema | | optional
typeCode | TypeCodeSchema | | optional
typeCode[gt] | TypeCodeGtSchema | | optional
typeCode[gte] | TypeCodeGteSchema | | optional
typeCode[in] | TypeCodeInSchema | | optional
typeCode[isnull] | TypeCodeIsnullSchema | | optional
typeCode[lt] | TypeCodeLtSchema | | optional
typeCode[lte] | TypeCodeLteSchema | | optional
typeCode[not] | TypeCodeNotSchema | | optional
typeOmschrijving | TypeOmschrijvingSchema | | optional
typeOmschrijving[in] | TypeOmschrijvingInSchema | | optional
typeOmschrijving[isempty] | TypeOmschrijvingIsemptySchema | | optional
typeOmschrijving[isnull] | TypeOmschrijvingIsnullSchema | | optional
typeOmschrijving[like] | TypeOmschrijvingLikeSchema | | optional
typeOmschrijving[not] | TypeOmschrijvingNotSchema | | optional
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

# BeschrijvingNaamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BeschrijvingNaamInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BeschrijvingNaamIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeschrijvingNaamIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeschrijvingNaamLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BeschrijvingNaamNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# GeometrieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieContainsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# NaamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamNenIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamNenIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamNenLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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

# StraatcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatcodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatcodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatcodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatcodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatcodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatnaamPttSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatnaamPttInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatnaamPttIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatnaamPttIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatnaamPttLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatnaamPttNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeOmschrijvingNotSchema

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
200 | [ApiResponseFor200](#bag_openbareruimtes_list.ApiResponseFor200) | 

#### bag_openbareruimtes_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagopenbareruimtesList**](../../models/PaginatedBagopenbareruimtesList.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagopenbareruimtesList**](../../models/PaginatedBagopenbareruimtesList.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagopenbareruimtesList**](../../models/PaginatedBagopenbareruimtesList.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bag_openbareruimtes_retrieve**
<a id="bag_openbareruimtes_retrieve"></a>
> Bagopenbareruimtes bag_openbareruimtes_retrieve(id)



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import openbareruimtes_api
from openapi_client.model.bagopenbareruimtes import Bagopenbareruimtes
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
    api_instance = openbareruimtes_api.OpenbareruimtesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "k",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.bag_openbareruimtes_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenbareruimtesApi->bag_openbareruimtes_retrieve: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "k",
    }
    query_params = {
        '_expand': True,
        '_expandScope': "heeftDossier",
        '_fields': "_fields_example",
        '_format': "json",
        '_sort': "_sort_example",
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
        'beschrijvingNaam': "beschrijvingNaam_example",
        'beschrijvingNaam[in]': [
        "beschrijvingNaam[in]_example"
    ],
        'beschrijvingNaam[isempty]': True,
        'beschrijvingNaam[isnull]': True,
        'beschrijvingNaam[like]': "beschrijvingNaam[like]_example",
        'beschrijvingNaam[not]': [
        "beschrijvingNaam[not]_example"
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
        'geometrie': "geometrie_example",
        'geometrie[contains]': "geometrie[contains]_example",
        'geometrie[isnull]': "geometrie[isnull]_example",
        'geometrie[not]': "geometrie[not]_example",
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
        'naam': "naam_example",
        'naamNen': "naamNen_example",
        'naamNen[in]': [
        "naamNen[in]_example"
    ],
        'naamNen[isempty]': True,
        'naamNen[isnull]': True,
        'naamNen[like]': "naamNen[like]_example",
        'naamNen[not]': [
        "naamNen[not]_example"
    ],
        'naam[in]': [
        "naam[in]_example"
    ],
        'naam[isempty]': True,
        'naam[isnull]': True,
        'naam[like]': "naam[like]_example",
        'naam[not]': [
        "naam[not]_example"
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
        'straatcode': "straatcode_example",
        'straatcode[in]': [
        "straatcode[in]_example"
    ],
        'straatcode[isempty]': True,
        'straatcode[isnull]': True,
        'straatcode[like]': "straatcode[like]_example",
        'straatcode[not]': [
        "straatcode[not]_example"
    ],
        'straatnaamPtt': "straatnaamPtt_example",
        'straatnaamPtt[in]': [
        "straatnaamPtt[in]_example"
    ],
        'straatnaamPtt[isempty]': True,
        'straatnaamPtt[isnull]': True,
        'straatnaamPtt[like]': "straatnaamPtt[like]_example",
        'straatnaamPtt[not]': [
        "straatnaamPtt[not]_example"
    ],
        'typeCode': 1,
        'typeCode[gt]': 1,
        'typeCode[gte]': 1,
        'typeCode[in]': [
        1
    ],
        'typeCode[isnull]': True,
        'typeCode[lt]': 1,
        'typeCode[lte]': 1,
        'typeCode[not]': [
        1
    ],
        'typeOmschrijving': "typeOmschrijving_example",
        'typeOmschrijving[in]': [
        "typeOmschrijving[in]_example"
    ],
        'typeOmschrijving[isempty]': True,
        'typeOmschrijving[isnull]': True,
        'typeOmschrijving[like]': "typeOmschrijving[like]_example",
        'typeOmschrijving[not]': [
        "typeOmschrijving[not]_example"
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
        api_response = api_instance.bag_openbareruimtes_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OpenbareruimtesApi->bag_openbareruimtes_retrieve: %s\n" % e)
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
beschrijvingNaam | BeschrijvingNaamSchema | | optional
beschrijvingNaam[in] | BeschrijvingNaamInSchema | | optional
beschrijvingNaam[isempty] | BeschrijvingNaamIsemptySchema | | optional
beschrijvingNaam[isnull] | BeschrijvingNaamIsnullSchema | | optional
beschrijvingNaam[like] | BeschrijvingNaamLikeSchema | | optional
beschrijvingNaam[not] | BeschrijvingNaamNotSchema | | optional
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
geometrie | GeometrieSchema | | optional
geometrie[contains] | GeometrieContainsSchema | | optional
geometrie[isnull] | GeometrieIsnullSchema | | optional
geometrie[not] | GeometrieNotSchema | | optional
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
naam | NaamSchema | | optional
naamNen | NaamNenSchema | | optional
naamNen[in] | NaamNenInSchema | | optional
naamNen[isempty] | NaamNenIsemptySchema | | optional
naamNen[isnull] | NaamNenIsnullSchema | | optional
naamNen[like] | NaamNenLikeSchema | | optional
naamNen[not] | NaamNenNotSchema | | optional
naam[in] | NaamInSchema | | optional
naam[isempty] | NaamIsemptySchema | | optional
naam[isnull] | NaamIsnullSchema | | optional
naam[like] | NaamLikeSchema | | optional
naam[not] | NaamNotSchema | | optional
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
straatcode | StraatcodeSchema | | optional
straatcode[in] | StraatcodeInSchema | | optional
straatcode[isempty] | StraatcodeIsemptySchema | | optional
straatcode[isnull] | StraatcodeIsnullSchema | | optional
straatcode[like] | StraatcodeLikeSchema | | optional
straatcode[not] | StraatcodeNotSchema | | optional
straatnaamPtt | StraatnaamPttSchema | | optional
straatnaamPtt[in] | StraatnaamPttInSchema | | optional
straatnaamPtt[isempty] | StraatnaamPttIsemptySchema | | optional
straatnaamPtt[isnull] | StraatnaamPttIsnullSchema | | optional
straatnaamPtt[like] | StraatnaamPttLikeSchema | | optional
straatnaamPtt[not] | StraatnaamPttNotSchema | | optional
typeCode | TypeCodeSchema | | optional
typeCode[gt] | TypeCodeGtSchema | | optional
typeCode[gte] | TypeCodeGteSchema | | optional
typeCode[in] | TypeCodeInSchema | | optional
typeCode[isnull] | TypeCodeIsnullSchema | | optional
typeCode[lt] | TypeCodeLtSchema | | optional
typeCode[lte] | TypeCodeLteSchema | | optional
typeCode[not] | TypeCodeNotSchema | | optional
typeOmschrijving | TypeOmschrijvingSchema | | optional
typeOmschrijving[in] | TypeOmschrijvingInSchema | | optional
typeOmschrijving[isempty] | TypeOmschrijvingIsemptySchema | | optional
typeOmschrijving[isnull] | TypeOmschrijvingIsnullSchema | | optional
typeOmschrijving[like] | TypeOmschrijvingLikeSchema | | optional
typeOmschrijving[not] | TypeOmschrijvingNotSchema | | optional
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

# BeschrijvingNaamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BeschrijvingNaamInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BeschrijvingNaamIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeschrijvingNaamIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# BeschrijvingNaamLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BeschrijvingNaamNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# GeometrieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieContainsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GeometrieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# NaamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamNenIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamNenIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamNenLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNenNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# NaamIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NaamLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NaamNotSchema

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

# StraatcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatcodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatcodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatcodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatcodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatcodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatnaamPttSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatnaamPttInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StraatnaamPttIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatnaamPttIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# StraatnaamPttLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StraatnaamPttNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TypeOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TypeOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeOmschrijvingNotSchema

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
200 | [ApiResponseFor200](#bag_openbareruimtes_retrieve.ApiResponseFor200) | 

#### bag_openbareruimtes_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagopenbareruimtes**](../../models/Bagopenbareruimtes.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagopenbareruimtes**](../../models/Bagopenbareruimtes.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagopenbareruimtes**](../../models/Bagopenbareruimtes.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

