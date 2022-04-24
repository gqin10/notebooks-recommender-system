import pandas as pd
import Constraint
from Constraint import String_Attribute, Number_Attribute, Attribute, NATURE
from Constraint import NOTEBOOK_LIST


def sum_priority(constraint):
    sum = 0
    for key, attr in constraint.__dict__.items():
        if isinstance(attr, Attribute):
            sum += attr.priority
    return sum


def need_computation(key, attr):
    if attr.priority <= 0 or attr.value == "":
        return False

    if isinstance(attr, String_Attribute) and len(attr.value) <= 0:
        return False

    if isinstance(attr, Number_Attribute) and float(attr.value) < 0:
        return False

    return True


def compute_similarity(constraint, item_list):
    if (item_list.shape)[0] <= 0:
        return

    item_list["similarity"] = [0 * i for i in range((item_list.shape)[0])]
    total_weight = sum_priority(constraint)

    for key, attr in constraint.__dict__.items():
        if not need_computation(key, attr):
            continue

        diff = 0

        if isinstance(attr, String_Attribute):
            # since items already filtered, all items fulfill the constraints
            diff = 1

        elif isinstance(attr, Number_Attribute) and attr.value > 0:
            item_list[key] = item_list[key].astype(float)
            min_value = min(item_list[key])
            max_value = max(item_list[key])
            if min_value == max_value:
                diff = 1
            elif attr.nature == NATURE.MORE:
                diff = (item_list[key] - attr.value) / (max_value - min_value)
            elif attr.nature == NATURE.LESS:
                diff = (attr.value - item_list[key]) / (max_value - min_value)
            elif attr.nature == NATURE.NEAR:
                diff = 1 - (abs(attr.value - item_list[key]) / (max_value - min_value))

        item_list["similarity"] += diff * attr.priority / total_weight

    return item_list
