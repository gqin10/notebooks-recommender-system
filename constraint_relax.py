import copy

from Notebook import *
from item_extrator import extract_notebooks


def relax_constraints(constraint):
    # search_minimal_failing_query(constraint)
    return hard_priority(constraint)


# hard relaxation on low priority constraint
def hard_priority(constraint):
    valid_constraint = [{"key": key, "attr": attr} for key, attr in constraint.__dict__.items() if
                        (isinstance(attr, Attribute) and attr.priority > 0)]
    sorted_constraint = sorted(valid_constraint, key=lambda item: item.get("attr").priority)

    dropped_constraints = []
    notebooks = pd.DataFrame()

    for c in sorted_constraint:
        if (notebooks.shape)[0] <= 0:
            dropped_constraints.append(c.get("key"))
            constraint = drop_constraint(constraint, c.get("key"))
            notebooks = extract_notebooks(constraint)
        else:
            break

    return notebooks, dropped_constraints

# soft relaxation on low priority constraint

# hard relax attribute that has lower priority in minimal failing subquery

# soft relax attribute that has lower priority in minimal failing subquery

# high priority -> soft relaxation, low priority -> hard relaxation

def drop_constraint(constraint, key):
    print("dropping constraint")
    if isinstance(constraint.get(key), String_Attribute) :
        constraint.get(key).value = []
    elif isinstance(constraint.get(key), Number_Attribute) :
        constraint.get(key).min_value = min(NOTEBOOK_LIST[key])
        constraint.get(key).max_value = max(NOTEBOOK_LIST[key])
    return constraint

# mfq