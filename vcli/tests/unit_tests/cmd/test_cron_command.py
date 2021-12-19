#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.cron_command import CronCommand
from vcli.util.static_params import (
    VAAS_MODULES,
    CRON_ACTION,
    TOGGLE_ACTION
)
from vcli.constant import (
    MAX_CRON_NAME_LENGTH
)
from vcli.constant import RETURN_CODE_SUCCESS
from argparse import ArgumentTypeError


class CronCommandTests(unittest.TestCase):
    """Cron command unit tests"""

    def setUp(self):
        self.default_profile = "default"
        self.test_profile = "test"
        self.data_success = "success"

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys, caplog):
        self.capsys = capsys
        self.caplog = caplog

    # -------------- tests -------------- #

    @patch('argparse.Namespace')
    def test_operation_cmd(self, mock_args):
        assert CronCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.cron_command.CronJobConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_add_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.cron_name = "start_db"
        mock_args.cron_action = CRON_ACTION.START.value
        mock_args.cron_expression = "59 02 * * ? *"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        CronCommand().operation_add(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.cron_command.CronJobConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_remove_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.cron_name = "start_db"
        mock_args.cron_action = CRON_ACTION.START.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_delete.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        CronCommand().operation_remove(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.cron_command.CronJobConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        CronCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.cron_command.CronJobConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_list_no_cronjobs(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_get.return_value.to_dict.return_value = {
            "data": None
        }

        CronCommand().operation_list(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": "There are no cronjobs associated with the database."
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.cron_command.CronUpdateConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_set_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.cron_name = "start_db"
        mock_args.cron_action = CRON_ACTION.START.value
        mock_args.action = TOGGLE_ACTION.DISABLE.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_schedule_name_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        CronCommand().operation_set(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.cron_command.CronUpdateConfigV1Api')
    @patch('vcli.cmd.cron_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_update_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.cron_name = "start_db"
        mock_args.cron_action = CRON_ACTION.START.value
        mock_args.cron_expression = "30 14 ? * * *"
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_cron_dbname_schedule_name_put.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        CronCommand().operation_update(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
