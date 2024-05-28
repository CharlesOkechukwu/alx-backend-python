#!/usr/bin/env python3
"""module for class to test of GithubOrgClient"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class that contains methods that test GithubOrgClient"""
    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org: str, getJson: MagicMock) -> None:
        """fuction to trest GithubOrgClient org property"""
        client = GithubOrgClient(org)
        self.assertEqual(client.org, getJson.return_value)
        getJson.assert_called_once_with(client.ORG_URL.format(org=org))
