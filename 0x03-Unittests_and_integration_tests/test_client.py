#!/usr/bin/env python3
"""
Test github org client
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('your_module.GithubOrgClient.get_json', return_value={})
    def test_org(self, org_name, mocked_get_json):
        """Test org"""
        # Instantiate GithubOrgClient with the organization name
        github_org_client = GithubOrgClient(org_name)
        
        # Call the org method
        org_info = github_org_client.org()
        
        # Assert that get_json was called once with the expected argument
        mocked_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
        # Assert that org_info is an empty dictionary (for now, since we mocked the response)
        self.assertEqual(org_info, {})
