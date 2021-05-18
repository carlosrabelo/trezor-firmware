# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class ECDHSessionKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 62

    def __init__(
        self,
        *,
        session_key: bytes,
        public_key: Optional[bytes] = None,
    ) -> None:
        self.session_key = session_key
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('session_key', p.BytesType, p.FLAG_REQUIRED),
            2: ('public_key', p.BytesType, None),
        }
