import copy

from constraint_processor import *
from item_extrator import extract_notebooks, has_item, has_n_item
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
    relax_threshold = 0.5

    # print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_user_requirements()
    # user_constraint = get_test_constraint()
    user_constraint = get_fail_constraint()

    max_priority = max([attr.priority for _, attr in user_constraint.__dict__.items()])
    for _, attr in user_constraint.__dict__.items():
        attr.priority /= max_priority

    copy_constraint = copy.deepcopy(user_constraint)

    matching_notebooks = extract_notebooks(user_constraint)

    mfq = None

    if not has_n_item(matching_notebooks, 3):
        mfq, min_relax = search_mfq(user_constraint)

        # TODO relax constraint
        mfq.sort(key=lambda x: sum([user_constraint.get(attr).priority for attr in x]), reverse=False)
        print(mfq)
        for item in mfq[0]:
            print(item, ":", user_constraint.get(item).priority)
            if user_constraint.get(item).priority > relax_threshold:
                user_constraint = loose_constraint(user_constraint, item)
            else:
                user_constraint = drop_constraint(user_constraint, item)

        matching_notebooks = extract_notebooks(user_constraint)

    if has_item(matching_notebooks):
        user_constraint = use_cpu_average(user_constraint) if not is_using_cpu_average(
            user_constraint) else user_constraint
        user_constraint = use_gpu_average(user_constraint) if not is_using_gpu_average(
            user_constraint) else user_constraint
        matching_notebooks = compute_similarity(copy_constraint, matching_notebooks)
        matching_notebooks = matching_notebooks.sort_values(by=['similarity'], ascending=False)

    print(matching_notebooks)
