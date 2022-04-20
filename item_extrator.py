import pandas as pd

from Constraint import Number_Attribute, String_Attribute, NOTEBOOK_LIST

def extract_notebooks(constraint):
    filtered_notebooks = NOTEBOOK_LIST

    for key, attr in constraint.__dict__.items():
        if (filtered_notebooks.shape)[0] <= 0:
            break

        if attr.priority <= 0:
            continue

        if isinstance(attr, String_Attribute) and attr.value != "":
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = filtered_notebooks[key].str.contains("|".join(attr.value), regex=True, case=False)
            filtered_notebooks = filtered_notebooks[filter]

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = (filtered_notebooks[key].astype(float) >= attr.min_value) & (
                    filtered_notebooks[key].astype(float) <= attr.max_value)
            filtered_notebooks = filtered_notebooks[filter]

    return filtered_notebooks
