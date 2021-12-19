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


class InlineObject2(object):
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
        'enable_ssh': 'bool',
        'external_access_cidr_block': 'list[str]'
    }

    attribute_map = {
        'enable_ssh': 'enable_ssh',
        'external_access_cidr_block': 'external_access_cidr_block'
    }

    def __init__(self, enable_ssh=None, external_access_cidr_block=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._enable_ssh = None
        self._external_access_cidr_block = None
        self.discriminator = None

        if enable_ssh is not None:
            self.enable_ssh = enable_ssh
        self.external_access_cidr_block = external_access_cidr_block

    @property
    def enable_ssh(self):
        """Gets the enable_ssh of this InlineObject2.  # noqa: E501


        :return: The enable_ssh of this InlineObject2.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssh

    @enable_ssh.setter
    def enable_ssh(self, enable_ssh):
        """Sets the enable_ssh of this InlineObject2.


        :param enable_ssh: The enable_ssh of this InlineObject2.  # noqa: E501
        :type enable_ssh: bool
        """

        self._enable_ssh = enable_ssh

    @property
    def external_access_cidr_block(self):
        """Gets the external_access_cidr_block of this InlineObject2.  # noqa: E501


        :return: The external_access_cidr_block of this InlineObject2.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_access_cidr_block

    @external_access_cidr_block.setter
    def external_access_cidr_block(self, external_access_cidr_block):
        """Sets the external_access_cidr_block of this InlineObject2.


        :param external_access_cidr_block: The external_access_cidr_block of this InlineObject2.  # noqa: E501
        :type external_access_cidr_block: list[str]
        """
        if self.local_vars_configuration.client_side_validation and external_access_cidr_block is None:  # noqa: E501
            raise ValueError("Invalid value for `external_access_cidr_block`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_access_cidr_block is not None and len(external_access_cidr_block) < 1):
            raise ValueError("Invalid value for `external_access_cidr_block`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._external_access_cidr_block = external_access_cidr_block

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
        if not isinstance(other, InlineObject2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject2):
            return True

        return self.to_dict() != other.to_dict()
