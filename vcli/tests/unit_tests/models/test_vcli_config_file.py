import unittest
import pytest

from unittest.mock import patch
from vcli.models.vcli_config_file import VcliConfigFile
from vcli.exceptions.vcli_custom_exception import (
    ValidationFailedError,
    ProfileNotExistError,
    ProfilePermissionError
)
from vcli.util.error_message import ErrorMessage


class VcliConfigFileTests(unittest.TestCase):
    """Vcli Config File unit tests"""

    def setUp(self):
        self.service_endpoint = "test_service_endpoint"
        self.default_profile = "default"
        self.test_obj = VcliConfigFile(self.service_endpoint)

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys):
        self.capsys = capsys

    # -------------- tests -------------- #

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_service_endpoint_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        with pytest.raises(ValidationFailedError) as err:
            test_obj = VcliConfigFile(service_endpoint=None)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.OA_SERVICE_CAN_NOT_BE_NONE)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_max_attempts_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        test_obj = VcliConfigFile(
            service_endpoint=self.service_endpoint, max_attempts=None)
        self.assertEqual(type(test_obj), type(self.test_obj))

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_check_profile_file_profile_not_exist(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = "profile_not_exist"
        mock_os_path_exists.return_value = False
        mock_os_access.return_value = True

        with pytest.raises(ProfileNotExistError) as err:
            self.test_obj.check_profile_file(profile=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_CONFIG_CONFIG_NOT_EXIST)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_check_profile_file_profile_not_readable(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = False

        with pytest.raises(ProfilePermissionError) as err:
            self.test_obj.check_profile_file(profile=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_CONFIG_CONFIG_NOT_READABLE)
