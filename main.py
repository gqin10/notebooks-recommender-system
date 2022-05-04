import pandas as pd
from Constraint import Problem, Constraint, Nature
from similarity_calculator import compute_similarity
from constraint_relax import search_mfs
import copy

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

if __name__ == "__main__":
    problem = Problem()

    c1: Constraint = Constraint("brand", "dell", 7, Nature.EQUAL)
    c2: Constraint = Constraint("weight", 1.2, 5, Nature.LESS)
    c3: Constraint = Constraint("ram", 16, 1, Nature.MORE)
    c4: Constraint = Constraint("screen_size", 15, 5, Nature.NEAR)
    c5: Constraint = Constraint("cpu", "i5", 5, Nature.EQUAL)
    c6: Constraint = Constraint("gpu", "rtx", 5, Nature.EQUAL)
    problem.add_constraint(c1)
    problem.add_constraint(c2)
    problem.add_constraint(c3)
    problem.add_constraint(c4)
    problem.add_constraint(c5)
    problem.add_constraint(c6)

    solution = problem.solve()

    if solution is None or (solution.shape)[0] <= 0:
        mfs = search_mfs(problem.constraint_list, copy.copy(problem.constraint_list))
        problem.relax(mfs)

    solution = problem.solve()
    # solution = compute_similarity(problem.constraint_list, solution)
    print(solution)
