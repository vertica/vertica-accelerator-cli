#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json
from unittest.mock import patch, MagicMock
from vcli.cmd.session_command import SessionCommand
from vcli.constant import RETURN_CODE_SUCCESS


class SessionCommandTests(unittest.TestCase):
    """Session Command unit tests"""

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
        assert SessionCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.session_command.SessionV1Api')
    @patch('vcli.cmd.session_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_sessions_dbname_get.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        SessionCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.session_command.SessionV1Api')
    @patch('vcli.cmd.session_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_remove_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.session = "test_session"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_sessions_dbname_delete.return_value.to_dict.return_value = {
            "data": self.job_id_success
        }

        SessionCommand().operation_remove(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
