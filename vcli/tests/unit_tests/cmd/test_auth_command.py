#
#  (c) Copyright 2021 Micro Focus or one of its affiliates.
#

import unittest
import pytest

from unittest.mock import MagicMock, patch, mock_open
from vcli.cmd.auth_command import AuthCommand
from vcli.constant import VCLI_CONFIG_PATH, VCLI_CONFIG_FILE, VCLI_CREDENTIAL_FILE
from vcli.models.vcli_credential_file import VcliCredentialFile
from vcli.exceptions.vcli_custom_exception import AccessTokenFailedError, ProfileNotExistError
from vcli.util.error_message import ErrorMessage
from vcli.util.utils import verify_access_token
from openapi_client.exceptions import ServiceException


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

MOCK_ACCESS_TOKEN_FILE = '''
xxxxxxxxxxxxxxxx
'''

input_values = [
    "test_username",
    "test_client_id",
    "test_auth_endpont",
    "test_service_endpoint",
    "3"
]


def my_open(filename, *args, **kwargs):
    content = ""
    if filename == f"{VCLI_CONFIG_PATH}/{VCLI_CONFIG_FILE}":
        content = MOCK_CONFIG_FILE_CONTENT
    elif filename == f"{VCLI_CONFIG_PATH}/{VCLI_CREDENTIAL_FILE}":
        content = MOCK_CREDENTIAL_FILE_CONTENT
    elif filename == f"{VCLI_CONFIG_PATH}/default_access_token_file":
        content = MOCK_ACCESS_TOKEN_FILE

    file_object = mock_open(read_data=content).return_value
    file_object.__iter__.return_value = content.splitlines(True)
    return file_object


