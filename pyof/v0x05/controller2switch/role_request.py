"""Request a change of the role of the controller."""

# System imports
from enum import IntEnum

# Third-party imports

# Local source tree imports
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.controller2switch.common import RoleBaseMessage
from pyof.foundation.basic_types import (Pad, UBInt32, UBInt64)

__all__ = ('RoleRequest', 'ControllerRole')


# Enums

class ControllerRole(IntEnum):
    """ Controller roles """

    #: Don’t change current role
    OFPCR_ROLE_NOCHANGE = 0
    #: Default role, full access
    OFPCR_ROLE_EQUAL = 1
    #: Full access, at most one master
    OFPCR_ROLE_MASTER = 2
    #: Read - only access
    OFPCR_ROLE_SLAVE = 3


# Classes

class RoleRequest(RoleBaseMessage):
    """RoleRequest Message.

    When the controller wants to change its role, it uses the OFPT_ROLE_REQUEST
    message.
    """
    header = Header(message_type=Type.OFPT_ROLE_REQUEST)
    role = UBInt32(enum_ref=ControllerRole)
    pad = Pad(4)
    generation_id = UBInt64()

    def __init__(self, xid=None, role=None, generation_id=None):
        """Create a RoleRequest with the optional parameters below.

        Args:
            xid (int): OpenFlow xid to the header.
            role (:class:`~.controller2switch.common.ControllerRole`):
                Is the new role that the controller wants to assume.
            generation_id (int): Master Election Generation Id.
        """
        super().__init__(xid, role, generation_id)

