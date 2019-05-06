"""Defines common structures and enums for controller2switch."""

# System imports
from enum import IntEnum

from pyof.foundation.base import GenericMessage, GenericStruct, GenericBitMask
from pyof.foundation.basic_types import (
    Char, FixedTypeList, Pad, UBInt8, UBInt16, UBInt32, UBInt64)
from pyof.foundation.constants import OFP_MAX_TABLE_NAME_LEN
from pyof.v0x05.asynchronous.flow_removed import FlowRemovedReason
from pyof.v0x05.asynchronous.packet_in import PacketInReason
from pyof.v0x05.asynchronous.port_status import PortReason
# Local source tree imports
from pyof.v0x05.common.action import (
    ActionHeader, ControllerMaxLen, ListOfActions, ActionType)
from pyof.v0x05.common.flow_instructions import ListOfInstruction, InstructionType
from pyof.v0x05.common.flow_match import ListOfOxmHeader
from pyof.v0x05.common.header import Header
from pyof.v0x05.controller2switch.modify_flow_table_message import Table

__all__ = ('ConfigFlag', 'ControllerRole', 'Bucket', 'BucketCounter', 'SwitchConfig',
           'ExperimenterMultipartHeader', 'MultipartType', 'AsyncConfig', 'RoleBaseMessage',
           'TableFeaturePropType', 'Property', 'InstructionsProperty', 'ActionID', 'PortStatsPropType',
           'NextTablesProperty', 'ActionsProperty', 'OxmProperty', 'ExperimenterProperty', 'PortStatsOpticalFlags',
           'ListOfProperty', 'TableFeatures', 'InstructionId', 'TableFeaturePropOxm', 'PortStatsPropHeader',
           'PortStatsPropEthernet', 'PortStatsPropOptical', 'PortStatsPropExperimenter', 'ListOfInstructionId',
           'ListActionID')

# Enum


class ConfigFlag(IntEnum):
    """Handling of IP fragments."""

    #: No special handling for fragments.
    OFPC_FRAG_NORMAL = 0
    #: Drop fragments.
    OFPC_FRAG_DROP = 1
    #: Reassemble (only if OFPC_IP_REASM set).
    OFPC_FRAG_REASM = 2
    OFPC_FRAG_MASK = 3


class ControllerRole(IntEnum):
    """Controller roles."""

    #: Don’t change current role.
    OFPCR_ROLE_NOCHANGE = 0
    #: Default role, full access.
    OFPCR_ROLE_EQUAL = 1
    #: Full access, at most one master.
    OFPCR_ROLE_MASTER = 2
    #: Read-only access.
    OFPCR_ROLE_SLAVE = 3


class TableFeaturePropType(IntEnum):
    """Table Property Types.

    Low order bit cleared indicates a property for a regular Flow Entry.
    Low order bit set indicates a property for the Table-Miss Flow Entry.
    """

    # Instructions property.
    OFPTFPT_INSTRUCTIONS = 0
    # Instructions for table-miss.
    OFPTFPT_INSTRUCTIONS_MISS = 1
    # Next Table property.
    OFPTFPT_NEXT_TABLES = 2
    # Next Table for table-miss.
    OFPTFPT_NEXT_TABLES_MISS = 3
    # Write Actions property.
    OFPTFPT_WRITE_ACTIONS = 4
    # Write Actions for table-miss.
    OFPTFPT_WRITE_ACTIONS_MISS = 5
    # Apply Actions property.
    OFPTFPT_APPLY_ACTIONS = 6
    # Apply Actions for table-miss.
    OFPTFPT_APPLY_ACTIONS_MISS = 7
    # Match property.
    OFPTFPT_MATCH = 8
    # Wildcards property.
    OFPTFPT_WILDCARDS = 10
    # Write Set-Field property.
    OFPTFPT_WRITE_SETFIELD = 12
    # Write Set-Field for table-miss.
    OFPTFPT_WRITE_SETFIELD_MISS = 13
    # Apply Set-Field property.
    OFPTFPT_APPLY_SETFIELD = 14
    # Apply Set-Field for table-miss.
    OFPTFPT_APPLY_SETFIELD_MISS = 15
    # Experimenter property.
    OFPTFPT_EXPERIMENTER = 0xFFFE
    # Experimenter for table-miss.
    OFPTFPT_EXPERIMENTER_MISS = 0xFFFF

    def find_class(self):
        """Return a class related with this type."""
        if self.value <= 1:
            return InstructionsProperty
        elif self.value <= 3:
            return NextTablesProperty
        elif self.value <= 7:
            return ActionsProperty

        return OxmProperty


