import pandas as pd

import item_extrator
from Nature import Nature, attribute_nature
from similarity_calculator import compute_similarity
from values import *


class Constraint:
    def __init__(self, name: str, value, priority: float):
        self.name: str = name
        self.value = value
        self.priority: float = priority
        if isinstance(name, Attribute):
            self.nature: Nature = attribute_nature.get(name.value)
        else:
            self.nature: Nature = attribute_nature.get(name)

    def __str__(self):
        return f"{self.name}: {self.value}: {self.priority}: {self.nature}"


class Problem:
    def __init__(self, item_path=real_data_path):
        self.constraint_list: set() = set()
        self.item_path: str = item_path

    def add_constraint(self, constraint: Constraint):
        self.constraint_list.add(constraint)

    def add_constraint_list(self, list: set()):
        self.constraint_list = self.constraint_list.union(list)

    def remove_constraint(self, constraint: Constraint):
        self.constraint_list = self.constraint_list.remove(constraint)

    def remove_constraint_list(self, list: set()):
        self.constraint_list = self.constraint_list.difference_update(list)

    def retrieve_items(self):
        solution = self.solve()
        if solution is None:
            return None
        else:
            solution = solution.sort_values(by=['similarity'])
        return solution.drop(columns=['cpu_average', 'gpu_average', 'similarity'], axis=1)

    def retrieve_items_top3(self):
        solution = self.solve()
        if solution is None:
            return None
        else:
            solution = solution.head(3)
            solution = solution.sort_values(by=['cpu_average', 'gpu_average', 'ram', 'storage'], ascending=False)
        # return solution.drop(columns=['cpu_average', 'gpu_average', 'similarity'], axis=1)
        return solution

    def solve(self):
        solution = item_extrator.extract_notebooks(self.constraint_list, self.item_path)
        solution = compute_similarity(self.constraint_list, solution, self.item_path)
        if not solution is None:
            solution = solution.sort_values(by=['similarity'])
        return solution

    def relax(self, constraint_list: set(), relax_threshold: float):
        max_priority = max([item.priority for item in self.constraint_list])

        for constraint in constraint_list:
            if constraint.priority > max_priority * relax_threshold:
                constraint = soft_relax(constraint, self.item_path)
            else:
                constraint = hard_relax(constraint)


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


def soft_relax(constraint: Constraint, item_path: str):
    all_items = pd.read_csv(item_path)
    if constraint.name in ["brand", "camera"]:
        hard_relax(constraint)
    elif constraint.name in ["cpu", "gpu", "ram", "storage", "os"]:
        if isinstance(constraint.value, str):
            recommend = set(constraint.value.split("|"))
            for spec_value in constraint.value.split("|"):
                curr_index = spec.get(constraint.name).index(spec_value)
                if constraint.nature.name == Nature.EQUAL.name:
                    if curr_index - 1 >= 0:
                        recommend.add(spec.get(constraint.name)[curr_index - 1])
                    if curr_index + 1 <= len(spec.get(constraint.name)) - 1:
                        recommend.add(spec.get(constraint.name)[curr_index + 1])
                elif constraint.nature.name == Nature.LESS.name:
                    recommend = spec.get(constraint.name)[curr_index + 1]
                elif constraint.nature.name == Nature.MORE.name:
                    recommend = spec.get(constraint.name)[curr_index - 1]
            constraint.value = "|".join(recommend)
        else:
            curr_index = spec.get(constraint.name).index(constraint.value)
            if constraint.nature.name == Nature.LESS.name:
                constraint.value = spec.get(constraint.name)[curr_index + 1]
            elif constraint.nature.name == Nature.MORE.name:
                constraint.value = spec.get(constraint.name)[curr_index - 1]

    elif constraint.name in ["weight", "price", "cpu_average", "gpu_average"]:
        max_value = max(all_items[constraint.name])
        min_value = min(all_items[constraint.name])
        rate = 0.05
        if constraint.nature.name == Nature.MORE.name:
            constraint.value -= rate * abs(max_value - min_value)
        elif constraint.nature.name == Nature.LESS.name:
            constraint.value += rate * abs(max_value - min_value)
    return constraint


def hard_relax(constraint: Constraint):
    constraint.value = ""
    return constraint
