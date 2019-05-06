"""Test of Port class from common module."""
from pyof.v0x05.common.port import Port
from tests.test_struct import TestStruct


class TestPort(TestStruct):
    """Port structure tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x05', 'port')
        super().set_raw_dump_object(Port)
        super().set_minimum_size(64)
