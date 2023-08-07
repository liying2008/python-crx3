# -*- coding: utf-8 -*-

import os
import unittest

from crx3 import verifier
from tests.common import EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME, TESTCASES_DIR, read_public_key_str, \
    EXAMPLE_EXTENSION_CRX_ID
from tests.mytest import MyTest


class VerifierTestCase(MyTest):

    def test_01_verify_ok_full(self):
        crx_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.crx')
        public_key_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '-public-key.pem')
        verifier_result, header_info = verifier.verify(crx_file)
        # print(verifier_result, header_info)
        self.assertEqual(verifier_result, verifier.VerifierResult.OK_FULL)
        public_key = read_public_key_str(public_key_file)
        self.assertEqual(header_info, verifier.CrxHeaderInfo(EXAMPLE_EXTENSION_CRX_ID, public_key))

    def test_02_verify_error_file_not_readable(self):
        verifier_result, header_info = verifier.verify('non-existent-file.crx')
        # print(verifier_result, header_info)
        self.assertEqual(verifier_result, verifier.VerifierResult.ERROR_FILE_NOT_READABLE)
        self.assertEqual(header_info, None)

    def test_03_verify_error_header_invalid(self):
        zip_file = os.path.join(EXAMPLE_EXTENSION_DIR, EXAMPLE_EXTENSION_NAME + '.zip')
        verifier_result, header_info = verifier.verify(zip_file)
        # print(verifier_result, header_info)
        self.assertEqual(verifier_result, verifier.VerifierResult.ERROR_HEADER_INVALID)
        self.assertEqual(header_info, None)

        version_number_error_file = os.path.join(TESTCASES_DIR, "testdata", "version-number-error.crx")
        verifier_result, header_info = verifier.verify(version_number_error_file)
        # print(verifier_result, header_info)
        self.assertEqual(verifier_result, verifier.VerifierResult.ERROR_HEADER_INVALID)
        self.assertEqual(header_info, None)

    def test_04_verify_error_signature_verification_failed(self):
        header_error_file = os.path.join(TESTCASES_DIR, "testdata", "verification-error.crx")
        verifier_result, header_info = verifier.verify(header_error_file)
        # print(verifier_result, header_info)
        self.assertEqual(verifier_result, verifier.VerifierResult.ERROR_SIGNATURE_VERIFICATION_FAILED)
        self.assertEqual(header_info, None)


if __name__ == '__main__':
    unittest.main()
