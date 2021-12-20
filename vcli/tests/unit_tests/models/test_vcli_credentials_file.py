#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest

from unittest.mock import patch
from vcli.models.vcli_credential_file import VcliCredentialFile
from vcli.exceptions.vcli_custom_exception import (
    ValidationFailedError,
    ProfileNotExistError,
    ProfilePermissionError
)
from vcli.util.error_message import ErrorMessage


class VcliCredentialFileTests(unittest.TestCase):
    """Vcli Credential File unit tests"""

    def setUp(self):
        self.username = "test_username"
        self.password = "test_password"
        self.client_id = "test_client_id"
        self.auth_endpont = "test_auth_endpoint"
        self.access_token_file = "test_token_file"
        self.default_profile = "default"
        self.test_obj = VcliCredentialFile(self.username, self.password, self.client_id,
                                           self.auth_endpont, self.access_token_file)

    def tearDown(self):
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys):
        self.capsys = capsys

    # -------------- tests -------------- #

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_username_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        with pytest.raises(ValidationFailedError) as err:
            test_obj = VcliCredentialFile(username=None, password=self.password,
                                          client_id=self.client_id, auth_endpont=self.auth_endpont)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.USERNAME_CAN_NOT_BE_NONE)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_password_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        with pytest.raises(ValidationFailedError) as err:
            test_obj = VcliCredentialFile(username=self.username, password=None,
                                          client_id=self.client_id, auth_endpont=self.auth_endpont)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.PASSWORD_CAN_NOT_BE_NONE)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_client_id_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        with pytest.raises(ValidationFailedError) as err:
            test_obj = VcliCredentialFile(username=self.username, password=self.password,
                                          client_id=None, auth_endpont=self.auth_endpont)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.OKTA_CLIENT_CAN_NOT_BE_NONE)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_post_init_auth_endpoint_none(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True

        with pytest.raises(ValidationFailedError) as err:
            test_obj = VcliCredentialFile(username=self.username, password=self.password,
                                          client_id=self.client_id, auth_endpont=None)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.OKTA_AUTH_ENDPOINT_CAN_NOT_BE_NONE)

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
            err.value.msg, ErrorMessage.ERROR_CREDENTIAL_CONFIG_NOT_EXIST)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_check_profile_file_profile_file_not_readable(self, mock_args, mock_os_path_exists, mock_os_access):
        mock_args.profile = self.default_profile
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = False

        with pytest.raises(ProfilePermissionError) as err:
            self.test_obj.check_profile_file(profile=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_CREDENTIAL_CONFIG_NOT_READABLE)

    @patch('os.path.exists')
    @patch('argparse.Namespace')
    def test_get_access_token_profile_not_exist(self, mock_args, mock_os_path_exists):
        mock_args.profile = "profile_not_exist"
        mock_os_path_exists.return_value = False

        with pytest.raises(ProfileNotExistError) as err:
            self.test_obj.get_access_token(profile=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, f"credential file section profile: {mock_args} does not exist")

    @patch('os.remove')
    @patch('os.path.exists')
    def test_delete_access_token_file_exists(self, mock_os_path_exists, mock_remove):
        mock_os_path_exists.return_value = True

        self.test_obj.delete_access_token(profile=self.default_profile)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
