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


class InlineObject18(object):
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
        'az': 'str',
        'enable_ssh': 'bool',
        'external_access_cidr_block': 'list[str]',
        'force': 'bool',
        'instance_type': 'str',
        'vertica_version': 'str'
    }

    attribute_map = {
        'az': 'az',
        'enable_ssh': 'enable_ssh',
        'external_access_cidr_block': 'external_access_cidr_block',
        'force': 'force',
        'instance_type': 'instance_type',
        'vertica_version': 'vertica_version'
    }

    def __init__(self, az=None, enable_ssh=None, external_access_cidr_block=None, force=None, instance_type=None, vertica_version=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject18 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._az = None
        self._enable_ssh = None
        self._external_access_cidr_block = None
        self._force = None
        self._instance_type = None
        self._vertica_version = None
        self.discriminator = None

        if az is not None:
            self.az = az
        if enable_ssh is not None:
            self.enable_ssh = enable_ssh
        if external_access_cidr_block is not None:
            self.external_access_cidr_block = external_access_cidr_block
        if force is not None:
            self.force = force
        if instance_type is not None:
            self.instance_type = instance_type
        if vertica_version is not None:
            self.vertica_version = vertica_version

    @property
    def az(self):
        """Gets the az of this InlineObject18.  # noqa: E501


        :return: The az of this InlineObject18.  # noqa: E501
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this InlineObject18.


        :param az: The az of this InlineObject18.  # noqa: E501
        :type az: str
        """

        self._az = az

    @property
    def enable_ssh(self):
        """Gets the enable_ssh of this InlineObject18.  # noqa: E501


        :return: The enable_ssh of this InlineObject18.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssh

    @enable_ssh.setter
    def enable_ssh(self, enable_ssh):
        """Sets the enable_ssh of this InlineObject18.


        :param enable_ssh: The enable_ssh of this InlineObject18.  # noqa: E501
        :type enable_ssh: bool
        """

        self._enable_ssh = enable_ssh

    @property
    def external_access_cidr_block(self):
        """Gets the external_access_cidr_block of this InlineObject18.  # noqa: E501


        :return: The external_access_cidr_block of this InlineObject18.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_access_cidr_block

    @external_access_cidr_block.setter
    def external_access_cidr_block(self, external_access_cidr_block):
        """Sets the external_access_cidr_block of this InlineObject18.


        :param external_access_cidr_block: The external_access_cidr_block of this InlineObject18.  # noqa: E501
        :type external_access_cidr_block: list[str]
        """

        self._external_access_cidr_block = external_access_cidr_block

    @property
    def force(self):
        """Gets the force of this InlineObject18.  # noqa: E501


        :return: The force of this InlineObject18.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this InlineObject18.


        :param force: The force of this InlineObject18.  # noqa: E501
        :type force: bool
        """

        self._force = force

    @property
    def instance_type(self):
        """Gets the instance_type of this InlineObject18.  # noqa: E501


        :return: The instance_type of this InlineObject18.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InlineObject18.


        :param instance_type: The instance_type of this InlineObject18.  # noqa: E501
        :type instance_type: str
        """

        self._instance_type = instance_type

    @property
    def vertica_version(self):
        """Gets the vertica_version of this InlineObject18.  # noqa: E501


        :return: The vertica_version of this InlineObject18.  # noqa: E501
        :rtype: str
        """
        return self._vertica_version

    @vertica_version.setter
    def vertica_version(self, vertica_version):
        """Sets the vertica_version of this InlineObject18.


        :param vertica_version: The vertica_version of this InlineObject18.  # noqa: E501
        :type vertica_version: str
        """

        self._vertica_version = vertica_version

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
        if not isinstance(other, InlineObject18):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject18):
            return True

        return self.to_dict() != other.to_dict()