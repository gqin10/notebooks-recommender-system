from enum import Enum
from Nature import Nature


class Attribute(Enum):
    BRAND = "brand"
    CPU = "cpu"
    GPU = "gpu"
    STORAGE = "storage"
    RAM = "ram"
    OS = "os"
    CAMERA = "camera"
    PRICE = "price"
    WEIGHT = "weight"
    SCREEN_SIZE = "screen_size"


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

spec = {
    'brand': ['acer', 'asus', 'dell', 'hp', 'huawei', 'lenovo', 'microsoft', 'msi'],
    'cpu': ['celeron', 'athlon', 'pentium', 'i3', 'ryzen 3', 'i5', 'ryzen 5', 'i7', 'ryzen 7', 'ryzen 9'],
    'gpu': ['radeon', 'iris', 'mx', 'gtx', 'rtx'],
    'storage': [32, 64, 128, 256, 512, 1024, 2048],
    'ram': [2, 4, 8, 16, 32, 64],
    'os': ['os', '10', '11']
}
