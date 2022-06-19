import pandas as pd

from Constraint import Problem, Constraint, real_data_path
from constraint_relax import search_mfs
from values import Attribute


class ConstraintRS:
    def __init__(self):
        self.csp = Problem()

    def add_constraint(self, constraint):
        if isinstance(constraint.name, Attribute):
            constraint.name = constraint.name.value
        self.csp.add_constraint(constraint)

    def remove_constraint(self, constraint):
        self.csp.remove_constraint(constraint)

    def get_constraints(self):
        return self.csp.constraint_list

    def read_constraints(self):
        df = pd.DataFrame()
        for c in self.get_constraints():
            df = pd.concat([df, pd.DataFrame([{
                'attribute': c.name,
                'value': c.value,
                'priority': c.priority
            }])])
        return df

    def get_items(self):
        solution = self.csp.retrieve_items_top3()
        if solution is None:
            preferred_diagnose = search_mfs(self.csp.constraint_list, real_data_path)
            print("No items are found.\nThe following are suggested constraints you can edit to obtain some items: ")
            for d in preferred_diagnose:
                print(f'{str(d.name)}: {str(d.value)}')
        return solution
