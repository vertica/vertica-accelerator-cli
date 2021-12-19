import unittest

from vcli.exceptions.vcli_custom_exception import BaseCustomException


class VcliCustomExceptionTests(unittest.TestCase):
    """Vcli Custom Exception unit tests"""

    def setUp(self):
        self.test_obj = BaseCustomException(
            msg="test_message",
            error_code=000
        )
        self.output = f"{self.test_obj.msg}, with error_code: {self.test_obj.error_code}"

    def tearDown(self):
        pass

    # -------------- tests -------------- #

    def test_str_success(self):
        self.assertEqual(self.test_obj.__str__(), self.output)
