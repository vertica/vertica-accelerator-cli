# coding: utf-8

"""
    VAAS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ScheduleAutoScalingV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_vaas_databases_dbname_auto_scaling_delete(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_delete  # noqa: E501

        Delete auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_delete(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject12
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2002
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_vaas_databases_dbname_auto_scaling_delete_with_http_info(dbname, **kwargs)  # noqa: E501

    def v1_vaas_databases_dbname_auto_scaling_delete_with_http_info(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_delete  # noqa: E501

        Delete auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_delete_with_http_info(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject12
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'dbname',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_vaas_databases_dbname_auto_scaling_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dbname' is set
        if self.api_client.client_side_validation and ('dbname' not in local_var_params or  # noqa: E501
                                                        local_var_params['dbname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dbname` when calling `v1_vaas_databases_dbname_auto_scaling_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dbname' in local_var_params:
            path_params['dbname'] = local_var_params['dbname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "InlineResponse2002",
            408: None,
            500: None,
        }

        return self.api_client.call_api(
            '/v1/vaas/databases/{dbname}/auto-scaling', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def v1_vaas_databases_dbname_auto_scaling_get(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_get  # noqa: E501

        Get auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_get(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param enabled: Filter result by the enable flag. All schedule configures will be returned if no flag is specified.
        :type enabled: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse200
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_vaas_databases_dbname_auto_scaling_get_with_http_info(dbname, **kwargs)  # noqa: E501

    def v1_vaas_databases_dbname_auto_scaling_get_with_http_info(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_get  # noqa: E501

        Get auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_get_with_http_info(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param enabled: Filter result by the enable flag. All schedule configures will be returned if no flag is specified.
        :type enabled: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse200, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'dbname',
            'enabled'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_vaas_databases_dbname_auto_scaling_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dbname' is set
        if self.api_client.client_side_validation and ('dbname' not in local_var_params or  # noqa: E501
                                                        local_var_params['dbname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dbname` when calling `v1_vaas_databases_dbname_auto_scaling_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dbname' in local_var_params:
            path_params['dbname'] = local_var_params['dbname']  # noqa: E501

        query_params = []
        if 'enabled' in local_var_params and local_var_params['enabled'] is not None:  # noqa: E501
            query_params.append(('enabled', local_var_params['enabled']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "InlineResponse200",
            404: "InlineResponse404",
            408: None,
            500: None,
        }

        return self.api_client.call_api(
            '/v1/vaas/databases/{dbname}/auto-scaling', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def v1_vaas_databases_dbname_auto_scaling_put(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_put  # noqa: E501

        Upsert auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_put(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: DBAutoscalingJobConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2002
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_vaas_databases_dbname_auto_scaling_put_with_http_info(dbname, **kwargs)  # noqa: E501

    def v1_vaas_databases_dbname_auto_scaling_put_with_http_info(self, dbname, **kwargs):  # noqa: E501
        """v1_vaas_databases_dbname_auto_scaling_put  # noqa: E501

        Upsert auto-scaling configuration for specific database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_dbname_auto_scaling_put_with_http_info(dbname, async_req=True)
        >>> result = thread.get()

        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: DBAutoscalingJobConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'dbname',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_vaas_databases_dbname_auto_scaling_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dbname' is set
        if self.api_client.client_side_validation and ('dbname' not in local_var_params or  # noqa: E501
                                                        local_var_params['dbname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dbname` when calling `v1_vaas_databases_dbname_auto_scaling_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dbname' in local_var_params:
            path_params['dbname'] = local_var_params['dbname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "InlineResponse2002",
            408: None,
            428: "InlineResponse428",
            500: None,
        }

        return self.api_client.call_api(
            '/v1/vaas/databases/{dbname}/auto-scaling', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
