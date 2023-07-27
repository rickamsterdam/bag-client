<a id="__pageTop"></a>
# openapi_client.apis.tags.verblijfsobjecten_api.VerblijfsobjectenApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bag_verblijfsobjecten_list**](#bag_verblijfsobjecten_list) | **get** /v1/bag/verblijfsobjecten/ | 
[**bag_verblijfsobjecten_retrieve**](#bag_verblijfsobjecten_retrieve) | **get** /v1/bag/verblijfsobjecten/{id}/ | 

# **bag_verblijfsobjecten_list**
<a id="bag_verblijfsobjecten_list"></a>
> PaginatedBagverblijfsobjectenList bag_verblijfsobjecten_list()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import verblijfsobjecten_api
from openapi_client.model.paginated_bagverblijfsobjecten_list import PaginatedBagverblijfsobjectenList
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
    api_instance = verblijfsobjecten_api.VerblijfsobjectenApi(api_client)

    # example passing only optional values
    query_params = {
        '_count': True,
        '_expand': True,
        '_expandScope': "heeftDossier",
        '_fields': "_fields_example",
        '_format': "json",
        '_pageSize': 1,
        '_sort': "_sort_example",
        'aantalBouwlagen': 1,
        'aantalBouwlagen[gt]': 1,
        'aantalBouwlagen[gte]': 1,
        'aantalBouwlagen[in]': [
        1
    ],
        'aantalBouwlagen[isnull]': True,
        'aantalBouwlagen[lt]': 1,
        'aantalBouwlagen[lte]': 1,
        'aantalBouwlagen[not]': [
        1
    ],
        'aantalEenhedenComplex': 1,
        'aantalEenhedenComplex[gt]': 1,
        'aantalEenhedenComplex[gte]': 1,
        'aantalEenhedenComplex[in]': [
        1
    ],
        'aantalEenhedenComplex[isnull]': True,
        'aantalEenhedenComplex[lt]': 1,
        'aantalEenhedenComplex[lte]': 1,
        'aantalEenhedenComplex[not]': [
        1
    ],
        'aantalKamers': 1,
        'aantalKamers[gt]': 1,
        'aantalKamers[gte]': 1,
        'aantalKamers[in]': [
        1
    ],
        'aantalKamers[isnull]': True,
        'aantalKamers[lt]': 1,
        'aantalKamers[lte]': 1,
        'aantalKamers[not]': [
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
        'cbsNummer': "cbsNummer_example",
        'cbsNummer[in]': [
        "cbsNummer[in]_example"
    ],
        'cbsNummer[isempty]': True,
        'cbsNummer[isnull]': True,
        'cbsNummer[like]': "cbsNummer[like]_example",
        'cbsNummer[not]': [
        "cbsNummer[not]_example"
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
        'eigendomsverhoudingCode': 1,
        'eigendomsverhoudingCode[gt]': 1,
        'eigendomsverhoudingCode[gte]': 1,
        'eigendomsverhoudingCode[in]': [
        1
    ],
        'eigendomsverhoudingCode[isnull]': True,
        'eigendomsverhoudingCode[lt]': 1,
        'eigendomsverhoudingCode[lte]': 1,
        'eigendomsverhoudingCode[not]': [
        1
    ],
        'eigendomsverhoudingOmschrijving': "eigendomsverhoudingOmschrijving_example",
        'eigendomsverhoudingOmschrijving[in]': [
        "eigendomsverhoudingOmschrijving[in]_example"
    ],
        'eigendomsverhoudingOmschrijving[isempty]': True,
        'eigendomsverhoudingOmschrijving[isnull]': True,
        'eigendomsverhoudingOmschrijving[like]': "eigendomsverhoudingOmschrijving[like]_example",
        'eigendomsverhoudingOmschrijving[not]': [
        "eigendomsverhoudingOmschrijving[not]_example"
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
        'feitelijkGebruikCode': 1,
        'feitelijkGebruikCode[gt]': 1,
        'feitelijkGebruikCode[gte]': 1,
        'feitelijkGebruikCode[in]': [
        1
    ],
        'feitelijkGebruikCode[isnull]': True,
        'feitelijkGebruikCode[lt]': 1,
        'feitelijkGebruikCode[lte]': 1,
        'feitelijkGebruikCode[not]': [
        1
    ],
        'feitelijkGebruikOmschrijving': "feitelijkGebruikOmschrijving_example",
        'feitelijkGebruikOmschrijving[in]': [
        "feitelijkGebruikOmschrijving[in]_example"
    ],
        'feitelijkGebruikOmschrijving[isempty]': True,
        'feitelijkGebruikOmschrijving[isnull]': True,
        'feitelijkGebruikOmschrijving[like]': "feitelijkGebruikOmschrijving[like]_example",
        'feitelijkGebruikOmschrijving[not]': [
        "feitelijkGebruikOmschrijving[not]_example"
    ],
        'financieringscodeCode': 1,
        'financieringscodeCode[gt]': 1,
        'financieringscodeCode[gte]': 1,
        'financieringscodeCode[in]': [
        1
    ],
        'financieringscodeCode[isnull]': True,
        'financieringscodeCode[lt]': 1,
        'financieringscodeCode[lte]': 1,
        'financieringscodeCode[not]': [
        1
    ],
        'financieringscodeOmschrijving': "financieringscodeOmschrijving_example",
        'financieringscodeOmschrijving[in]': [
        "financieringscodeOmschrijving[in]_example"
    ],
        'financieringscodeOmschrijving[isempty]': True,
        'financieringscodeOmschrijving[isnull]': True,
        'financieringscodeOmschrijving[like]': "financieringscodeOmschrijving[like]_example",
        'financieringscodeOmschrijving[not]': [
        "financieringscodeOmschrijving[not]_example"
    ],
        'gebruiksdoel.code': "gebruiksdoel.code_example",
        'gebruiksdoel.code[in]': [
        "gebruiksdoel.code[in]_example"
    ],
        'gebruiksdoel.code[isempty]': True,
        'gebruiksdoel.code[isnull]': True,
        'gebruiksdoel.code[like]': "gebruiksdoel.code[like]_example",
        'gebruiksdoel.code[not]': [
        "gebruiksdoel.code[not]_example"
    ],
        'gebruiksdoel.omschrijving': "gebruiksdoel.omschrijving_example",
        'gebruiksdoel.omschrijving[in]': [
        "gebruiksdoel.omschrijving[in]_example"
    ],
        'gebruiksdoel.omschrijving[isempty]': True,
        'gebruiksdoel.omschrijving[isnull]': True,
        'gebruiksdoel.omschrijving[like]': "gebruiksdoel.omschrijving[like]_example",
        'gebruiksdoel.omschrijving[not]': [
        "gebruiksdoel.omschrijving[not]_example"
    ],
        'gebruiksdoelGezondheidszorgfunctieCode': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[gt]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[gte]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[in]': [
        1
    ],
        'gebruiksdoelGezondheidszorgfunctieCode[isnull]': True,
        'gebruiksdoelGezondheidszorgfunctieCode[lt]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[lte]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[not]': [
        1
    ],
        'gebruiksdoelGezondheidszorgfunctieOmschrijving': "gebruiksdoelGezondheidszorgfunctieOmschrijving_example",
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[in]': [
        "gebruiksdoelGezondheidszorgfunctieOmschrijving[in]_example"
    ],
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[isempty]': True,
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[isnull]': True,
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[like]': "gebruiksdoelGezondheidszorgfunctieOmschrijving[like]_example",
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[not]': [
        "gebruiksdoelGezondheidszorgfunctieOmschrijving[not]_example"
    ],
        'gebruiksdoelWoonfunctieCode': 1,
        'gebruiksdoelWoonfunctieCode[gt]': 1,
        'gebruiksdoelWoonfunctieCode[gte]': 1,
        'gebruiksdoelWoonfunctieCode[in]': [
        1
    ],
        'gebruiksdoelWoonfunctieCode[isnull]': True,
        'gebruiksdoelWoonfunctieCode[lt]': 1,
        'gebruiksdoelWoonfunctieCode[lte]': 1,
        'gebruiksdoelWoonfunctieCode[not]': [
        1
    ],
        'gebruiksdoelWoonfunctieOmschrijving': "gebruiksdoelWoonfunctieOmschrijving_example",
        'gebruiksdoelWoonfunctieOmschrijving[in]': [
        "gebruiksdoelWoonfunctieOmschrijving[in]_example"
    ],
        'gebruiksdoelWoonfunctieOmschrijving[isempty]': True,
        'gebruiksdoelWoonfunctieOmschrijving[isnull]': True,
        'gebruiksdoelWoonfunctieOmschrijving[like]': "gebruiksdoelWoonfunctieOmschrijving[like]_example",
        'gebruiksdoelWoonfunctieOmschrijving[not]': [
        "gebruiksdoelWoonfunctieOmschrijving[not]_example"
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
        'heeftHoofdadres.identificatie': "heeftHoofdadres.identificatie_example",
        'heeftHoofdadres.identificatie[in]': [
        "heeftHoofdadres.identificatie[in]_example"
    ],
        'heeftHoofdadres.identificatie[isempty]': True,
        'heeftHoofdadres.identificatie[isnull]': True,
        'heeftHoofdadres.identificatie[like]': "heeftHoofdadres.identificatie[like]_example",
        'heeftHoofdadres.identificatie[not]': [
        "heeftHoofdadres.identificatie[not]_example"
    ],
        'heeftHoofdadres.volgnummer': 1,
        'heeftHoofdadres.volgnummer[gt]': 1,
        'heeftHoofdadres.volgnummer[gte]': 1,
        'heeftHoofdadres.volgnummer[in]': [
        1
    ],
        'heeftHoofdadres.volgnummer[isnull]': True,
        'heeftHoofdadres.volgnummer[lt]': 1,
        'heeftHoofdadres.volgnummer[lte]': 1,
        'heeftHoofdadres.volgnummer[not]': [
        1
    ],
        'heeftNevenadres.identificatie': "heeftNevenadres.identificatie_example",
        'heeftNevenadres.identificatie[in]': [
        "heeftNevenadres.identificatie[in]_example"
    ],
        'heeftNevenadres.identificatie[isempty]': True,
        'heeftNevenadres.identificatie[isnull]': True,
        'heeftNevenadres.identificatie[like]': "heeftNevenadres.identificatie[like]_example",
        'heeftNevenadres.identificatie[not]': [
        "heeftNevenadres.identificatie[not]_example"
    ],
        'heeftNevenadres.volgnummer': 1,
        'heeftNevenadres.volgnummer[gt]': 1,
        'heeftNevenadres.volgnummer[gte]': 1,
        'heeftNevenadres.volgnummer[in]': [
        1
    ],
        'heeftNevenadres.volgnummer[isnull]': True,
        'heeftNevenadres.volgnummer[lt]': 1,
        'heeftNevenadres.volgnummer[lte]': 1,
        'heeftNevenadres.volgnummer[not]': [
        1
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
        'hoogsteBouwlaag': 1,
        'hoogsteBouwlaag[gt]': 1,
        'hoogsteBouwlaag[gte]': 1,
        'hoogsteBouwlaag[in]': [
        1
    ],
        'hoogsteBouwlaag[isnull]': True,
        'hoogsteBouwlaag[lt]': 1,
        'hoogsteBouwlaag[lte]': 1,
        'hoogsteBouwlaag[not]': [
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
        'indicatieWoningvoorraad': "indicatieWoningvoorraad_example",
        'indicatieWoningvoorraad[in]': [
        "indicatieWoningvoorraad[in]_example"
    ],
        'indicatieWoningvoorraad[isempty]': True,
        'indicatieWoningvoorraad[isnull]': True,
        'indicatieWoningvoorraad[like]': "indicatieWoningvoorraad[like]_example",
        'indicatieWoningvoorraad[not]': [
        "indicatieWoningvoorraad[not]_example"
    ],
        'laagsteBouwlaag': 1,
        'laagsteBouwlaag[gt]': 1,
        'laagsteBouwlaag[gte]': 1,
        'laagsteBouwlaag[in]': [
        1
    ],
        'laagsteBouwlaag[isnull]': True,
        'laagsteBouwlaag[lt]': 1,
        'laagsteBouwlaag[lte]': 1,
        'laagsteBouwlaag[not]': [
        1
    ],
        'ligtInBuurt.identificatie': "ligtInBuurt.identificatie_example",
        'ligtInBuurt.identificatie[in]': [
        "ligtInBuurt.identificatie[in]_example"
    ],
        'ligtInBuurt.identificatie[isempty]': True,
        'ligtInBuurt.identificatie[isnull]': True,
        'ligtInBuurt.identificatie[like]': "ligtInBuurt.identificatie[like]_example",
        'ligtInBuurt.identificatie[not]': [
        "ligtInBuurt.identificatie[not]_example"
    ],
        'ligtInBuurt.volgnummer': 1,
        'ligtInBuurt.volgnummer[gt]': 1,
        'ligtInBuurt.volgnummer[gte]': 1,
        'ligtInBuurt.volgnummer[in]': [
        1
    ],
        'ligtInBuurt.volgnummer[isnull]': True,
        'ligtInBuurt.volgnummer[lt]': 1,
        'ligtInBuurt.volgnummer[lte]': 1,
        'ligtInBuurt.volgnummer[not]': [
        1
    ],
        'ligtInPanden.identificatie': "ligtInPanden.identificatie_example",
        'ligtInPanden.identificatie[in]': [
        "ligtInPanden.identificatie[in]_example"
    ],
        'ligtInPanden.identificatie[isempty]': True,
        'ligtInPanden.identificatie[isnull]': True,
        'ligtInPanden.identificatie[like]': "ligtInPanden.identificatie[like]_example",
        'ligtInPanden.identificatie[not]': [
        "ligtInPanden.identificatie[not]_example"
    ],
        'ligtInPanden.volgnummer': 1,
        'ligtInPanden.volgnummer[gt]': 1,
        'ligtInPanden.volgnummer[gte]': 1,
        'ligtInPanden.volgnummer[in]': [
        1
    ],
        'ligtInPanden.volgnummer[isnull]': True,
        'ligtInPanden.volgnummer[lt]': 1,
        'ligtInPanden.volgnummer[lte]': 1,
        'ligtInPanden.volgnummer[not]': [
        1
    ],
        'oppervlakte': 1,
        'oppervlakte[gt]': 1,
        'oppervlakte[gte]': 1,
        'oppervlakte[in]': [
        1
    ],
        'oppervlakte[isnull]': True,
        'oppervlakte[lt]': 1,
        'oppervlakte[lte]': 1,
        'oppervlakte[not]': [
        1
    ],
        'page': 1,
        'redenafvoerCode': 1,
        'redenafvoerCode[gt]': 1,
        'redenafvoerCode[gte]': 1,
        'redenafvoerCode[in]': [
        1
    ],
        'redenafvoerCode[isnull]': True,
        'redenafvoerCode[lt]': 1,
        'redenafvoerCode[lte]': 1,
        'redenafvoerCode[not]': [
        1
    ],
        'redenafvoerOmschrijving': "redenafvoerOmschrijving_example",
        'redenafvoerOmschrijving[in]': [
        "redenafvoerOmschrijving[in]_example"
    ],
        'redenafvoerOmschrijving[isempty]': True,
        'redenafvoerOmschrijving[isnull]': True,
        'redenafvoerOmschrijving[like]': "redenafvoerOmschrijving[like]_example",
        'redenafvoerOmschrijving[not]': [
        "redenafvoerOmschrijving[not]_example"
    ],
        'redenopvoerCode': 1,
        'redenopvoerCode[gt]': 1,
        'redenopvoerCode[gte]': 1,
        'redenopvoerCode[in]': [
        1
    ],
        'redenopvoerCode[isnull]': True,
        'redenopvoerCode[lt]': 1,
        'redenopvoerCode[lte]': 1,
        'redenopvoerCode[not]': [
        1
    ],
        'redenopvoerOmschrijving': "redenopvoerOmschrijving_example",
        'redenopvoerOmschrijving[in]': [
        "redenopvoerOmschrijving[in]_example"
    ],
        'redenopvoerOmschrijving[isempty]': True,
        'redenopvoerOmschrijving[isnull]': True,
        'redenopvoerOmschrijving[like]': "redenopvoerOmschrijving[like]_example",
        'redenopvoerOmschrijving[not]': [
        "redenopvoerOmschrijving[not]_example"
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
        'toegang.code': "toegang.code_example",
        'toegang.code[in]': [
        "toegang.code[in]_example"
    ],
        'toegang.code[isempty]': True,
        'toegang.code[isnull]': True,
        'toegang.code[like]': "toegang.code[like]_example",
        'toegang.code[not]': [
        "toegang.code[not]_example"
    ],
        'toegang.omschrijving': "toegang.omschrijving_example",
        'toegang.omschrijving[in]': [
        "toegang.omschrijving[in]_example"
    ],
        'toegang.omschrijving[isempty]': True,
        'toegang.omschrijving[isnull]': True,
        'toegang.omschrijving[like]': "toegang.omschrijving[like]_example",
        'toegang.omschrijving[not]': [
        "toegang.omschrijving[not]_example"
    ],
        'verdiepingToegang': 1,
        'verdiepingToegang[gt]': 1,
        'verdiepingToegang[gte]': 1,
        'verdiepingToegang[in]': [
        1
    ],
        'verdiepingToegang[isnull]': True,
        'verdiepingToegang[lt]': 1,
        'verdiepingToegang[lte]': 1,
        'verdiepingToegang[not]': [
        1
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
        api_response = api_instance.bag_verblijfsobjecten_list(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerblijfsobjectenApi->bag_verblijfsobjecten_list: %s\n" % e)
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
aantalBouwlagen | AantalBouwlagenSchema | | optional
aantalBouwlagen[gt] | AantalBouwlagenGtSchema | | optional
aantalBouwlagen[gte] | AantalBouwlagenGteSchema | | optional
aantalBouwlagen[in] | AantalBouwlagenInSchema | | optional
aantalBouwlagen[isnull] | AantalBouwlagenIsnullSchema | | optional
aantalBouwlagen[lt] | AantalBouwlagenLtSchema | | optional
aantalBouwlagen[lte] | AantalBouwlagenLteSchema | | optional
aantalBouwlagen[not] | AantalBouwlagenNotSchema | | optional
aantalEenhedenComplex | AantalEenhedenComplexSchema | | optional
aantalEenhedenComplex[gt] | AantalEenhedenComplexGtSchema | | optional
aantalEenhedenComplex[gte] | AantalEenhedenComplexGteSchema | | optional
aantalEenhedenComplex[in] | AantalEenhedenComplexInSchema | | optional
aantalEenhedenComplex[isnull] | AantalEenhedenComplexIsnullSchema | | optional
aantalEenhedenComplex[lt] | AantalEenhedenComplexLtSchema | | optional
aantalEenhedenComplex[lte] | AantalEenhedenComplexLteSchema | | optional
aantalEenhedenComplex[not] | AantalEenhedenComplexNotSchema | | optional
aantalKamers | AantalKamersSchema | | optional
aantalKamers[gt] | AantalKamersGtSchema | | optional
aantalKamers[gte] | AantalKamersGteSchema | | optional
aantalKamers[in] | AantalKamersInSchema | | optional
aantalKamers[isnull] | AantalKamersIsnullSchema | | optional
aantalKamers[lt] | AantalKamersLtSchema | | optional
aantalKamers[lte] | AantalKamersLteSchema | | optional
aantalKamers[not] | AantalKamersNotSchema | | optional
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
cbsNummer | CbsNummerSchema | | optional
cbsNummer[in] | CbsNummerInSchema | | optional
cbsNummer[isempty] | CbsNummerIsemptySchema | | optional
cbsNummer[isnull] | CbsNummerIsnullSchema | | optional
cbsNummer[like] | CbsNummerLikeSchema | | optional
cbsNummer[not] | CbsNummerNotSchema | | optional
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
eigendomsverhoudingCode | EigendomsverhoudingCodeSchema | | optional
eigendomsverhoudingCode[gt] | EigendomsverhoudingCodeGtSchema | | optional
eigendomsverhoudingCode[gte] | EigendomsverhoudingCodeGteSchema | | optional
eigendomsverhoudingCode[in] | EigendomsverhoudingCodeInSchema | | optional
eigendomsverhoudingCode[isnull] | EigendomsverhoudingCodeIsnullSchema | | optional
eigendomsverhoudingCode[lt] | EigendomsverhoudingCodeLtSchema | | optional
eigendomsverhoudingCode[lte] | EigendomsverhoudingCodeLteSchema | | optional
eigendomsverhoudingCode[not] | EigendomsverhoudingCodeNotSchema | | optional
eigendomsverhoudingOmschrijving | EigendomsverhoudingOmschrijvingSchema | | optional
eigendomsverhoudingOmschrijving[in] | EigendomsverhoudingOmschrijvingInSchema | | optional
eigendomsverhoudingOmschrijving[isempty] | EigendomsverhoudingOmschrijvingIsemptySchema | | optional
eigendomsverhoudingOmschrijving[isnull] | EigendomsverhoudingOmschrijvingIsnullSchema | | optional
eigendomsverhoudingOmschrijving[like] | EigendomsverhoudingOmschrijvingLikeSchema | | optional
eigendomsverhoudingOmschrijving[not] | EigendomsverhoudingOmschrijvingNotSchema | | optional
eindGeldigheid | EindGeldigheidSchema | | optional
eindGeldigheid[gt] | EindGeldigheidGtSchema | | optional
eindGeldigheid[gte] | EindGeldigheidGteSchema | | optional
eindGeldigheid[in] | EindGeldigheidInSchema | | optional
eindGeldigheid[isnull] | EindGeldigheidIsnullSchema | | optional
eindGeldigheid[lt] | EindGeldigheidLtSchema | | optional
eindGeldigheid[lte] | EindGeldigheidLteSchema | | optional
eindGeldigheid[not] | EindGeldigheidNotSchema | | optional
feitelijkGebruikCode | FeitelijkGebruikCodeSchema | | optional
feitelijkGebruikCode[gt] | FeitelijkGebruikCodeGtSchema | | optional
feitelijkGebruikCode[gte] | FeitelijkGebruikCodeGteSchema | | optional
feitelijkGebruikCode[in] | FeitelijkGebruikCodeInSchema | | optional
feitelijkGebruikCode[isnull] | FeitelijkGebruikCodeIsnullSchema | | optional
feitelijkGebruikCode[lt] | FeitelijkGebruikCodeLtSchema | | optional
feitelijkGebruikCode[lte] | FeitelijkGebruikCodeLteSchema | | optional
feitelijkGebruikCode[not] | FeitelijkGebruikCodeNotSchema | | optional
feitelijkGebruikOmschrijving | FeitelijkGebruikOmschrijvingSchema | | optional
feitelijkGebruikOmschrijving[in] | FeitelijkGebruikOmschrijvingInSchema | | optional
feitelijkGebruikOmschrijving[isempty] | FeitelijkGebruikOmschrijvingIsemptySchema | | optional
feitelijkGebruikOmschrijving[isnull] | FeitelijkGebruikOmschrijvingIsnullSchema | | optional
feitelijkGebruikOmschrijving[like] | FeitelijkGebruikOmschrijvingLikeSchema | | optional
feitelijkGebruikOmschrijving[not] | FeitelijkGebruikOmschrijvingNotSchema | | optional
financieringscodeCode | FinancieringscodeCodeSchema | | optional
financieringscodeCode[gt] | FinancieringscodeCodeGtSchema | | optional
financieringscodeCode[gte] | FinancieringscodeCodeGteSchema | | optional
financieringscodeCode[in] | FinancieringscodeCodeInSchema | | optional
financieringscodeCode[isnull] | FinancieringscodeCodeIsnullSchema | | optional
financieringscodeCode[lt] | FinancieringscodeCodeLtSchema | | optional
financieringscodeCode[lte] | FinancieringscodeCodeLteSchema | | optional
financieringscodeCode[not] | FinancieringscodeCodeNotSchema | | optional
financieringscodeOmschrijving | FinancieringscodeOmschrijvingSchema | | optional
financieringscodeOmschrijving[in] | FinancieringscodeOmschrijvingInSchema | | optional
financieringscodeOmschrijving[isempty] | FinancieringscodeOmschrijvingIsemptySchema | | optional
financieringscodeOmschrijving[isnull] | FinancieringscodeOmschrijvingIsnullSchema | | optional
financieringscodeOmschrijving[like] | FinancieringscodeOmschrijvingLikeSchema | | optional
financieringscodeOmschrijving[not] | FinancieringscodeOmschrijvingNotSchema | | optional
gebruiksdoel.code | GebruiksdoelCodeSchema | | optional
gebruiksdoel.code[in] | GebruiksdoelCodeInSchema | | optional
gebruiksdoel.code[isempty] | GebruiksdoelCodeIsemptySchema | | optional
gebruiksdoel.code[isnull] | GebruiksdoelCodeIsnullSchema | | optional
gebruiksdoel.code[like] | GebruiksdoelCodeLikeSchema | | optional
gebruiksdoel.code[not] | GebruiksdoelCodeNotSchema | | optional
gebruiksdoel.omschrijving | GebruiksdoelOmschrijvingSchema | | optional
gebruiksdoel.omschrijving[in] | GebruiksdoelOmschrijvingInSchema | | optional
gebruiksdoel.omschrijving[isempty] | GebruiksdoelOmschrijvingIsemptySchema | | optional
gebruiksdoel.omschrijving[isnull] | GebruiksdoelOmschrijvingIsnullSchema | | optional
gebruiksdoel.omschrijving[like] | GebruiksdoelOmschrijvingLikeSchema | | optional
gebruiksdoel.omschrijving[not] | GebruiksdoelOmschrijvingNotSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode | GebruiksdoelGezondheidszorgfunctieCodeSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[gt] | GebruiksdoelGezondheidszorgfunctieCodeGtSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[gte] | GebruiksdoelGezondheidszorgfunctieCodeGteSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[in] | GebruiksdoelGezondheidszorgfunctieCodeInSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[isnull] | GebruiksdoelGezondheidszorgfunctieCodeIsnullSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[lt] | GebruiksdoelGezondheidszorgfunctieCodeLtSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[lte] | GebruiksdoelGezondheidszorgfunctieCodeLteSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[not] | GebruiksdoelGezondheidszorgfunctieCodeNotSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving | GebruiksdoelGezondheidszorgfunctieOmschrijvingSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[in] | GebruiksdoelGezondheidszorgfunctieOmschrijvingInSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[isempty] | GebruiksdoelGezondheidszorgfunctieOmschrijvingIsemptySchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[isnull] | GebruiksdoelGezondheidszorgfunctieOmschrijvingIsnullSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[like] | GebruiksdoelGezondheidszorgfunctieOmschrijvingLikeSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[not] | GebruiksdoelGezondheidszorgfunctieOmschrijvingNotSchema | | optional
gebruiksdoelWoonfunctieCode | GebruiksdoelWoonfunctieCodeSchema | | optional
gebruiksdoelWoonfunctieCode[gt] | GebruiksdoelWoonfunctieCodeGtSchema | | optional
gebruiksdoelWoonfunctieCode[gte] | GebruiksdoelWoonfunctieCodeGteSchema | | optional
gebruiksdoelWoonfunctieCode[in] | GebruiksdoelWoonfunctieCodeInSchema | | optional
gebruiksdoelWoonfunctieCode[isnull] | GebruiksdoelWoonfunctieCodeIsnullSchema | | optional
gebruiksdoelWoonfunctieCode[lt] | GebruiksdoelWoonfunctieCodeLtSchema | | optional
gebruiksdoelWoonfunctieCode[lte] | GebruiksdoelWoonfunctieCodeLteSchema | | optional
gebruiksdoelWoonfunctieCode[not] | GebruiksdoelWoonfunctieCodeNotSchema | | optional
gebruiksdoelWoonfunctieOmschrijving | GebruiksdoelWoonfunctieOmschrijvingSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[in] | GebruiksdoelWoonfunctieOmschrijvingInSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[isempty] | GebruiksdoelWoonfunctieOmschrijvingIsemptySchema | | optional
gebruiksdoelWoonfunctieOmschrijving[isnull] | GebruiksdoelWoonfunctieOmschrijvingIsnullSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[like] | GebruiksdoelWoonfunctieOmschrijvingLikeSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[not] | GebruiksdoelWoonfunctieOmschrijvingNotSchema | | optional
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
heeftHoofdadres.identificatie | HeeftHoofdadresIdentificatieSchema | | optional
heeftHoofdadres.identificatie[in] | HeeftHoofdadresIdentificatieInSchema | | optional
heeftHoofdadres.identificatie[isempty] | HeeftHoofdadresIdentificatieIsemptySchema | | optional
heeftHoofdadres.identificatie[isnull] | HeeftHoofdadresIdentificatieIsnullSchema | | optional
heeftHoofdadres.identificatie[like] | HeeftHoofdadresIdentificatieLikeSchema | | optional
heeftHoofdadres.identificatie[not] | HeeftHoofdadresIdentificatieNotSchema | | optional
heeftHoofdadres.volgnummer | HeeftHoofdadresVolgnummerSchema | | optional
heeftHoofdadres.volgnummer[gt] | HeeftHoofdadresVolgnummerGtSchema | | optional
heeftHoofdadres.volgnummer[gte] | HeeftHoofdadresVolgnummerGteSchema | | optional
heeftHoofdadres.volgnummer[in] | HeeftHoofdadresVolgnummerInSchema | | optional
heeftHoofdadres.volgnummer[isnull] | HeeftHoofdadresVolgnummerIsnullSchema | | optional
heeftHoofdadres.volgnummer[lt] | HeeftHoofdadresVolgnummerLtSchema | | optional
heeftHoofdadres.volgnummer[lte] | HeeftHoofdadresVolgnummerLteSchema | | optional
heeftHoofdadres.volgnummer[not] | HeeftHoofdadresVolgnummerNotSchema | | optional
heeftNevenadres.identificatie | HeeftNevenadresIdentificatieSchema | | optional
heeftNevenadres.identificatie[in] | HeeftNevenadresIdentificatieInSchema | | optional
heeftNevenadres.identificatie[isempty] | HeeftNevenadresIdentificatieIsemptySchema | | optional
heeftNevenadres.identificatie[isnull] | HeeftNevenadresIdentificatieIsnullSchema | | optional
heeftNevenadres.identificatie[like] | HeeftNevenadresIdentificatieLikeSchema | | optional
heeftNevenadres.identificatie[not] | HeeftNevenadresIdentificatieNotSchema | | optional
heeftNevenadres.volgnummer | HeeftNevenadresVolgnummerSchema | | optional
heeftNevenadres.volgnummer[gt] | HeeftNevenadresVolgnummerGtSchema | | optional
heeftNevenadres.volgnummer[gte] | HeeftNevenadresVolgnummerGteSchema | | optional
heeftNevenadres.volgnummer[in] | HeeftNevenadresVolgnummerInSchema | | optional
heeftNevenadres.volgnummer[isnull] | HeeftNevenadresVolgnummerIsnullSchema | | optional
heeftNevenadres.volgnummer[lt] | HeeftNevenadresVolgnummerLtSchema | | optional
heeftNevenadres.volgnummer[lte] | HeeftNevenadresVolgnummerLteSchema | | optional
heeftNevenadres.volgnummer[not] | HeeftNevenadresVolgnummerNotSchema | | optional
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
hoogsteBouwlaag | HoogsteBouwlaagSchema | | optional
hoogsteBouwlaag[gt] | HoogsteBouwlaagGtSchema | | optional
hoogsteBouwlaag[gte] | HoogsteBouwlaagGteSchema | | optional
hoogsteBouwlaag[in] | HoogsteBouwlaagInSchema | | optional
hoogsteBouwlaag[isnull] | HoogsteBouwlaagIsnullSchema | | optional
hoogsteBouwlaag[lt] | HoogsteBouwlaagLtSchema | | optional
hoogsteBouwlaag[lte] | HoogsteBouwlaagLteSchema | | optional
hoogsteBouwlaag[not] | HoogsteBouwlaagNotSchema | | optional
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
indicatieWoningvoorraad | IndicatieWoningvoorraadSchema | | optional
indicatieWoningvoorraad[in] | IndicatieWoningvoorraadInSchema | | optional
indicatieWoningvoorraad[isempty] | IndicatieWoningvoorraadIsemptySchema | | optional
indicatieWoningvoorraad[isnull] | IndicatieWoningvoorraadIsnullSchema | | optional
indicatieWoningvoorraad[like] | IndicatieWoningvoorraadLikeSchema | | optional
indicatieWoningvoorraad[not] | IndicatieWoningvoorraadNotSchema | | optional
laagsteBouwlaag | LaagsteBouwlaagSchema | | optional
laagsteBouwlaag[gt] | LaagsteBouwlaagGtSchema | | optional
laagsteBouwlaag[gte] | LaagsteBouwlaagGteSchema | | optional
laagsteBouwlaag[in] | LaagsteBouwlaagInSchema | | optional
laagsteBouwlaag[isnull] | LaagsteBouwlaagIsnullSchema | | optional
laagsteBouwlaag[lt] | LaagsteBouwlaagLtSchema | | optional
laagsteBouwlaag[lte] | LaagsteBouwlaagLteSchema | | optional
laagsteBouwlaag[not] | LaagsteBouwlaagNotSchema | | optional
ligtInBuurt.identificatie | LigtInBuurtIdentificatieSchema | | optional
ligtInBuurt.identificatie[in] | LigtInBuurtIdentificatieInSchema | | optional
ligtInBuurt.identificatie[isempty] | LigtInBuurtIdentificatieIsemptySchema | | optional
ligtInBuurt.identificatie[isnull] | LigtInBuurtIdentificatieIsnullSchema | | optional
ligtInBuurt.identificatie[like] | LigtInBuurtIdentificatieLikeSchema | | optional
ligtInBuurt.identificatie[not] | LigtInBuurtIdentificatieNotSchema | | optional
ligtInBuurt.volgnummer | LigtInBuurtVolgnummerSchema | | optional
ligtInBuurt.volgnummer[gt] | LigtInBuurtVolgnummerGtSchema | | optional
ligtInBuurt.volgnummer[gte] | LigtInBuurtVolgnummerGteSchema | | optional
ligtInBuurt.volgnummer[in] | LigtInBuurtVolgnummerInSchema | | optional
ligtInBuurt.volgnummer[isnull] | LigtInBuurtVolgnummerIsnullSchema | | optional
ligtInBuurt.volgnummer[lt] | LigtInBuurtVolgnummerLtSchema | | optional
ligtInBuurt.volgnummer[lte] | LigtInBuurtVolgnummerLteSchema | | optional
ligtInBuurt.volgnummer[not] | LigtInBuurtVolgnummerNotSchema | | optional
ligtInPanden.identificatie | LigtInPandenIdentificatieSchema | | optional
ligtInPanden.identificatie[in] | LigtInPandenIdentificatieInSchema | | optional
ligtInPanden.identificatie[isempty] | LigtInPandenIdentificatieIsemptySchema | | optional
ligtInPanden.identificatie[isnull] | LigtInPandenIdentificatieIsnullSchema | | optional
ligtInPanden.identificatie[like] | LigtInPandenIdentificatieLikeSchema | | optional
ligtInPanden.identificatie[not] | LigtInPandenIdentificatieNotSchema | | optional
ligtInPanden.volgnummer | LigtInPandenVolgnummerSchema | | optional
ligtInPanden.volgnummer[gt] | LigtInPandenVolgnummerGtSchema | | optional
ligtInPanden.volgnummer[gte] | LigtInPandenVolgnummerGteSchema | | optional
ligtInPanden.volgnummer[in] | LigtInPandenVolgnummerInSchema | | optional
ligtInPanden.volgnummer[isnull] | LigtInPandenVolgnummerIsnullSchema | | optional
ligtInPanden.volgnummer[lt] | LigtInPandenVolgnummerLtSchema | | optional
ligtInPanden.volgnummer[lte] | LigtInPandenVolgnummerLteSchema | | optional
ligtInPanden.volgnummer[not] | LigtInPandenVolgnummerNotSchema | | optional
oppervlakte | OppervlakteSchema | | optional
oppervlakte[gt] | OppervlakteGtSchema | | optional
oppervlakte[gte] | OppervlakteGteSchema | | optional
oppervlakte[in] | OppervlakteInSchema | | optional
oppervlakte[isnull] | OppervlakteIsnullSchema | | optional
oppervlakte[lt] | OppervlakteLtSchema | | optional
oppervlakte[lte] | OppervlakteLteSchema | | optional
oppervlakte[not] | OppervlakteNotSchema | | optional
page | PageSchema | | optional
redenafvoerCode | RedenafvoerCodeSchema | | optional
redenafvoerCode[gt] | RedenafvoerCodeGtSchema | | optional
redenafvoerCode[gte] | RedenafvoerCodeGteSchema | | optional
redenafvoerCode[in] | RedenafvoerCodeInSchema | | optional
redenafvoerCode[isnull] | RedenafvoerCodeIsnullSchema | | optional
redenafvoerCode[lt] | RedenafvoerCodeLtSchema | | optional
redenafvoerCode[lte] | RedenafvoerCodeLteSchema | | optional
redenafvoerCode[not] | RedenafvoerCodeNotSchema | | optional
redenafvoerOmschrijving | RedenafvoerOmschrijvingSchema | | optional
redenafvoerOmschrijving[in] | RedenafvoerOmschrijvingInSchema | | optional
redenafvoerOmschrijving[isempty] | RedenafvoerOmschrijvingIsemptySchema | | optional
redenafvoerOmschrijving[isnull] | RedenafvoerOmschrijvingIsnullSchema | | optional
redenafvoerOmschrijving[like] | RedenafvoerOmschrijvingLikeSchema | | optional
redenafvoerOmschrijving[not] | RedenafvoerOmschrijvingNotSchema | | optional
redenopvoerCode | RedenopvoerCodeSchema | | optional
redenopvoerCode[gt] | RedenopvoerCodeGtSchema | | optional
redenopvoerCode[gte] | RedenopvoerCodeGteSchema | | optional
redenopvoerCode[in] | RedenopvoerCodeInSchema | | optional
redenopvoerCode[isnull] | RedenopvoerCodeIsnullSchema | | optional
redenopvoerCode[lt] | RedenopvoerCodeLtSchema | | optional
redenopvoerCode[lte] | RedenopvoerCodeLteSchema | | optional
redenopvoerCode[not] | RedenopvoerCodeNotSchema | | optional
redenopvoerOmschrijving | RedenopvoerOmschrijvingSchema | | optional
redenopvoerOmschrijving[in] | RedenopvoerOmschrijvingInSchema | | optional
redenopvoerOmschrijving[isempty] | RedenopvoerOmschrijvingIsemptySchema | | optional
redenopvoerOmschrijving[isnull] | RedenopvoerOmschrijvingIsnullSchema | | optional
redenopvoerOmschrijving[like] | RedenopvoerOmschrijvingLikeSchema | | optional
redenopvoerOmschrijving[not] | RedenopvoerOmschrijvingNotSchema | | optional
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
toegang.code | ToegangCodeSchema | | optional
toegang.code[in] | ToegangCodeInSchema | | optional
toegang.code[isempty] | ToegangCodeIsemptySchema | | optional
toegang.code[isnull] | ToegangCodeIsnullSchema | | optional
toegang.code[like] | ToegangCodeLikeSchema | | optional
toegang.code[not] | ToegangCodeNotSchema | | optional
toegang.omschrijving | ToegangOmschrijvingSchema | | optional
toegang.omschrijving[in] | ToegangOmschrijvingInSchema | | optional
toegang.omschrijving[isempty] | ToegangOmschrijvingIsemptySchema | | optional
toegang.omschrijving[isnull] | ToegangOmschrijvingIsnullSchema | | optional
toegang.omschrijving[like] | ToegangOmschrijvingLikeSchema | | optional
toegang.omschrijving[not] | ToegangOmschrijvingNotSchema | | optional
verdiepingToegang | VerdiepingToegangSchema | | optional
verdiepingToegang[gt] | VerdiepingToegangGtSchema | | optional
verdiepingToegang[gte] | VerdiepingToegangGteSchema | | optional
verdiepingToegang[in] | VerdiepingToegangInSchema | | optional
verdiepingToegang[isnull] | VerdiepingToegangIsnullSchema | | optional
verdiepingToegang[lt] | VerdiepingToegangLtSchema | | optional
verdiepingToegang[lte] | VerdiepingToegangLteSchema | | optional
verdiepingToegang[not] | VerdiepingToegangNotSchema | | optional
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

# AantalBouwlagenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalBouwlagenLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalEenhedenComplexLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalKamersLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersNotSchema

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

# CbsNummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CbsNummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CbsNummerIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# CbsNummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# CbsNummerLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CbsNummerNotSchema

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

# EigendomsverhoudingCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingNotSchema

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

# FeitelijkGebruikCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FinancieringscodeCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinancieringscodeOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FinancieringscodeOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinancieringscodeOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelCodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelCodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelWoonfunctieCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# HeeftHoofdadresIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftHoofdadresIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftHoofdadresIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftHoofdadresIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftHoofdadresVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftNevenadresIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftNevenadresIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftNevenadresIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftNevenadresVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

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

# HoogsteBouwlaagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HoogsteBouwlaagLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagNotSchema

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

# IndicatieWoningvoorraadSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndicatieWoningvoorraadInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IndicatieWoningvoorraadIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IndicatieWoningvoorraadIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IndicatieWoningvoorraadLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndicatieWoningvoorraadNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LaagsteBouwlaagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LaagsteBouwlaagLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInBuurtIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInBuurtIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInBuurtIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInBuurtVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInPandenIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInPandenIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInPandenIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInPandenVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# OppervlakteLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteNotSchema

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

# RedenafvoerCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenafvoerOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenafvoerOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenafvoerOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenopvoerCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenopvoerOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenopvoerOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenopvoerOmschrijvingNotSchema

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

# ToegangCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangCodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangCodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# VerdiepingToegangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# VerdiepingToegangLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#bag_verblijfsobjecten_list.ApiResponseFor200) | 

#### bag_verblijfsobjecten_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagverblijfsobjectenList**](../../models/PaginatedBagverblijfsobjectenList.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagverblijfsobjectenList**](../../models/PaginatedBagverblijfsobjectenList.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedBagverblijfsobjectenList**](../../models/PaginatedBagverblijfsobjectenList.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bag_verblijfsobjecten_retrieve**
<a id="bag_verblijfsobjecten_retrieve"></a>
> Bagverblijfsobjecten bag_verblijfsobjecten_retrieve(id)



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import verblijfsobjecten_api
from openapi_client.model.bagverblijfsobjecten import Bagverblijfsobjecten
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
    api_instance = verblijfsobjecten_api.VerblijfsobjectenApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "k",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        api_response = api_instance.bag_verblijfsobjecten_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerblijfsobjectenApi->bag_verblijfsobjecten_retrieve: %s\n" % e)

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
        'aantalBouwlagen': 1,
        'aantalBouwlagen[gt]': 1,
        'aantalBouwlagen[gte]': 1,
        'aantalBouwlagen[in]': [
        1
    ],
        'aantalBouwlagen[isnull]': True,
        'aantalBouwlagen[lt]': 1,
        'aantalBouwlagen[lte]': 1,
        'aantalBouwlagen[not]': [
        1
    ],
        'aantalEenhedenComplex': 1,
        'aantalEenhedenComplex[gt]': 1,
        'aantalEenhedenComplex[gte]': 1,
        'aantalEenhedenComplex[in]': [
        1
    ],
        'aantalEenhedenComplex[isnull]': True,
        'aantalEenhedenComplex[lt]': 1,
        'aantalEenhedenComplex[lte]': 1,
        'aantalEenhedenComplex[not]': [
        1
    ],
        'aantalKamers': 1,
        'aantalKamers[gt]': 1,
        'aantalKamers[gte]': 1,
        'aantalKamers[in]': [
        1
    ],
        'aantalKamers[isnull]': True,
        'aantalKamers[lt]': 1,
        'aantalKamers[lte]': 1,
        'aantalKamers[not]': [
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
        'cbsNummer': "cbsNummer_example",
        'cbsNummer[in]': [
        "cbsNummer[in]_example"
    ],
        'cbsNummer[isempty]': True,
        'cbsNummer[isnull]': True,
        'cbsNummer[like]': "cbsNummer[like]_example",
        'cbsNummer[not]': [
        "cbsNummer[not]_example"
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
        'eigendomsverhoudingCode': 1,
        'eigendomsverhoudingCode[gt]': 1,
        'eigendomsverhoudingCode[gte]': 1,
        'eigendomsverhoudingCode[in]': [
        1
    ],
        'eigendomsverhoudingCode[isnull]': True,
        'eigendomsverhoudingCode[lt]': 1,
        'eigendomsverhoudingCode[lte]': 1,
        'eigendomsverhoudingCode[not]': [
        1
    ],
        'eigendomsverhoudingOmschrijving': "eigendomsverhoudingOmschrijving_example",
        'eigendomsverhoudingOmschrijving[in]': [
        "eigendomsverhoudingOmschrijving[in]_example"
    ],
        'eigendomsverhoudingOmschrijving[isempty]': True,
        'eigendomsverhoudingOmschrijving[isnull]': True,
        'eigendomsverhoudingOmschrijving[like]': "eigendomsverhoudingOmschrijving[like]_example",
        'eigendomsverhoudingOmschrijving[not]': [
        "eigendomsverhoudingOmschrijving[not]_example"
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
        'feitelijkGebruikCode': 1,
        'feitelijkGebruikCode[gt]': 1,
        'feitelijkGebruikCode[gte]': 1,
        'feitelijkGebruikCode[in]': [
        1
    ],
        'feitelijkGebruikCode[isnull]': True,
        'feitelijkGebruikCode[lt]': 1,
        'feitelijkGebruikCode[lte]': 1,
        'feitelijkGebruikCode[not]': [
        1
    ],
        'feitelijkGebruikOmschrijving': "feitelijkGebruikOmschrijving_example",
        'feitelijkGebruikOmschrijving[in]': [
        "feitelijkGebruikOmschrijving[in]_example"
    ],
        'feitelijkGebruikOmschrijving[isempty]': True,
        'feitelijkGebruikOmschrijving[isnull]': True,
        'feitelijkGebruikOmschrijving[like]': "feitelijkGebruikOmschrijving[like]_example",
        'feitelijkGebruikOmschrijving[not]': [
        "feitelijkGebruikOmschrijving[not]_example"
    ],
        'financieringscodeCode': 1,
        'financieringscodeCode[gt]': 1,
        'financieringscodeCode[gte]': 1,
        'financieringscodeCode[in]': [
        1
    ],
        'financieringscodeCode[isnull]': True,
        'financieringscodeCode[lt]': 1,
        'financieringscodeCode[lte]': 1,
        'financieringscodeCode[not]': [
        1
    ],
        'financieringscodeOmschrijving': "financieringscodeOmschrijving_example",
        'financieringscodeOmschrijving[in]': [
        "financieringscodeOmschrijving[in]_example"
    ],
        'financieringscodeOmschrijving[isempty]': True,
        'financieringscodeOmschrijving[isnull]': True,
        'financieringscodeOmschrijving[like]': "financieringscodeOmschrijving[like]_example",
        'financieringscodeOmschrijving[not]': [
        "financieringscodeOmschrijving[not]_example"
    ],
        'gebruiksdoel.code': "gebruiksdoel.code_example",
        'gebruiksdoel.code[in]': [
        "gebruiksdoel.code[in]_example"
    ],
        'gebruiksdoel.code[isempty]': True,
        'gebruiksdoel.code[isnull]': True,
        'gebruiksdoel.code[like]': "gebruiksdoel.code[like]_example",
        'gebruiksdoel.code[not]': [
        "gebruiksdoel.code[not]_example"
    ],
        'gebruiksdoel.omschrijving': "gebruiksdoel.omschrijving_example",
        'gebruiksdoel.omschrijving[in]': [
        "gebruiksdoel.omschrijving[in]_example"
    ],
        'gebruiksdoel.omschrijving[isempty]': True,
        'gebruiksdoel.omschrijving[isnull]': True,
        'gebruiksdoel.omschrijving[like]': "gebruiksdoel.omschrijving[like]_example",
        'gebruiksdoel.omschrijving[not]': [
        "gebruiksdoel.omschrijving[not]_example"
    ],
        'gebruiksdoelGezondheidszorgfunctieCode': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[gt]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[gte]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[in]': [
        1
    ],
        'gebruiksdoelGezondheidszorgfunctieCode[isnull]': True,
        'gebruiksdoelGezondheidszorgfunctieCode[lt]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[lte]': 1,
        'gebruiksdoelGezondheidszorgfunctieCode[not]': [
        1
    ],
        'gebruiksdoelGezondheidszorgfunctieOmschrijving': "gebruiksdoelGezondheidszorgfunctieOmschrijving_example",
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[in]': [
        "gebruiksdoelGezondheidszorgfunctieOmschrijving[in]_example"
    ],
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[isempty]': True,
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[isnull]': True,
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[like]': "gebruiksdoelGezondheidszorgfunctieOmschrijving[like]_example",
        'gebruiksdoelGezondheidszorgfunctieOmschrijving[not]': [
        "gebruiksdoelGezondheidszorgfunctieOmschrijving[not]_example"
    ],
        'gebruiksdoelWoonfunctieCode': 1,
        'gebruiksdoelWoonfunctieCode[gt]': 1,
        'gebruiksdoelWoonfunctieCode[gte]': 1,
        'gebruiksdoelWoonfunctieCode[in]': [
        1
    ],
        'gebruiksdoelWoonfunctieCode[isnull]': True,
        'gebruiksdoelWoonfunctieCode[lt]': 1,
        'gebruiksdoelWoonfunctieCode[lte]': 1,
        'gebruiksdoelWoonfunctieCode[not]': [
        1
    ],
        'gebruiksdoelWoonfunctieOmschrijving': "gebruiksdoelWoonfunctieOmschrijving_example",
        'gebruiksdoelWoonfunctieOmschrijving[in]': [
        "gebruiksdoelWoonfunctieOmschrijving[in]_example"
    ],
        'gebruiksdoelWoonfunctieOmschrijving[isempty]': True,
        'gebruiksdoelWoonfunctieOmschrijving[isnull]': True,
        'gebruiksdoelWoonfunctieOmschrijving[like]': "gebruiksdoelWoonfunctieOmschrijving[like]_example",
        'gebruiksdoelWoonfunctieOmschrijving[not]': [
        "gebruiksdoelWoonfunctieOmschrijving[not]_example"
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
        'heeftHoofdadres.identificatie': "heeftHoofdadres.identificatie_example",
        'heeftHoofdadres.identificatie[in]': [
        "heeftHoofdadres.identificatie[in]_example"
    ],
        'heeftHoofdadres.identificatie[isempty]': True,
        'heeftHoofdadres.identificatie[isnull]': True,
        'heeftHoofdadres.identificatie[like]': "heeftHoofdadres.identificatie[like]_example",
        'heeftHoofdadres.identificatie[not]': [
        "heeftHoofdadres.identificatie[not]_example"
    ],
        'heeftHoofdadres.volgnummer': 1,
        'heeftHoofdadres.volgnummer[gt]': 1,
        'heeftHoofdadres.volgnummer[gte]': 1,
        'heeftHoofdadres.volgnummer[in]': [
        1
    ],
        'heeftHoofdadres.volgnummer[isnull]': True,
        'heeftHoofdadres.volgnummer[lt]': 1,
        'heeftHoofdadres.volgnummer[lte]': 1,
        'heeftHoofdadres.volgnummer[not]': [
        1
    ],
        'heeftNevenadres.identificatie': "heeftNevenadres.identificatie_example",
        'heeftNevenadres.identificatie[in]': [
        "heeftNevenadres.identificatie[in]_example"
    ],
        'heeftNevenadres.identificatie[isempty]': True,
        'heeftNevenadres.identificatie[isnull]': True,
        'heeftNevenadres.identificatie[like]': "heeftNevenadres.identificatie[like]_example",
        'heeftNevenadres.identificatie[not]': [
        "heeftNevenadres.identificatie[not]_example"
    ],
        'heeftNevenadres.volgnummer': 1,
        'heeftNevenadres.volgnummer[gt]': 1,
        'heeftNevenadres.volgnummer[gte]': 1,
        'heeftNevenadres.volgnummer[in]': [
        1
    ],
        'heeftNevenadres.volgnummer[isnull]': True,
        'heeftNevenadres.volgnummer[lt]': 1,
        'heeftNevenadres.volgnummer[lte]': 1,
        'heeftNevenadres.volgnummer[not]': [
        1
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
        'hoogsteBouwlaag': 1,
        'hoogsteBouwlaag[gt]': 1,
        'hoogsteBouwlaag[gte]': 1,
        'hoogsteBouwlaag[in]': [
        1
    ],
        'hoogsteBouwlaag[isnull]': True,
        'hoogsteBouwlaag[lt]': 1,
        'hoogsteBouwlaag[lte]': 1,
        'hoogsteBouwlaag[not]': [
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
        'indicatieWoningvoorraad': "indicatieWoningvoorraad_example",
        'indicatieWoningvoorraad[in]': [
        "indicatieWoningvoorraad[in]_example"
    ],
        'indicatieWoningvoorraad[isempty]': True,
        'indicatieWoningvoorraad[isnull]': True,
        'indicatieWoningvoorraad[like]': "indicatieWoningvoorraad[like]_example",
        'indicatieWoningvoorraad[not]': [
        "indicatieWoningvoorraad[not]_example"
    ],
        'laagsteBouwlaag': 1,
        'laagsteBouwlaag[gt]': 1,
        'laagsteBouwlaag[gte]': 1,
        'laagsteBouwlaag[in]': [
        1
    ],
        'laagsteBouwlaag[isnull]': True,
        'laagsteBouwlaag[lt]': 1,
        'laagsteBouwlaag[lte]': 1,
        'laagsteBouwlaag[not]': [
        1
    ],
        'ligtInBuurt.identificatie': "ligtInBuurt.identificatie_example",
        'ligtInBuurt.identificatie[in]': [
        "ligtInBuurt.identificatie[in]_example"
    ],
        'ligtInBuurt.identificatie[isempty]': True,
        'ligtInBuurt.identificatie[isnull]': True,
        'ligtInBuurt.identificatie[like]': "ligtInBuurt.identificatie[like]_example",
        'ligtInBuurt.identificatie[not]': [
        "ligtInBuurt.identificatie[not]_example"
    ],
        'ligtInBuurt.volgnummer': 1,
        'ligtInBuurt.volgnummer[gt]': 1,
        'ligtInBuurt.volgnummer[gte]': 1,
        'ligtInBuurt.volgnummer[in]': [
        1
    ],
        'ligtInBuurt.volgnummer[isnull]': True,
        'ligtInBuurt.volgnummer[lt]': 1,
        'ligtInBuurt.volgnummer[lte]': 1,
        'ligtInBuurt.volgnummer[not]': [
        1
    ],
        'ligtInPanden.identificatie': "ligtInPanden.identificatie_example",
        'ligtInPanden.identificatie[in]': [
        "ligtInPanden.identificatie[in]_example"
    ],
        'ligtInPanden.identificatie[isempty]': True,
        'ligtInPanden.identificatie[isnull]': True,
        'ligtInPanden.identificatie[like]': "ligtInPanden.identificatie[like]_example",
        'ligtInPanden.identificatie[not]': [
        "ligtInPanden.identificatie[not]_example"
    ],
        'ligtInPanden.volgnummer': 1,
        'ligtInPanden.volgnummer[gt]': 1,
        'ligtInPanden.volgnummer[gte]': 1,
        'ligtInPanden.volgnummer[in]': [
        1
    ],
        'ligtInPanden.volgnummer[isnull]': True,
        'ligtInPanden.volgnummer[lt]': 1,
        'ligtInPanden.volgnummer[lte]': 1,
        'ligtInPanden.volgnummer[not]': [
        1
    ],
        'oppervlakte': 1,
        'oppervlakte[gt]': 1,
        'oppervlakte[gte]': 1,
        'oppervlakte[in]': [
        1
    ],
        'oppervlakte[isnull]': True,
        'oppervlakte[lt]': 1,
        'oppervlakte[lte]': 1,
        'oppervlakte[not]': [
        1
    ],
        'redenafvoerCode': 1,
        'redenafvoerCode[gt]': 1,
        'redenafvoerCode[gte]': 1,
        'redenafvoerCode[in]': [
        1
    ],
        'redenafvoerCode[isnull]': True,
        'redenafvoerCode[lt]': 1,
        'redenafvoerCode[lte]': 1,
        'redenafvoerCode[not]': [
        1
    ],
        'redenafvoerOmschrijving': "redenafvoerOmschrijving_example",
        'redenafvoerOmschrijving[in]': [
        "redenafvoerOmschrijving[in]_example"
    ],
        'redenafvoerOmschrijving[isempty]': True,
        'redenafvoerOmschrijving[isnull]': True,
        'redenafvoerOmschrijving[like]': "redenafvoerOmschrijving[like]_example",
        'redenafvoerOmschrijving[not]': [
        "redenafvoerOmschrijving[not]_example"
    ],
        'redenopvoerCode': 1,
        'redenopvoerCode[gt]': 1,
        'redenopvoerCode[gte]': 1,
        'redenopvoerCode[in]': [
        1
    ],
        'redenopvoerCode[isnull]': True,
        'redenopvoerCode[lt]': 1,
        'redenopvoerCode[lte]': 1,
        'redenopvoerCode[not]': [
        1
    ],
        'redenopvoerOmschrijving': "redenopvoerOmschrijving_example",
        'redenopvoerOmschrijving[in]': [
        "redenopvoerOmschrijving[in]_example"
    ],
        'redenopvoerOmschrijving[isempty]': True,
        'redenopvoerOmschrijving[isnull]': True,
        'redenopvoerOmschrijving[like]': "redenopvoerOmschrijving[like]_example",
        'redenopvoerOmschrijving[not]': [
        "redenopvoerOmschrijving[not]_example"
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
        'toegang.code': "toegang.code_example",
        'toegang.code[in]': [
        "toegang.code[in]_example"
    ],
        'toegang.code[isempty]': True,
        'toegang.code[isnull]': True,
        'toegang.code[like]': "toegang.code[like]_example",
        'toegang.code[not]': [
        "toegang.code[not]_example"
    ],
        'toegang.omschrijving': "toegang.omschrijving_example",
        'toegang.omschrijving[in]': [
        "toegang.omschrijving[in]_example"
    ],
        'toegang.omschrijving[isempty]': True,
        'toegang.omschrijving[isnull]': True,
        'toegang.omschrijving[like]': "toegang.omschrijving[like]_example",
        'toegang.omschrijving[not]': [
        "toegang.omschrijving[not]_example"
    ],
        'verdiepingToegang': 1,
        'verdiepingToegang[gt]': 1,
        'verdiepingToegang[gte]': 1,
        'verdiepingToegang[in]': [
        1
    ],
        'verdiepingToegang[isnull]': True,
        'verdiepingToegang[lt]': 1,
        'verdiepingToegang[lte]': 1,
        'verdiepingToegang[not]': [
        1
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
        api_response = api_instance.bag_verblijfsobjecten_retrieve(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VerblijfsobjectenApi->bag_verblijfsobjecten_retrieve: %s\n" % e)
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
aantalBouwlagen | AantalBouwlagenSchema | | optional
aantalBouwlagen[gt] | AantalBouwlagenGtSchema | | optional
aantalBouwlagen[gte] | AantalBouwlagenGteSchema | | optional
aantalBouwlagen[in] | AantalBouwlagenInSchema | | optional
aantalBouwlagen[isnull] | AantalBouwlagenIsnullSchema | | optional
aantalBouwlagen[lt] | AantalBouwlagenLtSchema | | optional
aantalBouwlagen[lte] | AantalBouwlagenLteSchema | | optional
aantalBouwlagen[not] | AantalBouwlagenNotSchema | | optional
aantalEenhedenComplex | AantalEenhedenComplexSchema | | optional
aantalEenhedenComplex[gt] | AantalEenhedenComplexGtSchema | | optional
aantalEenhedenComplex[gte] | AantalEenhedenComplexGteSchema | | optional
aantalEenhedenComplex[in] | AantalEenhedenComplexInSchema | | optional
aantalEenhedenComplex[isnull] | AantalEenhedenComplexIsnullSchema | | optional
aantalEenhedenComplex[lt] | AantalEenhedenComplexLtSchema | | optional
aantalEenhedenComplex[lte] | AantalEenhedenComplexLteSchema | | optional
aantalEenhedenComplex[not] | AantalEenhedenComplexNotSchema | | optional
aantalKamers | AantalKamersSchema | | optional
aantalKamers[gt] | AantalKamersGtSchema | | optional
aantalKamers[gte] | AantalKamersGteSchema | | optional
aantalKamers[in] | AantalKamersInSchema | | optional
aantalKamers[isnull] | AantalKamersIsnullSchema | | optional
aantalKamers[lt] | AantalKamersLtSchema | | optional
aantalKamers[lte] | AantalKamersLteSchema | | optional
aantalKamers[not] | AantalKamersNotSchema | | optional
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
cbsNummer | CbsNummerSchema | | optional
cbsNummer[in] | CbsNummerInSchema | | optional
cbsNummer[isempty] | CbsNummerIsemptySchema | | optional
cbsNummer[isnull] | CbsNummerIsnullSchema | | optional
cbsNummer[like] | CbsNummerLikeSchema | | optional
cbsNummer[not] | CbsNummerNotSchema | | optional
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
eigendomsverhoudingCode | EigendomsverhoudingCodeSchema | | optional
eigendomsverhoudingCode[gt] | EigendomsverhoudingCodeGtSchema | | optional
eigendomsverhoudingCode[gte] | EigendomsverhoudingCodeGteSchema | | optional
eigendomsverhoudingCode[in] | EigendomsverhoudingCodeInSchema | | optional
eigendomsverhoudingCode[isnull] | EigendomsverhoudingCodeIsnullSchema | | optional
eigendomsverhoudingCode[lt] | EigendomsverhoudingCodeLtSchema | | optional
eigendomsverhoudingCode[lte] | EigendomsverhoudingCodeLteSchema | | optional
eigendomsverhoudingCode[not] | EigendomsverhoudingCodeNotSchema | | optional
eigendomsverhoudingOmschrijving | EigendomsverhoudingOmschrijvingSchema | | optional
eigendomsverhoudingOmschrijving[in] | EigendomsverhoudingOmschrijvingInSchema | | optional
eigendomsverhoudingOmschrijving[isempty] | EigendomsverhoudingOmschrijvingIsemptySchema | | optional
eigendomsverhoudingOmschrijving[isnull] | EigendomsverhoudingOmschrijvingIsnullSchema | | optional
eigendomsverhoudingOmschrijving[like] | EigendomsverhoudingOmschrijvingLikeSchema | | optional
eigendomsverhoudingOmschrijving[not] | EigendomsverhoudingOmschrijvingNotSchema | | optional
eindGeldigheid | EindGeldigheidSchema | | optional
eindGeldigheid[gt] | EindGeldigheidGtSchema | | optional
eindGeldigheid[gte] | EindGeldigheidGteSchema | | optional
eindGeldigheid[in] | EindGeldigheidInSchema | | optional
eindGeldigheid[isnull] | EindGeldigheidIsnullSchema | | optional
eindGeldigheid[lt] | EindGeldigheidLtSchema | | optional
eindGeldigheid[lte] | EindGeldigheidLteSchema | | optional
eindGeldigheid[not] | EindGeldigheidNotSchema | | optional
feitelijkGebruikCode | FeitelijkGebruikCodeSchema | | optional
feitelijkGebruikCode[gt] | FeitelijkGebruikCodeGtSchema | | optional
feitelijkGebruikCode[gte] | FeitelijkGebruikCodeGteSchema | | optional
feitelijkGebruikCode[in] | FeitelijkGebruikCodeInSchema | | optional
feitelijkGebruikCode[isnull] | FeitelijkGebruikCodeIsnullSchema | | optional
feitelijkGebruikCode[lt] | FeitelijkGebruikCodeLtSchema | | optional
feitelijkGebruikCode[lte] | FeitelijkGebruikCodeLteSchema | | optional
feitelijkGebruikCode[not] | FeitelijkGebruikCodeNotSchema | | optional
feitelijkGebruikOmschrijving | FeitelijkGebruikOmschrijvingSchema | | optional
feitelijkGebruikOmschrijving[in] | FeitelijkGebruikOmschrijvingInSchema | | optional
feitelijkGebruikOmschrijving[isempty] | FeitelijkGebruikOmschrijvingIsemptySchema | | optional
feitelijkGebruikOmschrijving[isnull] | FeitelijkGebruikOmschrijvingIsnullSchema | | optional
feitelijkGebruikOmschrijving[like] | FeitelijkGebruikOmschrijvingLikeSchema | | optional
feitelijkGebruikOmschrijving[not] | FeitelijkGebruikOmschrijvingNotSchema | | optional
financieringscodeCode | FinancieringscodeCodeSchema | | optional
financieringscodeCode[gt] | FinancieringscodeCodeGtSchema | | optional
financieringscodeCode[gte] | FinancieringscodeCodeGteSchema | | optional
financieringscodeCode[in] | FinancieringscodeCodeInSchema | | optional
financieringscodeCode[isnull] | FinancieringscodeCodeIsnullSchema | | optional
financieringscodeCode[lt] | FinancieringscodeCodeLtSchema | | optional
financieringscodeCode[lte] | FinancieringscodeCodeLteSchema | | optional
financieringscodeCode[not] | FinancieringscodeCodeNotSchema | | optional
financieringscodeOmschrijving | FinancieringscodeOmschrijvingSchema | | optional
financieringscodeOmschrijving[in] | FinancieringscodeOmschrijvingInSchema | | optional
financieringscodeOmschrijving[isempty] | FinancieringscodeOmschrijvingIsemptySchema | | optional
financieringscodeOmschrijving[isnull] | FinancieringscodeOmschrijvingIsnullSchema | | optional
financieringscodeOmschrijving[like] | FinancieringscodeOmschrijvingLikeSchema | | optional
financieringscodeOmschrijving[not] | FinancieringscodeOmschrijvingNotSchema | | optional
gebruiksdoel.code | GebruiksdoelCodeSchema | | optional
gebruiksdoel.code[in] | GebruiksdoelCodeInSchema | | optional
gebruiksdoel.code[isempty] | GebruiksdoelCodeIsemptySchema | | optional
gebruiksdoel.code[isnull] | GebruiksdoelCodeIsnullSchema | | optional
gebruiksdoel.code[like] | GebruiksdoelCodeLikeSchema | | optional
gebruiksdoel.code[not] | GebruiksdoelCodeNotSchema | | optional
gebruiksdoel.omschrijving | GebruiksdoelOmschrijvingSchema | | optional
gebruiksdoel.omschrijving[in] | GebruiksdoelOmschrijvingInSchema | | optional
gebruiksdoel.omschrijving[isempty] | GebruiksdoelOmschrijvingIsemptySchema | | optional
gebruiksdoel.omschrijving[isnull] | GebruiksdoelOmschrijvingIsnullSchema | | optional
gebruiksdoel.omschrijving[like] | GebruiksdoelOmschrijvingLikeSchema | | optional
gebruiksdoel.omschrijving[not] | GebruiksdoelOmschrijvingNotSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode | GebruiksdoelGezondheidszorgfunctieCodeSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[gt] | GebruiksdoelGezondheidszorgfunctieCodeGtSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[gte] | GebruiksdoelGezondheidszorgfunctieCodeGteSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[in] | GebruiksdoelGezondheidszorgfunctieCodeInSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[isnull] | GebruiksdoelGezondheidszorgfunctieCodeIsnullSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[lt] | GebruiksdoelGezondheidszorgfunctieCodeLtSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[lte] | GebruiksdoelGezondheidszorgfunctieCodeLteSchema | | optional
gebruiksdoelGezondheidszorgfunctieCode[not] | GebruiksdoelGezondheidszorgfunctieCodeNotSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving | GebruiksdoelGezondheidszorgfunctieOmschrijvingSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[in] | GebruiksdoelGezondheidszorgfunctieOmschrijvingInSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[isempty] | GebruiksdoelGezondheidszorgfunctieOmschrijvingIsemptySchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[isnull] | GebruiksdoelGezondheidszorgfunctieOmschrijvingIsnullSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[like] | GebruiksdoelGezondheidszorgfunctieOmschrijvingLikeSchema | | optional
gebruiksdoelGezondheidszorgfunctieOmschrijving[not] | GebruiksdoelGezondheidszorgfunctieOmschrijvingNotSchema | | optional
gebruiksdoelWoonfunctieCode | GebruiksdoelWoonfunctieCodeSchema | | optional
gebruiksdoelWoonfunctieCode[gt] | GebruiksdoelWoonfunctieCodeGtSchema | | optional
gebruiksdoelWoonfunctieCode[gte] | GebruiksdoelWoonfunctieCodeGteSchema | | optional
gebruiksdoelWoonfunctieCode[in] | GebruiksdoelWoonfunctieCodeInSchema | | optional
gebruiksdoelWoonfunctieCode[isnull] | GebruiksdoelWoonfunctieCodeIsnullSchema | | optional
gebruiksdoelWoonfunctieCode[lt] | GebruiksdoelWoonfunctieCodeLtSchema | | optional
gebruiksdoelWoonfunctieCode[lte] | GebruiksdoelWoonfunctieCodeLteSchema | | optional
gebruiksdoelWoonfunctieCode[not] | GebruiksdoelWoonfunctieCodeNotSchema | | optional
gebruiksdoelWoonfunctieOmschrijving | GebruiksdoelWoonfunctieOmschrijvingSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[in] | GebruiksdoelWoonfunctieOmschrijvingInSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[isempty] | GebruiksdoelWoonfunctieOmschrijvingIsemptySchema | | optional
gebruiksdoelWoonfunctieOmschrijving[isnull] | GebruiksdoelWoonfunctieOmschrijvingIsnullSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[like] | GebruiksdoelWoonfunctieOmschrijvingLikeSchema | | optional
gebruiksdoelWoonfunctieOmschrijving[not] | GebruiksdoelWoonfunctieOmschrijvingNotSchema | | optional
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
heeftHoofdadres.identificatie | HeeftHoofdadresIdentificatieSchema | | optional
heeftHoofdadres.identificatie[in] | HeeftHoofdadresIdentificatieInSchema | | optional
heeftHoofdadres.identificatie[isempty] | HeeftHoofdadresIdentificatieIsemptySchema | | optional
heeftHoofdadres.identificatie[isnull] | HeeftHoofdadresIdentificatieIsnullSchema | | optional
heeftHoofdadres.identificatie[like] | HeeftHoofdadresIdentificatieLikeSchema | | optional
heeftHoofdadres.identificatie[not] | HeeftHoofdadresIdentificatieNotSchema | | optional
heeftHoofdadres.volgnummer | HeeftHoofdadresVolgnummerSchema | | optional
heeftHoofdadres.volgnummer[gt] | HeeftHoofdadresVolgnummerGtSchema | | optional
heeftHoofdadres.volgnummer[gte] | HeeftHoofdadresVolgnummerGteSchema | | optional
heeftHoofdadres.volgnummer[in] | HeeftHoofdadresVolgnummerInSchema | | optional
heeftHoofdadres.volgnummer[isnull] | HeeftHoofdadresVolgnummerIsnullSchema | | optional
heeftHoofdadres.volgnummer[lt] | HeeftHoofdadresVolgnummerLtSchema | | optional
heeftHoofdadres.volgnummer[lte] | HeeftHoofdadresVolgnummerLteSchema | | optional
heeftHoofdadres.volgnummer[not] | HeeftHoofdadresVolgnummerNotSchema | | optional
heeftNevenadres.identificatie | HeeftNevenadresIdentificatieSchema | | optional
heeftNevenadres.identificatie[in] | HeeftNevenadresIdentificatieInSchema | | optional
heeftNevenadres.identificatie[isempty] | HeeftNevenadresIdentificatieIsemptySchema | | optional
heeftNevenadres.identificatie[isnull] | HeeftNevenadresIdentificatieIsnullSchema | | optional
heeftNevenadres.identificatie[like] | HeeftNevenadresIdentificatieLikeSchema | | optional
heeftNevenadres.identificatie[not] | HeeftNevenadresIdentificatieNotSchema | | optional
heeftNevenadres.volgnummer | HeeftNevenadresVolgnummerSchema | | optional
heeftNevenadres.volgnummer[gt] | HeeftNevenadresVolgnummerGtSchema | | optional
heeftNevenadres.volgnummer[gte] | HeeftNevenadresVolgnummerGteSchema | | optional
heeftNevenadres.volgnummer[in] | HeeftNevenadresVolgnummerInSchema | | optional
heeftNevenadres.volgnummer[isnull] | HeeftNevenadresVolgnummerIsnullSchema | | optional
heeftNevenadres.volgnummer[lt] | HeeftNevenadresVolgnummerLtSchema | | optional
heeftNevenadres.volgnummer[lte] | HeeftNevenadresVolgnummerLteSchema | | optional
heeftNevenadres.volgnummer[not] | HeeftNevenadresVolgnummerNotSchema | | optional
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
hoogsteBouwlaag | HoogsteBouwlaagSchema | | optional
hoogsteBouwlaag[gt] | HoogsteBouwlaagGtSchema | | optional
hoogsteBouwlaag[gte] | HoogsteBouwlaagGteSchema | | optional
hoogsteBouwlaag[in] | HoogsteBouwlaagInSchema | | optional
hoogsteBouwlaag[isnull] | HoogsteBouwlaagIsnullSchema | | optional
hoogsteBouwlaag[lt] | HoogsteBouwlaagLtSchema | | optional
hoogsteBouwlaag[lte] | HoogsteBouwlaagLteSchema | | optional
hoogsteBouwlaag[not] | HoogsteBouwlaagNotSchema | | optional
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
indicatieWoningvoorraad | IndicatieWoningvoorraadSchema | | optional
indicatieWoningvoorraad[in] | IndicatieWoningvoorraadInSchema | | optional
indicatieWoningvoorraad[isempty] | IndicatieWoningvoorraadIsemptySchema | | optional
indicatieWoningvoorraad[isnull] | IndicatieWoningvoorraadIsnullSchema | | optional
indicatieWoningvoorraad[like] | IndicatieWoningvoorraadLikeSchema | | optional
indicatieWoningvoorraad[not] | IndicatieWoningvoorraadNotSchema | | optional
laagsteBouwlaag | LaagsteBouwlaagSchema | | optional
laagsteBouwlaag[gt] | LaagsteBouwlaagGtSchema | | optional
laagsteBouwlaag[gte] | LaagsteBouwlaagGteSchema | | optional
laagsteBouwlaag[in] | LaagsteBouwlaagInSchema | | optional
laagsteBouwlaag[isnull] | LaagsteBouwlaagIsnullSchema | | optional
laagsteBouwlaag[lt] | LaagsteBouwlaagLtSchema | | optional
laagsteBouwlaag[lte] | LaagsteBouwlaagLteSchema | | optional
laagsteBouwlaag[not] | LaagsteBouwlaagNotSchema | | optional
ligtInBuurt.identificatie | LigtInBuurtIdentificatieSchema | | optional
ligtInBuurt.identificatie[in] | LigtInBuurtIdentificatieInSchema | | optional
ligtInBuurt.identificatie[isempty] | LigtInBuurtIdentificatieIsemptySchema | | optional
ligtInBuurt.identificatie[isnull] | LigtInBuurtIdentificatieIsnullSchema | | optional
ligtInBuurt.identificatie[like] | LigtInBuurtIdentificatieLikeSchema | | optional
ligtInBuurt.identificatie[not] | LigtInBuurtIdentificatieNotSchema | | optional
ligtInBuurt.volgnummer | LigtInBuurtVolgnummerSchema | | optional
ligtInBuurt.volgnummer[gt] | LigtInBuurtVolgnummerGtSchema | | optional
ligtInBuurt.volgnummer[gte] | LigtInBuurtVolgnummerGteSchema | | optional
ligtInBuurt.volgnummer[in] | LigtInBuurtVolgnummerInSchema | | optional
ligtInBuurt.volgnummer[isnull] | LigtInBuurtVolgnummerIsnullSchema | | optional
ligtInBuurt.volgnummer[lt] | LigtInBuurtVolgnummerLtSchema | | optional
ligtInBuurt.volgnummer[lte] | LigtInBuurtVolgnummerLteSchema | | optional
ligtInBuurt.volgnummer[not] | LigtInBuurtVolgnummerNotSchema | | optional
ligtInPanden.identificatie | LigtInPandenIdentificatieSchema | | optional
ligtInPanden.identificatie[in] | LigtInPandenIdentificatieInSchema | | optional
ligtInPanden.identificatie[isempty] | LigtInPandenIdentificatieIsemptySchema | | optional
ligtInPanden.identificatie[isnull] | LigtInPandenIdentificatieIsnullSchema | | optional
ligtInPanden.identificatie[like] | LigtInPandenIdentificatieLikeSchema | | optional
ligtInPanden.identificatie[not] | LigtInPandenIdentificatieNotSchema | | optional
ligtInPanden.volgnummer | LigtInPandenVolgnummerSchema | | optional
ligtInPanden.volgnummer[gt] | LigtInPandenVolgnummerGtSchema | | optional
ligtInPanden.volgnummer[gte] | LigtInPandenVolgnummerGteSchema | | optional
ligtInPanden.volgnummer[in] | LigtInPandenVolgnummerInSchema | | optional
ligtInPanden.volgnummer[isnull] | LigtInPandenVolgnummerIsnullSchema | | optional
ligtInPanden.volgnummer[lt] | LigtInPandenVolgnummerLtSchema | | optional
ligtInPanden.volgnummer[lte] | LigtInPandenVolgnummerLteSchema | | optional
ligtInPanden.volgnummer[not] | LigtInPandenVolgnummerNotSchema | | optional
oppervlakte | OppervlakteSchema | | optional
oppervlakte[gt] | OppervlakteGtSchema | | optional
oppervlakte[gte] | OppervlakteGteSchema | | optional
oppervlakte[in] | OppervlakteInSchema | | optional
oppervlakte[isnull] | OppervlakteIsnullSchema | | optional
oppervlakte[lt] | OppervlakteLtSchema | | optional
oppervlakte[lte] | OppervlakteLteSchema | | optional
oppervlakte[not] | OppervlakteNotSchema | | optional
redenafvoerCode | RedenafvoerCodeSchema | | optional
redenafvoerCode[gt] | RedenafvoerCodeGtSchema | | optional
redenafvoerCode[gte] | RedenafvoerCodeGteSchema | | optional
redenafvoerCode[in] | RedenafvoerCodeInSchema | | optional
redenafvoerCode[isnull] | RedenafvoerCodeIsnullSchema | | optional
redenafvoerCode[lt] | RedenafvoerCodeLtSchema | | optional
redenafvoerCode[lte] | RedenafvoerCodeLteSchema | | optional
redenafvoerCode[not] | RedenafvoerCodeNotSchema | | optional
redenafvoerOmschrijving | RedenafvoerOmschrijvingSchema | | optional
redenafvoerOmschrijving[in] | RedenafvoerOmschrijvingInSchema | | optional
redenafvoerOmschrijving[isempty] | RedenafvoerOmschrijvingIsemptySchema | | optional
redenafvoerOmschrijving[isnull] | RedenafvoerOmschrijvingIsnullSchema | | optional
redenafvoerOmschrijving[like] | RedenafvoerOmschrijvingLikeSchema | | optional
redenafvoerOmschrijving[not] | RedenafvoerOmschrijvingNotSchema | | optional
redenopvoerCode | RedenopvoerCodeSchema | | optional
redenopvoerCode[gt] | RedenopvoerCodeGtSchema | | optional
redenopvoerCode[gte] | RedenopvoerCodeGteSchema | | optional
redenopvoerCode[in] | RedenopvoerCodeInSchema | | optional
redenopvoerCode[isnull] | RedenopvoerCodeIsnullSchema | | optional
redenopvoerCode[lt] | RedenopvoerCodeLtSchema | | optional
redenopvoerCode[lte] | RedenopvoerCodeLteSchema | | optional
redenopvoerCode[not] | RedenopvoerCodeNotSchema | | optional
redenopvoerOmschrijving | RedenopvoerOmschrijvingSchema | | optional
redenopvoerOmschrijving[in] | RedenopvoerOmschrijvingInSchema | | optional
redenopvoerOmschrijving[isempty] | RedenopvoerOmschrijvingIsemptySchema | | optional
redenopvoerOmschrijving[isnull] | RedenopvoerOmschrijvingIsnullSchema | | optional
redenopvoerOmschrijving[like] | RedenopvoerOmschrijvingLikeSchema | | optional
redenopvoerOmschrijving[not] | RedenopvoerOmschrijvingNotSchema | | optional
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
toegang.code | ToegangCodeSchema | | optional
toegang.code[in] | ToegangCodeInSchema | | optional
toegang.code[isempty] | ToegangCodeIsemptySchema | | optional
toegang.code[isnull] | ToegangCodeIsnullSchema | | optional
toegang.code[like] | ToegangCodeLikeSchema | | optional
toegang.code[not] | ToegangCodeNotSchema | | optional
toegang.omschrijving | ToegangOmschrijvingSchema | | optional
toegang.omschrijving[in] | ToegangOmschrijvingInSchema | | optional
toegang.omschrijving[isempty] | ToegangOmschrijvingIsemptySchema | | optional
toegang.omschrijving[isnull] | ToegangOmschrijvingIsnullSchema | | optional
toegang.omschrijving[like] | ToegangOmschrijvingLikeSchema | | optional
toegang.omschrijving[not] | ToegangOmschrijvingNotSchema | | optional
verdiepingToegang | VerdiepingToegangSchema | | optional
verdiepingToegang[gt] | VerdiepingToegangGtSchema | | optional
verdiepingToegang[gte] | VerdiepingToegangGteSchema | | optional
verdiepingToegang[in] | VerdiepingToegangInSchema | | optional
verdiepingToegang[isnull] | VerdiepingToegangIsnullSchema | | optional
verdiepingToegang[lt] | VerdiepingToegangLtSchema | | optional
verdiepingToegang[lte] | VerdiepingToegangLteSchema | | optional
verdiepingToegang[not] | VerdiepingToegangNotSchema | | optional
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

# AantalBouwlagenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalBouwlagenLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalBouwlagenNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalEenhedenComplexLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalEenhedenComplexNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# AantalKamersLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AantalKamersNotSchema

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

# CbsNummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CbsNummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CbsNummerIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# CbsNummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# CbsNummerLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CbsNummerNotSchema

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

# EigendomsverhoudingCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# EigendomsverhoudingOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# EigendomsverhoudingOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EigendomsverhoudingOmschrijvingNotSchema

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

# FeitelijkGebruikCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FeitelijkGebruikOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FeitelijkGebruikOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FeitelijkGebruikOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FinancieringscodeCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FinancieringscodeOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinancieringscodeOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FinancieringscodeOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FinancieringscodeOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FinancieringscodeOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelCodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelCodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelGezondheidszorgfunctieOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelWoonfunctieCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GebruiksdoelWoonfunctieOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# HeeftHoofdadresIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftHoofdadresIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftHoofdadresIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftHoofdadresIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftHoofdadresVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftHoofdadresVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftHoofdadresVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftNevenadresIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftNevenadresIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeeftNevenadresIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# HeeftNevenadresVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HeeftNevenadresVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeeftNevenadresVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

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

# HoogsteBouwlaagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HoogsteBouwlaagLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HoogsteBouwlaagNotSchema

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

# IndicatieWoningvoorraadSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndicatieWoningvoorraadInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IndicatieWoningvoorraadIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IndicatieWoningvoorraadIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IndicatieWoningvoorraadLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndicatieWoningvoorraadNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LaagsteBouwlaagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LaagsteBouwlaagLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaagsteBouwlaagNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInBuurtIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInBuurtIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInBuurtIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInBuurtVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInBuurtVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInBuurtVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenIdentificatieSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInPandenIdentificatieInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInPandenIdentificatieIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenIdentificatieIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenIdentificatieLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LigtInPandenIdentificatieNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LigtInPandenVolgnummerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# LigtInPandenVolgnummerLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LigtInPandenVolgnummerNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# OppervlakteLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OppervlakteNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenafvoerOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenafvoerOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenafvoerOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenafvoerOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenafvoerOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenopvoerCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerCodeLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RedenopvoerOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenopvoerOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RedenopvoerOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RedenopvoerOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RedenopvoerOmschrijvingNotSchema

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

# ToegangCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangCodeInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangCodeIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangCodeIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangCodeLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangCodeNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangOmschrijvingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangOmschrijvingInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ToegangOmschrijvingIsemptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangOmschrijvingIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ToegangOmschrijvingLikeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToegangOmschrijvingNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# VerdiepingToegangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangGtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangGteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangInSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangIsnullSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# VerdiepingToegangLtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangLteSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerdiepingToegangNotSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#bag_verblijfsobjecten_retrieve.ApiResponseFor200) | 

#### bag_verblijfsobjecten_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, SchemaFor200ResponseBodyTextCsv, SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagverblijfsobjecten**](../../models/Bagverblijfsobjecten.md) |  | 


# SchemaFor200ResponseBodyTextCsv
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagverblijfsobjecten**](../../models/Bagverblijfsobjecten.md) |  | 


# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bagverblijfsobjecten**](../../models/Bagverblijfsobjecten.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

