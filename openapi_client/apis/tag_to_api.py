import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.brondocumenten_api import BrondocumentenApi
from openapi_client.apis.tags.dossiers_api import DossiersApi
from openapi_client.apis.tags.ligplaatsen_api import LigplaatsenApi
from openapi_client.apis.tags.nummeraanduidingen_api import NummeraanduidingenApi
from openapi_client.apis.tags.onderzoeken_api import OnderzoekenApi
from openapi_client.apis.tags.openbareruimtes_api import OpenbareruimtesApi
from openapi_client.apis.tags.panden_api import PandenApi
from openapi_client.apis.tags.standplaatsen_api import StandplaatsenApi
from openapi_client.apis.tags.verblijfsobjecten_api import VerblijfsobjectenApi
from openapi_client.apis.tags.woonplaatsen_api import WoonplaatsenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRONDOCUMENTEN: BrondocumentenApi,
        TagValues.DOSSIERS: DossiersApi,
        TagValues.LIGPLAATSEN: LigplaatsenApi,
        TagValues.NUMMERAANDUIDINGEN: NummeraanduidingenApi,
        TagValues.ONDERZOEKEN: OnderzoekenApi,
        TagValues.OPENBARERUIMTES: OpenbareruimtesApi,
        TagValues.PANDEN: PandenApi,
        TagValues.STANDPLAATSEN: StandplaatsenApi,
        TagValues.VERBLIJFSOBJECTEN: VerblijfsobjectenApi,
        TagValues.WOONPLAATSEN: WoonplaatsenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRONDOCUMENTEN: BrondocumentenApi,
        TagValues.DOSSIERS: DossiersApi,
        TagValues.LIGPLAATSEN: LigplaatsenApi,
        TagValues.NUMMERAANDUIDINGEN: NummeraanduidingenApi,
        TagValues.ONDERZOEKEN: OnderzoekenApi,
        TagValues.OPENBARERUIMTES: OpenbareruimtesApi,
        TagValues.PANDEN: PandenApi,
        TagValues.STANDPLAATSEN: StandplaatsenApi,
        TagValues.VERBLIJFSOBJECTEN: VerblijfsobjectenApi,
        TagValues.WOONPLAATSEN: WoonplaatsenApi,
    }
)
