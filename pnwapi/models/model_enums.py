from enum import Enum


class ContinentEnum(str, Enum):
    NORTH_AMERICA = "na"
    SOUTH_AMERICA = "sa"
    EUROPE = "eu"
    AFRICA = "af"
    ASIA = "as"
    AUSTRALIA = "au"
    ANTARCTICA = "an"


class WarPolicyEnum(str, Enum):
    ATTRITION = "ATTRITION"
    TURTLE = "TURTLE"
    BLITZKRIEG = "BLITZKRIEG"
    FORTRESS = "FORTRESS"
    MONEYBAGS = "MONEYBAGS"
    PIRATE = "PIRATE"
    TACTICIAN = "TACTICIAN"
    GUARDIAN = "GUARDIAN"
    COVERT = "COVERT"
    ARCANE = "ARCANE"


class DomesticPolicyEnum(str, Enum):
    MANIFEST_DESTINY = "MANIFEST_DESTINY"
    OPEN_MARKETS = "OPEN_MARKETS"
    TECHNOLOGICAL_ADVANCEMENT = "TECHNOLOGICAL_ADVANCEMENT"
    IMPERIALISM = "IMPERIALISM"
    URBANIZATION = "URBANIZATION"
    RAPID_EXPANSION = "RAPID_EXPANSION"


class ColorEnum(str, Enum):
    AQUA = "aqua"
    BLACK = "black"
    BLUE = "blue"
    BROWN = "brown"
    GREEN = "green"
    LIME = "lime"
    MAROON = "maroon"
    OLIVE = "olive"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"
    BEIGE = "beige"
    GRAY = "gray"


class WarTypeEnum(str, Enum):
    ORDINARY = "ORDINARY"
    ATTRITION = "ATTRITION"
    RAID = "RAID"


class TreatyTypeEnum(str, Enum):
    NPT = "NPT"
    PROTECTORATE = "Protectorate"
    NAP = "NAP"
    PIAT = "PIAT"
    ODP = "ODP"
    ODoAP = "ODoAP"
    MDP = "MDP"
    MDoAP = "MDoAP"


class WarAttackTypeEnum(str, Enum):
    GROUND = "GROUND"
    AIR_INFRA = "AIRVINFRA"
    AIR_SOLDIERS = "AIRVSOLDIERS"
    AIR_TANKS = "AIRVTANKS"
    AIR_MONEY = "AIRVMONEY"
    AIR_AIR = "AIRVAIR"
    NAVAL = "NAVAL"
    MISSILE = "MISSILE"
    MISSILE_FAIL = "MISSILE_FAIL"
    NUKE = "NUKE"
    NUKE_FAIL = "NUKE_FAIL"
    FORTIFY = "FORTIFY"
    PEACE = "PEACE"
    VICTORY = "VICTORY"
    ALLIANCELOOT = "ALLIANCELOOT"


class WarAttackOutcomeEnum(int, Enum):
    IMMENSE_TRIUMPH = 3
    MODERATE_SUCCESS = 2
    PYRRHIC_VICTORY = 1
    UTTER_FAILURE = 0


class BankRecordSenderTypeEnum(int, Enum):
    NATION = 1
    ALLIANCE = 2
