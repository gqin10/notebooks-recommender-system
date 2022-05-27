import math
import random

import pandas as pd

from Constraint import Constraint, Problem, data_path
from spec_list import spec, attribute_list
from Nature import attribute_nature

NOTEBOOK_LIST = pd.read_csv(data_path)


def get_cpu_category(cpu_name):
    if pd.isna(cpu_name):
        return
    for cpu in spec.get('cpu'):
        if cpu in cpu_name:
            return cpu


def get_gpu_category(gpu_name):
    if pd.isna(gpu_name):
        return
    for gpu in spec.get('gpu'):
        if gpu in gpu_name:
            return gpu


def get_os_category(os_name):
    if pd.isna(os_name):
        return
    for os in spec.get('os'):
        if os in os_name:
            return os


def get_str_len(str):
    if str == None:
        return 0
    return len(str.strip())


if __name__ == "__main__":
    constraint_list = []
    for i in range(1000):
        random_item = NOTEBOOK_LIST.sample(n=1)

        problem = Problem()

        #randomize attribute to restrict
        selected_attribute = random.sample(attribute_list, k=random.randint(
            math.ceil((len(attribute_list) - 1) / 2),
            (len(attribute_list) - 1)
        ))

        for key in selected_attribute:
            if not key in attribute_list:
                continue

            curr_value = random_item.loc[:, key].values[0]
            new_value = ''
            # attributes that have values defined in spec_list.py
            if key in ['brand']:
                min_limit = 1
                max_limit = math.ceil((len(spec.get('brand')) - 1) / 2)
                new_value = random.sample(spec.get('brand'), k=random.randint(min_limit, max_limit))
                new_value = "|".join(new_value)
            elif key in ['cpu', 'gpu', 'ram', 'storage', 'os']:
                if key == 'cpu':
                    curr_value = get_cpu_category(curr_value)
                    if get_str_len(curr_value) <= 0:
                        continue
                elif key == 'gpu':
                    curr_value = get_gpu_category(curr_value)
                    if get_str_len(curr_value) <= 0:
                        continue
                elif key == 'os':
                    curr_value = get_os_category(curr_value)
                    if get_str_len(curr_value) <= 0:
                        continue
                curr_index = spec.get(key).index(curr_value)

                if key in ['cpu', 'gpu']:
                    start_index = max(0, curr_index - 2)
                    end_index = min(curr_index + 2, len(spec.get(key)))
                    n = random.randint(1, math.floor((end_index - start_index + 1) / 2))
                    new_value = random.sample(spec.get(key)[start_index:end_index], k=n)
                    new_value = "|".join(new_value)
                elif key in ['ram', 'storage', 'os']:
                    new_index = random.randint(max(0, curr_index - 1), min(curr_index + 1, len(spec.get(key)) - 1))
                    new_value = spec.get(key)[new_index]
            elif key in ['camera']:
                # get camera value (True or False)
                if pd.isna(curr_value):
                    new_value = False
                else:
                    new_value = True
                if random.randint(0, 1) == 1:
                    # use opposite value
                    new_value = not new_value
            elif key in ['price', 'weight', 'screen_size']:
                percentage = random.random() / 10
                increase_value = random.randint(-1, 1)
                new_value = max(0, curr_value + increase_value * percentage * (
                        max(NOTEBOOK_LIST[key]) - min(NOTEBOOK_LIST[key])))
                new_value = round(new_value, 2)
            constraint = Constraint(key, new_value, random.randint(1, 10), attribute_nature.get(key))
            problem.add_constraint(constraint)
        constraint_list.append(problem.constraint_list)

    index = 0
    count = 0
    str_list = {}
    for constraint_set in constraint_list:
        for constraint in constraint_set:
            constraint.__dict__.update({'constraint_no': count})
            constraint.__dict__.pop('nature')
            str_list.update({index: constraint.__dict__})
            index += 1
        count += 1

    constraint_df = pd.DataFrame.from_dict(str_list, orient='index')
    constraint_df.to_csv('./experiment_constraint_data.csv', index=False)
