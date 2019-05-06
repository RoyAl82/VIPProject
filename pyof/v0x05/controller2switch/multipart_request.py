"""Controller requesting state from datapath."""

# System imports
from enum import Enum

# Local source tree imports
from pyof.foundation.base import GenericMessage, GenericStruct, IntEnum
from pyof.foundation.basic_types import (
    BinaryData, FixedTypeList, Pad, UBInt8, UBInt16, UBInt32, UBInt64)
from pyof.v0x05.common.flow_match import Match
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.common.port import PortNo
from pyof.v0x05.controller2switch.common import (
    ExperimenterMultipartHeader, MultipartType, TableFeatures)
from pyof.v0x05.controller2switch.group_mod import Group
from pyof.v0x05.controller2switch.meter_mod import Meter
from pyof.v0x05.controller2switch.modify_flow_table_message import Table

# Third-party imports

__all__ = ('MultipartRequest', 'MultipartRequestFlags', 'FlowMonitorCommand', 'FlowMonitorFlags',
           'AggregateStatsRequest', 'FlowStatsRequest', 'FlowMonitorRequest',
           'PortStatsRequest', 'QueueStatsRequest',
           'GroupStatsRequest', 'MeterMultipartRequest')


# Enum


class MultipartRequestFlags(IntEnum):
    """Flags for MultipartRequest."""

    #: No more requests to follow (This is not part of spec). Thanks @jondef95
    OFPMPF_REQ_NONE = 0

    #: More requests to follow
    OFPMPF_REQ_MORE = 1 << 0


class FlowMonitorCommand(IntEnum):
    """Flow monitor commands"""

    #: New flow monitor
    OFPFMC_ADD = 0
    #: Modify existing flow monitor
    OFPFMC_MODIFY = 1
    #: Delete / cancel existing flow monitor
    OFPFMC_DELETE = 2


class FlowMonitorFlags(IntEnum):
    """’flags’ bits in struct of_flow_monitor_request"""

    #: Initially matching flows
    OFPFMF_INITIAL = 1 << 0
    #: New matching flows as they are added
    OFPFMF_ADD = 1 << 1
    #: Old matching flows as they are removed
    OFPFMF_REMOVED = 1 << 2
    #: Matching flows as they are changed What to include in updates
    OFPFMF_MODIFY = 1 << 3
    #: If set, instructions are included
    OFPFMF_INSTRUCTIONS = 1 << 4
    #: If set, include own changes in full
    OFPFMF_NO_ABBREV = 1 << 5
    #: If set, don’t include other controllers
    OFPFMF_ONLY_OWN = 1 << 6


# Classes


class MultipartRequest(GenericMessage):
    """Request datapath state.

    While the system is running, the controller may request state from the
    datapath using the OFPT_MULTIPART_REQUEST message.
    """

    #: Openflow :class:`~pyof.v0x05.common.header.Header`
    header = Header(message_type=Type.OFPT_MULTIPART_REQUEST)
    #: One of the OFPMP_* constants.
    multipart_type = UBInt16(enum_ref=MultipartType)
    #: OFPMPF_REQ_* flags.
    flags = UBInt16(enum_ref=MultipartRequestFlags)
    #: Padding
    pad = Pad(4)
    #: Body of the request
    body = BinaryData()

    def __init__(self, xid=None, multipart_type=None, flags=0, body=b''):
        """Create a MultipartRequest with the optional parameters below.

        Args:
            xid (int): xid to the header.
            multipart_type (int): One of the OFPMP_* constants.
            flags (int): OFPMPF_REQ_* flags.
            body (bytes): Body of the request.
        """
        super().__init__(xid)
        self.multipart_type = multipart_type
        self.flags = flags
        self.body = body

    def pack(self, value=None):
        """Pack a MultipartRequest using the object's attributes.

        This method will pack the attribute body and multipart_type before pack
        the MultipartRequest object, then will return this struct as a
        binary data.

        Args:
            value (:class:`~MultipartRequest`): Object to be packed.

        Returns:
            bytes: Binary data with MultipartRequest packed.

        """
        buff = self.body
        if not value:
            value = self.body

        if value:
            if isinstance(value, (list, FixedTypeList)):
                obj = self._get_body_instance()
                obj.extend(value)
            elif hasattr(value, 'pack'):
                obj = value

            self.body = obj.pack()

        multipart_packed = super().pack()
        self.body = buff

        return multipart_packed

    def unpack(self, buff, offset=0):
        """Unpack a binary message into this object's attributes.

        Unpack the binary value *buff* and update this object attributes based
        on the results. It is an inplace method and it receives the binary data
        of the message **without the header**.

        This class' unpack method is like the :meth:`.GenericMessage.unpack`
        one, except for the ``body`` attribute which has its type determined
        by the ``multipart_type`` attribute.

        Args:
            buff (bytes): Binary data package to be unpacked, without the
                header.
        """
        super().unpack(buff[offset:])
        self._unpack_body()

    def _unpack_body(self):
        """Unpack `body` replace it by the result."""
        obj = self._get_body_instance()
        obj.unpack(self.body.value)
        self.body = obj

    def _get_body_instance(self):
        """Return the body instance."""
        simple_body = {
            MultipartType.OFPMP_FLOW: FlowStatsRequest,
            MultipartType.OFPMP_AGGREGATE: AggregateStatsRequest,
            MultipartType.OFPMP_PORT_STATS: PortStatsRequest,
            MultipartType.OFPMP_QUEUE: QueueStatsRequest,
            MultipartType.OFPMP_GROUP: GroupStatsRequest,
            MultipartType.OFPMP_METER: MeterMultipartRequest,
            MultipartType.OFPMP_EXPERIMENTER: ExperimenterMultipartHeader
        }

        array_of_bodies = {MultipartType.OFPMP_TABLE_FEATURES: TableFeatures}

        if isinstance(self.multipart_type, UBInt16):
            self.multipart_type = self.multipart_type.enum_ref(
                self.multipart_type.value)

        pyof_class = simple_body.get(self.multipart_type, None)
        if pyof_class:
            return pyof_class()

        array_of_class = array_of_bodies.get(self.multipart_type, None)
        if array_of_class:
            return FixedTypeList(pyof_class=array_of_class)

        return BinaryData(b'')


