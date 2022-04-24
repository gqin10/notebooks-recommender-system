import pandas as pd

from Constraint import Number_Attribute, String_Attribute, NOTEBOOK_LIST, NATURE


def extract_notebooks(constraint):
    filtered_notebooks = NOTEBOOK_LIST

    for key, attr in constraint.__dict__.items():
        if (filtered_notebooks.shape)[0] <= 0:
            break

        if attr.priority <= 0:
            continue

        filtered_notebooks = filtered_notebooks.dropna(subset=[key])
        if isinstance(attr, String_Attribute) and attr.value != "":
            filter = filtered_notebooks[key].str.contains("|".join(attr.value), regex=True, case=False)

        elif isinstance(attr, Number_Attribute) and attr.nature == NATURE.MORE and attr.value > 0:
            # get items that have attribute more than the given value
            filter = (filtered_notebooks[key].astype(float) >= attr.value)

        elif isinstance(attr, Number_Attribute) and attr.nature == NATURE.LESS and attr.value > 0:
            # get items that have attribute lesser than the given value
            filter = (filtered_notebooks[key].astype(float) <= attr.value)

        filtered_notebooks = filtered_notebooks[filter]

    return filtered_notebooks
