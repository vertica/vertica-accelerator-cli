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
from openapi_client.api.backup_v1_api import BackupV1Api  # noqa: E501
from openapi_client.rest import ApiException


class TestBackupV1Api(unittest.TestCase):
    """BackupV1Api unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.backup_v1_api.BackupV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_vaas_backups_config_dbname_config_script_base_post(self):
        """Test case for v1_vaas_backups_config_dbname_config_script_base_post

        """
        pass

    def test_v1_vaas_backups_config_script_base_archive_id_get(self):
        """Test case for v1_vaas_backups_config_script_base_archive_id_get

        """
        pass

    def test_v1_vaas_backups_dbname_get(self):
        """Test case for v1_vaas_backups_dbname_get

        """
        pass

    def test_v1_vaas_backups_dbname_post(self):
        """Test case for v1_vaas_backups_dbname_post

        """
        pass


if __name__ == '__main__':
    unittest.main()