from enum import Enum
import item_extrator
from spec_list import *
import pandas as pd
from item_extrator import data_path

NOTEBOOK_LIST = pd.read_csv(data_path)


class Nature(Enum):
    NEAR = "near"
    EQUAL = "equal"
    MORE = "more"
    LESS = "less"


class Constraint:
    def __init__(self, name: str, value, priority: float, nature: Nature):
        self.name: str = name
        self.value = value
        self.priority: float = priority
        self.nature: Nature = nature

    def __str__(self):
        return f"{self.name}: {self.value}: {self.priority}: {self.nature}"


class Problem:
    def __init__(self):
        self.constraint_list: set() = set()

    def add_constraint(self, constraint: Constraint):
        self.constraint_list = self.constraint_list.add(constraint)

    def add_constraint_list(self, constraint_list: set()):
        self.constraint_list = self.constraint_list.union(constraint_list, )

    def remove_constraint(self, constraint: Constraint):
        self.constraint_list = self.constraint_list.remove(constraint)

    def remove_constraint_list(self, constraint_list: set()):
        self.constraint_list = self.constraint_list.difference_update(constraint_list)

    def solve(self):
        return item_extrator.extract_notebooks(self.constraint_list)

    def relax(self, constraint_list: set(), relax_threshold: float):
        max_priority = max([item.priority for item in self.constraint_list])

        for constraint in constraint_list:
            if constraint.priority > max_priority * relax_threshold:
                soft_relax(constraint)
                print("soft relax", constraint.name, constraint.value)
            else:
                hard_relax(constraint)
                print("hard relax", constraint.name, constraint.value)


def split_constraint_list(constraint_set):
    constraint_list = list(constraint_set)
    constraint_list = sorted(constraint_list, key=lambda c: c.priority)

    constraint_left = set()
    constraint_right = set()

    half_size: int = int(len(constraint_list) / 2)
    for index in range(len(constraint_list)):
        if index < half_size:
            constraint_left.add(constraint_list[index])
        else:
            constraint_right.add(constraint_list[index])

    return constraint_left, constraint_right


def soft_relax(constraint: Constraint):
    if constraint.name in ["brand", "camera"]:
        hard_relax(constraint)
    elif constraint.name in ["cpu", "gpu", "ram", "storage", "os"]:
        if isinstance(constraint.value, str):
            recommend = set(constraint.value.split("|"))
            for spec_value in constraint.value.split("|"):
                curr_index = spec.get(constraint.name).index(spec_value)
                if constraint.nature == Nature.EQUAL:
                    if curr_index - 1 >= 0:
                        recommend.add(spec.get(constraint.name)[curr_index - 1])
                    if curr_index + 1 <= len(spec.get(constraint.name)) - 1:
                        recommend.add(spec.get(constraint.name)[curr_index + 1])
                elif constraint.nature == Nature.LESS:
                    recommend = spec.get(constraint.name)[curr_index + 1]
                elif constraint.nature == Nature.MORE:
                    recommend = spec.get(constraint.name)[curr_index - 1]
            constraint.value = "|".join(recommend)
        else:
            curr_index = spec.get(constraint.name).index(constraint.value)
            if constraint.nature == Nature.LESS:
                constraint.value = spec.get(constraint.name)[curr_index + 1]
            elif constraint.nature == Nature.MORE:
                constraint.value = spec.get(constraint.name)[curr_index - 1]

    elif constraint.name in ["weight", "price", "cpu_average", "gpu_average"]:
        max_value = max(NOTEBOOK_LIST[constraint.name])
        min_value = min(NOTEBOOK_LIST[constraint.name])
        rate = 0.2
        if constraint.nature == Nature.MORE:
            constraint.value -= rate * abs(max_value - min_value)
        elif constraint.nature == Nature.LESS:
            constraint.value += rate * abs(max_value - min_value)


def hard_relax(constraint: Constraint):
    constraint.value = ""