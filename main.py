import copy

from constraint_processor import *
from item_extrator import extract_notebooks
from similarity_calculator import compute_similarity
from constraint_relax import search_mfq, drop_constraint, loose_constraint
from user_interaction import get_user_requirements
from test.test_constraint import *
from Constraint import String_Attribute, Number_Attribute, NATURE

import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

if __name__ == "__main__":
    # print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_user_requirements()
    # user_constraint = get_test_constraint()
    user_constraint = get_fail_constraint()
    copy_constraint = copy.deepcopy(user_constraint)

    matching_notebooks = extract_notebooks(user_constraint)

    while (matching_notebooks.shape)[0] <= 0:
        mfq, min_relax = search_mfq(user_constraint)
        # TODO relax constraint
        mfq.sort(key=lambda x: sum([user_constraint.get(attr).priority for attr in x]), reverse=False)
        print(mfq)
        for item in mfq[0]:
            # user_constraint = drop_constraint(user_constraint, item)
            user_constraint = loose_constraint(user_constraint, item)

        matching_notebooks = extract_notebooks(user_constraint)

    if (matching_notebooks.shape)[0] > 0:
        copy_constraint = use_cpu_average(copy_constraint) if not is_using_cpu_average(
            copy_constraint) else copy_constraint
        user_constraint = use_gpu_average(user_constraint) if not is_using_gpu_average(
            user_constraint) else user_constraint
        matching_notebooks = compute_similarity(copy_constraint, matching_notebooks)
        matching_notebooks = matching_notebooks.sort_values(by=['similarity'], ascending=False)

    print(matching_notebooks)
