# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionSignInputAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 516

    def __init__(
        self,
        *,
        signature: Optional[bytes] = None,
        pseudo_out: Optional[bytes] = None,
    ) -> None:
        self.signature = signature
        self.pseudo_out = pseudo_out

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('signature', p.BytesType, None),
            2: ('pseudo_out', p.BytesType, None),
        }
