from enum import Enum


class NATURE(Enum):
    NEAR = "near"
    EQUAL = "equal"
    MORE = "more"
    LESS = "less"


class Attribute:
    def __init__(self, nature):
        self.priority = 0
        self.nature = nature

    def __str__(self) -> str:
        res = ""
        for key, value in self.__dict__.items():
            res += f"\t{key}: {value}\n"
        return res


class String_Attribute(Attribute):
    def __init__(self, nature):
        self.value = ""
        super().__init__(nature)


class Number_Attribute(Attribute):
    def __init__(self, nature):
        self.min_value = 0
        self.max_value = 0
        super().__init__(nature)


class Notebook:
    def __init__(self):
        self.brand = String_Attribute(NATURE.EQUAL)
        self.model = ""
        self.cpu_brand = ""
        self.cpu = String_Attribute(NATURE.NEAR)
        self.ram = Number_Attribute(NATURE.MORE)
        self.storage = Number_Attribute(NATURE.MORE)
        self.screen_size = Number_Attribute(NATURE.NEAR)
        self.gpu = String_Attribute(NATURE.MORE)
        self.weight = Number_Attribute(NATURE.LESS)
        self.height = ""
        self.width = ""
        self.depth = ""
        self.price = Number_Attribute(NATURE.LESS)

    def __str__(self) -> str:
        res = ""
        for key, value in self.__dict__.items():
            res += f"{key}:\n{value}\n"
        return res
