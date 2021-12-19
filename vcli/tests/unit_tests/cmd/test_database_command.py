#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.database_command import DatabaseCommand
from vcli.util.static_params import (
    SUPPORTED_AWS_REGIONS,
    VALID_NODES_NUMBERS,
    SUPPORTED_AWS_ZONES,
    AWS_INSTANCE_TYPES,
    SUPPORTED_VERTICA_VERSIONS
)
from vcli.constant import RETURN_CODE_SUCCESS


class DatabaseCommandTests(unittest.TestCase):
    """Database Command unit tests"""

    def setUp(self):
        self.default_profile = "default"
        self.test_profile = "test"
        self.job_id_success = "success"
        self.data_success = "success"

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys, caplog):
        self.capsys = capsys
        self.caplog = caplog

    # -------------- tests --------------

    @patch('argparse.Namespace')
    def test_operation_cmd(self, mock_args):
        assert DatabaseCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.database_command.DatabaseV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_create_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.password = "test_password"
        mock_args.nodes = VALID_NODES_NUMBERS.THREE.value
        mock_args.region = SUPPORTED_AWS_REGIONS.US_EAST_1.value
        mock_args.availability_zone = SUPPORTED_AWS_ZONES.US_EAST_1_A.value
        mock_args.instance_type = AWS_INSTANCE_TYPES.I3_2XLARGE.value
        mock_args.external_access_cidr_block = "1.1.1.1/32"
        mock_args.vertica_version = SUPPORTED_VERTICA_VERSIONS.VERSION_10_1_0_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_post.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_create(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.biref = True
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_get_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseCommand().operation_get(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_start_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_put.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseCommand().operation_start(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_stop_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_put.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseCommand().operation_stop(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseHibernateV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_hibernate_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_hibernate_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_hibernate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseReviveV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_revive_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.availability_zone = SUPPORTED_AWS_ZONES.US_EAST_1_A.value
        mock_args.instance_type = AWS_INSTANCE_TYPES.I3_2XLARGE.value
        mock_args.external_access_cidr_block = "1.1.1.1/32"
        mock_args.vertica_version = SUPPORTED_VERTICA_VERSIONS.VERSION_10_1_0_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_revive_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_revive(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_drop_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_delete.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_drop(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseResizeV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_resize_increase_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.instance_count = 6
        mock_args.module_name = "vertica_cluster"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_resize_increase_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_resize_increase(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseResizeV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_resize_decrease_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.instance_count = 6
        mock_args.module_name = "vertica_cluster"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_resize_decrease_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_resize_decrease(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseRescaleV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_rescale_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.instance_type = "i3.x2large"
        mock_args.module_name = "vertica_cluster"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_rescale_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_rescale(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.DatabaseUpgradeV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_upgrade_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.vertica_version = "11.0.0.1"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_upgrade_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_upgrade(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_command.NetworkConfigV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_update_network_config_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.external_access_cidr_block = "1.1.1.1/32"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_config_dbname_cidr_block_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseCommand().operation_update_network_config(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
