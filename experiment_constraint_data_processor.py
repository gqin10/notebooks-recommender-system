import pandas as pd

from Constraint import Problem, Constraint


def process_experiment_constraint_data(constraint_path: str, item_path: str):
    experiment_constraint_data = pd.read_csv(constraint_path)

    # read experiment constraints data
    problem_list = list()
    unique_constraint_no = experiment_constraint_data['constraint_no'].unique()
    for no in unique_constraint_no:
        problem: Problem = Problem(item_path=item_path)
        constraint_list = list()
        for index, item in experiment_constraint_data[experiment_constraint_data['constraint_no'] == no].iterrows():
            constraint = None
            if item.get('name') in ['brand', 'cpu', 'gpu', 'os']:
                constraint: Constraint = Constraint(item.get('name'), item.get('value'), item.get('priority'))
            elif item.get('name') in ['storage', 'ram', 'price', 'weight']:
                constraint: Constraint = Constraint(item.get('name'), float(item.get('value')), item.get('priority'))
            elif item.get('name') in ['camera']:
                constraint: Constraint = Constraint(item.get('name'), bool(item.get('value')), item.get('priority'))
            if constraint != None:
                constraint_list.append(constraint)
        problem.constraint_list = set(constraint_list)
        problem_list.append(problem)

    return problem_list
