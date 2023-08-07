# -*- coding: utf-8 -*-

import os.path
import shutil
import unittest

from crx3 import crxfile
from tests.common import OUTPUT_PATH, EXAMPLE_EXTENSION_NAME, EXAMPLE_EXTENSION_DIR
from tests.mytest import MyTest


class AnalyzerTestCase(MyTest):

    def test_01_convert_to_zip(self):
        crx_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.crx')
        output_zip_name = os.path.join(OUTPUT_PATH, EXAMPLE_EXTENSION_NAME + '.zip')
        if os.path.exists(output_zip_name):
            os.remove(output_zip_name)
        crxfile.convert_to_zip(crx_file, output_zip_name)
        self.assertTrue(os.path.exists(output_zip_name))

    def test_02_unpack(self):
        crx_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.zip')
        output_dir = os.path.join(OUTPUT_PATH, EXAMPLE_EXTENSION_NAME)
        if os.path.exists(output_dir):
            # os.remove(output_dir)
            shutil.rmtree(output_dir)
        crxfile.unpack(crx_file, output_dir)
        self.assertTrue(os.path.exists(output_dir))


if __name__ == '__main__':
    unittest.main()
