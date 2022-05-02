import copy
import math

from item_extrator import extract_notebooks, has_item
from Constraint import String_Attribute, Number_Attribute, Boolean_Attribute, NOTEBOOK_LIST, NATURE
from constraint_processor import use_cpu_average, use_gpu_average, is_using_gpu_average, is_using_cpu_average


def search_mfq(constraint):
    mfq, min_depth = search_failing_subquery(constraint)
    for key in reversed(mfq):
        if len(key) > min_depth:
            mfq.remove(key)

    return mfq, min_depth


def search_failing_subquery(constraint, depth=1, min_depth=math.inf):
    if depth > min_depth:
        return [], min_depth

    key_queue = [(key, attr) for key, attr in constraint.__dict__.items() if attr.priority > 0]
    mfq_group = list()

    for key, attr in key_queue:
        if not canRelax(attr):
            continue

        temp_constraint = drop_constraint(copy.deepcopy(constraint), key)
        notebooks = extract_notebooks(temp_constraint)
        if has_item(notebooks):
            mfq_group.append(set([key]))
            if depth < min_depth:
                min_depth = depth
        else:
            next_mfq, next_min_depth = search_failing_subquery(temp_constraint, depth=depth + 1, min_depth=min_depth)

            if next_mfq != None and len(next_mfq) > 0:
                if next_min_depth < min_depth:
                    min_depth = next_min_depth

                temp = set([key])

                for sub_mfq in next_mfq:
                    temp2 = temp.union(sub_mfq)

                if not temp2 in mfq_group:
                    mfq_group.append(temp2)

    return mfq_group, min_depth


def drop_constraint(constraint, key):
    if isinstance(constraint.get(key), String_Attribute):
        (constraint.get(key)).value = []
    elif isinstance(constraint.get(key), Number_Attribute):
        (constraint.get(key)).value = 0
    elif isinstance(constraint.get(key), Boolean_Attribute):
        (constraint.get(key)).value = ""
    (constraint.get(key)).has_relaxed = True
    return constraint


def loose_constraint(constraint, key):
    if key == "cpu":
        constraint = use_cpu_average(constraint) if not is_using_cpu_average(
            constraint) else constraint
        (constraint.get("cpu_average")).value += loose_value(constraint, "cpu_average")
        (constraint.get("cpu_average")).has_relaxed = True

    elif key == "gpu":
        constraint = use_gpu_average(constraint) if not is_using_gpu_average(
            constraint) else constraint
        (constraint.get("gpu_average")).value += loose_value(constraint, "gpu_average")
        (constraint.get("gpu_average")).has_relaxed = True

    elif isinstance(constraint.get(key), String_Attribute):
        (constraint.get(key)).value = []

    elif isinstance(constraint.get(key), Number_Attribute):
        (constraint.get(key)).value += loose_value(constraint, key)

    elif isinstance(constraint.get(key), Boolean_Attribute):
        (constraint.get(key)).value = ""

    (constraint.get(key)).has_relaxed = True
    return constraint


def loose_value(constraint, key):
    if (constraint.get(key)).nature == NATURE.MORE:
        diff = -(constraint.get(key)).increment
        if diff == 0:
            diff = -0.1 * (max(NOTEBOOK_LIST[key]) - min(NOTEBOOK_LIST[key]))

    elif (constraint.get(key).nature) == NATURE.LESS:
        diff = (constraint.get(key)).increment
        if diff == 0:
            diff = 0.1 * (max(NOTEBOOK_LIST[key]) - min(NOTEBOOK_LIST[key]))

    elif (constraint.get(key).nature) == NATURE.NEAR:
        diff = 0

    return diff


def canRelax(attr):
    if attr.priority <= 0 or attr.has_relaxed == True:
        return False

    if isinstance(attr, String_Attribute) and attr.value == []:
        return False

    if isinstance(attr, Number_Attribute) and attr.value == 0:
        return False

    if isinstance(attr, Boolean_Attribute) and (attr.value != True and attr.value != False):
        return False

    return True
