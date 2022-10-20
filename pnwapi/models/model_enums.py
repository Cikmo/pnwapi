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
