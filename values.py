from enum import Enum

real_data_path: str = "./data/data/notebook_data.csv"
simulated_data_path: str = "./data/data/simulated_data.csv"

attribute_list = [
    'brand',
    'cpu',
    'gpu',
    'storage',
    'ram',
    'os',
    'camera',
    'price',
    'weight',
    'screen_size'
]


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


spec = {
    'brand': ['acer', 'asus', 'dell', 'hp', 'huawei', 'lenovo', 'microsoft', 'msi'],
    'cpu': ['celeron', 'athlon', 'pentium', 'i3', 'ryzen 3', 'i5', 'ryzen 5', 'i7', 'ryzen 7', 'ryzen 9'],
    'gpu': ['radeon', 'iris', 'mx', 'gtx', 'rtx'],
    'storage': [32, 64, 128, 256, 512, 1024, 2048],
    'ram': [2, 4, 8, 16, 32, 64],
    'os': ['os', '10', '11']
}
