"""Echo reply message tests."""
from pyof.v0x05.symmetric.echo_reply import EchoReply
from pyof.foundation.basic_types import UBInt32, UBInt16, UBInt8, BinaryData
from tests.test_struct import TestStruct
from tests.v0x05.test_controller2switch.test_utils import MessageGenerator
import unittest


class TestEchoReplyByCases(unittest.TestCase):
    """

    """

    def setUp(self):
        """

        :return: None
        """
        self.type = UBInt8(2)
        self.length = UBInt16(6)
        self.xid = UBInt32(23)
        self.data = BinaryData(b'001100111101')
        self.test_object = EchoReply()
        self.test_object.header.__init__(self.type,self.length,self.xid)
        self.test_object1 = EchoReply(23, b'001100111101')

    def test_echo_reply(self):
        """
        Testing the Echo Reply messages
        :return: None
        """

        self.assertEqual(self.type, self.test_object.header.message_type)
        self.assertEqual(self.length, self.test_object.header.length)
        self.assertEqual(self.xid, self.test_object.header.xid)
        self.assertEqual(self.data, self.test_object1.data)
        self.assertNotEqual(self.type, self.test_object1.header.message_type)


class TestEchoReply(TestStruct):
    """Echo reply message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x05', 'ofpt_echo_reply')
        super().set_raw_dump_object(EchoReply, xid=0)
        super().set_minimum_size(8)


if __name__ == 'main':
    unittest.main()