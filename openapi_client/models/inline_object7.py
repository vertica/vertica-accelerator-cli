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


class InlineObject7(object):
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
        'action': 'str',
        'enable': 'bool',
        'module': 'str'
    }

    attribute_map = {
        'action': 'action',
        'enable': 'enable',
        'module': 'module'
    }

    def __init__(self, action=None, enable=None, module=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject7 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._enable = None
        self._module = None
        self.discriminator = None

        self.action = action
        self.enable = enable
        if module is not None:
            self.module = module

    @property
    def action(self):
        """Gets the action of this InlineObject7.  # noqa: E501


        :return: The action of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InlineObject7.


        :param action: The action of this InlineObject7.  # noqa: E501
        :type action: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["start", "stop"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def enable(self):
        """Gets the enable of this InlineObject7.  # noqa: E501


        :return: The enable of this InlineObject7.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineObject7.


        :param enable: The enable of this InlineObject7.  # noqa: E501
        :type enable: bool
        """
        if self.local_vars_configuration.client_side_validation and enable is None:  # noqa: E501
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def module(self):
        """Gets the module of this InlineObject7.  # noqa: E501


        :return: The module of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this InlineObject7.


        :param module: The module of this InlineObject7.  # noqa: E501
        :type module: str
        """
        allowed_values = ["vertica_cluster", "vertica_subcluster_1", "vertica_subcluster_2", "vertica_subcluster_3"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and module not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `module` ({0}), must be one of {1}"  # noqa: E501
                .format(module, allowed_values)
            )

        self._module = module

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
        if not isinstance(other, InlineObject7):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject7):
            return True

        return self.to_dict() != other.to_dict()
