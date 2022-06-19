from Constraint import *
from Nature import Nature


def sum_priority(constraint_list: set()):
    sum = 0
    for constraint in constraint_list:
        sum += constraint.priority
    return sum


def compute_similarity(constraint_list: set(), item_list: pd.DataFrame, path):
    all_items = pd.read_csv(path)
    if item_list is None:
        return
    if (item_list.shape)[0] <= 0:
        return

    item_list["similarity"] = [0 * i for i in range((item_list.shape)[0])]
    total_weight = sum_priority(constraint_list)

    for constraint in constraint_list:
        if constraint.value == "":
            continue

        if constraint.name in ["camera"]:
            if constraint.value == True:
                similarity = 1 * all_items[constraint.name].notnull()
            else:
                similarity = 1 * all_items[constraint.name].isna()
        elif constraint.name in ["brand", "os"]:
            similarity = 1
        elif constraint.name in ['cpu', 'gpu']:
            key = constraint.name + '_average'
            value = (all_items[all_items[constraint.name].str.contains(constraint.value, regex=True)])[key].mean()
            min_value = min(all_items[key])
            max_value = max(all_items[key])
            similarity = 1 - (abs(value - item_list[key]) / (max_value - min_value))
        elif constraint.name in ["ram", "storage", "price", "weight", "screen_size"]:
            min_value = min(all_items[constraint.name])
            max_value = max(all_items[constraint.name])
            if constraint.nature == Nature.MORE:
                similarity = (constraint.value - min_value) / (max_value - min_value)
            elif constraint.nature == Nature.LESS:
                similarity = (max_value - constraint.value) / (max_value - min_value)
            elif constraint.nature == Nature.NEAR:
                similarity = 1 - (abs(constraint.value - item_list[constraint.name]) / (max_value - min_value))

        item_list["similarity"] += similarity * constraint.priority / total_weight

    return item_list
