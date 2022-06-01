import math
import random
import os

import numpy as np
import pandas as pd

from Constraint import Constraint, Problem, real_data_path
from values import spec, attribute_list
from Nature import attribute_nature

NOTEBOOK_LIST = pd.read_csv(real_data_path)


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
    constraint_dict_list = {}
    for index in range(500):
        selected_original_item = NOTEBOOK_LIST.sample(1)
        constraint_dict = {}

        for key in attribute_list:
            curr_value = selected_original_item.iloc[0].loc[key]
            new_value = ''
            if key in ['brand']:
                min_limit = 1
                max_limit = math.ceil((len(spec.get('brand')) - 1) / 2)
                new_value = random.choice(spec.get('brand'))
            elif key in ['cpu', 'gpu', 'ram', 'storage', 'os']:
                if key == 'cpu':
                    curr_value = get_cpu_category(curr_value)
                elif key == 'gpu':
                    curr_value = get_gpu_category(curr_value)
                elif key == 'os':
                    curr_value = get_os_category(curr_value)

                if curr_value is None:
                    curr_index = spec.get(key).index(random.choice(spec.get(key)))
                else:
                    curr_index = spec.get(key).index(curr_value)

                if key in ['cpu', 'gpu', 'os']:
                    population_filter = NOTEBOOK_LIST[key].str.contains((spec.get(key))[curr_index], regex=False, case=False)
                    population_filter.replace(np.nan, False, inplace=True)
                    if key in ['cpu', 'gpu']:
                        population = (NOTEBOOK_LIST[population_filter])[[key, key + '_average']]
                        sample = population.sample()
                        constraint_dict.update({
                            key + '_average': sample.iloc[0, 1]
                        })
                        new_value = sample.iloc[0, 0]
                    else:
                        population = (NOTEBOOK_LIST[population_filter])[key]
                        new_value = random.choice(population.tolist())
                elif key in ['ram', 'storage']:
                    new_index = random.randint(max(0, curr_index - 1), min(curr_index + 1, len(spec.get(key)) - 1))
                    new_value = spec.get(key)[new_index]
            elif key in ['camera']:
                population = NOTEBOOK_LIST[key]
                new_value = random.choice(population.tolist())
            elif key in ['price', 'weight', 'screen_size']:
                percentage = random.random() / 10
                increase_value = random.randint(-1, 1)
                new_value = max(0, curr_value + increase_value * percentage * (
                        max(NOTEBOOK_LIST[key]) - min(NOTEBOOK_LIST[key])))
                new_value = round(new_value, 2)
            constraint = Constraint(key, new_value, random.randint(1, 5), attribute_nature.get(key))
            constraint_dict.update({
                constraint.name: constraint.value
            })
        constraint_dict_list.update({
            index: constraint_dict
        })

    constraint_df = pd.DataFrame.from_dict(constraint_dict_list, orient='index')

    if not os.path.isdir('./data/data'):
        os.mkdir('data')

    constraint_df.to_csv('./data/data/simulated_data.csv', index=False)
