import Constraint
from item_extrator import extract_notebooks


def is_consistent(constraint: set(), path):
    return (extract_notebooks(constraint, path).shape)[0] > 0


def fastdiag(diagnose: set(), constraint: set(), constraint_knowledge: set(), path: str):
    if len(diagnose) > 0 and is_consistent(constraint_knowledge, path):
        return set()
    elif len(constraint) == 1 :
        return constraint
    constraint_left, constraint_right = Constraint.split_constraint_list(constraint)
    diagnose_left: set() = fastdiag(constraint_left, constraint_right, constraint_knowledge.difference(constraint_left), path)
    diagnose_right: set() = fastdiag(diagnose_left, constraint_left, constraint_knowledge.difference(diagnose_left), path)
    return diagnose_left.union(diagnose_right)


def search_mfs(constraint: set(), constraint_knowledge: set(), path: str):
    if len(constraint) <= 0 or not is_consistent(constraint_knowledge.difference(constraint), path):
        return set()
    result = fastdiag(set(), constraint, constraint_knowledge, path)
    return result