class AuthCommandTests(unittest.TestCase):
    """Auth command unit tests"""

    def setUp(self):
        self.open_patch = patch('builtins.open', new=my_open)
        self.open_patch.start()
        self.default_profile = "default"
        self.test_profile = "test"
        self.access_token = "test_access_token"

    def tearDown(self):
        self.open_patch.stop()
        pass

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, capsys):
        self.capsys = capsys

    # -------------- tests --------------

    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_verify_access_token_success(self, mock_args, mock_post):
        mock_response = MagicMock()
        mock_post.return_value = mock_response
        mock_response.text = 'mock return'
        mock_response.json.return_value = {"active": True}
        mock_response.status_code = 200

        vcli_credential_data = VcliCredentialFile(
            username="test_username",
            password="test_password",
            client_id="test_client_id",
            auth_endpont="test_auth_endpont"
        )
        verify_access_token(
            credential_file=vcli_credential_data,
            access_token=self.access_token,
            profile=self.default_profile
        )
        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)

    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_verify_access_token_fail(self, mock_args, mock_post):
        mock_response = MagicMock()
        mock_post.return_value = mock_response
        mock_response.text = 'mock return'
        mock_response.json.return_value = {"active": False}
        mock_response.status_code = 400

        vcli_credential_data = VcliCredentialFile(
            username="test_username",
            password="test_password",
            client_id="test_client_id",
            auth_endpont="test_auth_endpont"
        )
        with pytest.raises(AccessTokenFailedError) as err:
            verify_access_token(
                credential_file=vcli_credential_data,
                access_token=self.access_token,
                profile=self.default_profile
            )

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_VERIFY_ACCESS_TOKEN_FAIL)

    @patch('os.path.exists')
    @patch('vcli.cmd.auth_command.IndexV1Api')
    @patch('uuid.uuid4')
    @patch('vcli.cmd.config_command.getpass')
    @patch('builtins.input', side_effect=input_values)
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_operation_cmd_success_no_default_profile_found(self,
                                                            mock_args, mock_post, mock_get, mock_inputs,
                                                            mock_getpass, mock_uuid, mock_veritfy_health, mock_os_path_exists
                                                            ):
        mock_veritfy_health.return_value.services_health_get.return_value = None
        mock_os_path_exists.return_value = False

        mock_uuid.return_value = "abc"
        mock_getpass.return_value = "test_password"
        mock_args.profile = "profile_not_exist"

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="abc"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        with pytest.raises(ProfileNotExistError):
            AuthCommand().operation_cmd(args=mock_args)
        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)

    @patch('vcli.cmd.auth_command.IndexV1Api')
    @patch('uuid.uuid4')
    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_operation_cmd_success_profile_exist(self,
                                                 mock_args, mock_post, mock_get, mock_os_path_exists,
                                                 mock_os_access, mock_uuid, mock_veritfy_health
                                                 ):
        mock_veritfy_health.return_value.services_health_get.return_value = None

        mock_uuid.return_value = "abc"
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="abc"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        AuthCommand().operation_cmd(args=mock_args)
        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('Login success\n', stdout)
        self.assertEqual('', stderr)

    @patch('vcli.cmd.auth_command.IndexV1Api')
    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_operation_cmd_fail_no_session_exists(self,
                                                  mock_args, mock_post, mock_get,
                                                  mock_os_path_exists, mock_os_access, mock_veritfy_health
                                                  ):
        mock_veritfy_health.return_value.services_health_get.return_value = None

        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {"sessionToken": None}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="abc"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        with pytest.raises(AccessTokenFailedError) as err:
            AuthCommand().operation_cmd(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.LOGIN_FAILED_BAD_USERNAME_OR_PASSWORD)

    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_operation_cmd_fail_state_is_empty(self,
                                               mock_args, mock_post, mock_get,
                                               mock_os_path_exists, mock_os_access
                                               ):
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = ''
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        with pytest.raises(AccessTokenFailedError) as err:
            AuthCommand().operation_cmd(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_STATE_PARAM_VERIFY_FAILED)

    @patch('uuid.uuid4')
    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_operation_cmd_fail_state_not_verified(self,
                                                   mock_args, mock_post, mock_get,
                                                   mock_os_path_exists, mock_os_access, mock_uuid
                                                   ):
        mock_uuid.return_value = "abc"
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="some"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        with pytest.raises(AccessTokenFailedError) as err:
            AuthCommand().operation_cmd(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('', stdout)
        self.assertEqual('', stderr)
        self.assertEqual(
            err.value.msg, ErrorMessage.ERROR_STATE_PARAM_VERIFY_FAILED)

    @patch('argparse.Namespace')
    def test_operation_logout_success(self, mock_args):
        mock_args.profile = self.default_profile

        AuthCommand().operation_logout(args=mock_args)
        stdout, stderr = self.capsys.readouterr()
        self.assertEqual('Logout success\n', stdout)
        self.assertEqual('', stderr)

    @patch('vcli.cmd.auth_command.IndexV1Api', side_effect=Exception)
    @patch('uuid.uuid4')
    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_valid_oa_health_exception(self, mock_args, mock_post, mock_get, mock_os_path_exists,
                                       mock_os_access, mock_uuid, mock_veritfy_health
                                       ):

        mock_uuid.return_value = "abc"
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="abc"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        AuthCommand()._valid_oa_health(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual(
            'WARNING: Failed to check OA Service health\n', stdout)
        self.assertEqual('', stderr)

    @patch('vcli.cmd.auth_command.IndexV1Api', side_effect=ServiceException)
    @patch('uuid.uuid4')
    @patch('os.access')
    @patch('os.path.exists')
    @patch('requests.get')
    @patch('requests.post')
    @patch('argparse.Namespace')
    def test_valid_oa_health_service_exception(self, mock_args, mock_post, mock_get, mock_os_path_exists,
                                               mock_os_access, mock_uuid, mock_veritfy_health
                                               ):

        mock_uuid.return_value = "abc"
        mock_os_path_exists.return_value = True
        mock_os_access.return_value = True
        mock_args.profile = self.default_profile

        mock_session_token_response = MagicMock()
        mock_session_token_response.text = 'mock return'
        mock_session_token_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_session_token_response.status_code = 200

        mock_access_token_response = MagicMock()
        mock_access_token_response.text = 'mock return'
        mock_access_token_response.json.return_value = {
            "access_token": "test_access_token"}
        mock_access_token_response.status_code = 200

        mock_verify_access_token_response = MagicMock()
        mock_verify_access_token_response.text = 'mock return'
        mock_verify_access_token_response.json.return_value = {"active": True}
        mock_verify_access_token_response.status_code = 200

        mock_post.side_effect = [mock_session_token_response,
                                 mock_access_token_response, mock_verify_access_token_response]

        mock_get_auth_code_response = MagicMock()
        mock_get_auth_code_response.text = \
            '<input type="hidden" name="state" value="abc"/><input type="hidden" name="code" value="123"/>'
        mock_get_auth_code_response.json.return_value = {
            "sessionToken": "test_sessionToken"}
        mock_get_auth_code_response.status_code = 200
        mock_get.side_effect = [mock_get_auth_code_response]

        AuthCommand()._valid_oa_health(args=mock_args)

        stdout, stderr = self.capsys.readouterr()
        self.assertEqual(
            'WARNING: OA Service health check did not pass\n', stdout)
        self.assertEqual('', stderr)
