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


class BagStandplaatsenLink(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The identifier of the relationship to standplaatsen.
    """


    class MetaOapg:
        required = {
            "identificatie",
            "volgnummer",
            "href",
            "title",
        }
        
        class properties:
            href = schemas.StrSchema
            title = schemas.StrSchema
            
            
            class identificatie(
                schemas.StrSchema
            ):
                pass
            
            
            class volgnummer(
                schemas.Int64Schema
            ):
                pass
            __annotations__ = {
                "href": href,
                "title": title,
                "identificatie": identificatie,
                "volgnummer": volgnummer,
            }
    
    identificatie: MetaOapg.properties.identificatie
    volgnummer: MetaOapg.properties.volgnummer
    href: MetaOapg.properties.href
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificatie"]) -> MetaOapg.properties.identificatie: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volgnummer"]) -> MetaOapg.properties.volgnummer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", "title", "identificatie", "volgnummer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificatie"]) -> MetaOapg.properties.identificatie: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volgnummer"]) -> MetaOapg.properties.volgnummer: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", "title", "identificatie", "volgnummer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        identificatie: typing.Union[MetaOapg.properties.identificatie, str, ],
        volgnummer: typing.Union[MetaOapg.properties.volgnummer, decimal.Decimal, int, ],
        href: typing.Union[MetaOapg.properties.href, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BagStandplaatsenLink':
        return super().__new__(
            cls,
            *_args,
            identificatie=identificatie,
            volgnummer=volgnummer,
            href=href,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )
