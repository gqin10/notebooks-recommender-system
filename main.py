import pandas as pd
from Constraint import Problem, Constraint, Nature

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

if __name__ == "__main__":
    problem = Problem()

    c1: Constraint = Constraint("brand", "dell|hp", 3, Nature.EQUAL)
    c2: Constraint = Constraint("weight", 1.8, 5, Nature.LESS)
    c3: Constraint = Constraint("camera", False, 5, Nature.BOOL)
    problem.add_constraint(c1)
    problem.add_constraint(c2)
    problem.add_constraint(c3)

    solution = problem.solve()
    print(solution)
