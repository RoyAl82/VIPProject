"""Hello message tests."""
import unittest
from tests.test_struct import TestStruct
import pyof.v0x05.symmetric.hello as Hello
import random
from pyof.foundation.basic_types import UBInt32, UBInt16, TypeList, BinaryData


class TestHello(unittest.TestCase):

    def test_hello_version_bitmap(self):
        """
        Test if the bitmap version is 1

        :return: None
        """

        self.assertEqual(1, Hello.HelloElemType.OFPHET_VERSIONBITMAP)

    def test_hello_elem_header(self):
        """
        Testing the HelloElemHeader one element.

        :return: None
        """

        test_value = b'\x00\x01\x00\x04'

        self.test_object_elem_header = Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP, 4)
        value = self.test_object_elem_header.pack()

        self.assertEqual(test_value,value)

    def test_hello_list_of_hello_elements(self):
        """
        Testing the HelloElemHeader more than one element.
        Testing the pack value return by the ListOfHelloElements more than one element.
        :return: None
        """

        test_value = b'\x00\x01\x00\x04\x00\x01\x00\x04\x00\x01\x00\x04'

        self.test_object_list_of_hello_elem = Hello.ListOfHelloElements()

        self.test_list_of_elem = [Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4),
                               Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4),
                               Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4)]

        self.test_object_list_of_hello_elem.__init__(items=self.test_list_of_elem)

        val = self.test_object_list_of_hello_elem.pack()

        self.assertEqual(test_value, val)

    def test_hello_list_of_hello_element(self):
        """
        Testing the HelloElemHeader one element.
        Testing the pack value return by the ListOfHelloElements one element.

        :return: None
        """
        print()
        print('')
        test_value = b'\x00\x01\x00\x04'
        self.test_object_list_of_hello_elem = Hello.ListOfHelloElements()

        self.test_object_list_of_hello_elem.__init__(Hello.HelloElemHeader(Hello.HelloElemType.OFPHET_VERSIONBITMAP,4))

        val = self.test_object_list_of_hello_elem.pack()

        self.assertEqual(test_value, val)

    def test_hello(self):
        """
        Testing the Hello Message pack.

        :return: None
        """

        _NUM_OF_TEST = 25

        for i in range(0, _NUM_OF_TEST):
            random.seed()

            test_val = i + random.randint(0,100)
            test_value = b'\x05\x00\x00\x08'+ UBInt32(test_val).pack()
            self.test_object_hello = Hello.Hello(test_val)

            val = self.test_object_hello.pack()
            self.assertEqual(test_value, val)

    def test_hello_elem_version_bitmap(self):
        """
        Testing the class HelloElemVersionBitmap.
        Test support 2 versions (ver 1 = 0x01 and ver 1.3 = 0x04)
        Testing 2 version support ver 1 and ver 1.3 based on the specification's example.

        :return: None
        """

        ver1 = 0x01
        ver3 = 0x04
        ver = ver1 << ver3
        ver = ver | 2

        test_val = b'\x00\x01\x00\x08\x00\x00\x00\x12'
        self.test_object_hello_elem_version = Hello.HelloElemVersionBitmap(UBInt16(8), UBInt32(ver).pack())
        val = self.test_object_hello_elem_version.pack()

        self.assertEqual(test_val,val)






# UNCOMMENT to used the previous tests
# class TestHelloStruct(TestStruct):
#     """Hello message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_hello')
#         super().set_raw_dump_object(Hello.Hello, xid=1)
#         super().set_minimum_size(8)




if __name__ == '__main__':
    unittest.main()