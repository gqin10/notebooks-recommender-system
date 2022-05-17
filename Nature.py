from enum import Enum


class Nature(Enum):
    NEAR = "near"
    EQUAL = "equal"
    MORE = "more"
    LESS = "less"


attribute_nature = {
    'brand': Nature.EQUAL,
    'cpu': Nature.EQUAL,
    'gpu': Nature.EQUAL,
    'storage': Nature.MORE,
    'ram': Nature.MORE,
    'os': Nature.EQUAL,
    'camera': Nature.EQUAL,
    'price': Nature.LESS,
    'weight': Nature.LESS,
    'screen_size': Nature.NEAR
}
