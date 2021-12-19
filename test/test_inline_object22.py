# coding: utf-8

"""
    VAAS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.inline_object22 import InlineObject22  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineObject22(unittest.TestCase):
    """InlineObject22 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject22
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_object22.InlineObject22()  # noqa: E501
        if include_optional :
            return InlineObject22(
                dnsname = '012', 
                module_names = [
                    'vertica_cluster'
                    ]
            )
        else :
            return InlineObject22(
                module_names = [
                    'vertica_cluster'
                    ],
        )

    def testInlineObject22(self):
        """Test InlineObject22"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()