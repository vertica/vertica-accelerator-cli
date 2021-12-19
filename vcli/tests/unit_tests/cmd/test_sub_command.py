import unittest

from unittest.mock import MagicMock, patch
from vcli.cmd.sub_command import SubCommand, SubCommandImplementation


class SubCommandTests(unittest.TestCase):
    """Sub Command unit tests"""

    @patch("vcli.cmd.sub_command.SubCommandImplementation.__abstractmethods__", set())
    def test_operation_cmd_abstract_method(self):
        mock_args = MagicMock()
        service = SubCommandImplementation()
        assert service.operation_cmd(mock_args) is None

    @patch("vcli.cmd.sub_command.SubCommandImplementation.__abstractmethods__", set())
    def test_operation_define_abstract_method(self):
        mock_subparser = MagicMock()
        service = SubCommandImplementation()
        assert service.operation_define(mock_subparser) is None

    @patch("vcli.cmd.sub_command.SubCommandImplementation", autospec=True)
    def test_constructor_success(self, mock_subcommand_implementation):
        sub_command = SubCommand(mock_subcommand_implementation)
        self.assertEqual(sub_command.implementation,
                         mock_subcommand_implementation)

    @patch("vcli.cmd.sub_command.SubCommandImplementation", autospec=True)
    def test_arg_operation(self, mock_implementation):
        mock_args = MagicMock()
        sub_command = SubCommand(mock_implementation)
        assert sub_command.arg_operation(mock_args) is None

    @patch("vcli.cmd.sub_command.SubCommandImplementation", autospec=True)
    def test_arg_define(self, mock_implementation):
        mock_args = MagicMock()
        sub_command = SubCommand(mock_implementation)
        assert sub_command.arg_define(mock_args) is None
