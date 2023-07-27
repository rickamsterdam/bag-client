# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
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

from openapi_client.model.paginated_bagdossiers_list import PaginatedBagdossiersList

from . import path

# Query params
CountSchema = schemas.BoolSchema
ExpandSchema = schemas.BoolSchema
ExpandScopeSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "json": "JSON",
            "csv": "CSV",
            "geojson": "GEOJSON",
        }
    
    @schemas.classproperty
    def JSON(cls):
        return cls("json")
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
    
    @schemas.classproperty
    def GEOJSON(cls):
        return cls("geojson")
PageSizeSchema = schemas.IntSchema
SortSchema = schemas.StrSchema
DossierSchema = schemas.StrSchema


class DossierInSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DossierInSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
DossierIsemptySchema = schemas.BoolSchema
DossierIsnullSchema = schemas.BoolSchema
DossierLikeSchema = schemas.StrSchema


class DossierNotSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DossierNotSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
HeeftBrondocumentenDocumentnummerSchema = schemas.StrSchema


class HeeftBrondocumentenDocumentnummerInSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'HeeftBrondocumentenDocumentnummerInSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
HeeftBrondocumentenDocumentnummerIsemptySchema = schemas.BoolSchema
HeeftBrondocumentenDocumentnummerIsnullSchema = schemas.BoolSchema
HeeftBrondocumentenDocumentnummerLikeSchema = schemas.StrSchema


class HeeftBrondocumentenDocumentnummerNotSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'HeeftBrondocumentenDocumentnummerNotSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
PageSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        '_count': typing.Union[CountSchema, bool, ],
        '_expand': typing.Union[ExpandSchema, bool, ],
        '_expandScope': typing.Union[ExpandScopeSchema, str, ],
        '_fields': typing.Union[FieldsSchema, str, ],
        '_format': typing.Union[FormatSchema, str, ],
        '_pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        '_sort': typing.Union[SortSchema, str, ],
        'dossier': typing.Union[DossierSchema, str, ],
        'dossier[in]': typing.Union[DossierInSchema, list, tuple, ],
        'dossier[isempty]': typing.Union[DossierIsemptySchema, bool, ],
        'dossier[isnull]': typing.Union[DossierIsnullSchema, bool, ],
        'dossier[like]': typing.Union[DossierLikeSchema, str, ],
        'dossier[not]': typing.Union[DossierNotSchema, list, tuple, ],
        'heeftBrondocumenten.documentnummer': typing.Union[HeeftBrondocumentenDocumentnummerSchema, str, ],
        'heeftBrondocumenten.documentnummer[in]': typing.Union[HeeftBrondocumentenDocumentnummerInSchema, list, tuple, ],
        'heeftBrondocumenten.documentnummer[isempty]': typing.Union[HeeftBrondocumentenDocumentnummerIsemptySchema, bool, ],
        'heeftBrondocumenten.documentnummer[isnull]': typing.Union[HeeftBrondocumentenDocumentnummerIsnullSchema, bool, ],
        'heeftBrondocumenten.documentnummer[like]': typing.Union[HeeftBrondocumentenDocumentnummerLikeSchema, str, ],
        'heeftBrondocumenten.documentnummer[not]': typing.Union[HeeftBrondocumentenDocumentnummerNotSchema, list, tuple, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_count = api_client.QueryParameter(
    name="_count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    explode=True,
)
request_query_expand = api_client.QueryParameter(
    name="_expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
request_query_expand_scope = api_client.QueryParameter(
    name="_expandScope",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandScopeSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="_fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="_format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="_pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="_sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_dossier = api_client.QueryParameter(
    name="dossier",
    style=api_client.ParameterStyle.FORM,
    schema=DossierSchema,
    explode=True,
)
request_query_dossier_in = api_client.QueryParameter(
    name="dossier[in]",
    style=api_client.ParameterStyle.FORM,
    schema=DossierInSchema,
)
request_query_dossier_isempty = api_client.QueryParameter(
    name="dossier[isempty]",
    style=api_client.ParameterStyle.FORM,
    schema=DossierIsemptySchema,
    explode=True,
)
request_query_dossier_isnull = api_client.QueryParameter(
    name="dossier[isnull]",
    style=api_client.ParameterStyle.FORM,
    schema=DossierIsnullSchema,
    explode=True,
)
request_query_dossier_like = api_client.QueryParameter(
    name="dossier[like]",
    style=api_client.ParameterStyle.FORM,
    schema=DossierLikeSchema,
    explode=True,
)
request_query_dossier_not = api_client.QueryParameter(
    name="dossier[not]",
    style=api_client.ParameterStyle.FORM,
    schema=DossierNotSchema,
    explode=True,
)
request_query_heeft_brondocumenten_documentnummer = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerSchema,
    explode=True,
)
request_query_heeft_brondocumenten_documentnummer_in = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer[in]",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerInSchema,
)
request_query_heeft_brondocumenten_documentnummer_isempty = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer[isempty]",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerIsemptySchema,
    explode=True,
)
request_query_heeft_brondocumenten_documentnummer_isnull = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer[isnull]",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerIsnullSchema,
    explode=True,
)
request_query_heeft_brondocumenten_documentnummer_like = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer[like]",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerLikeSchema,
    explode=True,
)
request_query_heeft_brondocumenten_documentnummer_not = api_client.QueryParameter(
    name="heeftBrondocumenten.documentnummer[not]",
    style=api_client.ParameterStyle.FORM,
    schema=HeeftBrondocumentenDocumentnummerNotSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
# Header params
AcceptCrsSchema = schemas.StrSchema
ContentCrsSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Accept-Crs': typing.Union[AcceptCrsSchema, str, ],
        'Content-Crs': typing.Union[ContentCrsSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_accept_crs = api_client.HeaderParameter(
    name="Accept-Crs",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AcceptCrsSchema,
)
request_header_content_crs = api_client.HeaderParameter(
    name="Content-Crs",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentCrsSchema,
)
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyApplicationHaljson = PaginatedBagdossiersList
SchemaFor200ResponseBodyTextCsv = PaginatedBagdossiersList
SchemaFor200ResponseBodyApplicationGeojson = PaginatedBagdossiersList


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationHaljson,
        SchemaFor200ResponseBodyTextCsv,
        SchemaFor200ResponseBodyApplicationGeojson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/hal+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationHaljson),
        'text/csv': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextCsv),
        'application/geo+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationGeojson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/hal+json',
    'text/csv',
    'application/geo+json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _bag_dossiers_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _bag_dossiers_list_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _bag_dossiers_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _bag_dossiers_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_count,
            request_query_expand,
            request_query_expand_scope,
            request_query_fields,
            request_query_format,
            request_query_page_size,
            request_query_sort,
            request_query_dossier,
            request_query_dossier_in,
            request_query_dossier_isempty,
            request_query_dossier_isnull,
            request_query_dossier_like,
            request_query_dossier_not,
            request_query_heeft_brondocumenten_documentnummer,
            request_query_heeft_brondocumenten_documentnummer_in,
            request_query_heeft_brondocumenten_documentnummer_isempty,
            request_query_heeft_brondocumenten_documentnummer_isnull,
            request_query_heeft_brondocumenten_documentnummer_like,
            request_query_heeft_brondocumenten_documentnummer_not,
            request_query_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_accept_crs,
            request_header_content_crs,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class BagDossiersList(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def bag_dossiers_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def bag_dossiers_list(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def bag_dossiers_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def bag_dossiers_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._bag_dossiers_list_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._bag_dossiers_list_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

