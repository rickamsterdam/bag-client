# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_BAG_BRONDOCUMENTEN_ = "/v1/bag/brondocumenten/"
    V1_BAG_BRONDOCUMENTEN_DOCUMENTNUMMER_ = "/v1/bag/brondocumenten/{documentnummer}/"
    V1_BAG_DOSSIERS_ = "/v1/bag/dossiers/"
    V1_BAG_DOSSIERS_DOSSIER_ = "/v1/bag/dossiers/{dossier}/"
    V1_BAG_LIGPLAATSEN_ = "/v1/bag/ligplaatsen/"
    V1_BAG_LIGPLAATSEN_ID_ = "/v1/bag/ligplaatsen/{id}/"
    V1_BAG_NUMMERAANDUIDINGEN_ = "/v1/bag/nummeraanduidingen/"
    V1_BAG_NUMMERAANDUIDINGEN_ID_ = "/v1/bag/nummeraanduidingen/{id}/"
    V1_BAG_ONDERZOEKEN_ = "/v1/bag/onderzoeken/"
    V1_BAG_ONDERZOEKEN_ID_ = "/v1/bag/onderzoeken/{id}/"
    V1_BAG_OPENBARERUIMTES_ = "/v1/bag/openbareruimtes/"
    V1_BAG_OPENBARERUIMTES_ID_ = "/v1/bag/openbareruimtes/{id}/"
    V1_BAG_PANDEN_ = "/v1/bag/panden/"
    V1_BAG_PANDEN_ID_ = "/v1/bag/panden/{id}/"
    V1_BAG_STANDPLAATSEN_ = "/v1/bag/standplaatsen/"
    V1_BAG_STANDPLAATSEN_ID_ = "/v1/bag/standplaatsen/{id}/"
    V1_BAG_VERBLIJFSOBJECTEN_ = "/v1/bag/verblijfsobjecten/"
    V1_BAG_VERBLIJFSOBJECTEN_ID_ = "/v1/bag/verblijfsobjecten/{id}/"
    V1_BAG_WOONPLAATSEN_ = "/v1/bag/woonplaatsen/"
    V1_BAG_WOONPLAATSEN_ID_ = "/v1/bag/woonplaatsen/{id}/"
