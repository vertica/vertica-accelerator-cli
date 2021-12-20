#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.task_command import TaskCommand
from vcli.constant import RETURN_CODE_SUCCESS


class TaskCommandTests(unittest.TestCase):
    """Task Command unit tests"""

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
        assert TaskCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.task_command.TaskV1Api')
    @patch('vcli.cmd.task_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.type = "running"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_tasks_get.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        TaskCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.task_command.TaskDetailV1Api')
    @patch('vcli.cmd.task_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_get_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.task_id = "test_task_id"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_tasks_task_id_get.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        TaskCommand().operation_get(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.task_command.TaskLatestStatusDetailV1Api')
    @patch('vcli.cmd.task_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_status_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.task_id = "test_task_id"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_tasks_task_id_latest_status_get.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        TaskCommand().operation_status(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
