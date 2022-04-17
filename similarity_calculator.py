import Notebook
from Notebook import String_Attribute, Number_Attribute, Attribute, NATURE


def sum_priority(constraint):
    sum = 0
    for key, attr in constraint.__dict__.items():
        if isinstance(attr, Attribute):
            sum += attr.priority
    return sum


def compute_similarity(constraint, item_list):
    if len(item_list) <= 0:
        return

    # assign 0 to each item's similarity
    item_list["similarity"] = [0 for i in range((item_list.shape)[0])]
    total_weight = sum_priority(constraint)

    for key, attr in constraint.__dict__.items():
        if not isinstance(attr, Attribute) or attr.priority <= 0:
            continue

        if isinstance(attr, String_Attribute) and len(attr.value) <= 0:
            continue

        if isinstance(attr, Number_Attribute) and (attr.min_value < 0 or attr.max_value < 0):
            continue

        diff = [0 * i for i in range((item_list.shape)[0])]

        if isinstance(attr, String_Attribute) and attr.value != "":
            # process string constraint

            # brand
            if attr.nature == NATURE.EQUAL:
                # since items already filtered, all items fulfill the constraints
                diff = 1
                continue

            # cpu
            if key == "cpu":
                if len(item_list["cpu"].unique()) <= 1:
                    diff = 1
                else:
                    diff = (item_list["cpu_average"]) / (max(item_list["cpu_average"]) - min(item_list["cpu_average"]))

            # gpu
            elif key == "gpu":
                if len(item_list["gpu"].unique()) <= 1:
                    diff = 1
                else:
                    diff = (item_list["gpu_average"]) / (max(item_list["gpu_average"]) - min(item_list["gpu_average"]))

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            item_list[key] = item_list[key].astype(float)
            # process number constraint
            if max(item_list[key]) == min(item_list[key]):
                diff = 1
            elif attr.nature == NATURE.MORE:
                # ram, storage
                diff = (item_list[key] - attr.min_value) / (
                            max(Notebook.NOTEBOOK_LIST[key]) - min(Notebook.NOTEBOOK_LIST[key]))
            elif attr.nature == NATURE.LESS:
                # price, weight
                diff = (attr.max_value - item_list[key]) / (
                            max(Notebook.NOTEBOOK_LIST[key]) - min(Notebook.NOTEBOOK_LIST[key]))
            elif attr.nature == NATURE.NEAR:
                # screen_size
                diff = abs(((attr.max_value + attr.min_value) / 2) - Notebook.NOTEBOOK_LIST[key]) / (
                            max(Notebook.NOTEBOOK_LIST[key]) - min(Notebook.NOTEBOOK_LIST[key]))

        # print(key, attr.priority, total_weight)
        item_list["similarity"] += attr.priority * diff * 100 / total_weight
        # print(attr.priority * diff * 100 / total_weight)

    return item_list
