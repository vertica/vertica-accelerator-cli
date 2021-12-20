#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import sys
import json
import unittest
import pytest

from unittest.mock import MagicMock, patch
from vcli.cmd.sub_command import SubCommand
from vcli.vcli_main import VcliMain
from vcli.constant import RETURN_CODE_SUCCESS


class VcliMainTests(unittest.TestCase):
    """Vcli Main unit tests"""

    def setUp(self):
        self.data_success = "success"

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys, caplog):
        self.capsys = capsys
        self.caplog = caplog

    # -------------- tests -------------- #

    @patch("vcli.cmd.dns_command.DNSCommand")
    @patch("vcli.cmd.report_command.ReportCommand")
    @patch("vcli.cmd.cron_command.CronCommand")
    @patch("vcli.cmd.task_command.TaskCommand")
    @patch("vcli.cmd.session_command.SessionCommand")
    @patch("vcli.cmd.backup_command.BackupCommand")
    @patch("vcli.cmd.subcluster_command.SubclusterCommand")
    @patch("vcli.cmd.database_command.DatabaseCommand")
    @patch("vcli.cmd.auth_command.AuthCommand")
    @patch("vcli.cmd.config_command.ConfigCommand")
    def test_constructor_success(self, mock_config, mock_auth,
                                 mock_database, mock_subcluster,
                                 mock_backup, mock_session,
                                 mock_task, mock_cron,
                                 mock_report, mock_dns):
        config_object = SubCommand(mock_config)
        auth_object = SubCommand(mock_auth)
        database_object = SubCommand(mock_database)
        subcluster_object = SubCommand(mock_subcluster)
        backup_object = SubCommand(mock_backup)
        session_object = SubCommand(mock_session)
        task_object = SubCommand(mock_task)
        cron_object = SubCommand(mock_cron)
        report_object = SubCommand(mock_report)
        dns_object = SubCommand(mock_dns)

        vcli_command = VcliMain()
        vcli_command.config_command = config_object
        vcli_command.auth_command = auth_object
        vcli_command.database_command = database_object
        vcli_command.subcluster_command = subcluster_object
        vcli_command.backup_command = backup_object
        vcli_command.session_command = session_object
        vcli_command.task_command = task_object
        vcli_command.cron_command = cron_object
        vcli_command.report_command = report_object
        vcli_command.dns_command = dns_object

        self.assertEqual(vcli_command.config_command, config_object)
        self.assertEqual(vcli_command.auth_command, auth_object)
        self.assertEqual(vcli_command.database_command, database_object)
        self.assertEqual(vcli_command.subcluster_command, subcluster_object)
        self.assertEqual(vcli_command.backup_command, backup_object)
        self.assertEqual(vcli_command.session_command, session_object)
        self.assertEqual(vcli_command.task_command, task_object)
        self.assertEqual(vcli_command.cron_command, cron_object)
        self.assertEqual(vcli_command.report_command, report_object)
        self.assertEqual(vcli_command.dns_command, dns_object)

    @patch('vcli.cmd.database_command.DatabaseDetailV1Api')
    @patch('vcli.cmd.database_command.build_api_client')
    def test_parse_success(self, mock_api_client, mock_client_class):
        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_databases_dbname_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        sys.argv[1:] = ['database', 'get', "--name", "dbname"]
        vcli_object = VcliMain()
        with self.assertRaises(SystemExit) as se:
            vcli_object.parse()
        self.assertEqual(se.exception.code, 0)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
