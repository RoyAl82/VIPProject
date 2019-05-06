"""Flow Table Modification message."""
from enum import IntEnum

from pyof.foundation.base import GenericMessage, GenericBitMask
from pyof.foundation.basic_types import Pad, UBInt8, UBInt32, UBInt16, GenericStruct, FixedTypeList
from pyof.v0x05.common.header import Header, Type

__all__ = ('Table', 'TableConfig', 'TableModPropType', 'TableModPropEvictionFlag', 'TableMod', 'TableModPropHeader',
           'TableModPropEviction', 'TableModPropVacancy')


class Table(IntEnum):
    """Table numbering. Tables can use any number up to OFPT_MAX."""

    #: Last usable table number.
    OFPTT_MAX = 0xfe
    # Fake tables.
    #: Wildcard table used for table config, flow stats and flow deletes.
    OFPTT_ALL = 0xff


class TableConfig(GenericBitMask):
    """Flags to configure the table."""

    #:Deprecated bits.
    OFPTC_DEPRECATED_MASK = 3
    #: Authorise table to evict flows.
    OFPTC_EVICTION = 1 << 2
    #: Enable vacancy events.
    OFPTC_VACANCY_EVENTS = 1 << 3


class TableModPropType(IntEnum):
    """Table Mod property types"""

    #: Eviction property.
    OFPTMPT_EVICTION = 0x2
    #: Vacancy property.
    OFPTMPT_VACANCY = 0x3
    #: Experimenter property
    OFPTMPT_EXPERIMENTER = 0xffff


class TableModPropEvictionFlag(GenericBitMask):
    """Eviction flags."""

    #: Using other factors.
    OFPTMPEF_OTHER = 1 << 0
    #: Using flow entry importance.
    OFPTMPEF_IMPORTANCE = 1 << 1
    #: Using flow entry lifetime.
    OFPTMPEF_LIFETIME = 1 << 2


class TableModPropHeader(GenericStruct):
    """Common header for all Table Mod Properties."""

    #: One of OFPTMPT_*.
    type = UBInt16()
    #: Length in bytes of this property.
    length = UBInt16()

    def __int__(self, type=TableModPropType, length=None):
        self.type = type
        self.length = length


class TableMod(GenericMessage):
    """Configure/Modify behavior of a flow table."""

    header = Header(message_type=Type.OFPT_TABLE_MOD)
    #: ID of the table, OFPTT_ALL indicates all tables
    table_id = UBInt8()
    #: Pad to 32 bits
    pad = Pad(3)
    #: Bitmap of OFPTC_* flags
    config = UBInt32()
    #: Table Mod Property list
    properties = FixedTypeList(TableModPropHeader)

    def __init__(self, xid=None, table_id=Table.OFPTT_ALL, config=3, properties=TableModPropHeader):
        """Assign parameters to object attributes.

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


class TableModPropEviction(TableModPropHeader):
    """Eviction table mod Property. Mostly used in OFPMP_TABLE_DESC replies."""

    #: Bitmap of OFPTMPEF_* flags
    flags = UBInt32()

    def __init__(self, flags=TableModPropEvictionFlag):
        """Assign parameters to object attributes.

                Args:
                    length (UBInt16): Length in bytes of this property.
                    flags (UBInt32): Bitmap of OFPTMPEF_* flags.

                """
        super().type = TableModPropType.OFPTMPT_EVICTION
        self.flas = flags


class TableModPropVacancy(TableModPropHeader):
    """Vacancy table mod property"""

    #: OFPTMPT_VACANCY.
    type = TableModPropType.OFPTMPT_VACANCY
    #: Length in bytes of this property.
    length = UBInt16()
    #: Vacancy threshold when space decreases (%).
    vacancy_down = UBInt8()
    #: Vacancy threshold when space increases (%).
    vacancy_up = UBInt8()
    #: Current vacancy (%) - only in TableDesc.
    vacancy = UBInt8()
    #: Align to 64 bits.
    pad1 = Pad(1)

    def __init__(self, vacancy_down=None, vacancy_up=None, vacancy=None):
        super().type = TableModPropType.OFPTMPT_VACANCY

        self.vacancy_down = vacancy_down

        self.vacancy_up = vacancy_up

        self.vacancy = vacancy


class TableModPropExperimenter(TableModPropHeader):
    """Experimenter table mod property"""

    #: Experimenter ID which takes the same form as in struct experimenter_header
    experimenter = UBInt32()
    #: Experimenter defined.
    exp_type = UBInt32()

    """Followed by:
        - Exactly (length - 12) bytes containing the experimenter data, then
        - Exactly (length + 7)/ 8 * 8 - (length) (between 0 and 7) bytes of all-zero bytes.
    """
    experimenter_data = UBInt32()

    def __init__(self, experimenter=None, exp_type=None):
        """

        :param experimenter: (int) Experimenter ID which takes the same form as in struct experimenter_header
        :param exp_type: (int) Experimenter defined.
        """
        super().__init__(TableModPropType.OFPTMPT_EXPERIMENTER)

        self.experimenter = experimenter

        self.exp_type = exp_type
        super().length = len(self)
