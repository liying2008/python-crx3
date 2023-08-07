# CRX3

[![PyPI](https://img.shields.io/pypi/v/crx3)](https://pypi.org/project/crx3/)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/crx3.svg)](https://pypi.python.org/pypi/crx3/)
[![Downloads](https://static.pepy.tech/badge/crx3)](https://pepy.tech/project/crx3)
[![GitHub Actions (Tests)](https://github.com/liying2008/python-crx3/actions/workflows/tests.yml/badge.svg)](https://github.com/liying2008/python-crx3/actions/workflows/tests.yml)

**crx3** is a python library for packaging and parsing crx files.

## Installation

`crx3` is available on PyPI:

```console
$ python -m pip install crx3
```

crx3 officially supports Python 3.7+.

## Functions

- Create a private key for signing the crx file.

```python
from crx3 import creator

creator.create_private_key_file('output/example-extension.pem')
```

- Packaging a zip file or extension code directory to a crx file.

```python
from crx3 import creator

creator.create_crx_file('example/example-extension', 'example/example-extension.pem', 'output/example-extension.crx')
```

- Verify if a file is a valid crx version 3 file.

```python
from crx3 import verifier

verifier_result, header_info = verifier.verify('example/example-extension.crx')

assert verifier_result == verifier.VerifierResult.OK_FULL
assert header_info.crx_id == 'jjomgndeajdmncfenopimafofpnflcfo'
assert header_info.public_key == 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMI...FkbU7H8sDQIDAQAB'
```
