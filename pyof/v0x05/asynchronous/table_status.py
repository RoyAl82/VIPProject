"""Defines an Table Status Message."""

# System imports
from enum import IntEnum

# Local source tree imports

from pyof.foundation.base import GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64, Pad
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.controller2switch.multipart_reply import TableDesc

# Third-party imports

__all__ = ('TableStatus', 'TableReason')

# Enums


class TableReason(IntEnum):
    """What changed about the table."""

    #: Vacancy down threshold event
    OFPTR_VACANCY_DOWN = 3
    #: Vacancy up threshold event
    OFPTR_VACANCY_UP = 4


# Classes

class TableStatus(GenericMessage):
    """OpenFlow TableStatus Message OFPT_TABLE_STATUS.
      A table config has changed in the datapath
     """

    #: :class:`~pyof.v0x05.common.action.ActionHeader`: OpenFlow Header
    header = Header(message_type=Type.OFPT_TABLE_STATUS)
    #: One of OFPTR_.*
    reason = UBInt8(enum_ref=TableReason)
    #: Pad to 64 bits
    pad = Pad(7)
    #: New table config
    table = TableDesc()

    def __init__(self, xid=None, reason=None, table=None):
        """Create a message with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            elements: List of elements - 0 or more
        """
        super().__init__(xid)
        self.reason = reason
        self.table = table

