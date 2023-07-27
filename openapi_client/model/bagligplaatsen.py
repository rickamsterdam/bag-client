# coding: utf-8

"""
    bag

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: datapunt@amsterdam.nl
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class Bagligplaatsen(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ligplaatsen
    """


    class MetaOapg:
        required = {
            "gebruiksdoel",
            "identificatie",
            "_links",
            "volgnummer",
            "heeftDossierId",
            "ligtInBuurtId",
            "heeftHoofdadresId",
        }
        
        class properties:
            
            
            class _links(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            BagLigplaatsenLinks,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_links':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class identificatie(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2147483647
            
            
            class volgnummer(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 9223372036854775807
                    inclusive_minimum = -9223372036854775808
            
            
            class heeftHoofdadresId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'heeftHoofdadresId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class ligtInBuurtId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ligtInBuurtId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class heeftDossierId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'heeftDossierId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class gebruiksdoel(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BagligplaatsenGebruiksdoel']:
                        return BagligplaatsenGebruiksdoel
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BagligplaatsenGebruiksdoel'], typing.List['BagligplaatsenGebruiksdoel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gebruiksdoel':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BagligplaatsenGebruiksdoel':
                    return super().__getitem__(i)
            
            
            class registratiedatum(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'registratiedatum':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class geconstateerd(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'geconstateerd':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class statusCode(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 9223372036854775807
                    inclusive_minimum = -9223372036854775808
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statusCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class statusOmschrijving(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 2147483647
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statusOmschrijving':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def geometrie() -> typing.Type['Geometry']:
                return Geometry
            
            
            class beginGeldigheid(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'beginGeldigheid':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class eindGeldigheid(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'eindGeldigheid':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class documentdatum(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentdatum':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class documentnummer(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 2147483647
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentnummer':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class bagprocesCode(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 9223372036854775807
                    inclusive_minimum = -9223372036854775808
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bagprocesCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class bagprocesOmschrijving(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 2147483647
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bagprocesOmschrijving':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "_links": _links,
                "identificatie": identificatie,
                "volgnummer": volgnummer,
                "heeftHoofdadresId": heeftHoofdadresId,
                "ligtInBuurtId": ligtInBuurtId,
                "heeftDossierId": heeftDossierId,
                "gebruiksdoel": gebruiksdoel,
                "registratiedatum": registratiedatum,
                "geconstateerd": geconstateerd,
                "statusCode": statusCode,
                "statusOmschrijving": statusOmschrijving,
                "geometrie": geometrie,
                "beginGeldigheid": beginGeldigheid,
                "eindGeldigheid": eindGeldigheid,
                "documentdatum": documentdatum,
                "documentnummer": documentnummer,
                "bagprocesCode": bagprocesCode,
                "bagprocesOmschrijving": bagprocesOmschrijving,
            }
    
    gebruiksdoel: MetaOapg.properties.gebruiksdoel
    identificatie: MetaOapg.properties.identificatie
    _links: MetaOapg.properties._links
    volgnummer: MetaOapg.properties.volgnummer
    heeftDossierId: MetaOapg.properties.heeftDossierId
    ligtInBuurtId: MetaOapg.properties.ligtInBuurtId
    heeftHoofdadresId: MetaOapg.properties.heeftHoofdadresId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificatie"]) -> MetaOapg.properties.identificatie: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volgnummer"]) -> MetaOapg.properties.volgnummer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftHoofdadresId"]) -> MetaOapg.properties.heeftHoofdadresId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ligtInBuurtId"]) -> MetaOapg.properties.ligtInBuurtId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftDossierId"]) -> MetaOapg.properties.heeftDossierId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gebruiksdoel"]) -> MetaOapg.properties.gebruiksdoel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registratiedatum"]) -> MetaOapg.properties.registratiedatum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geconstateerd"]) -> MetaOapg.properties.geconstateerd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusCode"]) -> MetaOapg.properties.statusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusOmschrijving"]) -> MetaOapg.properties.statusOmschrijving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geometrie"]) -> 'Geometry': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginGeldigheid"]) -> MetaOapg.properties.beginGeldigheid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eindGeldigheid"]) -> MetaOapg.properties.eindGeldigheid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentdatum"]) -> MetaOapg.properties.documentdatum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentnummer"]) -> MetaOapg.properties.documentnummer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bagprocesCode"]) -> MetaOapg.properties.bagprocesCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bagprocesOmschrijving"]) -> MetaOapg.properties.bagprocesOmschrijving: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "identificatie", "volgnummer", "heeftHoofdadresId", "ligtInBuurtId", "heeftDossierId", "gebruiksdoel", "registratiedatum", "geconstateerd", "statusCode", "statusOmschrijving", "geometrie", "beginGeldigheid", "eindGeldigheid", "documentdatum", "documentnummer", "bagprocesCode", "bagprocesOmschrijving", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificatie"]) -> MetaOapg.properties.identificatie: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volgnummer"]) -> MetaOapg.properties.volgnummer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftHoofdadresId"]) -> MetaOapg.properties.heeftHoofdadresId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ligtInBuurtId"]) -> MetaOapg.properties.ligtInBuurtId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftDossierId"]) -> MetaOapg.properties.heeftDossierId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gebruiksdoel"]) -> MetaOapg.properties.gebruiksdoel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registratiedatum"]) -> typing.Union[MetaOapg.properties.registratiedatum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geconstateerd"]) -> typing.Union[MetaOapg.properties.geconstateerd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusCode"]) -> typing.Union[MetaOapg.properties.statusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusOmschrijving"]) -> typing.Union[MetaOapg.properties.statusOmschrijving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geometrie"]) -> typing.Union['Geometry', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginGeldigheid"]) -> typing.Union[MetaOapg.properties.beginGeldigheid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eindGeldigheid"]) -> typing.Union[MetaOapg.properties.eindGeldigheid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentdatum"]) -> typing.Union[MetaOapg.properties.documentdatum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentnummer"]) -> typing.Union[MetaOapg.properties.documentnummer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bagprocesCode"]) -> typing.Union[MetaOapg.properties.bagprocesCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bagprocesOmschrijving"]) -> typing.Union[MetaOapg.properties.bagprocesOmschrijving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "identificatie", "volgnummer", "heeftHoofdadresId", "ligtInBuurtId", "heeftDossierId", "gebruiksdoel", "registratiedatum", "geconstateerd", "statusCode", "statusOmschrijving", "geometrie", "beginGeldigheid", "eindGeldigheid", "documentdatum", "documentnummer", "bagprocesCode", "bagprocesOmschrijving", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gebruiksdoel: typing.Union[MetaOapg.properties.gebruiksdoel, list, tuple, ],
        identificatie: typing.Union[MetaOapg.properties.identificatie, str, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        volgnummer: typing.Union[MetaOapg.properties.volgnummer, decimal.Decimal, int, ],
        heeftDossierId: typing.Union[MetaOapg.properties.heeftDossierId, None, str, ],
        ligtInBuurtId: typing.Union[MetaOapg.properties.ligtInBuurtId, None, str, ],
        heeftHoofdadresId: typing.Union[MetaOapg.properties.heeftHoofdadresId, None, str, ],
        registratiedatum: typing.Union[MetaOapg.properties.registratiedatum, None, str, datetime, schemas.Unset] = schemas.unset,
        geconstateerd: typing.Union[MetaOapg.properties.geconstateerd, None, bool, schemas.Unset] = schemas.unset,
        statusCode: typing.Union[MetaOapg.properties.statusCode, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        statusOmschrijving: typing.Union[MetaOapg.properties.statusOmschrijving, None, str, schemas.Unset] = schemas.unset,
        geometrie: typing.Union['Geometry', schemas.Unset] = schemas.unset,
        beginGeldigheid: typing.Union[MetaOapg.properties.beginGeldigheid, None, str, datetime, schemas.Unset] = schemas.unset,
        eindGeldigheid: typing.Union[MetaOapg.properties.eindGeldigheid, None, str, datetime, schemas.Unset] = schemas.unset,
        documentdatum: typing.Union[MetaOapg.properties.documentdatum, None, str, date, schemas.Unset] = schemas.unset,
        documentnummer: typing.Union[MetaOapg.properties.documentnummer, None, str, schemas.Unset] = schemas.unset,
        bagprocesCode: typing.Union[MetaOapg.properties.bagprocesCode, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bagprocesOmschrijving: typing.Union[MetaOapg.properties.bagprocesOmschrijving, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Bagligplaatsen':
        return super().__new__(
            cls,
            *_args,
            gebruiksdoel=gebruiksdoel,
            identificatie=identificatie,
            _links=_links,
            volgnummer=volgnummer,
            heeftDossierId=heeftDossierId,
            ligtInBuurtId=ligtInBuurtId,
            heeftHoofdadresId=heeftHoofdadresId,
            registratiedatum=registratiedatum,
            geconstateerd=geconstateerd,
            statusCode=statusCode,
            statusOmschrijving=statusOmschrijving,
            geometrie=geometrie,
            beginGeldigheid=beginGeldigheid,
            eindGeldigheid=eindGeldigheid,
            documentdatum=documentdatum,
            documentnummer=documentnummer,
            bagprocesCode=bagprocesCode,
            bagprocesOmschrijving=bagprocesOmschrijving,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.bag_ligplaatsen_links import BagLigplaatsenLinks
from openapi_client.model.bagligplaatsen_gebruiksdoel import BagligplaatsenGebruiksdoel
from openapi_client.model.geometry import Geometry