class MultipartType(IntEnum):
    """Types of Multipart Messages, both Request and Reply."""

    #: Description of this OpenFlow switch.
    #: The request body is empty.
    #: The reply body is struct ofp_desc.
    OFPMP_DESC = 0

    #: Individual flow statistics.
    #: The request body is struct ofp_flow_stats_request.
    #: The reply body is an array of struct ofp_flow_stats.
    OFPMP_FLOW = 1

    #: Aggregate flow statistics.
    #: The request body is struct ofp_aggregate_stats_request.
    #: The reply body is struct ofp_aggregate_stats_reply.
    OFPMP_AGGREGATE = 2

    #: Flow table statistics.
    #: The request body is empty.
    #: The reply body is an array of struct ofp_table_stats.
    OFPMP_TABLE = 3

    #: Port statistics.
    #: The request body is struct ofp_port_stats_request.
    #: The reply body is an array of struct ofp_port_stats.
    OFPMP_PORT_STATS = 4

    #: Queue statistics for a port.
    #: The request body is struct ofp_queue_stats_request.
    #: The reply body is an array of struct ofp_queue_stats.
    OFPMP_QUEUE_STATS = 5

    #: Group counter statistics.
    #: The request body is struct ofp_group_stats_request.
    #: The reply is an array of struct ofp_group_stats.
    OFPMP_GROUP = 6

    #: Group description.
    #: The request body is empty.
    #: The reply body is an array of struct ofp_group_desc_stats.
    OFPMP_GROUP_DESC = 7

    #: Group features.
    #: The request body is empty.
    #: The reply body is struct ofp_group_features.
    OFPMP_GROUP_FEATURES = 8

    #: Meter statistics.
    #: The request body is struct ofp_meter_multipart_requests.
    #: The reply body is an array of struct ofp_meter_stats.
    OFPMP_METER = 9

    #: Meter configuration.
    #: The request body is struct ofp_meter_multipart_requests.
    #: The reply body is an array of struct ofp_meter_config.
    OFPMP_METER_CONFIG = 10

    #: Meter features.
    #: The request body is empty.
    #: The reply body is struct ofp_meter_features.
    OFPMP_METER_FEATURES = 11

    #: Table features.
    #: The request body is either empty or contains an array of
    #: struct ofp_table_features containing the controller’s desired view of
    #: the switch. If the switch is unable to set the specified view an error
    #: is returned.
    #: The reply body is an array of struct ofp_table_features.
    OFPMP_TABLE_FEATURES = 12

    #: Port description.
    #: The request body is empty.
    #: The reply body is an array of struct ofp_port.
    OFPMP_PORT_DESC = 13

    #: Table description
    #: The request body is empty
    #: The reply body is an array of struct TableDesc.
    OFPMP_TABLE_DESC = 14

    #: Queue description
    #: The request body is struct QueueDescRequest.
    #: The reply body is an array of struct QueueDesc.
    OFPMP_QUEUE_DESC = 15

    #: Flow monitor. Reply may be an asynchronous message.
    #: The request body is an array of struct FlowMonitorRequest.
    #: The reply body is an array of struct FlowUpdateHeader.
    OFPMP_FLOW_MONITOR = 16

    #: Experimenter extension.
    #: The request and reply bodies begin with
    #: struct ofp_experimenter_multipart_header.
    #: The request and reply bodies are otherwise experimenter-defined.
    OFPMP_EXPERIMENTER = 0xffff


