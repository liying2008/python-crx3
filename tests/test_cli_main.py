import os.path
import unittest

from tests.common import TESTCASES_DIR
from tests.mytest import MyTest


class CliMainTestCase(MyTest):
    def test_01_main(self):
        source_path = os.path.abspath(os.path.join('example', 'example-extension'))
        output_path = os.path.abspath(os.path.join('output', 'example-extension.crx'))
        cmd = 'crx3 create {} -o {}'.format(source_path, output_path)
        ret = os.system(cmd)
        self.assertEqual(0, ret)
        private_key_path = os.path.abspath(os.path.join('output', 'example-extension.pem'))
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(os.path.exists(private_key_path))

        crx_path_ok = os.path.abspath(os.path.join('example', 'example-extension.crx'))
        cmd = 'crx3 verify {}'.format(crx_path_ok)
        ret = os.system(cmd)
        self.assertEqual(0, ret)

        crx_path_verification_error = os.path.abspath(os.path.join(TESTCASES_DIR, 'testdata', 'verification-error.crx'))
        cmd = 'crx3 verify {}'.format(crx_path_verification_error)
        ret = os.system(cmd)
        self.assertEqual(6, ret)

        crx_path_version_number_error = os.path.abspath(
            os.path.join(TESTCASES_DIR, 'testdata', 'version-number-error.crx'))
        cmd = 'crx3 verify {}'.format(crx_path_version_number_error)
        ret = os.system(cmd)
        self.assertEqual(2, ret)


if __name__ == '__main__':
    unittest.main()
