"""Defines a Request Forward Message."""
# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.base import GenericMessage
from pyof.v0x05.common.header import Header,Type

# Enums

class RequestForwardReason(IntEnum):
    """
    Request Forward Reason
    """

    #: Forward Group Mod requests
    OFPRFR_GROUP_MOD = 0

    #: Forward meter mod requests
    OFPRFR_METER_MOD = 1

# Classes

class RequestForwardHeader(GenericMessage):
    """Ofp Request Forward Header"""
    #: Type OFPT_REQUESTFORWARD
    header = Header(message_type=Type.OFPT_REQUESTFORWARD)
    #: Request being forwarded
    request = Header()
