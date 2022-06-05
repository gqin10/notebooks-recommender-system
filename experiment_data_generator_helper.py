import copy

import pandas as pd

from Constraint import Problem, Constraint
from Nature import attribute_nature
from constraint_relax import search_mfs
from values import real_data_path
from similarity_calculator import compute_similarity
import os


def get_df_len(df):
    if df is None:
        return 0
    return (df.shape)[0]


if __name__ == "__main__":
    i = 0
    while True:
        i = i + 1
        print('------------------------------------------------------------')
        print(f'round {i}')
        print('generating data...')
        os.system("python -m experiment_data_generator")
        experiment_constraint_data = pd.read_csv("./experiment_constraint_data.csv")

        print('reading data...')
        # read experiment constraints data
        problem_list = list()
        unique_constraint_no = experiment_constraint_data['constraint_no'].unique()
        for no in unique_constraint_no:
            problem: Problem = Problem()
            constraint_list = list()
            for index, item in experiment_constraint_data[experiment_constraint_data['constraint_no'] == no].iterrows():
                constraint = None
                if item.get('name') in ['brand', 'cpu', 'gpu', 'os']:
                    constraint: Constraint = Constraint(item.get('name'), item.get('value'), item.get('priority'),
                                                        attribute_nature.get(item.get('name')))
                elif item.get('name') in ['storage', 'ram', 'price', 'weight']:
                    constraint: Constraint = Constraint(item.get('name'), float(item.get('value')),
                                                        item.get('priority'), attribute_nature.get(item.get('name')))
                elif item.get('name') in ['camera']:
                    constraint: Constraint = Constraint(item.get('name'), bool(item.get('value')), item.get('priority'),
                                                        attribute_nature.get(item.get('name')))
                if constraint != None:
                    constraint_list.append(constraint)
            cl_set = set(constraint_list)
            problem.constraint_list = set(constraint_list)
            problem_list.append(problem)

        print('solving problems...')
        sol_list = []
        threshold_list = [0, 0.5, 1]
        for problem in problem_list:
            prob_sol_list = []
            p1 = copy.deepcopy(problem)  # original constraint
            prob_sol_list.append(p1.constraint_list)
            prob_sol_list.append(get_df_len(p1.solve()))

            for threshold in threshold_list:
                p = copy.deepcopy(problem)
                mfs = search_mfs(p.constraint_list, copy.copy(p.constraint_list), real_data_path)
                p.relax(mfs, threshold)
                prob_sol_list.append(p.constraint_list)
                prob_items = p.solve()
                prob_sol_list.append(get_df_len(prob_items))
                if not prob_items is None:
                    prob_sol_list.append((compute_similarity(p.constraint_list, prob_items, real_data_path))['similarity'].mean())
                else:
                    prob_sol_list.append(0)
            sol_list.append(prob_sol_list)

        print('done')
        result = pd.DataFrame(sol_list)
        valid = ((result.iloc[:, 1] < result.iloc[:, 3]) & (result.iloc[:, 3] < result.iloc[:, 6]) & (
                    result.iloc[:, 6] < result.iloc[:, 9]))
        valid_count = pd.value_counts(valid)

        size = (result[valid].shape)[0]
        print(f'result: {size}')

        if size >= 4:
            break
