import pandas as pd
from Notebook import Notebook, Number_Attribute, String_Attribute

notebooks = pd.read_csv("data/notebook_data.csv")

def extract_notebooks(constraint):
    filtered_notebooks = notebooks

    for key, attr in constraint.__dict__.items():
        if isinstance(attr, str) or attr.priority <= 0:
            print(f"skip {key}")
            continue

        if isinstance(attr, String_Attribute) and attr.value != "":
            # process stringconstraint
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = filtered_notebooks[key].str.contains("|".join(attr.value), regex=True, case=False)
            filtered_notebooks = filtered_notebooks[filter]
            print(filtered_notebooks.shape)
            pass

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            print(key, attr)
            # process number constraint
            filtered_notebooks = filtered_notebooks.dropna(subset=[key])
            filter = (filtered_notebooks[key].astype(float) >= attr.min_value) & (filtered_notebooks[key].astype(float) <= attr.max_value)
            filtered_notebooks = filtered_notebooks[filter]
            print(filtered_notebooks)
            pass