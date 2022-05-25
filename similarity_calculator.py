from Constraint import *
from item_extrator import data_path
from Nature import Nature

NOTEBOOK_LIST = pd.read_csv(data_path)


def sum_priority(constraint_list: set()):
    sum = 0
    for constraint in constraint_list:
        sum += constraint.priority
    return sum


def compute_similarity(constraint_list: set(), item_list: pd.DataFrame):
    if (item_list.shape)[0] <= 0:
        return

    item_list["similarity"] = [0 * i for i in range((item_list.shape)[0])]
    total_weight = sum_priority(constraint_list)

    for constraint in constraint_list:
        if constraint.value == "":
            continue

        if constraint.name in ["camera"]:
            if constraint.value == True:
                similarity = 1 * NOTEBOOK_LIST[constraint.name].notnull()
            else:
                similarity = 1 * NOTEBOOK_LIST[constraint.name].isna()
        elif constraint.name in ["brand", "os"]:
            similarity = 1
        elif constraint.name in ['cpu', 'gpu']:
            key = constraint.name
            average_benchmark = item_list[key + '_average'].mean()
            min_value = min(NOTEBOOK_LIST[key + '_average'])
            max_value = max(NOTEBOOK_LIST[key + '_average'])
            similarity = (average_benchmark - min_value) / (max_value - min_value)
        elif constraint.name in ["ram", "storage", "price", "weight", "screen_size"]:
            min_value = min(NOTEBOOK_LIST[constraint.name])
            max_value = max(NOTEBOOK_LIST[constraint.name])
            if constraint.nature == Nature.MORE:
                similarity = (constraint.value - min_value) / (max_value - min_value)
            elif constraint.nature == Nature.LESS:
                similarity = (max_value - constraint.value) / (max_value - min_value)
            elif constraint.nature == Nature.NEAR:
                similarity = 1 - (abs(constraint.value - item_list[constraint.name]) / (max_value - min_value))

        item_list["similarity"] += similarity * constraint.priority / total_weight

    return item_list