class PortStatsPropType(IntEnum):
    """
    Port stats property types.
    """

    #: Ethernet property.
    OFPPSPT_ETHERNET = 0
    #: Optical property
    OFPPSPT_OPTICAL = 1
    #: Experimenter property
    OFPPSPT_EXPERIMENTER = 0xffff


class PortStatsOpticalFlags(GenericBitMask):
    """
    Flags is one of OFPOSF_ bellow
    """
    #: Receiver tune info valid
    OFPOSF_RX_TUNE = 1 << 0
    #: Transmit tune info valid
    OFPOSF_TX_TUNE = 1 << 1
    #: TX Power is valid
    OFPOSF_TX_PWR = 1 << 2
    #: RX Power is valid
    OFPOSF_RX_PWR = 1 << 4
    #: Transmit bias is valid
    OFPOSF_TX_BIAS = 1 << 5
    #: TX temp is valid
    OFPOSF_TX_TEMP = 1 << 6

# Classes


class Bucket(GenericStruct):
    """Bucket for use in groups."""

    length = UBInt16()
    weight = UBInt16()
    watch_port = UBInt32()
    watch_group = UBInt32()
    pad = Pad(4)
    actions = FixedTypeList(ActionHeader)

    def __init__(self, length=None, weight=None, watch_port=None,
                 watch_group=None, actions=None):
        """Initialize all instance variables.

        Args:
            length (int): Length the bucket in bytes, including this header and
                any padding to make it 64-bit aligned.
            weight (int): Relative weight of bucket. Only defined for select
                groups.
            watch_port (int): Port whose state affects whether this bucket is
                live. Only required for fast failover groups.
            watch_group (int): Group whose state affects whether this bucket is
                live. Only required for fast failover groups.
            actions (~pyof.v0x05.common.action.ListOfActions): The action
                length is inferred from the length field in the header.
        """
        super().__init__()
        self.length = length
        self.weight = weight
        self.watch_port = watch_port
        self.watch_group = watch_group
        self.actions = actions


class BucketCounter(GenericStruct):
    """Used in group stats replies."""

    #: Number of packets processed by bucket.
    packet_count = UBInt64()
    #: Number of bytes processed by bucket.
    byte_count = UBInt64()

    def __init__(self, packet_count=None, byte_count=None):
        """Create BucketCounter with the optional parameters below.

        Args:
            packet_count (int): Number of packets processed by bucket.
            byte_count (int): Number of bytes processed by bucket.
        """
        super().__init__()
        self.packet_count = packet_count
        self.byte_count = byte_count


# Base Classes for other messages - not meant to be directly used, so, because
# of that, they will not be inserted on the __all__ attribute.


class AsyncConfig(GenericMessage):
    """Asynchronous message configuration base class.

    Common structure for SetAsync and GetAsyncReply messages.

    AsyncConfig contains three 2-element arrays. Each array controls whether
    the controller receives asynchronous messages with a specific
    :class:`~pyof.v0x05.common.header.Type`. Within each array, element
    0 specifies messages of interest when the controller has a OFPCR_ROLE_EQUAL
    or OFPCR_ROLE_MASTER role; element 1, when the controller has a
    OFPCR_ROLE_SLAVE role. Each array element is a bit-mask in which a 0-bit
    disables receiving a message sent with the reason code corresponding to the
    bit index and a 1-bit enables receiving it.
    """

    #: OpenFlow :class:`~pyof.v0x05.common.header.Header`
    #: OFPT_GET_ASYNC_REPLY or OFPT_SET_ASYNC.
    header = Header()
    packet_in_mask1 = UBInt32(enum_ref=PacketInReason)
    packet_in_mask2 = UBInt32(enum_ref=PacketInReason)
    port_status_mask1 = UBInt32(enum_ref=PortReason)
    port_status_mask2 = UBInt32(enum_ref=PortReason)
    flow_removed_mask1 = UBInt32(enum_ref=FlowRemovedReason)
    flow_removed_mask2 = UBInt32(enum_ref=FlowRemovedReason)

    def __init__(self, xid=None, packet_in_mask1=None, packet_in_mask2=None,
                 port_status_mask1=None, port_status_mask2=None,
                 flow_removed_mask1=None, flow_removed_mask2=None):
        """Create a AsyncConfig with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            packet_in_mask1
                (~pyof.v0x05.asynchronous.packet_in.PacketInReason):
                    A instance of PacketInReason
            packet_in_mask2
                (~pyof.v0x05.asynchronous.packet_in.PacketInReason):
                    A instance of PacketInReason
            port_status_mask1
                (~pyof.v0x05.asynchronous.port_status.PortReason):
                    A instance of PortReason
            port_status_mask2
                (~pyof.v0x05.asynchronous.port_status.PortReason):
                    A instance of PortReason
            flow_removed_mask1
                (~pyof.v0x05.asynchronous.flow_removed.FlowRemoved):
                    A instance of FlowRemoved.
            flow_removed_mask2
                (~pyof.v0x05.asynchronous.flow_removed.FlowRemoved):
                    A instance of FlowRemoved.
        """
        super().__init__(xid)
        self.packet_in_mask1 = packet_in_mask1
        self.packet_in_mask2 = packet_in_mask2
        self.port_status_mask1 = port_status_mask1
        self.port_status_mask2 = port_status_mask2
        self.flow_removed_mask1 = flow_removed_mask1
        self.flow_removed_mask2 = flow_removed_mask2


