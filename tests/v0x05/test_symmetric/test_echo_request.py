"""Echo request message tests."""
from pyof.v0x05.symmetric.echo_request import EchoRequest
from pyof.foundation.basic_types import UBInt32, UBInt16, UBInt8, BinaryData
from tests.test_struct import TestStruct
import unittest


class TestEchoRequestByCases(unittest.TestCase):
    """
    Test the Echo Request message elements composition
    """

    def setUp(self):
        """

        :return: None
        """
        self.type = UBInt8(3)
        self.length = UBInt16(6)
        self.xid = UBInt32(23)
        self.data = BinaryData(b'001100111101')
        self.test_object = EchoRequest()
        self.test_object.header.__init__(self.type,self.length,self.xid)
        self.test_object1 = EchoRequest(23, b'001100111101')

    def test_echo_request_type(self):
        """
        Test the echo request type.
        :return: None
        """
        self.assertEqual(self.type, self.test_object.header.message_type)

    def test_echo_request_length(self):
        """
        Test the echo request length.
        :return: None
        """
        self.assertEqual(self.length, self.test_object.header.length)

    def test_echo_request_xid(self):
        """
        Test the echo request xid.
        :return: None
        """
        self.assertEqual(self.xid, self.test_object.header.xid)

    def test_echo_request_data(self):
        """
        Test the echo request data.
        :return: None
        """
        self.assertEqual(self.data, self.test_object1.data)



class TestEchoRequest(TestStruct):
    """Echo request message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x05', 'ofpt_echo_request')
        super().set_raw_dump_object(EchoRequest, xid=0)
        super().set_minimum_size(8)


if __name__ == '__main__':
    unittest.main()