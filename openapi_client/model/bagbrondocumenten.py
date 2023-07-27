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


class Bagbrondocumenten(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    brondocumenten
    """


    class MetaOapg:
        required = {
            "documentnummer",
            "_links",
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
                            BagBrondocumentenLinks,
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
            
            
            class documentnummer(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2147483647
            
            
            class bronleverancierCode(
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
                ) -> 'bronleverancierCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class bronleverancierOmschrijving(
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
                ) -> 'bronleverancierOmschrijving':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class typeDossierCode(
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
                ) -> 'typeDossierCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class typeDossierOmschrijving(
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
                ) -> 'typeDossierOmschrijving':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class typeBrondocumentCode(
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
                ) -> 'typeBrondocumentCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class typeBrondocumentOmschrijving(
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
                ) -> 'typeBrondocumentOmschrijving':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
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
            __annotations__ = {
                "_links": _links,
                "documentnummer": documentnummer,
                "bronleverancierCode": bronleverancierCode,
                "bronleverancierOmschrijving": bronleverancierOmschrijving,
                "typeDossierCode": typeDossierCode,
                "typeDossierOmschrijving": typeDossierOmschrijving,
                "typeBrondocumentCode": typeBrondocumentCode,
                "typeBrondocumentOmschrijving": typeBrondocumentOmschrijving,
                "registratiedatum": registratiedatum,
            }
    
    documentnummer: MetaOapg.properties.documentnummer
    _links: MetaOapg.properties._links
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentnummer"]) -> MetaOapg.properties.documentnummer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bronleverancierCode"]) -> MetaOapg.properties.bronleverancierCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bronleverancierOmschrijving"]) -> MetaOapg.properties.bronleverancierOmschrijving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeDossierCode"]) -> MetaOapg.properties.typeDossierCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeDossierOmschrijving"]) -> MetaOapg.properties.typeDossierOmschrijving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeBrondocumentCode"]) -> MetaOapg.properties.typeBrondocumentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeBrondocumentOmschrijving"]) -> MetaOapg.properties.typeBrondocumentOmschrijving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registratiedatum"]) -> MetaOapg.properties.registratiedatum: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "documentnummer", "bronleverancierCode", "bronleverancierOmschrijving", "typeDossierCode", "typeDossierOmschrijving", "typeBrondocumentCode", "typeBrondocumentOmschrijving", "registratiedatum", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentnummer"]) -> MetaOapg.properties.documentnummer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bronleverancierCode"]) -> typing.Union[MetaOapg.properties.bronleverancierCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bronleverancierOmschrijving"]) -> typing.Union[MetaOapg.properties.bronleverancierOmschrijving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeDossierCode"]) -> typing.Union[MetaOapg.properties.typeDossierCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeDossierOmschrijving"]) -> typing.Union[MetaOapg.properties.typeDossierOmschrijving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeBrondocumentCode"]) -> typing.Union[MetaOapg.properties.typeBrondocumentCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeBrondocumentOmschrijving"]) -> typing.Union[MetaOapg.properties.typeBrondocumentOmschrijving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registratiedatum"]) -> typing.Union[MetaOapg.properties.registratiedatum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "documentnummer", "bronleverancierCode", "bronleverancierOmschrijving", "typeDossierCode", "typeDossierOmschrijving", "typeBrondocumentCode", "typeBrondocumentOmschrijving", "registratiedatum", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        documentnummer: typing.Union[MetaOapg.properties.documentnummer, str, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        bronleverancierCode: typing.Union[MetaOapg.properties.bronleverancierCode, None, str, schemas.Unset] = schemas.unset,
        bronleverancierOmschrijving: typing.Union[MetaOapg.properties.bronleverancierOmschrijving, None, str, schemas.Unset] = schemas.unset,
        typeDossierCode: typing.Union[MetaOapg.properties.typeDossierCode, None, str, schemas.Unset] = schemas.unset,
        typeDossierOmschrijving: typing.Union[MetaOapg.properties.typeDossierOmschrijving, None, str, schemas.Unset] = schemas.unset,
        typeBrondocumentCode: typing.Union[MetaOapg.properties.typeBrondocumentCode, None, str, schemas.Unset] = schemas.unset,
        typeBrondocumentOmschrijving: typing.Union[MetaOapg.properties.typeBrondocumentOmschrijving, None, str, schemas.Unset] = schemas.unset,
        registratiedatum: typing.Union[MetaOapg.properties.registratiedatum, None, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Bagbrondocumenten':
        return super().__new__(
            cls,
            *_args,
            documentnummer=documentnummer,
            _links=_links,
            bronleverancierCode=bronleverancierCode,
            bronleverancierOmschrijving=bronleverancierOmschrijving,
            typeDossierCode=typeDossierCode,
            typeDossierOmschrijving=typeDossierOmschrijving,
            typeBrondocumentCode=typeBrondocumentCode,
            typeBrondocumentOmschrijving=typeBrondocumentOmschrijving,
            registratiedatum=registratiedatum,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.bag_brondocumenten_links import BagBrondocumentenLinks
