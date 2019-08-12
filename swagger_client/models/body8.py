# coding: utf-8

"""
    MaaS

    MaaS (Matomat as a Service) API definition  # noqa: E501

    OpenAPI spec version: 0.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body8(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'passwordnew': 'str',
        'passwordrepeat': 'str'
    }

    attribute_map = {
        'passwordnew': 'passwordnew',
        'passwordrepeat': 'passwordrepeat'
    }

    def __init__(self, passwordnew=None, passwordrepeat=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501
        self._passwordnew = None
        self._passwordrepeat = None
        self.discriminator = None
        self.passwordnew = passwordnew
        self.passwordrepeat = passwordrepeat

    @property
    def passwordnew(self):
        """Gets the passwordnew of this Body8.  # noqa: E501


        :return: The passwordnew of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._passwordnew

    @passwordnew.setter
    def passwordnew(self, passwordnew):
        """Sets the passwordnew of this Body8.


        :param passwordnew: The passwordnew of this Body8.  # noqa: E501
        :type: str
        """
        if passwordnew is None:
            raise ValueError("Invalid value for `passwordnew`, must not be `None`")  # noqa: E501

        self._passwordnew = passwordnew

    @property
    def passwordrepeat(self):
        """Gets the passwordrepeat of this Body8.  # noqa: E501


        :return: The passwordrepeat of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._passwordrepeat

    @passwordrepeat.setter
    def passwordrepeat(self, passwordrepeat):
        """Sets the passwordrepeat of this Body8.


        :param passwordrepeat: The passwordrepeat of this Body8.  # noqa: E501
        :type: str
        """
        if passwordrepeat is None:
            raise ValueError("Invalid value for `passwordrepeat`, must not be `None`")  # noqa: E501

        self._passwordrepeat = passwordrepeat

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body8, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body8):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
