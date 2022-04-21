import copy
import math

from item_extrator import extract_notebooks


def search_mfq(constraint):
    mfq, min_depth = search_failing_subquery(constraint)
    for item in reversed(mfq):
        if len(item) > min_depth:
            mfq.remove(item)

    return mfq, min_depth


def search_failing_subquery(constraint, depth=1, min_depth=math.inf):
    if depth > min_depth:
        return [], min_depth

    mfq_group = list()

    for key, attr in constraint.__dict__.items():
        if attr.priority <= 0:
            continue
        temp_constraint = drop_constraint(copy.deepcopy(constraint), key)
        notebooks = extract_notebooks(temp_constraint)
        if (notebooks.shape)[0] > 0:
            mfq_group.append(set([key]))
            if depth < min_depth:
                min_depth = depth
        else:
            next_mfq, _ = search_failing_subquery(temp_constraint, depth=depth + 1, min_depth=min_depth)
            if next_mfq != None and len(next_mfq) > 0:
                if _ < min_depth: min_depth = _
                temp = set([key])
                for sub_mfq in next_mfq:
                    temp2 = temp.union(sub_mfq)
                if not temp2 in mfq_group: mfq_group.append(temp2)

    return mfq_group, min_depth


def drop_constraint(constraint, key):
    (constraint.get(key)).priority = 0
    return constraint