import constraint_processor
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
    matching_notebooks = extract_notebooks(user_constraint) # extract items that fulfil constraints

    # relax constraint if  no items can be found

    if (matching_notebooks.shape)[0] > 0:
        user_constraint = constraint_processor.use_cpu_average(user_constraint)
        user_constraint = constraint_processor.use_gpu_average(user_constraint)
        matching_notebooks = compute_similarity(user_constraint, matching_notebooks)
        matching_notebooks = matching_notebooks.sort_values(by=['similarity'], ascending=False)

    print(matching_notebooks)