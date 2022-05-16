import math

import pandas as pd
import random

from Constraint import Constraint, Problem
from Nature import Nature
from spec_list import spec, attribute_nature

data_path = "./data/data/notebook_data.csv"
NOTEBOOK_LIST = pd.read_csv(data_path)


def create_constraint(constraints: {}) -> [Constraint]:
    constraint_list = []
    for item, value in constraints.__dict__.items():
        constraint: Constraint = Constraint()

        # TODO add constraint

        constraint_list.append(constraint)
    return constraint_list


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
    for index, row in NOTEBOOK_LIST.iterrows():
        problem = Problem()
        for key in row.keys():
            if not key in ['cpu', 'gpu', 'ram', 'storage', 'os', 'screen_size', 'camera', 'weight', 'price']:
                continue

            # randomize whether to constraint an attribute
            if random.randint(0, 1) == 0:
                continue

            curr_value = row.get(key)
            new_value = ''
            # attributes that have values defined in spec_list.py
            if key in ['brand']:
                curr_value = random.choices(spec.get('brand'), k=random.randint(1, len(spec.get('brand') / 2)))
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
                    new_value = random.choices(spec.get(key)[start_index:end_index], k=n)
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
                new_value = max(0, curr_value + increase_value * percentage * (max(NOTEBOOK_LIST[key]) - min(NOTEBOOK_LIST[key])))
                new_value = round(new_value, 2)
            constraint = Constraint(key, new_value, random.randint(1, 5), attribute_nature.get(key))
            problem.add_constraint(constraint)