class RoleBaseMessage(GenericMessage):
    """Role basic structure for RoleRequest and RoleReply messages."""

    #: :class:`~pyof.v0x05.common.header.Header`
    #: Type OFPT_ROLE_REQUEST/OFPT_ROLE_REPLY.
    header = Header()
    #: One of NX_ROLE_*. (:class:`~.controller2switch.common.ControllerRole`)
    role = UBInt32(enum_ref=ControllerRole)
    #: Align to 64 bits.
    pad = Pad(4)
    #: Master Election Generation Id.
    generation_id = UBInt64()

    def __init__(self, xid=None, role=None, generation_id=None):
        """Create a RoleBaseMessage with the optional parameters below.

        Args:
            xid (int): OpenFlow xid to the header.
            role (:class:`~.controller2switch.common.ControllerRole`): .
            generation_id (int): Master Election Generation Id.
        """
        super().__init__(xid)
        self.role = role
        self.generation_id = generation_id


class SwitchConfig(GenericMessage):
    """Used as base class for SET_CONFIG and GET_CONFIG_REPLY messages."""

    #: OpenFlow :class:`~pyof.v0x05.common.header.Header`
    header = Header()
    flags = UBInt16(enum_ref=ConfigFlag)
    miss_send_len = UBInt16()

    def __init__(self, xid=None, flags=ConfigFlag.OFPC_FRAG_NORMAL,
                 miss_send_len=ControllerMaxLen.OFPCML_NO_BUFFER):
        """Create a SwitchConfig with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            flags (ConfigFlag): OFPC_* flags.
            miss_send_len (int): UBInt16 max bytes of new flow that the
                datapath should send to the controller.
        """
        super().__init__(xid)
        self.flags = flags
        self.miss_send_len = miss_send_len


# Multipart body

class ExperimenterMultipartHeader(GenericStruct):
    """Body for ofp_multipart_request/reply of type OFPMP_EXPERIMENTER."""

    experimenter = UBInt32()
    exp_type = UBInt32()
    #: Followed by experimenter-defined arbitrary data.

    def __init__(self, experimenter=None, exp_type=None):
        """Create a ExperimenterMultipartHeader with the parameters below.

        Args:
            experimenter: Experimenter ID which takes the same form as in
                struct ofp_experimenter_header (
                :class:`~pyof.v0x05.symmetric.experimenter.ExperimenterHeader`)
            exp_type: Experimenter defined.
        """
        super().__init__()
        self.experimenter = experimenter
        self.exp_type = exp_type


