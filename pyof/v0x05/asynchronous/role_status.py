"""Defines a Controller Role Status Message."""

# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.base import GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16, UBInt8, UBInt32, UBInt64, Pad
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.controller2switch.role_request import ControllerRole

# Third-party imports

__all__ = ('RoleReason', 'RolePropertyType', 'RolePropHeader', 'RoleStatusMsg')


# Enums

class RoleReason(IntEnum):
    """What changed about the controller role."""

    #: Another controller asked to be master
    OFPCRR_MASTER_REQUEST = 0
    #: Configuration changed on the switch
    OFPCRR_CONFIG = 1
    #: Experimenter data changed
    OFPCRR_EXPERIMENTER = 2


class RolePropertyType(IntEnum):
    """Role property types"""

    #: Experimenter property
    OFPRPT_EXPERIMENTER = 0xFFFF


class RolePropHeader(GenericStruct):
    """Common header for all Role properties"""

    #: One of OFPRPT_
    role_type = UBInt16(enum_ref=RolePropertyType)
    #: Length in bytes of this property
    length = UBInt16()

    def __init__(self, role_type=RolePropertyType()):
        super().__init__()
        self.role_type = role_type


class ListOfRoleProperties(FixedTypeList):
    """List of RoleProperties.

    Represented by instances of RolePropHeader.
    """
    def __init__(self, items=None):
        """Create a ListOfProperties with the optional parameters below.

        Args:
            items (|RolePropHeader_v0x05|): Instance or a list of instances.
        """
        super().__init__(pyof_class=RolePropHeader, items=items)



class RoleStatusMsg(GenericMessage):
    """OpenFlow Controller Role Status Message OFPT_ROLE_REQUEST. """

    """Assign parameters to object attributes.

    Args:
        xid (int): :class:`~pyof.v0x05.common.header.Header`'s xid.
            Defaults to random.
        generation_id (int): Master Election Generation Id
        reason (int): One of OFPCRR_*.
        role (int): One of OFPCR_ROLE_*
    """

    #: Type OFPT_ROLE_STATUS
    header = Header(message_type=Type.OFPT_ROLE_STATUS)
    #: One of OFPCR_ROLE_*
    role = UBInt32(enum_ref=ControllerRole)
    #: One of OFPCRR_*.
    reason = UBInt8(enum_ref=RoleReason)
    #: Align to 64 bits
    pad = Pad(3)
    #: Master Election Generation Id
    generation_id = UBInt64()
    #: Role Property list
    properties = ListOfRoleProperties()

    def __init__(self, xid=None, role=ControllerRole, reason=RoleReason, generation_id=None, properties=None):
        """Create a message with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            role (int): the new role of the controller
            reason (int): one of RoleReason
            generation_id (int): the generation ID that was included in the role request message that
            triggered the role change
            properties: a list of role properties, describing dynamic parameters of table configuration

        """
        super().__init__()
        self.header.xid = xid
        self.role = role
        self.reason = reason
        self.generation_id = generation_id
        self.properties = properties if properties else []


class ExperimenterRoleProperty(RolePropHeader):
    """ Experimenter role property"""

    #: Experimenter ID which takes the same form as in struct ofp_experimenter_header
    experimenter = UBInt32()
    #: Experimenter defined
    exp_type = UBInt32()

    """Followed by:
        - Exactly (length - 12) bytes containing the experimenter data, then
        - Exactly (length + 7)/ 8 * 8 - (length) (between 0 and 7) bytes of all-zero bytes.
    """

    experimenter_data = UBInt32()

    def __init__(self, experimenter=None, exp_type=None):
        """
            Create the Experimenter Role Property
        :param experimenter: Experimenter ID which takes the same form as in struct ofp_experimenter_header
        :param exp_type: Experimenter defined
        """
        super().__init__(role_type=RolePropertyType.OFPRPT_EXPERIMENTER)
        # super().type = RolePropertyType.OFPRPT_EXPERIMENTER

        self.experimenter = experimenter

        self.exp_type = exp_type

        super().length = self.__sizeof__()
