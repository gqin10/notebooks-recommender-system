from constraint_processor import *
from item_extrator import extract_notebooks
from similarity_calculator import compute_similarity
from constraint_relax import search_mfq
from user_interaction import get_user_requirements
from test.test_constraint import *

import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

if __name__ == "__main__":
    # print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_user_requirements()
    # user_constraint = get_test_constraint()
    user_constraint = get_fail_constraint()

    matching_notebooks = extract_notebooks(user_constraint)

    while (matching_notebooks.shape)[0] <= 0:
        mfq, min_relax = search_mfq(user_constraint)
        # TODO relax constraint
        mfq.sort(key = lambda x: sum([user_constraint.get(attr).priority for attr in x]), reverse=False)
        print(mfq)
        for item in mfq[0]:
            (user_constraint.get(item)).priority = 0
        matching_notebooks = extract_notebooks(user_constraint)

    if (matching_notebooks.shape)[0] > 0:
        user_constraint = use_cpu_average(user_constraint) if not is_using_cpu_average(
            user_constraint) else user_constraint
        user_constraint = use_gpu_average(user_constraint) if not is_using_gpu_average(
            user_constraint) else user_constraint
        matching_notebooks = compute_similarity(user_constraint, matching_notebooks)
        matching_notebooks = matching_notebooks.sort_values(by=['similarity'], ascending=False)

    print(matching_notebooks)
