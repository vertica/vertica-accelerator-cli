import unittest
import json

from vcli.models.response_model import ResponseModel


class ResponseModelTests(unittest.TestCase):
    """Response model unit tests"""

    def setUp(self):
        self.test_obj = ResponseModel(
            return_code="000",
            data={"test_key": "test_val"},
            job_id="test_jobid",
            error_message="test_error"
        )
        self.output = {
            "return_code": "000",
            "data": {
                "test_key": "test_val"
            },
            "job_id": "test_jobid",
            "error_message": "test_error"
        }

    def tearDown(self):
        pass

    # -------------- tests -------------- #

    def test_repr_success(self):
        self.assertEqual(self.test_obj.__repr__(),
                         json.dumps(self.output, indent=4))

    def test_str_success(self):
        self.assertEqual(self.test_obj.__str__(),
                         json.dumps(self.output, indent=4))
