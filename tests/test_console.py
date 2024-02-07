#!/usr/bin/env python

"""
This contains the tests for the console application
"""

import unittest
import console


class ConsoleTestCase(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(console.main())
