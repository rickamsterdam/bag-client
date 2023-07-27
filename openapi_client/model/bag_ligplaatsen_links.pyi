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


class BagLigplaatsenLinks(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The contents of the `ligplaatsen._links` field. It contains all relationships with objects.
    """


    class MetaOapg:
        required = {
            "schema",
            "heeftDossier",
            "heeftNevenadres",
            "ligtInBuurt",
            "heeftHoofdadres",
            "self",
            "heeftOnderzoeken",
        }
        
        class properties:
            schema = schemas.StrSchema
        
            @staticmethod
            def _self() -> typing.Type['BagLigplaatsenLink']:
                return BagLigplaatsenLink
        
            @staticmethod
            def heeftHoofdadres() -> typing.Type['BagNummeraanduidingenLink']:
                return BagNummeraanduidingenLink
        
            @staticmethod
            def ligtInBuurt() -> typing.Type['GebiedenBuurtenLink']:
                return GebiedenBuurtenLink
        
            @staticmethod
            def heeftDossier() -> typing.Type['BagdossiersLink']:
                return BagdossiersLink
            
            
            class heeftNevenadres(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BagligplaatsenHeeftNevenadresM2M']:
                        return BagligplaatsenHeeftNevenadresM2M
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BagligplaatsenHeeftNevenadresM2M'], typing.List['BagligplaatsenHeeftNevenadresM2M']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'heeftNevenadres':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BagligplaatsenHeeftNevenadresM2M':
                    return super().__getitem__(i)
            
            
            class heeftOnderzoeken(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BagligplaatsenHeeftOnderzoekenM2M']:
                        return BagligplaatsenHeeftOnderzoekenM2M
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BagligplaatsenHeeftOnderzoekenM2M'], typing.List['BagligplaatsenHeeftOnderzoekenM2M']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'heeftOnderzoeken':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BagligplaatsenHeeftOnderzoekenM2M':
                    return super().__getitem__(i)
            __annotations__ = {
                "schema": schema,
                "self": _self,
                "heeftHoofdadres": heeftHoofdadres,
                "ligtInBuurt": ligtInBuurt,
                "heeftDossier": heeftDossier,
                "heeftNevenadres": heeftNevenadres,
                "heeftOnderzoeken": heeftOnderzoeken,
            }
    
    schema: MetaOapg.properties.schema
    heeftDossier: 'BagdossiersLink'
    heeftNevenadres: MetaOapg.properties.heeftNevenadres
    ligtInBuurt: 'GebiedenBuurtenLink'
    heeftHoofdadres: 'BagNummeraanduidingenLink'
    heeftOnderzoeken: MetaOapg.properties.heeftOnderzoeken
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> 'BagLigplaatsenLink': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftHoofdadres"]) -> 'BagNummeraanduidingenLink': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ligtInBuurt"]) -> 'GebiedenBuurtenLink': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftDossier"]) -> 'BagdossiersLink': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftNevenadres"]) -> MetaOapg.properties.heeftNevenadres: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heeftOnderzoeken"]) -> MetaOapg.properties.heeftOnderzoeken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schema", "self", "heeftHoofdadres", "ligtInBuurt", "heeftDossier", "heeftNevenadres", "heeftOnderzoeken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> 'BagLigplaatsenLink': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftHoofdadres"]) -> 'BagNummeraanduidingenLink': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ligtInBuurt"]) -> 'GebiedenBuurtenLink': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftDossier"]) -> 'BagdossiersLink': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftNevenadres"]) -> MetaOapg.properties.heeftNevenadres: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heeftOnderzoeken"]) -> MetaOapg.properties.heeftOnderzoeken: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schema", "self", "heeftHoofdadres", "ligtInBuurt", "heeftDossier", "heeftNevenadres", "heeftOnderzoeken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schema: typing.Union[MetaOapg.properties.schema, str, ],
        heeftDossier: 'BagdossiersLink',
        heeftNevenadres: typing.Union[MetaOapg.properties.heeftNevenadres, list, tuple, ],
        ligtInBuurt: 'GebiedenBuurtenLink',
        heeftHoofdadres: 'BagNummeraanduidingenLink',
        heeftOnderzoeken: typing.Union[MetaOapg.properties.heeftOnderzoeken, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BagLigplaatsenLinks':
        return super().__new__(
            cls,
            *_args,
            schema=schema,
            heeftDossier=heeftDossier,
            heeftNevenadres=heeftNevenadres,
            ligtInBuurt=ligtInBuurt,
            heeftHoofdadres=heeftHoofdadres,
            heeftOnderzoeken=heeftOnderzoeken,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.bag_ligplaatsen_link import BagLigplaatsenLink
from openapi_client.model.bag_nummeraanduidingen_link import BagNummeraanduidingenLink
from openapi_client.model.bagdossiers_link import BagdossiersLink
from openapi_client.model.bagligplaatsen_heeft_nevenadres_m2_m import BagligplaatsenHeeftNevenadresM2M
from openapi_client.model.bagligplaatsen_heeft_onderzoeken_m2_m import BagligplaatsenHeeftOnderzoekenM2M
from openapi_client.model.gebieden_buurten_link import GebiedenBuurtenLink