class Property(GenericStruct):
    """Table Property class.

    This class represents a Table Property generic structure.
    """

    property_type = UBInt16(enum_ref=TableFeaturePropType)
    length = UBInt16(4)

    def __init__(self, property_type=None):
        """Create a Property with the optional parameters below.

        Args:
            type(|TableFeaturePropType_v0x05|):
                Property Type value of this instance.
        """
        super().__init__()
        self.property_type = property_type

    def pack(self, value=None):
        """Pack method used to update the length of instance and  packing.

        Args:
            value: Structure to be packed.
        """
        self.update_length()
        return super().pack(value)

    def unpack(self, buff=None, offset=0):
        """Unpack *buff* into this object.

        This method will convert a binary data into a readable value according
        to the attribute format.

        Args:
            buff (bytes): Binary buffer.
            offset (int): Where to begin unpacking.

        Raises:
            :exc:`~.exceptions.UnpackException`: If unpack fails.

        """
        property_type = UBInt16(enum_ref=TableFeaturePropType)
        property_type.unpack(buff, offset)
        self.__class__ = TableFeaturePropType(property_type.value).find_class()

        length = UBInt16()
        length.unpack(buff, offset=offset+2)
        super().unpack(buff[:offset+length.value], offset=offset)

    def update_length(self):
        """Update the length of current instance."""
        self.length = self.get_size()


class InstructionId(GenericStruct):
    """Instruction ID"""

    #: One of OFPIT_*.
    type = UBInt16(InstructionType)
    #: Length is 4 or experimenter defined.
    length = UBInt16(4)
    #: Optional experimenter id + data.
    exp_data = UBInt8()

    def __init__(self, type=InstructionType, length=None, exp_data=None):
        """The instruction_ids field is the list of instructions supported by this table.
        The elements of that list are variable in size to enable expressing experimenter
         instructions. Non-experimenter instructions are 4 bytes.

            Args:
                type(InstructionType): One of OFPIT_*.
                length(int): Length is 4 or experimenter defined.
                exp_data(int): Optional experimenter id + data.
        """
        super().__init__()
        self.type = type
        self.length = UBInt16(4) if length is None else length
        self.exp_data = exp_data


class ListOfInstructionId(FixedTypeList):
    """
    List of Instruction IDs.
    """

    def __init__(self, items=None):
        """
        Create a list of Instruction IDs.

        :param items: Instance or a list of instances.
        """
        super().__init__(pyof_class=InstructionId,items=items)


class InstructionsProperty(Property):
    """Instructions property.

    This class represents Property with the following types:
        OFPTFPT_INSTRUCTIONS
        OFPTFPT_INSTRUCTIONS_MISS
    """

    instruction_ids = ListOfInstructionId()

    def __init__(self, property_type=TableFeaturePropType.OFPTFPT_INSTRUCTIONS,
                 instruction_ids=None):
        """Create a InstructionsProperty with the optional parameters below.

        Args:
            type(|TableFeaturePropType_v0x05|):
                Property Type value of this instance.
            instruction_ids(|ListOfInstruction_v0x05|):
                List of InstructionGotoTable instances.
        """
        super().__init__(property_type=property_type)
        self.instruction_ids = instruction_ids if instruction_ids else []
        self.update_length()


class NextTablesProperty(Property):
    """Next Tables Property.

    This class represents Property with the following types:
        OFPTFPT_NEXT_TABLES
        OFPTFPT_NEXT_TABLES_MISS
        OFPTFPT_TABLE_SYNC_FROM
    """

    next_table_ids = ListOfInstruction()

    def __init__(self, property_type=TableFeaturePropType.OFPTFPT_NEXT_TABLES,
                 next_table_ids=None):
        """Create a NextTablesProperty with the optional parameters below.

        Args:
            type(|TableFeaturePropType_v0x05|):
                Property Type value of this instance.
            next_table_ids (|ListOfInstruction_v0x05|):
                List of InstructionGotoTable instances.
        """
        super().__init__(property_type)
        self.next_table_ids = (ListOfInstruction() if next_table_ids is None
                               else next_table_ids)
        self.update_length()