class AggregateStatsRequest(GenericStruct):
    """Body for ofp_stats_request of type OFPST_AGGREGATE."""

    #: ID of table to read (from ofp_table_stats) OFPTT_ALL for all tables.
    table_id = UBInt8()
    #: Align to 32 bits.
    pad = Pad(3)
    #: Require matching entries to include this as an output port. A value of
    #: OFPP_ANY indicates no restriction.
    out_port = UBInt32()
    #: Require matching entries to include this as an output group. A value of
    #: OFPG_ANY indicates no restriction.
    out_group = UBInt32()
    #: Align to 64 bits
    pad2 = Pad(4)
    #: Require matching entries to contain this cookie value
    cookie = UBInt64()
    #: Mask used to restrict the cookie bits that must match. A value of 0
    #: indicates no restriction.
    cookie_mask = UBInt64()
    #: Fields to match. Variable size.
    match = Match()

    def __init__(self, table_id=Table.OFPTT_ALL, out_port=PortNo.OFPP_ANY,
                 out_group=Group.OFPG_ANY, cookie=0, cookie_mask=0,
                 match=None):
        """Create a AggregateStatsRequest with the optional parameters below.

        Args:
            table_id (int): ID of table to read (from ofp_table_stats)
                OFPTT_ALL for all tables.
            out_port (int): Require matching entries to include this as an
                output port. A value of OFPP_ANY indicates no restriction.
            out_group (int): Require matching entries to include this as an
                output group. A value of OFPG_ANY indicates no restriction.
            cookie (int): Require matching entries to contain this cookie value
            cookie_mask (int): Mask used to restrict the cookie bits that must
                match. A value of 0 indicates no restriction.
            match (~pyof.v0x05.common.flow_match.Match):
                Fields to match. Variable size
        """
        super().__init__()
        self.table_id = table_id
        self.out_port = out_port
        self.out_group = out_group
        self.cookie = cookie
        self.cookie_mask = cookie_mask
        self.match = Match() if match is None else match


class FlowStatsRequest(GenericStruct):
    """Body for ofp_stats_request of type OFPST_FLOW."""

    table_id = UBInt8()
    #: Align to 32 bits.
    pad = Pad(3)
    out_port = UBInt32()
    out_group = UBInt32()
    pad2 = Pad(4)
    cookie = UBInt64()
    cookie_mask = UBInt64()
    match = Match()

    def __init__(self, table_id=Table.OFPTT_ALL, out_port=PortNo.OFPP_ANY,
                 out_group=Group.OFPG_ANY, cookie=0, cookie_mask=0,
                 match=None):
        """Create a FlowStatsRequest with the optional parameters below.

        Args:
            table_id (int): ID of table to read (from pyof_table_stats)
                0xff for all tables or 0xfe for emergency.
            out_port (:class:`int`, :class:`~pyof.v0x05.common.port.PortNo`):
                Require matching entries to include this as an output port.
                A value of :attr:`.PortNo.OFPP_ANY` indicates no restriction.
            out_group: Require matching entries to include this as an output
                group. A value of :attr:`Group.OFPG_ANY` indicates no
                restriction.
            cookie: Requires matching entries to contain this cookie value
            cookie_mask: Mask used to restrict the cookie bits that must match.
                A value of 0 indicates no restriction.
            match (~pyof.v0x05.common.flow_match.Match): Fields to match.
        """
        super().__init__()
        self.table_id = table_id
        self.out_port = out_port
        self.out_group = out_group
        self.cookie = cookie
        self.cookie_mask = cookie_mask
        self.match = Match() if match is None else match


