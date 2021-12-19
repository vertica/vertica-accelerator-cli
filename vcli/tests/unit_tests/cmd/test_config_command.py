#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest

from unittest.mock import patch, mock_open
from vcli.cmd.config_command import ConfigCommand
from vcli.constant import VCLI_CONFIG_PATH, VCLI_CONFIG_FILE, VCLI_CREDENTIAL_FILE
from vcli.models.vcli_credential_file import VcliCredentialFile
from vcli.models.vcli_config_file import VcliConfigFile
from vcli.exceptions.vcli_custom_exception import ValidationFailedError, ProfileNotExistError

MOCK_CONFIG_FILE_CONTENT = '''
[default]
service_endpoint = default_service_endpoint
max_attempts = 3

[test]
service_endpoint = test_service_endpoint
max_attempts = 3
'''

MOCK_CREDENTIAL_FILE_CONTENT = '''
[default]
username = default_username
password = default_password
client_id = default_client_id
auth_endpont = default_auth_endpont
access_token_file = default_access_token_file

[test]
username = test_username
password = test_password
client_id = test_client_id
auth_endpont = test_auth_endpont
'''

input_values = [
    "test_username",
    "test_client_id",
    "test_auth_endpont",
    "test_service_endpoint",
    "3"
]


def my_open(filename, *args, **kwargs):
    if filename == f"{VCLI_CONFIG_PATH}/{VCLI_CONFIG_FILE}":
        content = MOCK_CONFIG_FILE_CONTENT
    elif filename == f"{VCLI_CONFIG_PATH}/{VCLI_CREDENTIAL_FILE}":
        content = MOCK_CREDENTIAL_FILE_CONTENT

    file_object = mock_open(read_data=content).return_value
    file_object.__iter__.return_value = content.splitlines(True)
    return file_object


