# -*- coding: utf-8 -*-

import os
import unittest

from crx3 import key_util, utils
from tests.common import EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME
from tests.mytest import MyTest


class KeyUtilTestCase(MyTest):

    def test_01_key_util_functions(self):
        private_key_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.pem')
        private_key_pem_data = utils.get_file_data(private_key_file)
        private_key = key_util.load_private_key_from_pem(private_key_pem_data)
        public_key_actual = key_util.extract_public_key_from_private_key(private_key)
        public_key_data_actual = key_util.get_public_key_data(public_key_actual)

        public_key_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '-public-key.pem')
        public_key_pem_data = utils.get_file_data(public_key_file)
        public_key_expected = key_util.load_public_key_from_pem(public_key_pem_data)
        public_key_data_expected = key_util.get_public_key_data(public_key_expected)
        self.assertEqual(public_key_data_expected, public_key_data_actual)


if __name__ == '__main__':
    unittest.main()
