# -*- coding: utf-8 -*-

import os.path
import unittest

from crx3 import creator
from tests.mytest import MyTest
from tests.common import OUTPUT_PATH, EXAMPLE_EXTENSION_NAME, EXAMPLE_EXTENSION_DIR


class CreatorTestCase(MyTest):

    def test_01_create_private_key_file(self):
        output_key_file = os.path.join(OUTPUT_PATH, EXAMPLE_EXTENSION_NAME + '.pem')
        if os.path.exists(output_key_file):
            os.remove(output_key_file)
        creator.create_private_key_file(output_key_file)
        self.assertTrue(os.path.exists(output_key_file))

    def test_02_create_crx_file_from_zip(self):
        extension_zip = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.zip')
        private_key_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.pem')
        output_file = os.path.join(OUTPUT_PATH, EXAMPLE_EXTENSION_NAME + '.crx')
        if os.path.exists(output_file):
            os.remove(output_file)
        creator.create_crx_file(extension_zip, private_key_file, output_file)
        self.assertTrue(os.path.exists(output_file))

    def test_03_create_crx_file_from_dir(self):
        extension_dir = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME)
        private_key_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.pem')
        output_file = os.path.join(OUTPUT_PATH, EXAMPLE_EXTENSION_NAME + '.crx')
        if os.path.exists(output_file):
            os.remove(output_file)
        creator.create_crx_file(extension_dir, private_key_file, output_file)
        self.assertTrue(os.path.exists(output_file))


if __name__ == '__main__':
    unittest.main()
