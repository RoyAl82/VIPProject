"""Testing v0x05 error message class."""
from pyof.v0x05.symmetric.error_message import ErrorMsg
import pyof.v0x05.symmetric.error_message as Error
from tests.test_struct import TestStruct
from pyof.foundation.basic_types import UBInt8,UBInt16,UBInt32,UBInt64,BinaryData
import unittest
import random

#
# class TestErrorMsg(TestStruct):
#     """ErroMsg message tests (also those in :class:`.TestDump`)."""
#
#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         super().setUpClass()
#         super().set_raw_dump_file('v0x05', 'ofpt_error_msg')
#         super().set_raw_dump_object(ErrorMsg, xid=1, error_type=1, code=1)
#         super().set_minimum_size(12)


class TestErrorMessageTestCases(unittest.TestCase):
    """
    This class will test the Error Message classes and codes with assert tests.
    """

    MAX_ERROR_TYPE_VALUE = 18

    MAX_BAD_ACTION_CODE_VALUE = 15
    MAX_BAD_INSTRUCTION_CODE_VALUE = 9
    MAX_BAD_MATCH_CODE_VALUE = 11
    MAX_BAD_REQUEST_CODE_VALUE = 15
    MAX_FLOW_MOD_FAILED_CODE_VALUE = 10
    MAX_GROUP_MOD_FAILED_CODE_VALUE = 14
    MAX_HELLO_FAILED_CODE_VALUE = 1
    MAX_METER_MOD_FAILED_CODE_VALUE = 11
    MAX_PORT_MOD_FAILED_CODE_VALUE = 4
    MAX_QUEUE_OP_FAILED_CODE_VALUE = 2
    MAX_ROLE_REQUEST_FAILED_CODE_VALUE = 2
    MAX_SWITCH_CONFIG_FAILED_CODE_VALUE = 2
    MAX_TABLE_FEATURE_FAILED_CODE_VALUE = 5
    MAX_TABLE_MOD_FAILED_CODE_VALUE = 2
    MAX_BAD_PROPERTY_CODE_VALUE = 8
    MAX_ASYNC_CONFIG_FAILED_CODE_VALUE = 2
    MAX_FLOW_MONITOR_FAILED_CODE_VALUE = 7
    MAX_BUNDLE_FAILED_CODE_VALUE = 15
    MAX_EXPERIMENTER_VALUE = 0

    random.seed()

    def setUp(self):
        self.test_generic_failed_code = Error.GenericFailedCode
        self.test_bad_action_code = Error.BadActionCode
        self.test_bad_instruction_code = Error.BadInstructionCode
        self.test_bad_match_code = Error.BadMatchCode
        self.test_bad_request_code = Error.BadRequestCode
        self.test_error_type = Error.ErrorType
        self.test_flow_mod_failed_code = Error.FlowModFailedCode
        self.test_group_mod_failed_code = Error.GroupModFailedCode
        self.test_hello_failed_code = Error.HelloFailedCode
        self.test_meter_mod_failed_code = Error.MeterModFailedCode
        self.test_port_mod_failed_code = Error.PortModFailedCode
        self.test_queue_op_failed_code = Error.QueueOpFailedCode
        self.test_role_request_failed_code = Error.RoleRequestFailedCode
        self.test_switch_config_failed_code = Error.SwitchConfigFailedCode
        self.test_table_feature_failed_code = Error.TableFeaturesFailedCode
        self.test_table_mod_failed_code = Error.TableModFailedCode
        self.test_bad_property_code = Error.BadPropertyCode
        self.test_async_config_failed_code = Error.AsyncConfigFailedCode
        self.test_flow_monitor_failed_code = Error.FlowMonitorFailedCode
        self.test_bundle_failed_code = Error.BundleFailedCode
        self.test_error_message = Error.ErrorMsg()
        self.test_error_experimenter_message = Error.ErrorExperimenterMsg()

    def tearDown(self):
        pass

    def test_generic_failed_code_value(self):
        """
        Testing the Generic Failed Codes Values.
        This function will test the only code value for this enum class.
        :return: None
        """
        value = 0

        for elem in self.test_generic_failed_code:
            self.assertEqual(value, elem)

    def test_bad_action_code_value(self):
        """
        Testing the Bad Action Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0
        iter_given_code = self.test_bad_action_code.__iter__()
        length = self.test_bad_action_code.__len__()

        while value < self.MAX_BAD_ACTION_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BAD_ACTION_CODE_VALUE:
                value += 1

            length -= 1

    def test_bad_instruction_code_value(self):
        """
        Testing the Bad Instruction Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_bad_instruction_code.__iter__()
        length = self.test_bad_instruction_code.__len__()

        while value < self.MAX_BAD_INSTRUCTION_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BAD_INSTRUCTION_CODE_VALUE:
                value += 1

            length -= 1

    def test_bad_match_code_value(self):
        """
        Testing the Bad Match Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_bad_match_code.__iter__()
        length = self.test_bad_match_code.__len__()

        while value < self.MAX_BAD_MATCH_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BAD_MATCH_CODE_VALUE:
                value += 1

            length -= 1

    def test_bad_request_code_value(self):
        """
        Testing the Bad Request Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_bad_request_code.__iter__()
        length = self.test_bad_request_code.__len__()

        while value < self.MAX_BAD_REQUEST_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BAD_REQUEST_CODE_VALUE:
                value += 1

            length -= 1

    def test_error_type(self):
        """
        Testing the Error Types Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_error_type.__iter__()
        length = self.test_error_type.__len__()

        while value < self.MAX_ERROR_TYPE_VALUE or length > 0:

            if value == 18:
                value = 0xffff

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_ERROR_TYPE_VALUE:
                value += 1

            length -= 1

    def test_flow_mod_failed_code_value(self):
        """
        Testing the Flow Mod Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_flow_mod_failed_code.__iter__()
        length = self.test_flow_mod_failed_code.__len__()

        while value < self.MAX_FLOW_MOD_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_FLOW_MOD_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_group_mod_failed_code_value(self):
        """
        Testing the Group Mod Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_group_mod_failed_code.__iter__()
        length = self.test_group_mod_failed_code.__len__()

        while value < self.MAX_GROUP_MOD_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_GROUP_MOD_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_hello_failed_code_value(self):
        """
        Testing the Hello Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_hello_failed_code.__iter__()
        length = self.test_hello_failed_code.__len__()

        while value < self.MAX_HELLO_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_HELLO_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_meter_mod_failed_code_value(self):
        """
        Testing the Meter Mod Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_meter_mod_failed_code.__iter__()
        length = self.test_meter_mod_failed_code.__len__()

        while value < self.MAX_METER_MOD_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_METER_MOD_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_port_mod_failed_code_value(self):
        """
        Testing the Port Mod Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_port_mod_failed_code.__iter__()
        length = self.test_port_mod_failed_code.__len__()

        while value < self.MAX_PORT_MOD_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_PORT_MOD_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_queue_op_failed_code_value(self):
        """
        Testing the Queue Op Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """
        value = 0

        iter_given_code = self.test_queue_op_failed_code.__iter__()
        length = self.test_queue_op_failed_code.__len__()

        while value < self.MAX_QUEUE_OP_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_QUEUE_OP_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_role_request_failed_code_value(self):
        """
        Testing the Role Request Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """
        value = 0

        iter_given_code = self.test_role_request_failed_code.__iter__()
        length = self.test_role_request_failed_code.__len__()

        while value < self.MAX_ROLE_REQUEST_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_ROLE_REQUEST_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_switch_config_failed_code_value(self):
        """
        Testing the Switch Config Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_switch_config_failed_code.__iter__()
        length = self.test_switch_config_failed_code.__len__()

        while value < self.MAX_SWITCH_CONFIG_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_SWITCH_CONFIG_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_table_feature_failed_code_value(self):
        """
        Testing the Table Feature Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_table_feature_failed_code.__iter__()
        length = self.test_table_feature_failed_code.__len__()

        while value < self.MAX_TABLE_FEATURE_FAILED_CODE_VALUE or length > 0:

            if value == 2:
                value = 5

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_TABLE_FEATURE_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_table_mod_failed_code_value(self):
        """
        Testing the Table Mod Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_table_mod_failed_code.__iter__()
        length = self.test_table_mod_failed_code.__len__()

        while value < self.MAX_TABLE_MOD_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_TABLE_MOD_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_bad_property_code_value(self):
        """
        Testing the Bad Property Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_bad_property_code.__iter__()
        length = self.test_bad_property_code.__len__()

        while value < self.MAX_BAD_PROPERTY_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BAD_PROPERTY_CODE_VALUE:
                value += 1

            length -= 1

    def test_async_config_failed_code_value(self):
        """
        Testing the Async Config Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_async_config_failed_code.__iter__()
        length = self.test_async_config_failed_code.__len__()

        while value < self.MAX_ASYNC_CONFIG_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_ASYNC_CONFIG_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_flow_monitor_failed_code_value(self):
        """
        Testing the Flow Monitor Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_flow_monitor_failed_code.__iter__()
        length = self.test_flow_monitor_failed_code.__len__()

        while value < self.MAX_FLOW_MONITOR_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_FLOW_MONITOR_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_bundle_failed_code_value(self):
        """
        Testing the Bundle Failed Codes Values.
        This function will test all code values for this enum class.
        :return: None
        """

        value = 0

        iter_given_code = self.test_bundle_failed_code.__iter__()
        length = self.test_bundle_failed_code.__len__()

        while value < self.MAX_BUNDLE_FAILED_CODE_VALUE or length > 0:

            self.assertEqual(value, iter_given_code.__next__())

            if value < self.MAX_BUNDLE_FAILED_CODE_VALUE:
                value += 1

            length -= 1

    def test_error_message_header_hello_failed_codes(self):
        """
        Testing the header HelloFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """
        error_type = 0
        error_type_value = Error.ErrorType.OFPET_HELLO_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_HELLO_FAILED_CODE_VALUE or length > 0:

            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_HELLO_FAILED_CODE_VALUE:
                error_code += 1

            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bad_request_codes(self):
        """
        Testing the header BadRequestCodes.
        This function will test all code values for this enum class.
        :return: None
        """
        error_type = 1
        error_type_value = Error.ErrorType.OFPET_BAD_REQUEST

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BAD_REQUEST_CODE_VALUE or length > 0:

            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BAD_REQUEST_CODE_VALUE:
                error_code += 1

            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bad_action_codes(self):
        """
        Testing the header BadActionCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 2
        error_type_value = Error.ErrorType.OFPET_BAD_ACTION

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BAD_ACTION_CODE_VALUE or length > 0:

            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BAD_ACTION_CODE_VALUE:
                error_code += 1

            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bad_instruction_codes(self):
        """
        Testing the header BadInstructionCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 3
        error_type_value = Error.ErrorType.OFPET_BAD_INSTRUCTION

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BAD_INSTRUCTION_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BAD_INSTRUCTION_CODE_VALUE:
                error_code += 1

            length -= 1
            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bad_match_codes(self):
        """
        Testing the header BadMatchCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 4
        error_type_value = Error.ErrorType.OFPET_BAD_MATCH

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BAD_MATCH_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BAD_MATCH_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_flow_mod_failed_codes(self):
        """
        Testing the header FlowModFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 5
        error_type_value = Error.ErrorType.OFPET_FLOW_MOD_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_FLOW_MOD_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_FLOW_MOD_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_group_mod_failed_codes(self):
        """
        Testing the header GroupModFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 6
        error_type_value = Error.ErrorType.OFPET_GROUP_MOD_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_GROUP_MOD_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_GROUP_MOD_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1
            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_port_mod_failed_codes(self):
        """
        Testing the header PortModFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 7
        error_type_value = Error.ErrorType.OFPET_PORT_MOD_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_PORT_MOD_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_PORT_MOD_FAILED_CODE_VALUE:
                error_code += 1

            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_table_mod_failed_codes(self):
        """
        Testing the header TableModFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 8
        error_type_value = Error.ErrorType.OFPET_TABLE_MOD_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_TABLE_MOD_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_TABLE_MOD_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_queue_op_failed_codes(self):
        """
        Testing the header QueueOpFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 9
        error_type_value = Error.ErrorType.OFPET_QUEUE_OP_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_QUEUE_OP_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_QUEUE_OP_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_switch_config_failed_codes(self):
        """
        Testing the header SwitchConfigFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 10
        error_type_value = Error.ErrorType.OFPET_SWITCH_CONFIG_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_SWITCH_CONFIG_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_SWITCH_CONFIG_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1
            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_role_request_failed_codes(self):
        """
        Testing the header RoleRequestFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 11
        error_type_value = Error.ErrorType.OFPET_ROLE_REQUEST_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_ROLE_REQUEST_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_ROLE_REQUEST_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_meter_mod_failed_codes(self):
        """
        Testing the header MeterModFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 12
        error_type_value = Error.ErrorType.OFPET_METER_MOD_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_METER_MOD_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_METER_MOD_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_table_features_failed_codes(self):
        """
        Testing the header TableFeaturesFailedCodes.
        This function will test all code values for this enum class.
        :return:  None
        """

        error_type = 13
        error_type_value = Error.ErrorType.OFPET_TABLE_FEATURES_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_TABLE_FEATURE_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            if error_code == 2:
                error_code = 5

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_TABLE_FEATURE_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bad_property_codes(self):
        """
        Testing the header BadPropertyCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 14
        error_type_value = Error.ErrorType.OFPET_BAD_PROPERTY

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BAD_PROPERTY_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BAD_PROPERTY_CODE_VALUE:
                error_code += 1
            length -= 1
            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_async_config_failed_codes(self):
        """
        Testing the header AsyncConfigFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 15
        error_type_value = Error.ErrorType.OFPET_ASYNC_CONFIG_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_ASYNC_CONFIG_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_ASYNC_CONFIG_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_flow_monitor_failed_codes(self):
        """
        Testing the header FlowMonitorFailedCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 16
        error_type_value = Error.ErrorType.OFPET_FLOW_MONITOR_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_FLOW_MONITOR_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_FLOW_MONITOR_FAILED_CODE_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_bundle_failed_codes(self):
        """
        Testing the header BundleFailed.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type = 17
        error_type_value = Error.ErrorType.OFPET_BUNDLE_FAILED

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_BUNDLE_FAILED_CODE_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_BUNDLE_FAILED_CODE_VALUE:
                error_code += 1

            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_message_header_experimenter_codes(self):
        """
        Testing the header ExperimenterCodes.
        This function will test all code values for this enum class.
        :return: None
        """

        error_type_value = Error.ErrorType.OFPET_EXPERIMENTER
        error_type = 0xffff

        error_code = 0

        iter_given_code = Error.ErrorType.get_class(error_type_value).__iter__()
        length = Error.ErrorType.get_class(error_type_value).__len__()

        while error_code < self.MAX_EXPERIMENTER_VALUE or length > 0:
            data = UBInt32(random.randint(2, 250)).pack()
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x10' + UBInt32(xid).pack() + UBInt16(error_type).pack() + \
                        UBInt16(error_code).pack() + data

            if error_code < self.MAX_EXPERIMENTER_VALUE:
                error_code += 1
            length -= 1

            test_object_error_messages = Error.ErrorMsg(xid, error_type_value, iter_given_code.__next__(), data).pack()

            self.assertEqual(test_value, test_object_error_messages)

    def test_error_experimenter_message(self):
        """
        Testing the Experimenter Message.
        This function will test all code values for this enum class.
        :return: None
        """
        MAX_VALUE = 5
        # Max number of IDs to be created in the test
        MAX_NUM_ID = 20

        type = 0xffff

        for id in range(0, MAX_NUM_ID):

            # Generate a random int number between 2 and 250
            exp_code = random.randint(2, 250)

            # Generate a random int number between 2 and 120 and then convert it in binary
            data = UBInt8(random.randint(2, 120)).pack()

            # Generate a random int number between 2 and 250
            xid = random.randint(2, 250)

            test_value = b'\x05\x01\x00\x11' + UBInt32(xid).pack() + UBInt16(type).pack() + \
                        UBInt16(exp_code).pack() + UBInt32(id).pack() + data

            self.test_error_experimenter_message.__init__(xid, exp_code, id, data)

            test_object_error_messages = self.test_error_experimenter_message.pack()

            self.assertEqual(test_value, test_object_error_messages)




if __name__ == '__main__':
    unittest.main()