# -*- coding: utf-8 -*-
import os.path
import sys
import unittest

if __name__ == '__main__':
    testcase_dir = os.path.abspath(os.path.dirname(__file__))
    # print(testcase_dir)
    root_path = os.path.split(testcase_dir)[0]
    # print(root_path)
    sys.path.append(root_path)

    os.chdir(testcase_dir)

    suite = unittest.defaultTestLoader.discover(testcase_dir, pattern='test_*.py', )
    unittest.TextTestRunner(verbosity=2).run(suite)
