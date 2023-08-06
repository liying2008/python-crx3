# -*- coding: utf-8 -*-
import os
import unittest

from tests.common import TESTCASES_DIR, OUTPUT_PATH


class MyTest(unittest.TestCase):
    def setUp(self):
        os.chdir('..')
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)

    def tearDown(self):
        os.chdir(TESTCASES_DIR)
