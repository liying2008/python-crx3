# CRX3

[![PyPI version](https://badge.fury.io/py/crx3.svg)](https://badge.fury.io/py/crx3)
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

creator.create_private_key_file('{output_private_key_file.pem}')
```

- Packaging a zip file or extension code directory to a crx file.

```python
from crx3 import creator

creator.create_crx_file('{extension_zip_or_dir}', '{private_key.pem}', '{output_crx_file.crx}')
```

- Verify if a file is a valid crx version 3 file.

```python
from crx3 import verifier

verifier_result, header_info = verifier.verify('{crx_file.crx}')
print(verifier_result, header_info)
assert verifier_result == verifier.VerifierResult.OK_FULL
assert header_info.crx_id == '{alphabet crx id string}'
assert header_info.public_key == '{public key string}'
```