class ConfigCommandTests(unittest.TestCase):
    """Config Command unit tests"""

    def setUp(self):
        self.open_patch = patch('builtins.open', new=my_open)
        self.open_patch.start()
        self.default_profile = "default"
        self.test_profile = "test"

    def tearDown(self):
        self.open_patch.stop()
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys, caplog):
        self.capsys = capsys
        self.caplog = caplog

    # -------------- tests --------------

    @patch('vcli.models.vcli_credential_file.VcliCredentialFile.read_profile_config')
    @patch('vcli.models.vcli_config_file.VcliConfigFile.read_profile_config')
    @patch('argparse.Namespace')
    def test_read_user_input_detail_success_all_default(self, mock_args, mock_config_read_profile, mock_credentials_read_profile):
        mock_args.username = None
        mock_args.password = None
        mock_args.client_id = None
        mock_args.auth_endpont = None
        mock_args.service_endpoint = None
        mock_args.max_attempts = None
        mock_args.profile = self.default_profile

        mock_config_read_profile.return_value = VcliConfigFile(service_endpoint="default_service_endpoint",
                                                               max_attempts='3')
        mock_credentials_read_profile.return_value = VcliCredentialFile(username="default_username",
                                                                        password="default_password",
                                                                        client_id="default_client_id",
                                                                        auth_endpont="default_auth_endpont")
        vcli_config_data, vcli_credential_data = ConfigCommand.read_user_input_detail(
            args=mock_args)

        self.assertEqual(type(vcli_config_data), VcliConfigFile)
        self.assertEqual(type(vcli_credential_data), VcliCredentialFile)

        self.assertEqual(vcli_credential_data.username,
                         f"{self.default_profile}_username")
        self.assertEqual(vcli_credential_data.password,
                         f"{self.default_profile}_password")
        self.assertEqual(vcli_credential_data.client_id,
                         f"{self.default_profile}_client_id")
        self.assertEqual(vcli_credential_data.auth_endpont,
                         f"{self.default_profile}_auth_endpont")
        self.assertEqual(vcli_config_data.service_endpoint,
                         f"{self.default_profile}_service_endpoint")
        self.assertEqual(vcli_config_data.max_attempts, "3")

    @patch('argparse.Namespace')
    def test_read_user_input_detail_success_all_input(self, mock_args):
        mock_args.username = "test_username"
        mock_args.password = "test_password"
        mock_args.client_id = "test_client_id"
        mock_args.auth_endpont = "test_auth_endpont"
        mock_args.service_endpoint = "test_service_endpoint"
        mock_args.max_attempts = "4"
        mock_args.profile = self.default_profile
        vcli_config_data, vcli_credential_data = ConfigCommand.read_user_input_detail(
            args=mock_args)

        self.assertEqual(type(vcli_config_data), VcliConfigFile)
        self.assertEqual(type(vcli_credential_data), VcliCredentialFile)

        self.assertEqual(vcli_credential_data.username, "test_username")
        self.assertEqual(vcli_credential_data.password, "test_password")
        self.assertEqual(vcli_credential_data.client_id, "test_client_id")
        self.assertEqual(vcli_credential_data.auth_endpont, "test_auth_endpont")
        self.assertEqual(vcli_config_data.service_endpoint, "test_service_endpoint")
        self.assertEqual(vcli_config_data.max_attempts, "4")

    @patch('argparse.Namespace')
    def test_read_user_input_detail_fail_profile_not_exit(self, mock_args):
        mock_args.profile = "Nope"
        with self.assertRaises(ProfileNotExistError):
            _, _ = ConfigCommand.read_user_input_detail(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=input_values)
    @patch('argparse.Namespace')
    def test_read_user_input_all_success_all_input(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        vcli_config_data, vcli_credential_data = ConfigCommand.read_user_input_all(
            args=mock_args)

        self.assertEqual(type(vcli_config_data), VcliConfigFile)
        self.assertEqual(type(vcli_credential_data), VcliCredentialFile)

        self.assertEqual(vcli_credential_data.username, "test_username")
        self.assertEqual(vcli_credential_data.password, "test_password")
        self.assertEqual(vcli_credential_data.client_id, "test_client_id")
        self.assertEqual(vcli_credential_data.auth_endpont, "test_auth_endpont")
        self.assertEqual(vcli_config_data.service_endpoint, "test_service_endpoint")
        self.assertEqual(vcli_config_data.max_attempts, "3")

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_no_input(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['username', '', '', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_no_password(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = ""

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['test_username', '', '', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_no_client_id(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['test_username', 'test_okta_client_id', '', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_no_auth_endpoint(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['test_username', 'test_okta_client_id', 'test_auth_endpoint', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_no_service_endpoint(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=['', '', '', '', ''])
    @patch('argparse.Namespace')
    def test_read_user_input_all_fail_profile_not_exit(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = "Nope"
        mock_getpass.return_value = "test_password"

        with self.assertRaises(ValidationFailedError):
            _, _ = ConfigCommand.read_user_input_all(args=mock_args)

    def test_set_config_data_success(self):
        vcli_config_data = VcliConfigFile(
            service_endpoint="test_service_endpoint",
            max_attempts=3
        )
        vcli_credential_data = VcliCredentialFile(
            username="test_username",
            password="test_password",
            client_id="test_client_id",
            auth_endpont="test_auth_endpont"
        )

        ConfigCommand.set_config_data(
            vcli_config_data=vcli_config_data,
            vcli_credential_data=vcli_credential_data,
            profile=self.default_profile
        )

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=input_values)
    @patch('argparse.Namespace')
    def test_operation_cmd_success(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_getpass.return_value = "test_password"

        ConfigCommand().operation_cmd(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('Config update success\n', stdout)
        self.assertEqual('', stderr)

    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=input_values)
    @patch('argparse.Namespace')
    def test_operation_set_detail_success(self, mock_args, mock_inputs, mock_getpass):
        mock_args.profile = self.default_profile
        mock_args.username = None
        mock_args.password = None
        mock_args.client_id = None
        mock_args.auth_endpont = None
        mock_args.service_endpoint = None
        mock_args.max_attempts = None

        ConfigCommand().operation_set_detail(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('Config update success\n', stdout)
        self.assertEqual('', stderr)
