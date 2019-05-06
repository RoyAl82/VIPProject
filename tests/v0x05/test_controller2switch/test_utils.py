"""
This class Generate Messages to test the unpack method of classes.
"""
import random
from pyof.foundation.basic_types import UBInt16,UBInt32, UBInt8, UBInt64, Pad
from pyof.foundation.base import GenericMessage
from pyof.v0x05.common.header import Type


class MessageGenerator():
    """
    Generate messages for test used only.
    """

    MAX_32BITS_VALUE = 1000
    MAX_8BITS_VALUE = 128
    MAX_16BITS_VALUE = 1000
    MAX_64BITS_VALUE = 1000
    MIN_NUM_OF_MESSAGE = 10
    MAX_NUM_OF_OXMTLV = 5
    MAX_NUM_OF_ACTIONS = 3

    random.seed()
    type_of_msg = Type
    listOfConfigMessage = list()
    max_num_of_mesg = random.randint(MIN_NUM_OF_MESSAGE, MIN_NUM_OF_MESSAGE * 2)
    xid = UBInt32()
    item = 0

    def generate_messages(self):
        """
        Generate Messages to be tested. All messages will be added to a list.
        :return: None
        """

        for index in range(0, self.max_num_of_mesg):

            version = b'\x05'
            msg_type = UBInt8(self.type_of_mesg).pack()

            if self.xid is None:
                self.xid = UBInt32(random.randint(0, self.MAX_32BITS_VALUE))

            if self.type_of_mesg == Type.OFPT_GET_CONFIG_REPLY:

                test_length = b'\x00\x00'

                test_header = version + msg_type + test_length + self.xid.pack()

                flags = UBInt16(random.randint(0, 3)).pack()

                miss_send = UBInt16(random.randint(0, 0xffe5)).pack()

                test_value = test_header + flags + miss_send

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + self.xid.pack()

                value = header + flags + miss_send

                self.item = (self.xid, value)

            elif self.type_of_mesg == Type.OFPT_PACKET_IN:

                test_length = b'\x00\x00'

                header = version + msg_type + test_length + self.xid.pack()

                buffer_id = UBInt32(random.randint(0, self.MAX_32BITS_VALUE)).pack()

                total_len = UBInt16(random.randint(0, self.MAX_16BITS_VALUE)).pack()

                reason = UBInt8(random.randint(0, 5)).pack()

                table_id = UBInt8(random.randint(0, self.MAX_8BITS_VALUE)).pack()

                cookie = UBInt64(random.randint(0, self.MAX_64BITS_VALUE)).pack()

                oxmtlv = b''

                for i in range(1, random.randint(1,self.MAX_NUM_OF_OXMTLV)):

                    oxm_class = UBInt16(0x8000).pack()
                    oxm_field_and_mask = UBInt8(0).pack()
                    oxm_length = UBInt8(0)
                    oxm_value = UBInt32(random.randint(1, self.MAX_32BITS_VALUE)).pack()

                    test_value = oxm_class + oxm_field_and_mask + oxm_length.pack()
                    oxm_length = UBInt8(len(test_value)).pack()
                    val = oxm_class + oxm_field_and_mask + oxm_length + oxm_value

                    oxmtlv += val

                match_type = UBInt16(1).pack()
                match_length = UBInt16(0)
                match_pad = UBInt32(0).pack()
                test_length = match_type + match_length.pack() + oxmtlv + match_pad

                match_length = UBInt16(len(test_length)).pack()

                matchVal = match_type + match_length + oxmtlv + match_pad

                test_value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + self.xid.pack()

                value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                self.item = (self.xid, value)

            elif self.type_of_mesg == Type.OFPT_ECHO_REPLY:

                test_length = b'\x00\x00'

                header = version + msg_type + test_length + self.xid.pack()

                buffer_id = UBInt32(random.randint(0, self.MAX_32BITS_VALUE)).pack()

                total_len = UBInt16(random.randint(0, self.MAX_16BITS_VALUE)).pack()

                reason = UBInt8(random.randint(0, 5)).pack()

                table_id = UBInt8(random.randint(0, self.MAX_8BITS_VALUE)).pack()

                cookie = UBInt64(random.randint(0, self.MAX_64BITS_VALUE)).pack()

                oxmtlv = b''

                for i in range(0, random.randint(1, self.MAX_NUM_OF_OXMTLV)):
                    oxm_class = UBInt16(0x8000).pack()
                    oxm_field_and_mask = UBInt8(0).pack()
                    oxm_length = UBInt8(0)
                    oxm_value = UBInt32(random.randint(1, self.MAX_32BITS_VALUE)).pack()

                    test_value = oxm_class + oxm_field_and_mask + oxm_length.pack()
                    oxm_length = UBInt8(len(test_value)).pack()
                    val = oxm_class + oxm_field_and_mask + oxm_length + oxm_value

                    oxmtlv += val

                match_type = UBInt16(1).pack()
                match_length = UBInt16(0)
                match_pad = UBInt32(0).pack()
                test_length = match_type + match_length.pack() + oxmtlv + match_pad

                match_length = UBInt16(len(test_length)).pack()

                matchVal = match_type + match_length + oxmtlv + match_pad

                test_value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + self.xid.pack()

                value = header + buffer_id + total_len + reason + table_id + cookie + matchVal

                self.item = (self.xid, value)

            elif self.type_of_mesg == Type.OFPT_PACKET_OUT:

                test_length = b'\x00\x00'

                header = version + msg_type + test_length + self.xid.pack()

                buffer_id = UBInt32(random.randint(0, self.MAX_32BITS_VALUE)).pack()

                in_port = UBInt32(random.randint(0xfffffffd,  0xffffffff)).pack()

                actions_len = UBInt16(0).pack()

                pad = b'\00\00\00\00\00\00'

                list_of_actions = b''

                for i in range(1, random.randint(1, self.MAX_NUM_OF_ACTIONS)):
                    random_type = random.randint(15, 27)

                    #: there is message 25 that needs revision
                    while random_type == 25:
                        random_type = random.randint(15, 27)

                    action_type = UBInt16(random_type).pack()
                    action_length = UBInt16(8)
                    action_val = b''

                    if random_type in (15, 23):
                        action_ttl = UBInt8(random.randint(0, self.MAX_8BITS_VALUE)).pack()
                        action_pad = b'\00\00\00'
                        action_val = action_ttl + action_pad
                    elif random_type in (16, 18, 24, 27):
                        action_val = b'\00\00\00\00'
                    elif random_type in (17, 19, 20, 26):
                        ethertype = UBInt16(random.randint(0, self.MAX_16BITS_VALUE)).pack()
                        action_pad = b'\00\00'
                        action_val = ethertype + action_pad
                    elif random_type in (21, 22):
                        action_id = UBInt32(random.randint(0, self.MAX_32BITS_VALUE)).pack()
                        action_val = action_id
                    elif random_type == 25:
                        oxm_class = UBInt16(0x8000).pack()
                        oxm_field_and_mask = UBInt8(random.randint(0, 39)).pack()
                        oxm_length = UBInt8(0).pack()
                        oxm_value = UBInt32(random.randint(1, self.MAX_32BITS_VALUE)).pack()

                        test_value = oxm_class + oxm_field_and_mask + oxm_length
                        oxm_length = UBInt8(len(test_value))
                        field = oxm_class + oxm_field_and_mask + oxm_length.pack() + oxm_value

                        #: For update the length on the message pack but the the unpack doesn't have the function
                        #: to unpack the padding

                        # update_length = 4 + len(field)
                        # overflow = update_length % 8
                        # action_length = update_length
                        # if overflow:
                        #     action_length = update_length + 8 - overflow
                        #
                        # padded_size = action_length
                        # padding_bytes = padded_size - len(field)
                        # if padding_bytes > 0:
                        #     field += Pad(padding_bytes).pack()

                        #action_length = UBInt16(len(action_type + action_length + field)).pack()

                        action_val = field

                    val = action_type + action_length.pack() + action_val
                    list_of_actions += val

                actions_len = UBInt16(len(list_of_actions)).pack()

                test_value = header + buffer_id + in_port + actions_len + pad + list_of_actions

                length = UBInt16(len(test_value)).pack()

                header = version + msg_type + length + self.xid.pack()

                value = header + buffer_id + in_port + actions_len + pad + list_of_actions

                self.item = (self.xid, value)

            else:
                pass

            self.listOfConfigMessage.append(self.item)

    def __init__(self, type_of_mesg=Type, xid=None):
        """
        Initialize the class with values and messages types
        :param type_of_mesg: Type of messsage to be generated
        :param xid: Expecific message XID
        """

        if type_of_mesg is None:
            raise Exception()

        self.type_of_mesg = type_of_mesg
        self.xid = xid

    def get(self, index=None):
        """
        This function will access the message's list and return the desire message
        :param index: an integer index to access the message list
        :return: binary type the desired message access with the index
        """

        if index is not None:
            return self.listOfConfigMessage[index]

    def length(self):
        """
        This function will return the number of messages in a list
        :return: an integer value with the length of the list
        """
        return self.listOfConfigMessage.__len__()


