#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest
import json

from unittest.mock import patch, MagicMock
from vcli.cmd.report_command import ReportCommand
from vcli.util.static_params import (
    VAAS_MODULES,
    VALID_REPORT_NAME,
    VALID_REPORT_RANGE
)
from vcli.constant import RETURN_CODE_SUCCESS


class ReportCommandTests(unittest.TestCase):
    """Report command unit tests"""

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
        assert ReportCommand().operation_cmd(args=mock_args) is None

    @patch('vcli.cmd.report_command.DcGraphGetReportQueryPerHourV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_query_per_hour_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.QUERY_PER_HOUR.value
        mock_args.range = VALID_REPORT_RANGE.ONE_HOUR.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_query_per_hour_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportDepotUtilizationV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_depot_utilization_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.DEPOT_UTILIZATION.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_depot_utilization_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportQueryResponseDistributionV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_response_distribution_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.QUERY_RESPONSE_DISTRIBUTION.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_response_distribution_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportTotalQueriesPerHrV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_query_by_hour_top5_users_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.QUERY_PER_HOUR_TOP_5_USERS.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_query_by_hour_top5_users_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportCpuPerHourByNodeV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_cpu_per_hour_by_node_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.CPU_PER_HOUR_BY_NODE.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_cpu_per_hour_by_node_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportUsageByTimeRangeV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_cpu_usage_by_time_range_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.CPU_BY_TIME_RANGE.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_usage_by_time_range_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportAllUsageByTimeRangeV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_usage_by_time_range_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.ALL_USAGE_BY_TIME_RANGE.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_usage_by_time_range_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportBillingSummaryV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_billing_summary_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.BILLING_SUMMARY.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_billing_summary_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportBillingTotalSummaryV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_billing_summary_total_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.BILLING_SUMMARY_TOTAL.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_billing_summary_total_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportBillingTotalPerDbSummaryV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_billing_summary_total_per_db_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.BILLING_SUMMARY_TOTAL_PER_DB.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_billing_summary_total_per_db_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphGetReportMemoryUsageV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_show_memory_usage_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.module = VAAS_MODULES.VERTICA_CLUSTER.value
        mock_args.report_name = VALID_REPORT_NAME.MEMORY_USAGE.value
        mock_args.range = VALID_REPORT_RANGE.ONE_MONTH.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_memory_usage_get.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_show(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    # --------- Report Generate Test Cases --------- #

    @patch('vcli.cmd.report_command.DcGraphQueryPerHourV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_query_per_hour_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.QUERY_PER_HOUR.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_query_per_hour_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphDepotUtilizationV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_depot_utilization_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.DEPOT_UTILIZATION.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_depot_utilization_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphQueryResponseDistributionV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_response_distribution_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.QUERY_RESPONSE_DISTRIBUTION.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_response_distribution_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphTotalQueriesPerHrV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_query_by_hour_top5_users_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.QUERY_PER_HOUR_TOP_5_USERS.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_query_by_hour_top5_users_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphCpuPerHourByNodeV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_cpu_per_hour_by_node_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.CPU_PER_HOUR_BY_NODE.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_cpu_per_hour_by_node_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphBillingSummaryV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_billing_summary_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.BILLING_SUMMARY.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_billing_summary_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphBillingSummaryTotalV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_billing_summary_total_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.BILLING_SUMMARY_TOTAL.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_billing_summary_total_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)

    @patch('vcli.cmd.report_command.DcGraphMemoryUsageV1Api')
    @patch('vcli.cmd.report_command.build_api_client')
    @patch('argparse.Namespace')
    def test_operation_generate_memory_usage_success(self, mock_args, mock_api_client, mock_client_class):
        mock_args.name = "test_db"
        mock_args.report_name = VALID_REPORT_NAME.MEMORY_USAGE.value

        mock_api_client.return_value = MagicMock()
        mock_client_class.return_value.v1_vaas_reports_dbname_memory_usage_post.return_value.to_dict.return_value = {
            "data": self.data_success
        }

        ReportCommand().operation_generate(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual({
            "return_code": RETURN_CODE_SUCCESS,
            "data": self.data_success
        }, json.loads(stdout))
        self.assertEqual('', stderr)
