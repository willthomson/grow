"""Tests for Base Updater."""

import unittest
from grow.pods import pods
from grow.pods import storage
from grow.sdk import updater
from grow.testing import testing


class UpdaterTestCase(unittest.TestCase):
    """Test the Base Updater."""

    def setUp(self):
        self.dir_path = testing.create_test_pod_dir()
        self.pod = pods.Pod(self.dir_path, storage=storage.FileStorage)
        self.updater = updater.Updater([], self.pod)

    def test_failure(self):
        """Failure message formatting."""
        message = self.updater.failure('Bring Me Another Shrubbery!')
        expected = '\x1b[38;5;1m\x1b[1m[\xe2\x9c\x98] Bring Me Another Shrubbery!\x1b[0m'
        self.assertEqual(expected, message)

    def test_failure_with_extras(self):
        """Failure message formatting with extra messages."""
        message = self.updater.failure('Bring Me Another Shrubbery!', extras=['1', 'A'])
        expected = ('\x1b[38;5;1m\x1b[1m[\xe2\x9c\x98] '
                    'Bring Me Another Shrubbery!'
                    '\n   1\n   A\x1b[0m')
        self.assertEqual(expected, message)

    def test_success(self):
        """Success message formatting."""
        message = self.updater.success('Holy Hand Grenade')
        expected = '\x1b[38;5;2m[\xe2\x9c\x93] Holy Hand Grenade\x1b[0m'
        self.assertEqual(expected, message)

    def test_success_with_extras(self):
        """Success message formatting with extra messages."""
        message = self.updater.success('Holy Hand Grenade', extras=['1', 'A'])
        expected = ('\x1b[38;5;2m[\xe2\x9c\x93] '
                    'Holy Hand Grenade'
                    '\n   1\n   A\x1b[0m')
        self.assertEqual(expected, message)
