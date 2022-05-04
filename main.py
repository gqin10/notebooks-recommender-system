import copy
import pandas as pd
from constraint_relax import search_mfs
from test.test_constraint import *
from similarity_calculator import compute_similarity

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

if __name__ == "__main__":
    problem: Problem = get_prob_2()
    solution = problem.solve()

    relax_values = [0, 0.25, 0.5, 0.75, 1]

    if solution is None or (solution.shape)[0] <= 0:
        mfs = search_mfs(problem.constraint_list, copy.copy(problem.constraint_list))
        for value in relax_values:
            print((copy.deepcopy(problem)).relax(mfs, value))

    solution = problem.solve()
    solution = compute_similarity(problem.constraint_list, solution)
    print(solution)
