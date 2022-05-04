from enum import Enum
import item_extrator


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
        self.constraint_list.add(constraint)

    def add_constraint_list(self, constraint_list: set()):
        self.constraint_list.union(constraint_list)

    def remove_constraint(self, constraint: Constraint):
        self.constraint_list.remove(constraint)

    def remove_constraint_list(self, constraint_list: set()):
        self.constraint_list.difference_update(constraint_list)

    def solve(self):
        return item_extrator.extract_notebooks(self.constraint_list)


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
