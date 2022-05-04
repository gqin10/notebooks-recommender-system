from Constraint import Constraint, Problem, Nature


def get_prob_1():
    problem: Problem = Problem()
    c1: Constraint = Constraint("cpu", "i5|ryzen 5", 5, Nature.EQUAL)
    c2: Constraint = Constraint("ram", 8, 4, Nature.MORE)
    c3: Constraint = Constraint("screen_size", 15, 2, Nature.NEAR)
    c4: Constraint = Constraint("brand", "hp|dell", 4, Nature.EQUAL)
    problem.add_constraint_list(set([c1, c2, c3, c4]))
    return problem


def get_prob_2():
    problem = Problem()
    c1: Constraint = Constraint("brand", "dell", 7, Nature.EQUAL)
    c2: Constraint = Constraint("weight", 1.2, 5, Nature.LESS)
    c3: Constraint = Constraint("ram", 16, 1, Nature.MORE)
    c4: Constraint = Constraint("screen_size", 15, 5, Nature.NEAR)
    c5: Constraint = Constraint("cpu", "i5", 5, Nature.EQUAL)
    c6: Constraint = Constraint("gpu", "rtx", 5, Nature.EQUAL)
    problem.add_constraint_list([c1, c2, c3, c4, c5, c6])
    return problem
