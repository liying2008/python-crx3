# -*- coding: utf-8 -*-
import os
import unittest

from tests.common import TESTCASES_DIR


class MyTest(unittest.TestCase):
    def setUp(self):
        os.chdir('..')

    def tearDown(self):
        os.chdir(TESTCASES_DIR)
