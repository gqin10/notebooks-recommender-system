import pandas as pd

from Notebook import Number_Attribute, String_Attribute

notebooks = pd.read_csv("data/notebook_data.csv")

def extract_notebooks(constraint):
    filtered_notebooks = notebooks

    for key, attr in constraint.__dict__.items():
        if isinstance(attr, str) or attr.priority <= 0:
            continue

        if isinstance(attr, String_Attribute) and attr.value != "":
            # process string constraint
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = filtered_notebooks[key].str.contains("|".join(attr.value), regex=True, case=False)
            filtered_notebooks = filtered_notebooks[filter]

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            # process number constraint
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = (filtered_notebooks[key].astype(float) >= attr.min_value) & (filtered_notebooks[key].astype(float) <= attr.max_value)
            filtered_notebooks = filtered_notebooks[filter]

    return filtered_notebooks