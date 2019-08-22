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


class ServiceStatsUsersCredits(object):
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
        'sum': 'int',
        'avg': 'int',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'sum': 'sum',
        'avg': 'avg',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, sum=None, avg=None, min=None, max=None):  # noqa: E501
        """ServiceStatsUsersCredits - a model defined in Swagger"""  # noqa: E501
        self._sum = None
        self._avg = None
        self._min = None
        self._max = None
        self.discriminator = None
        if sum is not None:
            self.sum = sum
        if avg is not None:
            self.avg = avg
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def sum(self):
        """Gets the sum of this ServiceStatsUsersCredits.  # noqa: E501


        :return: The sum of this ServiceStatsUsersCredits.  # noqa: E501
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this ServiceStatsUsersCredits.


        :param sum: The sum of this ServiceStatsUsersCredits.  # noqa: E501
        :type: int
        """

        self._sum = sum

    @property
    def avg(self):
        """Gets the avg of this ServiceStatsUsersCredits.  # noqa: E501


        :return: The avg of this ServiceStatsUsersCredits.  # noqa: E501
        :rtype: int
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this ServiceStatsUsersCredits.


        :param avg: The avg of this ServiceStatsUsersCredits.  # noqa: E501
        :type: int
        """

        self._avg = avg

    @property
    def min(self):
        """Gets the min of this ServiceStatsUsersCredits.  # noqa: E501


        :return: The min of this ServiceStatsUsersCredits.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ServiceStatsUsersCredits.


        :param min: The min of this ServiceStatsUsersCredits.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this ServiceStatsUsersCredits.  # noqa: E501


        :return: The max of this ServiceStatsUsersCredits.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ServiceStatsUsersCredits.


        :param max: The max of this ServiceStatsUsersCredits.  # noqa: E501
        :type: int
        """

        self._max = max

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
        if issubclass(ServiceStatsUsersCredits, dict):
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
        if not isinstance(other, ServiceStatsUsersCredits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
