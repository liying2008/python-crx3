from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CrxFileHeader(_message.Message):
    __slots__ = ["sha256_with_rsa", "sha256_with_ecdsa", "verified_contents", "signed_header_data"]
    SHA256_WITH_RSA_FIELD_NUMBER: _ClassVar[int]
    SHA256_WITH_ECDSA_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SIGNED_HEADER_DATA_FIELD_NUMBER: _ClassVar[int]
    sha256_with_rsa: _containers.RepeatedCompositeFieldContainer[AsymmetricKeyProof]
    sha256_with_ecdsa: _containers.RepeatedCompositeFieldContainer[AsymmetricKeyProof]
    verified_contents: bytes
    signed_header_data: bytes
    def __init__(self, sha256_with_rsa: _Optional[_Iterable[_Union[AsymmetricKeyProof, _Mapping]]] = ..., sha256_with_ecdsa: _Optional[_Iterable[_Union[AsymmetricKeyProof, _Mapping]]] = ..., verified_contents: _Optional[bytes] = ..., signed_header_data: _Optional[bytes] = ...) -> None: ...

class AsymmetricKeyProof(_message.Message):
    __slots__ = ["public_key", "signature"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    signature: bytes
    def __init__(self, public_key: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...

class SignedData(_message.Message):
    __slots__ = ["crx_id"]
    CRX_ID_FIELD_NUMBER: _ClassVar[int]
    crx_id: bytes
    def __init__(self, crx_id: _Optional[bytes] = ...) -> None: ...
