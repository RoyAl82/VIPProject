""" Defines Bundle Add message."""

# System imports

from pyof.foundation.base import GenericMessage
from pyof.foundation.basic_types import UBInt32, UBInt16, FixedTypeList, Pad
from pyof.v0x05.common.header import Header, Type
from pyof.v0x05.controller2switch.bundle_ctrl import BundleFlags, BundlePropHeader


class ListOfBundleProperties(FixedTypeList):
    """List of BundleProperties.

    Represented by instances of BundlePropHeader.
    """

    def __init__(self, items=None):
        """Create a ListOfBundleProperties with the optional parameters below.

        Args:
            items (|BundlePropHeader_v0x05|): Instance or a list of instances.
        """
        super().__init__(pyof_class=BundlePropHeader, items=items)


class BundleAddMsg(GenericMessage):
    """ Message structure for OFPT_BUNDLE_ADD_MESSAGE.
        Adding a message in a bundle is done with"""

    header = Header(message_type=Type.OFPT_BUNDLE_ADD_MESSAGE)
    #: Identify the bundle
    bundle_id = UBInt32()
    #: Align to 64 bits
    pad = Pad()
    #: Bitmap of OFPBF_* flags.
    flags = UBInt16(enum_ref=BundleFlags)
    #: Message added to the bundle
    message = Header()

    """ If there is one property or more, ’message’ is followed by:
       Exactly (message.length + 7)/8*8 - (message.length) (between 0 and 7)
       bytes of all-zero bytes"""

    #: Bundle Property list
    property = ListOfBundleProperties()

    def __init__(self, xid=None, bundle_id=None, flags=BundleFlags, message=None, properties=None):
        """Assign parameters to object attributes.

        Args:
            xid (int): :class:`~pyof.v0x05.common.header.Header`'s xid.
                Defaults to random.
            bundle_id (int): ID of the bundle. A 32 bit number chosen by the controller. The bundle
            identifier should be a bundle that has been previously opened and not yet closed
            flags (int): Bitmap of OFPBF_* flags
            message :a OpenFlow message to be added to the bundle, it can be any OpenFlow message that
            the switch can support in a bundle. The field xid in the message must be identical to the field xid of
            the OFPT_BUNDLE_ADD_MESSAGE message.

        """
        super().__init__(xid)
        self.bundle_id = bundle_id
        self.flags = flags
        self.message = message
        self.properties = properties
