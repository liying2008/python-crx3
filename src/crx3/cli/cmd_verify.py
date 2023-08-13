# -*- coding: utf-8 -*-
from crx3 import verifier
from crx3.verifier import VerifierResult


def verify(crx_file):
    result, header_info = verifier.verify(crx_file)
    print(result.value)
    # print(header_info)
    if result == VerifierResult.OK_FULL:
        return 0
    elif result == VerifierResult.ERROR_FILE_NOT_READABLE:
        return 1
    elif result == VerifierResult.ERROR_HEADER_INVALID:
        return 2
    elif result == VerifierResult.ERROR_SIGNATURE_VERIFICATION_FAILED:
        return 6
    elif result == VerifierResult.ERROR_REQUIRED_PROOF_MISSING:
        return 7
    # unreachable
    return -1
