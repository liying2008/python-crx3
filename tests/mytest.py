# -*- coding: utf-8 -*-
import os
import unittest

from tests.common import TESTCASES_DIR


class MyTest(unittest.TestCase):
    def setUp(self):
        testcase_verbose = os.getenv('CRX3_TESTCASE_VERBOSE')
        if testcase_verbose == 'true' or testcase_verbose == '1':
            self.verbose = True
        else:
            self.verbose = False
        os.chdir('..')

    def tearDown(self):
        os.chdir(TESTCASES_DIR)
