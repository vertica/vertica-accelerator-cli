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


class CronUpdateConfigV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_vaas_cron_dbname_schedule_name_post(self, schedule_name, dbname, **kwargs):  # noqa: E501
        """v1_vaas_cron_dbname_schedule_name_post  # noqa: E501

        Enable or Disable a cron job from the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_cron_dbname_schedule_name_post(schedule_name, dbname, async_req=True)
        >>> result = thread.get()

        :param schedule_name: (required)
        :type schedule_name: str
        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject7
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
        return self.v1_vaas_cron_dbname_schedule_name_post_with_http_info(schedule_name, dbname, **kwargs)  # noqa: E501

    def v1_vaas_cron_dbname_schedule_name_post_with_http_info(self, schedule_name, dbname, **kwargs):  # noqa: E501
        """v1_vaas_cron_dbname_schedule_name_post  # noqa: E501

        Enable or Disable a cron job from the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_cron_dbname_schedule_name_post_with_http_info(schedule_name, dbname, async_req=True)
        >>> result = thread.get()

        :param schedule_name: (required)
        :type schedule_name: str
        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject7
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
            'schedule_name',
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
                    " to method v1_vaas_cron_dbname_schedule_name_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'schedule_name' is set
        if self.api_client.client_side_validation and ('schedule_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['schedule_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `schedule_name` when calling `v1_vaas_cron_dbname_schedule_name_post`")  # noqa: E501
        # verify the required parameter 'dbname' is set
        if self.api_client.client_side_validation and ('dbname' not in local_var_params or  # noqa: E501
                                                        local_var_params['dbname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dbname` when calling `v1_vaas_cron_dbname_schedule_name_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_name' in local_var_params:
            path_params['schedule_name'] = local_var_params['schedule_name']  # noqa: E501
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
            ['*/*', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "InlineResponse200",
            408: None,
            500: None,
        }

        return self.api_client.call_api(
            '/v1/vaas/cron/{dbname}/{schedule_name}', 'POST',
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

    def v1_vaas_cron_dbname_schedule_name_put(self, schedule_name, dbname, **kwargs):  # noqa: E501
        """v1_vaas_cron_dbname_schedule_name_put  # noqa: E501

        Update an existing cron job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_cron_dbname_schedule_name_put(schedule_name, dbname, async_req=True)
        >>> result = thread.get()

        :param schedule_name: (required)
        :type schedule_name: str
        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject6
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
        return self.v1_vaas_cron_dbname_schedule_name_put_with_http_info(schedule_name, dbname, **kwargs)  # noqa: E501

    def v1_vaas_cron_dbname_schedule_name_put_with_http_info(self, schedule_name, dbname, **kwargs):  # noqa: E501
        """v1_vaas_cron_dbname_schedule_name_put  # noqa: E501

        Update an existing cron job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_cron_dbname_schedule_name_put_with_http_info(schedule_name, dbname, async_req=True)
        >>> result = thread.get()

        :param schedule_name: (required)
        :type schedule_name: str
        :param dbname: (required)
        :type dbname: str
        :param body:
        :type body: InlineObject6
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
            'schedule_name',
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
                    " to method v1_vaas_cron_dbname_schedule_name_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'schedule_name' is set
        if self.api_client.client_side_validation and ('schedule_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['schedule_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `schedule_name` when calling `v1_vaas_cron_dbname_schedule_name_put`")  # noqa: E501
        # verify the required parameter 'dbname' is set
        if self.api_client.client_side_validation and ('dbname' not in local_var_params or  # noqa: E501
                                                        local_var_params['dbname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dbname` when calling `v1_vaas_cron_dbname_schedule_name_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_name' in local_var_params:
            path_params['schedule_name'] = local_var_params['schedule_name']  # noqa: E501
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
            ['*/*', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "InlineResponse200",
            408: None,
            500: None,
        }

        return self.api_client.call_api(
            '/v1/vaas/cron/{dbname}/{schedule_name}', 'PUT',
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
