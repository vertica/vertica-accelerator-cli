# coding: utf-8

"""
    VAAS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.database_upgrade_v1_api import DatabaseUpgradeV1Api  # noqa: E501
from openapi_client.rest import ApiException


class TestDatabaseUpgradeV1Api(unittest.TestCase):
    """DatabaseUpgradeV1Api unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.database_upgrade_v1_api.DatabaseUpgradeV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_vaas_databases_dbname_upgrade_put(self):
        """Test case for v1_vaas_databases_dbname_upgrade_put

        """
        pass


if __name__ == '__main__':
    unittest.main()
