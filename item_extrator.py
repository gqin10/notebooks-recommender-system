import pandas as pd
import Constraint
from Nature import Nature


def extract_notebooks(constraint_list: [Constraint], path):
    all_notebooks = pd.read_csv(path)
    filtered_notebooks = pd.read_csv(path)

    for constraint in constraint_list:
        target_key = constraint.name
        target_value = constraint.value

        item_filter = None

        if constraint.nature == Nature.EQUAL and (constraint.value == True or constraint.value == False):
            if target_value == True:
                item_filter = filtered_notebooks[target_key].notnull()
            elif target_value == False:
                item_filter = filtered_notebooks[target_key].isna()

        elif constraint.value != "":
            filtered_notebooks = filtered_notebooks.dropna(subset=[target_key])

            if constraint.nature == Nature.EQUAL:
                item_filter = filtered_notebooks[target_key].str.contains(target_value, regex=True, case=False)

            elif constraint.nature == Nature.LESS:
                item_filter = filtered_notebooks[target_key] <= float(target_value)

            elif constraint.nature == Nature.MORE:
                item_filter = filtered_notebooks[target_key] >= float(target_value)

            elif constraint.nature == Nature.NEAR:
                min_value = min(all_notebooks[target_key])
                max_value = max(all_notebooks[target_key])
                range_diff = 0.1 * (max_value - min_value)
                item_filter = (filtered_notebooks[target_key] >= (constraint.value - range_diff)) & (
                        filtered_notebooks[target_key] <= (constraint.value + range_diff))

        if not item_filter is None:
            filtered_notebooks = filtered_notebooks.loc[item_filter]

    return filtered_notebooks
