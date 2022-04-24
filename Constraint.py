import pandas as pd
from enum import Enum

NOTEBOOK_LIST = pd.read_csv("./data/data/notebook_data.csv")


class NATURE(Enum):
    NEAR = "near"
    EQUAL = "equal"
    MORE = "more"
    LESS = "less"


class Attribute:
    def __init__(self, nature):
        self.priority = 0
        self.nature = nature
        self.value = ""

    def __str__(self) -> str:
        res = ""
        for key, value in self.__dict__.items():
            res += f"\t{key}: {value}\n"
        return res


class String_Attribute(Attribute):
    def __init__(self, nature):
        super().__init__(nature)


class Number_Attribute(Attribute):
    def __init__(self, nature, increment=0):
        self.increment = increment
        super().__init__(nature)


class Constraint:
    def __init__(self):
        self.brand = String_Attribute(NATURE.EQUAL)
        self.cpu = String_Attribute(NATURE.NEAR)
        self.ram = Number_Attribute(NATURE.MORE, 4)
        self.storage = Number_Attribute(NATURE.MORE, 216)
        self.screen_size = Number_Attribute(NATURE.NEAR, 0.5)
        self.gpu = String_Attribute(NATURE.MORE)
        self.weight = Number_Attribute(NATURE.LESS)
        self.price = Number_Attribute(NATURE.LESS)
        self.cpu_average = Number_Attribute(NATURE.MORE)
        self.gpu_average = Number_Attribute(NATURE.MORE)

    def __str__(self) -> str:
        res = ""
        for key, value in self.__dict__.items():
            res += f"{key}:\n{value}\n"
        return res

    def get(self, key):
        return self.__getattribute__(key)
