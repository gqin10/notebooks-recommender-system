import pandas as pd
import Constraint

data_path: str = "./data/data/notebook_data.csv"


def extract_notebooks(constraint_list: [Constraint]):
    filtered_notebooks = pd.read_csv(data_path)

    for constraint in constraint_list:
        target_key = constraint.name
        target_value = constraint.value

        item_filter = None

        if constraint.value == True or constraint.value == False:
            if target_value == True:
                item_filter = filtered_notebooks[target_key].notnull()
            elif target_value == False:
                item_filter = filtered_notebooks[target_key].isna()

        else:
            filtered_notebooks = filtered_notebooks.dropna(subset=[target_key])

            if constraint.nature == Constraint.Nature.EQUAL:
                item_filter = filtered_notebooks[target_key].str.contains(target_value, regex=True, case=False)

            elif constraint.nature == Constraint.Nature.LESS:
                item_filter = filtered_notebooks[target_key] <= float(target_value)

            elif constraint.nature == Constraint.Nature.MORE:
                item_filter = filtered_notebooks[target_key] >= float(target_value)

        if not item_filter is None:
            filtered_notebooks = filtered_notebooks.loc[item_filter]

    return filtered_notebooks
