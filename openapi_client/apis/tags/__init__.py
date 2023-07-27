# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BRONDOCUMENTEN = "brondocumenten"
    DOSSIERS = "dossiers"
    LIGPLAATSEN = "ligplaatsen"
    NUMMERAANDUIDINGEN = "nummeraanduidingen"
    ONDERZOEKEN = "onderzoeken"
    OPENBARERUIMTES = "openbareruimtes"
    PANDEN = "panden"
    STANDPLAATSEN = "standplaatsen"
    VERBLIJFSOBJECTEN = "verblijfsobjecten"
    WOONPLAATSEN = "woonplaatsen"