class ActionID(GenericStruct):
    """Action ID"""

    type = UBInt16(ActionType)
    len = UBInt16()
    exp_data = UBInt8()

    def __init__(self, type=ActionType, len=None, exp_data=None):
        """Action ID
            Args:
                type(ActionType): One of OFPAT_*.
                len(int): Length is 4 or experimenter defined.
                exp_data(int): Optional experimenter id + data.
        """
        super().__init__()
        self.type = type if isinstance(type, ActionType) else None
        self.len = UBInt16(4) if len is not None else len
        self.exp_data = exp_data


class ListActionID(FixedTypeList):
    """
    List of action ID.

    """

    def __init__(self, items=None):
        """
        Create a list of Action IDs.

        :param items: Instance or a list of instances
        """
        super().__init__(pyof_class=ActionID,items=items)


class ActionsProperty(Property):
    """Actions Property.

    This class represents Property with the following type:
        OFPTFPT_WRITE_ACTIONS
        OFPTFPT_WRITE_ACTIONS_MISS
        OFPTFPT_APPLY_ACTIONS
        OFPTFPT_APPLY_ACTIONS_MISS
    """

    action_ids = ListActionID()

    def __init__(self,
                 property_type=TableFeaturePropType.OFPTFPT_WRITE_ACTIONS,
                 action_ids=None):
        """Create a ActionsProperty with the optional parameters below.

        Args:
            type(|TableFeaturePropType_v0x05|):
                Property Type value of this instance.
            action_ids(|ListOfActions_v0x05|):
                List of Action instances.
        """
        super().__init__(property_type)
        self.action_ids = action_ids if action_ids else []
        self.update_length()


class OxmProperty(Property):
    """Match, Wildcard or Set-Field property.

    This class represents Property with the following types:
        OFPTFPT_MATCH
        OFPTFPT_WILDCARDS
        OFPTFPT_WRITE_SETFIELD
        OFPTFPT_WRITE_SETFIELD_MISS
        OFPTFPT_APPLY_SETFIELD
        OFPTFPT_APPLY_SETFIELD_MISS
    """

    oxm_ids = ListOfOxmHeader()

    def __init__(self, property_type=TableFeaturePropType.OFPTFPT_MATCH,
                 oxm_ids=None):
        """Create an OxmProperty with the optional parameters below.

        Args:
            type(|TableFeaturePropType_v0x05|):
                Property Type value of this instance.
            oxm_ids(|ListOfOxmHeader_v0x05|):
                List of OxmHeader instances.
        """
        super().__init__(property_type)
        self.oxm_ids = ListOfOxmHeader() if oxm_ids is None else oxm_ids
        self.update_length()


class ExperimenterProperty(Property):
    """Experimenter table feature property.

    This class represents property with the following types:
        OFPTFPT_EXPERIMENTER
        OFPTFPT_EXPERIMENTER_MISS

    """
    experimenter = UBInt32()
    exp_type = UBInt32()

    experimenter_data = UBInt32()

    def __init__(self, property_type=TableFeaturePropType.OFPTFPT_EXPERIMENTER, experimenter=None, exp_type=None, experimenter_data=None):
        """ Create or initialize an object Experimenter table feature property.

        :param property_type(int): One of OFPTFPT_EXPERIMENTER, OFPTFPT_EXPERIMENTER_MISS.
        :param experimenter(int): Experimenter ID which takes the same form as in strcut ExperimenterHeader.
        :param exp_type(int): Experimenter defined.
        Followed by:
            - Exactly (length - 12) bytes containing the experimenter data, then
            - Exactly (length + 7)/8*8 - (length) (between 0 and 7) bytes of all-zero bytes.
        :param experimenter_data(int): Experimenter data.
        """

        super().__init__(property_type)
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data
        self.update_length()


