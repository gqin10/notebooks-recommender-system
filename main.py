from item_extrator import extract_notebooks
from similarity_calculator import compute_similarity
from constraint_relax import relax_constraints
from user_interaction import get_user_requirements
from test.test_constraint import get_test_constraint

import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

if __name__ == "__main__":
    print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_user_requirements()
    user_constraint = get_test_constraint()

    dropped_constraint = set()

    filtered_notebooks = extract_notebooks(user_constraint)

    while len(filtered_notebooks) <= 0:
        filtered_notebooks, dropped_constraint = relax_constraints(user_constraint)

    filtered_notebooks = compute_similarity(user_constraint, filtered_notebooks)
    filtered_notebooks = filtered_notebooks.sort_values(by=["similarity"], ascending=False)
    if len(dropped_constraint) > 0:
        print("Dropped constraints:", dropped_constraint)
    print(filtered_notebooks)
