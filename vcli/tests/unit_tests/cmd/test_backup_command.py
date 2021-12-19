#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#
import unittest
import pytest
import json
from unittest.mock import patch, MagicMock
from vcli.cmd.backup_command import BackupCommand
from vcli.constant import RETURN_CODE_SUCCESS


class BackupCommandTests(unittest.TestCase):
    """Backup Command unit tests"""

    def setUp(self):
        self.default_profile = "default"
        self.test_profile = "test"
        self.job_id_success = "success"

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys, caplog):
        self.capsys = capsys
        self.caplog = caplog

    # -------------- tests --------------

    @patch('argparse.Namespace')
    def test_operation_cmd(self, mock_args):
        assert BackupCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.backup_command.BackupV1Api')
    @patch('vcli.cmd.backup_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_backups_dbname_get.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        BackupCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.backup_command.BackupV1Api')
    @patch('vcli.cmd.backup_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_create_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.config_script_base = "test_config_script_base"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_backups_dbname_post.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        BackupCommand().operation_create(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.backup_command.BackupRestoreV1Api')
    @patch('vcli.cmd.backup_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_restore_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.archive_id = "test_archive_id"
        mock_args.include_objects = "test_object_1,test_object_2,test_object_3"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_restore_dbname_archive_id_post.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        BackupCommand().operation_restore(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
