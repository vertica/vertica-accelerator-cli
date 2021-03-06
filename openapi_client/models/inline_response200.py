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


class InlineResponse200(object):
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
        'data': 'object',
        'href': 'str',
        'mime_type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'href': 'href',
        'mime_type': 'mime-type'
    }

    def __init__(self, data=None, href=None, mime_type=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._href = None
        self._mime_type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if href is not None:
            self.href = href
        if mime_type is not None:
            self.mime_type = mime_type

    @property
    def data(self):
        """Gets the data of this InlineResponse200.  # noqa: E501


        :return: The data of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse200.


        :param data: The data of this InlineResponse200.  # noqa: E501
        :type data: object
        """

        self._data = data

    @property
    def href(self):
        """Gets the href of this InlineResponse200.  # noqa: E501


        :return: The href of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InlineResponse200.


        :param href: The href of this InlineResponse200.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def mime_type(self):
        """Gets the mime_type of this InlineResponse200.  # noqa: E501


        :return: The mime_type of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this InlineResponse200.


        :param mime_type: The mime_type of this InlineResponse200.  # noqa: E501
        :type mime_type: str
        """

        self._mime_type = mime_type

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()
