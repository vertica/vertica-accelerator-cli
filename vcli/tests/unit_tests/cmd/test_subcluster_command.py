#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.subcluster_command import SubclusterCommand
from vcli.util.static_params import (
    VALID_NODES_NUMBERS,
    AWS_INSTANCE_TYPES,
    VAAS_MODULES
)
from vcli.constant import RETURN_CODE_SUCCESS


class SubclusterCommandTests(unittest.TestCase):
    """Subcluster Command unit tests"""

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

    # -------------- tests -------------- #

    @patch('argparse.Namespace')
    def test_operation_cmd(self, mock_args):
        assert SubclusterCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.subcluster_command.SubclusterV1Api')
    @patch('vcli.cmd.subcluster_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_create_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.subcluster_name = "test_subcluster"
        mock_args.nodes = VALID_NODES_NUMBERS.THREE.value
        mock_args.instance_type = AWS_INSTANCE_TYPES.I3_4XLARGE.value
        mock_args.module = VAAS_MODULES.VERTICA_SUBCLUSTER_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_subclusters_post.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        SubclusterCommand().operation_create(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.subcluster_command.SubclusterV1Api')
    @patch('vcli.cmd.subcluster_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_drop_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_SUBCLUSTER_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_subclusters_delete.return_value.to_dict.return_value = {
            "jobid": self.job_id_success
        }

        SubclusterCommand().operation_drop(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "job_id": self.job_id_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.subcluster_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.subcluster_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_start_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_SUBCLUSTER_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_put.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        SubclusterCommand().operation_start(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.subcluster_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.subcluster_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_stop_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_SUBCLUSTER_1.value
        mock_args.profile = self.default_profile

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_put.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        SubclusterCommand().operation_stop(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
