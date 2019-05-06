""" Defines Flow Table Modification message."""

# System imports

from enum import IntEnum

from pyof.foundation.base import GenericBitMask, GenericMessage, GenericStruct
from pyof.foundation.basic_types import Pad, UBInt8, UBInt32, UBInt16, FixedTypeList
from pyof.v0x05.common.header import Header, Type

# Third-party imports

__all__ = ('Table', 'TableMod', 'TableModPropType', 'TableModPropHeader', 'TableConfig', 'TableModPropEviction',
           'TableModPropEvictionFlag')


# Enums


class Table(IntEnum):
    """Table numbering. Tables can use any number up to OFPT_MAX."""

    #: Last usable table number.
    OFPTT_MAX = 0xfe
    # Fake tables.
    #: Wildcard table used for table config, flow stats and flow deletes.
    OFPTT_ALL = 0xff


class TableModPropType(IntEnum):
    """Table Mod property types"""

    #: Eviction property
    OFPTMPT_EVICTION = 0x2
    #: Vacancy property
    OFPTMPT_VACANCY = 0x3
    #: Experimenter
    OFPTMPT_EXPERIMENTER = 0xFFFF


# Classes


class TableModPropEvictionFlag(GenericBitMask):
    """Eviction flags"""

    #: Using other factors
    OFPTMPEF_OTHER = 1 << 0
    #: Using flow entry importance
    OFPTMPEF_IMPORTANCE = 1 << 1
    #: Using flow entry lifetime
    OFPTMPEF_LIFETIME = 1 << 2


class TableConfig(GenericBitMask):
    """Flags to configure the table"""

    #: Deprecated bits
    OFPTC_DEPRECATED_MASK = 3
    #: Authorise table to evict flows
    OFPTC_EVICTION = 1 << 2
    #: Enable vacancy events
    OFPTC_VACANCY_EVENTS = 1 << 3


class TableModPropHeader(GenericStruct):
    """Common header for all Table Mod Properties"""

    #: One of OFPTMPT_*
    type = UBInt16(enum_ref=TableModPropType)
    #: Length in bytes of this property
    length = UBInt16()

    def __init__(self, type=None, length=None):
        super().__init__()
        self.type = type
        self.length = length


class TableModPropEviction(GenericStruct):
    """Eviction table mod Property. Mostly used in OFPMP_TABLE_DESC replies"""

    #: OFPTMPT_EVICTION
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()
    #: Bitmap of OFPTMPEF_* flags
    flags = UBInt32()

    def __init__(self, type=TableModPropType.OFPTMPT_EVICTION, length=None, flags=None):
        super().__init__()
        self.type = type
        self.length = length
        self.flags = flags


class TableModPropVacancy(GenericStruct):
    """Vacancy table mod property"""

    #: OFPTMPT_VACANCY
    type = UBInt16()
    #: Length in bytes of this property
    length = UBInt16()
    #: Vacancy threshold when space decreases (%)
    vacancy_down = UBInt8()
    #: Vacancy threshold when space increases (%)
    vacancy_up = UBInt8()
    #: Current vacancy (%) - only in ofp_table_desc
    vacancy = UBInt8()
    #: Align to 64 bits
    pad = Pad(1)

    def __init__(self, type=TableModPropType.OFPTMPT_VACANCY, length=None, vacancy_down=None, vacancy_up=None,
                 vacancy=None):
        super().__init__()
        self.type = type
        self.length = length
        self.vacancy_down = vacancy_down
        self.vacancy_up = vacancy_up
        self.vacancy = vacancy


class TableModPropExperimenter(GenericStruct):
    """Experimenter table mod property"""

    #: OFPTMPT_EXPERIMENTER
    type = UBInt16(TableModPropType.OFPTMPT_EXPERIMENTER)
    #: Length in bytes of this property
    length = UBInt16()
    #: Experimenter ID which takes the same
    # form as in struct
    # ofp_experimenter_header.
    experimenter = UBInt32()
    #: Experimenter defined
    exp_type = UBInt32()
    #: Followed by: Exactly (length - 12) bytes containing the experimenter data, then
    # Exactly (length + 7)/8*8 - (length) (between 0 and 7)
    # bytes of all-zero bytes
    experimenter_data = UBInt32()

    def __int__(self, type=Type.OFPRPT_EXPERIMENTER, length=None, experimenter=None, exp_type=None,
                experimenter_data=None):
        self.type = type
        self.length = length
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data


class TableMod(GenericMessage):
    """Configure/Modify behavior of a flow table."""

    #: class:`~pyof.v0x05.common.action.ActionHeader`: OpenFlow Header
    header = Header(message_type=Type.OFPT_TABLE_MOD)
    #: ID of the table, OFPTT_ALL indicates all tables
    table_id = UBInt8()
    #: Pad to 32 bits
    pad = Pad(3)
    #: Bitmap of OFPTC_* flags
    config = UBInt32()
    #: Table Mod Property list
    properties = FixedTypeList(TableModPropHeader)

    def __init__(self, xid=None, table_id=Table.OFPTT_ALL, config=3, properties=None):
        """Assing parameters to object attributes.

        Args:
            xid (int): :class:`~pyof.v0x05.common.header.Header`'s xid.
                Defaults to random.
            table_id (int): ID of the table, OFPTT_ALL indicates all tables.
            config (int): Bitmap of OFPTC_* flags
        """

        super().__init__(xid)
        self.table_id = table_id
        # This is reserved for future used. The default value is the only valid
        # one from the Enum.
        self.config = config
        self.properties = properties
