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


class SubclusterHostDetailV1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete(self, host_id, database_name, subcluster_name, **kwargs):  # noqa: E501
        """v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete  # noqa: E501

        Removes a host from the subcluster and stops the host. (removes this in the list of active hosts for the subcluster)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete(host_id, database_name, subcluster_name, async_req=True)
        >>> result = thread.get()

        :param host_id: (required)
        :type host_id: str
        :param database_name: (required)
        :type database_name: str
        :param subcluster_name: (required)
        :type subcluster_name: str
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete_with_http_info(host_id, database_name, subcluster_name, **kwargs)  # noqa: E501

    def v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete_with_http_info(self, host_id, database_name, subcluster_name, **kwargs):  # noqa: E501
        """v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete  # noqa: E501

        Removes a host from the subcluster and stops the host. (removes this in the list of active hosts for the subcluster)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete_with_http_info(host_id, database_name, subcluster_name, async_req=True)
        >>> result = thread.get()

        :param host_id: (required)
        :type host_id: str
        :param database_name: (required)
        :type database_name: str
        :param subcluster_name: (required)
        :type subcluster_name: str
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'host_id',
            'database_name',
            'subcluster_name'
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
                    " to method v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'host_id' is set
        if self.api_client.client_side_validation and ('host_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['host_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `host_id` when calling `v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete`")  # noqa: E501
        # verify the required parameter 'database_name' is set
        if self.api_client.client_side_validation and ('database_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['database_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `database_name` when calling `v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete`")  # noqa: E501
        # verify the required parameter 'subcluster_name' is set
        if self.api_client.client_side_validation and ('subcluster_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['subcluster_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subcluster_name` when calling `v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']  # noqa: E501
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']  # noqa: E501
        if 'subcluster_name' in local_var_params:
            path_params['subcluster_name'] = local_var_params['subcluster_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            '/v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts/{host_id}', 'DELETE',
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