class PortStatsRequest(GenericStruct):
    """Body for ofp_stats_request of type OFPST_PORT."""

    port_no = UBInt32()
    #: Align to 64-bits.
    pad = Pad(4)

    def __init__(self, port_no=PortNo.OFPP_ANY):
        """Create a PortStatsRequest with the optional parameters below.

        Args:
            port_no (:class:`int`, :class:`~pyof.v0x05.common.port.PortNo`):
                :attr:`StatsType.OFPST_PORT` message must request statistics
                either for a single port (specified in ``port_no``) or for all
                ports (if ``port_no`` == :attr:`.PortNo.OFPP_ANY`).
        """
        super().__init__()
        self.port_no = port_no


class QueueStatsRequest(GenericStruct):
    """Implements the request body of a ``port_no``."""

    port_no = UBInt32()
    queue_id = UBInt32()

    def __init__(self, port_no=PortNo.OFPP_ANY, queue_id=0xffffffff):
        """Create a QueueStatsRequest with the optional parameters below.

        Args:
            port_no (:class:`int`, :class:`~pyof.v0x05.common.port.Port`):
                All ports if :attr:`.Port.OFPP_ALL`.
            queue_id (int): All queues if OFPQ_ALL (``0xfffffff``).
        """
        super().__init__()
        self.port_no = port_no
        self.queue_id = queue_id


class GroupStatsRequest(GenericStruct):
    """Body of OFPMP_GROUP request."""

    #: Group id. All groups is OFPG_ALL
    group_id = UBInt32()
    #: Align to 64 bits
    pad = Pad(4)

    def __init__(self, group_id=Group.OFPG_ALL):
        """Create a GroupStatsRequest with the optional parameters below.

        Args:
            group_id(int): ID of group to read. OFPG_ALL to request informatio
                for all groups.
        """
        super().__init__()
        self.group_id = group_id


class MeterMultipartRequest(GenericStruct):
    """MeterMultipartRequest structure.

    This class represents the structure for ofp_meter_multipart_request.
    This structure is a body of OFPMP_METER and OFPMP_METER_CONFIG requests.
    """

    # Meter instance, or OFPM_ALL.
    meter_id = UBInt32()

    # Align to 64 bits.
    pad = Pad(4)

    def __init__(self, meter_id=Meter.OFPM_ALL):
        """Create a MeterMultipartRequest with the optional parameters below.

        Args:
            meter_id(Meter): Meter Indentify.The value Meter.OFPM_ALL is used
                             to refer to all Meters on the switch.
        """
        super().__init__()
        self.meter_id = meter_id


class FlowMonitorRequest(GenericStruct):
    """
    Body for ofp_multipart_request of type OFPMP_FLOW_MONITOR.

     The OFPMP_FLOW_MONITOR request’s body consists of an array of zero or more
     instances of this structure. The request arranges to monitor the flows
     that match the specified criteria, which are interpreted in the same way as
     for OFPMP_FLOW.

    ’id’ identifies a particular monitor for the purpose of allowing it to be
     canceled later with OFPFMC_DELETE. ’id’ must be unique among
     existing monitors that have not already been canceled.

    """
    #: Controller-assigned ID for this monitor
    monitor_id = UBInt32()
    #: Required output port, if not OFPP_ANY
    out_port = UBInt32(enum_ref=PortNo)
    #: Required group number, if not OFPG_ANY
    out_group = UBInt32(enum_ref=Group)
    #: OFPFMF_*
    flags = UBInt16(enum_ref=FlowMonitorFlags)
    #: One table’s ID or OFPTT_ALL (all tables)
    table_id = UBInt8(enum_ref=Table)
    #: One of OFPFMC_*
    command = UBInt8(enum_ref=FlowMonitorCommand)
    #: Fields to match. Variable size
    match = Match()

    def __init__(self, monitor_id=None, out_port=PortNo.OFPP_ANY, out_group=Group.OFPG_ANY, flags=FlowMonitorFlags,
                 table_id=Table.OFPTT_ALL,
                 command=FlowMonitorCommand, match=None):
        """
        Create a FlowStatsRequest with the optional parameters below.

        Args:
            monitor_id (int): uniquely identifies a monitor for a specific controller connection within a switch
            (from pyof_table_stats)
                0xff for all tables or 0xfe for emergency.
            out_port (:class:`int`, :class:`~pyof.v0x05.common.port.PortNo`):
                Require matching entries to include this as an output port.
                A value of :attr:`.PortNo.OFPP_ANY` indicates no restriction.
            out_group: Require matching entries to include this as an output
                group. A value of :attr:`Group.OFPG_ANY` indicates no
                restriction.
            table_id (int): ID of table to read (from pyof_table_stats)
                0xff for all tables or 0xfe for emergency.
            command: defines what operation must be done on that monitor
            match (~pyof.v0x05.common.flow_match.Match): Fields to match.
        """
        super().__init__()
        self.monitor_id = monitor_id
        self.out_port = out_port
        self.out_group = out_group
        self.flags = flags
        self.table_id = table_id
        self.command = command
        self.match = Match() if match is None else match