class TableFeaturePropOxm(Property):
    """Match, Wildcard or Set-Field property."""

    oxm_ids = UBInt32()

    def __init__(self, property_type=TableFeaturePropType.OFPTFPT_MATCH, oxm_ids=None):
        """ Create or initialize an object Match, Wildcard or Set-Field property

        :param property_type(int): One of OFPTFPT_MATCH, OFPTFPT_WILDCARDS, OFPTFPT_WRITE_SETFIELD,
        OFPTFPT_WRITE_SETWIELD_MISS, OFPTFPT_APPLY_SETFIELD, OFPTFPT_APPLY_SETFIELD_MISS.
        Followed by:
            - Exactly (length - 4) bytes containing the oxm_ids, then
            - Exactly (length + 7)/8*8 - (length) (between 0 and 7) bytes
            of all-zero bytes.
        :param oxm_ids(int): Array of OXM headers.

        """
        super().__init__(property_type)

        self.oxm_ids = oxm_ids if oxm_ids is FixedTypeList else []
        self.update_length()



class ListOfProperty(FixedTypeList):
    """List of Table Property.

    Represented by instances of Property.
    """

    def __init__(self, items=None):
        """Create a ListOfProperty with the optional parameters below.

        Args:
            items (|Property_v0x05|): Instance or a list of instances.
        """
        super().__init__(pyof_class=Property, items=items)


class TableFeatures(GenericStruct):
    """Abstration of common class Table Features.

    Body for MultipartRequest of type OFPMP_TABLE_FEATURES.
    Body of reply to OFPMP_TABLE_FEATURES request.
    """

    length = UBInt16()
    # /* Identifier of table.  Lower numbered tables are consulted first. */
    table_id = UBInt8()
    # /* Align to 64-bits. */
    pad = Pad(5)
    name = Char(length=OFP_MAX_TABLE_NAME_LEN)
    # /* Bits of metadata table can match. */
    metadata_match = UBInt64()
    # /* Bits of metadata table can write. */
    metadata_write = UBInt64()
    # /* Bitmap of OFPTC_* values */
    capabilities = UBInt32()
    # /* Max number of entries supported. */
    max_entries = UBInt32()
    # /* Table Feature Property list */
    properties = ListOfProperty()

    def __init__(self, table_id=Table.OFPTT_ALL, name="",
                 metadata_match=0xFFFFFFFFFFFFFFFF,
                 metadata_write=0xFFFFFFFFFFFFFFFF,
                 capabilities=0,
                 max_entries=0,
                 properties=None):
        """Create a TableFeatures with the optional parameters below.

        Args:
            table_id(int): Indetifier of table.The default value
                OFPTT_ALL(``0xff``) will apply the configuration to all tables
                in the switch.
            name(Char): Characters representing the table name.
            metadata_match(int): Indicate the bits of the metadata field that
               the table can match on.The default value ``0xFFFFFFFFFFFFFFFF``
               indicates that the table can match the full metadata field.
            metadata_write(int): Indicates the bits of the metadata field that
               the table can write using the OFPIT_WRITE_METADATA instruction.
               The default value ``0xFFFFFFFFFFFFFFFF`` indicates that the
               table can write the full metadata field.
            capabilities(int): Field reseved for future use.
            max_entries(int): Describe the maximum number of flow entries that
                can be inserted into that table.
            properties(~pyof.v0x05.controller2switch.common.ListOfProperty):
                List of Property intances.
        """
        super().__init__()
        self.table_id = table_id
        self.name = name
        self.metadata_match = metadata_match
        self.metadata_write = metadata_write
        self.capabilities = capabilities
        self.max_entries = max_entries
        self.properties = (ListOfProperty() if properties is None else
                           properties)
        self.update_length()

    def pack(self, value=None):
        """Pack method used to update the length of instance and packing.

        Args:
            value: Structure to be packed.
        """
        self.update_length()
        return super().pack(value)

    def update_length(self):
        """Update the length of current instance."""
        self.length = self.get_size()

    def unpack(self, buff=None, offset=0):
        """Unpack *buff* into this object.

        This method will convert a binary data into a readable value according
        to the attribute format.

        Args:
            buff (bytes): Binary buffer.
            offset (int): Where to begin unpacking.

        Raises:
            :exc:`~.exceptions.UnpackException`: If unpack fails.

        """
        length = UBInt16()
        length.unpack(buff, offset)
        super().unpack(buff[:offset+length.value], offset)


