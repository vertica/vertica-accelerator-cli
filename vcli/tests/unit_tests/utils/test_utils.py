#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest

from datetime import datetime as dt
from unittest.mock import patch
from argparse import ArgumentTypeError
from vcli.util.cli_options import CliOptions
from vcli.util.utils import (
    str_to_bool,
    cron_name_validate,
    get_date_time,
    db_name_validate,
    dns_name_validate,
    http_name_validate
)
from vcli.util.static_params import (
    VALID_REPORT_RANGE
)


class UtilsTests(unittest.TestCase):
    """Utils unit tests"""

    def test_str_to_bool(self):
        self.assertEqual(str_to_bool('y'), True)
        self.assertEqual(str_to_bool('n'), False)
        self.assertEqual(str_to_bool(True), True)

        with self.assertRaises(ArgumentTypeError):
            str_to_bool('abc')

    def test_cron_name_validate(self):
        self.assertEqual(cron_name_validate('name'), 'name')

        with self.assertRaises(ArgumentTypeError):
            cron_name_validate('some_big_name')

    @patch("vcli.util.utils.dt")
    def test_get_date_time(self, mock_dt):
        end_date = dt(2021, 12, 1, 0, 0)
        mock_dt.utcnow.return_value = end_date

        three_month = (dt(2021, 9, 2), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.THREE_MONTH.value), three_month)

        one_month = (dt(2021, 11, 1), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.ONE_MONTH.value), one_month)

        one_week = (dt(2021, 11, 24), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.ONE_WEEK.value), one_week)

        one_day = (dt(2021, 11, 30), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.ONE_DAY.value), one_day)

        eight_hour = (dt(2021, 11, 30, 16, 0), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.EIGHT_HOURS.value), eight_hour)

        one_hour = (dt(2021, 11, 30, 23, 0), end_date)
        self.assertEqual(get_date_time(
            VALID_REPORT_RANGE.ONE_HOUR.value), one_hour)

    def test_db_name_validate(self):
        self.assertEqual(db_name_validate('dbname'), 'dbname')

        with self.assertRaises(ArgumentTypeError):
            db_name_validate('some_another_big_dbname')

    def test_dns_name_validate(self):
        self.assertEqual(dns_name_validate('dnsname'), 'dnsname')

        with self.assertRaises(ArgumentTypeError):
            dns_name_validate('some_another_big_dnsname')

    def test_http_name_validate(self):
        self.assertEqual(http_name_validate('https://vertica.okta.com'), 'https://vertica.okta.com')

        with self.assertRaises(ArgumentTypeError):
            http_name_validate('some_random_string')
