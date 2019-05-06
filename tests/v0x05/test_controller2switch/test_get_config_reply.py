"""Config Reply message tests."""
import pyof.v0x05.controller2switch.get_config_reply as GetConfigReply
from tests.v0x05.test_controller2switch.test_utils import MessageGenerator, PrintTables
import unittest
from pyof.v0x05.common.header import Type


class TestGetConfigReply(unittest.TestCase):

    def test_getting_reply(self):

        print()
        print('Testing the GetConfigReply class.')

        values = MessageGenerator()
        values.__init__(Type.OFPT_GET_CONFIG_REPLY)
        values.generate_messages()

        for i in range(0, values.length()):

            (xid, val) = values.get(i)

            self.testObject = GetConfigReply.GetConfigReply(xid)
            self.testObject.unpack(val, 8)
            testValue = self.testObject.pack()
            print('Testing the unpack message expected value {} versus actual value {}'.format(val, testValue))
            self.assertEqual(val, testValue)



if __name__ == '__main__':
    unittest.main()
