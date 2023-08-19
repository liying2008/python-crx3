import os.path
import subprocess
import unittest

from tests.common import TESTCASES_DIR
from tests.mytest import MyTest


class CliMainTestCase(MyTest):
    def test_01_main(self):
        source_path = os.path.abspath(os.path.join('example', 'example-extension'))
        output_path = os.path.abspath(os.path.join('output', 'example-extension.crx'))
        cmd = ('crx3', 'create', source_path, '-o', output_path)
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, timeout=120)
        if self.verbose:
            print('\nargs: {}'.format(' '.join(process.args)))
            print('stdout: {}'.format(process.stdout))
            print('stderr: {}'.format(process.stderr))
        self.assertEqual(0, process.returncode)
        private_key_path = os.path.abspath(os.path.join('output', 'example-extension.pem'))
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(os.path.exists(private_key_path))

        crx_path_ok = os.path.abspath(os.path.join('example', 'example-extension.crx'))
        cmd = ('crx3', 'verify', crx_path_ok, '-v')
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, timeout=120)
        if self.verbose:
            print('\nargs: {}'.format(' '.join(process.args)))
            print('stdout: {}'.format(process.stdout))
            print('stderr: {}'.format(process.stderr))
        self.assertEqual(0, process.returncode)

        crx_path_verification_error = os.path.abspath(os.path.join(TESTCASES_DIR, 'testdata', 'verification-error.crx'))
        cmd = ('crx3', 'verify', crx_path_verification_error)
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, timeout=120)
        if self.verbose:
            print('\nargs: {}'.format(' '.join(process.args)))
            print('stdout: {}'.format(process.stdout))
            print('stderr: {}'.format(process.stderr))
        self.assertEqual(6, process.returncode)

        crx_path_version_number_error = os.path.abspath(
            os.path.join(TESTCASES_DIR, 'testdata', 'version-number-error.crx'))
        cmd = ('crx3', 'verify', crx_path_version_number_error)
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True, timeout=120)
        if self.verbose:
            print('\nargs: {}'.format(' '.join(process.args)))
            print('stdout: {}'.format(process.stdout))
            print('stderr: {}'.format(process.stderr))
        self.assertEqual(2, process.returncode)


if __name__ == '__main__':
    unittest.main()
