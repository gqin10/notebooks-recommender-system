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


class Problem:
    def __init__(self):
        self.constraint_list: [Constraint] = []

    def add_constraint(self, constraint: Constraint):
        self.constraint_list.append(constraint)

    def add_constraint_list(self, constraint_list: [Constraint]):
        self.constraint_list.extend(constraint_list)

    def solve(self):
        return item_extrator.extract_notebooks(self.constraint_list)
