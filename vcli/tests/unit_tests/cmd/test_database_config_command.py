#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.database_config_command import DatabaseConfigCommand
from vcli.constant import RETURN_CODE_SUCCESS


class DatabaseConfigCommandTests(unittest.TestCase):
    """Database Config command unit tests"""

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
        assert DatabaseConfigCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.database_config_command.ScheduleIdleShutdownV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_idle_shutdown_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_idle_shutdown_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseConfigCommand().operation_idle_shutdown_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_config_command.ScheduleIdleShutdownV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_idle_shutdown_update_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.shutdown_timeout = 15
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_idle_shutdown_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseConfigCommand().operation_idle_shutdown_update(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_config_command.ScheduleIdleShutdownV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_idle_shutdown_delete_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.permanent = False
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_idle_shutdown_delete.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseConfigCommand().operation_idle_shutdown_delete(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_config_command.ScheduleAutoScalingV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_auto_scale_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_auto_scaling_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        DatabaseConfigCommand().operation_auto_scale_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_config_command.ScheduleAutoScalingV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_auto_scale_update_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.client_drain_time = 5
        mock_args.sequence_count = 5
        mock_args.max_sessions = 5
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_auto_scaling_put.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseConfigCommand().operation_auto_scale_update(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.database_config_command.ScheduleAutoScalingV1Api')
    @patch('vcli.cmd.database_config_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_auto_scale_delete_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.permanent = False
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_auto_scaling_delete.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        DatabaseConfigCommand().operation_auto_scale_delete(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