class PortStatsPropHeader(GenericStruct):
    """
    Common header for all port stats properties.
    """
    #: One of OFPPSPT_*
    type = UBInt16()
    #: Length in bytes of this property.
    length = UBInt16()

class PortStatsPropEthernet(PortStatsPropHeader):
    """
    Ethernet port stats property
    """
    pad = Pad(4)

    rx_frame_err = UBInt64()
    rx_over_err = UBInt64()
    rx_crc_err = UBInt64()
    collisions = UBInt64()

    def __init__(self, rx_frame_err=None, rx_over_err=None, rx_crc_err=None, collisions=None):
        """
        Create the Ethernet port stats property.

        :param rx_frame_err: Number of frame alignment errors.
        :param rx_over_err: Number of packets with RX overrun.
        :param rx_crc_err: Number of CRC errors.
        :param collisions: Number of collisions.
        """
        super().type = PortStatsPropType.OFPPSPT_ETHERNET
        self.rx_frame_err = rx_frame_err
        self.rx_over_err = rx_over_err
        self.rx_crc_err = rx_crc_err
        self.collisions = collisions
        super().length = self.__sizeof__()


class PortStatsPropOptical(PortStatsPropHeader):
    """
    Optical port stats property.
    """

    pad = Pad(4)
    flags = UBInt32()
    tx_freq_lmda = UBInt32()
    tx_offset = UBInt32()
    tx_grid_span = UBInt32()
    rx_freq_lmda = UBInt32()
    rx_offset = UBInt32()
    rx_grid_span = UBInt32()
    tx_pwr = UBInt16()
    rx_pwr = UBInt16()
    bias_current = UBInt16()
    temperature = UBInt16()

    def __init__(self, flags=None, tx_freq_lmda=None, tx_offset=None, tx_grid_span=None, rx_freq_lmda=None,
                 rx_offset=None, rx_grid_span=None, tx_pwr=None, rx_pwr=None, bias_current=None, temperature=None):
        """
        Create the optical port stats property.

        :param flags: Features enabled by the port.
        :param tx_freq_lmda: Current TX Frequency/Wavelength
        :param tx_offset: TX Offset
        :param tx_grid_span: TX Grid Spacing
        :param rx_freq_lmda: Current RX Frequency/Wavelength
        :param rx_offset: RX Offset
        :param rx_grid_span: RX Grid Spacing
        :param tx_pwr: Current TX power
        :param rx_pwr: Current RX power
        :param bias_current: TX Bias Current
        :param temperature: TX Laser Temperature
        """
        super().type = PortStatsPropType.OFPPSPT_OPTICAL
        self.flags = flags
        self.tx_freq_lmda = tx_freq_lmda
        self.tx_offset = tx_offset
        self.tx_grid_span = tx_grid_span
        self.rx_freq_lmda = rx_freq_lmda
        self.rx_offset = rx_offset
        self.rx_grid_span = rx_grid_span
        self.tx_pwr = tx_pwr
        self.rx_pwr = rx_pwr
        self.bias_current = bias_current
        self.temperature = temperature
        super().length = self.__sizeof__()


class PortStatsPropExperimenter(PortStatsPropHeader):
    """
    Experimenter port stats property.
    """
    experimenter = UBInt32()
    exp_type = UBInt32()
    experimenter_data = UBInt32()

    def __init__(self, experimenter=None, exp_type=None, experimenter_data=None):
        """
        Create the experimenter port stats property.

        :param experimenter: Experimenter ID which takes the same form as in ExperimenterHeader
        :param exp_type: Experimenter defined
        Followed by:
            - Exactly (length - 12) bytes containing the experimenter data, then
            - Exactly (length + 7)/8*8 - (length) (between 0 and 7) bytes of all-zeros bytes
        :param experimenter_data: Experimenter Data
        """
        super().type = PortStatsPropType.OFPPSPT_EXPERIMENTER
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data
        super().length = self.__sizeof__()
