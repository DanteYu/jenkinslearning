#! /usr/bin/env python
"""unit tests for the project1.authentcation module"""

from unittest import TestCase
from mock import patch
import sys
sys.path.append("/Users/diyu/git_project/jenkinsleanring")
import project1.authentication as auth

class StandAloneTests(TestCase):
	"""Test the stand-alone module functions."""

	@patch('__builtin__.open')
	def test_login(self, mock_open):
		"""postive test case"""
		mock_open.return_value.read.return_value = "username|password\n"
		self.assertTrue(auth.login('username', 'password'))

	@patch('__builtin__.open')
	def test_login_bad_creds(self, mock_open):
		"""negative test case"""
		mock_open.return_value.read.return_value = "username|password"
		self.assertFalse(auth.login('username', 'badpassword'))

	@patch('__builtin__.open')
	def test_login_error(self, mock_open):
		"""IO exception test case"""
		mock_open.side_effect = IOError()
		self.assertFalse(auth.login('username', 'password'))
