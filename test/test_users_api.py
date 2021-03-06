# coding: utf-8

"""
    MaaS

    MaaS (Matomat as a Service) API definition  # noqa: E501

    OpenAPI spec version: 0.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_get(self):
        """Test case for users_get

        List all users  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Add a new user  # noqa: E501
        """
        pass

    def test_users_user_id_credits_add_patch(self):
        """Test case for users_user_id_credits_add_patch

        Add users credits  # noqa: E501
        """
        pass

    def test_users_user_id_credits_transfer_patch(self):
        """Test case for users_user_id_credits_transfer_patch

        Transfer credits  # noqa: E501
        """
        pass

    def test_users_user_id_credits_withdraw_patch(self):
        """Test case for users_user_id_credits_withdraw_patch

        Widthdraw users credits  # noqa: E501
        """
        pass

    def test_users_user_id_delete(self):
        """Test case for users_user_id_delete

        Delete user  # noqa: E501
        """
        pass

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Get user by user ID  # noqa: E501
        """
        pass

    def test_users_user_id_password_patch(self):
        """Test case for users_user_id_password_patch

        Change password for currently logged in user.  # noqa: E501
        """
        pass

    def test_users_user_id_resetpassword_patch(self):
        """Test case for users_user_id_resetpassword_patch

        Set password for user ID  # noqa: E501
        """
        pass

    def test_users_user_id_stats_get(self):
        """Test case for users_user_id_stats_get

        Get matomat stats for user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
