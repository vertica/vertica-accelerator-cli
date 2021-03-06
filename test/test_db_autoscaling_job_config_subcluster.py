# coding: utf-8

"""
    VAAS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.db_autoscaling_job_config_subcluster import DBAutoscalingJobConfigSubcluster  # noqa: E501
from openapi_client.rest import ApiException

class TestDBAutoscalingJobConfigSubcluster(unittest.TestCase):
    """DBAutoscalingJobConfigSubcluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DBAutoscalingJobConfigSubcluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.db_autoscaling_job_config_subcluster.DBAutoscalingJobConfigSubcluster()  # noqa: E501
        if include_optional :
            return DBAutoscalingJobConfigSubcluster(
                vertica_subcluster_1_max_session = 1, 
                vertica_subcluster_2_max_session = 1, 
                vertica_subcluster_3_max_session = 1
            )
        else :
            return DBAutoscalingJobConfigSubcluster(
                vertica_subcluster_1_max_session = 1,
        )

    def testDBAutoscalingJobConfigSubcluster(self):
        """Test DBAutoscalingJobConfigSubcluster"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
