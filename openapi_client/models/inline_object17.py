# coding: utf-8

"""
    VAAS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class InlineObject17(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instance_count': 'int',
        'module_name': 'str',
        'subcluster_name': 'str'
    }

    attribute_map = {
        'instance_count': 'instance_count',
        'module_name': 'module_name',
        'subcluster_name': 'subcluster_name'
    }

    def __init__(self, instance_count=None, module_name=None, subcluster_name=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject17 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instance_count = None
        self._module_name = None
        self._subcluster_name = None
        self.discriminator = None

        self.instance_count = instance_count
        self.module_name = module_name
        if subcluster_name is not None:
            self.subcluster_name = subcluster_name

    @property
    def instance_count(self):
        """Gets the instance_count of this InlineObject17.  # noqa: E501


        :return: The instance_count of this InlineObject17.  # noqa: E501
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this InlineObject17.


        :param instance_count: The instance_count of this InlineObject17.  # noqa: E501
        :type instance_count: int
        """
        if self.local_vars_configuration.client_side_validation and instance_count is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_count`, must not be `None`")  # noqa: E501
        allowed_values = [3, 4, 6, 12]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instance_count not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instance_count` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_count, allowed_values)
            )

        self._instance_count = instance_count

    @property
    def module_name(self):
        """Gets the module_name of this InlineObject17.  # noqa: E501


        :return: The module_name of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this InlineObject17.


        :param module_name: The module_name of this InlineObject17.  # noqa: E501
        :type module_name: str
        """
        if self.local_vars_configuration.client_side_validation and module_name is None:  # noqa: E501
            raise ValueError("Invalid value for `module_name`, must not be `None`")  # noqa: E501
        allowed_values = ["vertica_cluster", "vertica_subcluster_1", "vertica_subcluster_2", "vertica_subcluster_3"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and module_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `module_name` ({0}), must be one of {1}"  # noqa: E501
                .format(module_name, allowed_values)
            )

        self._module_name = module_name

    @property
    def subcluster_name(self):
        """Gets the subcluster_name of this InlineObject17.  # noqa: E501


        :return: The subcluster_name of this InlineObject17.  # noqa: E501
        :rtype: str
        """
        return self._subcluster_name

    @subcluster_name.setter
    def subcluster_name(self, subcluster_name):
        """Sets the subcluster_name of this InlineObject17.


        :param subcluster_name: The subcluster_name of this InlineObject17.  # noqa: E501
        :type subcluster_name: str
        """

        self._subcluster_name = subcluster_name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject17):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject17):
            return True

        return self.to_dict() != other.to_dict()
