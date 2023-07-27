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


class PaginatedBagnummeraanduidingenList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class page(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        number = schemas.IntSchema
                        size = schemas.IntSchema
                        totalElements = schemas.IntSchema
                        totalPages = schemas.IntSchema
                        __annotations__ = {
                            "number": number,
                            "size": size,
                            "totalElements": totalElements,
                            "totalPages": totalPages,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["totalElements"]) -> MetaOapg.properties.totalElements: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["number", "size", "totalElements", "totalPages", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["totalElements"]) -> typing.Union[MetaOapg.properties.totalElements, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> typing.Union[MetaOapg.properties.totalPages, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["number", "size", "totalElements", "totalPages", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    totalElements: typing.Union[MetaOapg.properties.totalElements, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'page':
                    return super().__new__(
                        cls,
                        *_args,
                        number=number,
                        size=size,
                        totalElements=totalElements,
                        totalPages=totalPages,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class _links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class _self(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    href = schemas.StrSchema
                                    __annotations__ = {
                                        "href": href,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> '_self':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    href=href,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class next(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class href(
                                        schemas.StrBase,
                                        schemas.NoneBase,
                                        schemas.Schema,
                                        schemas.NoneStrMixin
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            format = 'uri'
                                    
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[None, str, ],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'href':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                _configuration=_configuration,
                                            )
                                    __annotations__ = {
                                        "href": href,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                href: typing.Union[MetaOapg.properties.href, None, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'next':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    href=href,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class previous(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class href(
                                        schemas.StrBase,
                                        schemas.NoneBase,
                                        schemas.Schema,
                                        schemas.NoneStrMixin
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            format = 'uri'
                                    
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[None, str, ],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'href':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                _configuration=_configuration,
                                            )
                                    __annotations__ = {
                                        "href": href,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                href: typing.Union[MetaOapg.properties.href, None, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'previous':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    href=href,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "self": _self,
                            "next": next,
                            "previous": previous,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["next"]) -> MetaOapg.properties.next: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["previous"]) -> MetaOapg.properties.previous: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["self", "next", "previous", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["previous"]) -> typing.Union[MetaOapg.properties.previous, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["self", "next", "previous", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    next: typing.Union[MetaOapg.properties.next, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    previous: typing.Union[MetaOapg.properties.previous, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_links':
                    return super().__new__(
                        cls,
                        *_args,
                        next=next,
                        previous=previous,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class _embedded(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class nummeraanduidingen(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['Bagnummeraanduidingen']:
                                    return Bagnummeraanduidingen
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['Bagnummeraanduidingen'], typing.List['Bagnummeraanduidingen']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'nummeraanduidingen':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'Bagnummeraanduidingen':
                                return super().__getitem__(i)
                        __annotations__ = {
                            "nummeraanduidingen": nummeraanduidingen,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["nummeraanduidingen"]) -> MetaOapg.properties.nummeraanduidingen: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["nummeraanduidingen", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["nummeraanduidingen"]) -> typing.Union[MetaOapg.properties.nummeraanduidingen, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nummeraanduidingen", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    nummeraanduidingen: typing.Union[MetaOapg.properties.nummeraanduidingen, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_embedded':
                    return super().__new__(
                        cls,
                        *_args,
                        nummeraanduidingen=nummeraanduidingen,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "page": page,
                "_links": _links,
                "_embedded": _embedded,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_embedded"]) -> MetaOapg.properties._embedded: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "_links", "_embedded", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_embedded"]) -> typing.Union[MetaOapg.properties._embedded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "_links", "_embedded", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        page: typing.Union[MetaOapg.properties.page, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _embedded: typing.Union[MetaOapg.properties._embedded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaginatedBagnummeraanduidingenList':
        return super().__new__(
            cls,
            *_args,
            page=page,
            _links=_links,
            _embedded=_embedded,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.bagnummeraanduidingen import Bagnummeraanduidingen
