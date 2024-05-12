#!/usr/bin/env python3
"""
Test github org client
"""

import unittest
from unittest.mock import patch, Mock
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

        # Assert that get_json was called with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mocked_get_json.assert_called_once_with(expected_url)

        # Assert that org_info is an empty dictionary
        self.assertEqual(org_info, {})


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    def test_public_repos_url(self):
        """Test public_repos_url"""
        mock_org = Mock()
        mock_org.return_value = {'repos_url': '(link unavailable)'}
        with patch.object(GithubOrgClient, 'org', property(mock_org)):
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, '(link unavailable)')
