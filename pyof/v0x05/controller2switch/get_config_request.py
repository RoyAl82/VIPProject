"""Defines Get Config Request classes and related items."""

from pyof.foundation.base import GenericMessage
from pyof.v0x05.common.header import Header, Type

__all__ = ('GetConfigRequest',)

# Classes


class GetConfigRequest(GenericMessage):
    """Get Config Request message."""

    header = Header(message_type=Type.OFPT_GET_CONFIG_REQUEST)
