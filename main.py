import pandas as pd
from Constraint import Problem, Constraint, Nature
from similarity_calculator import compute_similarity

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

if __name__ == "__main__":
    problem = Problem()

    c1: Constraint = Constraint("brand", "dell|hp", 3, Nature.EQUAL)
    c2: Constraint = Constraint("weight", 1.8, 5, Nature.LESS)
    c3: Constraint = Constraint("ram", 8, 5, Nature.MORE)
    c4:Constraint = Constraint("screen_size", 15, 5, Nature.NEAR)
    problem.add_constraint(c1)
    problem.add_constraint(c2)
    problem.add_constraint(c3)
    problem.add_constraint(c4)

    solution = problem.solve()

    solution = compute_similarity(problem.constraint_list, solution)
    print(solution)
