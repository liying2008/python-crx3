# -*- coding: utf-8 -*-

OUTPUT_PATH = 'output'
EXAMPLE_EXTENSION_DIR = 'example'
EXAMPLE_EXTENSION_NAME = 'example-extension'
EXAMPLE_EXTENSION_CRX_ID = 'jjomgndeajdmncfenopimafofpnflcfo'

TESTCASES_DIR = 'tests'


def read_public_key_str(public_key_file):
    lines = []
    with open(public_key_file, 'r', encoding='utf-8') as f:
        file_lines = f.readlines()
        for file_line in file_lines:
            if file_line.startswith('-----'):
                continue
            lines.append(file_line.strip())
    return ''.join(lines)
