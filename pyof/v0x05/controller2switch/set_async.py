"""Define SetAsync message.

Sets whether a controller should receive a given asynchronous message that is
generated by the switch.
"""

# System imports

# Third-party imports

# Local imports
from pyof.v0x05.common.header import Type
from pyof.v0x05.controller2switch.common import AsyncConfig

__all__ = ('SetAsync',)


class SetAsync(AsyncConfig):
    """SetAsync message.

    Sets whether a controller should receive a given asynchronous message that
    is generated by the switch.
    """

    def __init__(self, xid=None, packet_in_mask1=None, packet_in_mask2=None,
                 port_status_mask1=None, port_status_mask2=None,
                 flow_removed_mask1=None, flow_removed_mask2=None):
        """Set attributes for SetAsync message.

        Args:
            xid (int): xid to be used on the message header.
            packet_in_mask1 (|PacketInReason_v0x05|):
                    A instance of PacketInReason
            packet_in_mask2 (|PacketInReason_v0x05|):
                    A instance of PacketInReason
            port_status_mask1 (|PortReason_v0x05|):
                    A instance of PortReason
            port_status_mask2 (|PortReason_v0x05|):
                    A instance of PortReason
            flow_removed_mask1 (|FlowRemoved_v0x05|):
                    A instance of FlowRemoved.
            flow_removed_mask2 (|FlowRemoved_v0x05|):
                    A instance of FlowRemoved.
        """
        super().__init__(xid, packet_in_mask1, packet_in_mask2,
                         port_status_mask1, port_status_mask2,
                         flow_removed_mask1, flow_removed_mask2)
        self.header.message_type = Type.OFPT_SET_ASYNC