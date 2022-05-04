import Constraint
from Constraint import Nature
from item_extrator import extract_notebooks


def is_consistent(constraint: set()):
    return (extract_notebooks(constraint).shape)[0] > 0


def fastdiag(diagnose: set(), constraint: set(), constraint_knowledge: set()):
    if len(diagnose) > 0 and is_consistent(constraint_knowledge):
        return set()
    elif len(constraint) == 1:
        return constraint
    constraint_left, constraint_right = Constraint.split_constraint_list(constraint)
    diagnose_left: set() = fastdiag(constraint_left, constraint_right, constraint_knowledge.difference(constraint_left))
    diagnose_right: set() = fastdiag(diagnose_left, constraint_left, constraint_knowledge.difference(diagnose_left))
    return diagnose_left.union(diagnose_right)


def search_mfs(constraint: set(), constraint_knowledge: set()):
    if len(constraint) <= 0 or not is_consistent(constraint_knowledge.difference(constraint)):
        return set()
    result = fastdiag(set(), constraint, constraint_knowledge)
    return result
