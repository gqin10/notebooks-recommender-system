from Notebook import Notebook
from spec_list import brand_list, cpu_list, gpu_list
from item_extrator import extract_notebooks
from similarity_calculator import compute_similarity

import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199


def get_requirements():
    user_constraint = Notebook()

    user_constraint.brand.priority = float(input("Enter brand priority: "))
    if user_constraint.brand.priority > 0:
        temp = input("Enter brand option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.brand.value = [brand_list[t] for t in temp]

    user_constraint.cpu.priority = float(input("Enter CPU priority: "))
    if user_constraint.cpu.priority > 0:
        temp = input("Enter CPU option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.cpu.value = [cpu_list[t] for t in temp]

    user_constraint.gpu.priority = float(input("Enter GPU priority: "))
    if user_constraint.gpu.priority > 0:
        temp = input("Enter GPU option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.gpu.value = [gpu_list[t] for t in temp]

    user_constraint.ram.priority = float(input("Enter RAM priority: "))
    if user_constraint.ram.priority > 0:
        user_constraint.ram.min_value = float(input("Enter minimum RAM (GB): "))
        user_constraint.ram.max_value = float(input("Enter maximum RAM (GB): "))

    user_constraint.storage.priority = float(input("Enter storage priority: "))
    if user_constraint.storage.priority > 0:
        user_constraint.storage.min_value = float(input("Enter minimum storage (GB): "))
        user_constraint.storage.max_value = float(input("Enter maximum storage (GB): "))

    user_constraint.screen_size.priority = float(input("Enter screen size priority: "))
    if user_constraint.screen_size.priority > 0:
        user_constraint.screen_size.min_value = float(input("Enter minimum screen size (inches): "))
        user_constraint.screen_size.max_value = float(input("Enter maximum screen size (inches): "))

    user_constraint.weight.priority = float(input("Enter weight priority: "))
    if user_constraint.weight.priority > 0:
        user_constraint.weight.min_value = float(input("Enter minimum weight (kg): "))
        user_constraint.weight.max_value = float(input("Enter maximum weight(kg): "))

    user_constraint.price.priority = float(input("Enter price priority: "))
    if user_constraint.price.priority > 0:
        user_constraint.price.min_value = float(input("Enter minimum price (RM): "))
        user_constraint.price.max_value = float(input("Enter maximum price (RM): "))

    return user_constraint


def get_test_constraint():
    user_constraint = Notebook()

    user_constraint.brand.value = []
    user_constraint.brand.priority = 0
    user_constraint.cpu.value = ["i7","i5"]
    user_constraint.cpu.priority = 5
    user_constraint.gpu.value = ["rtx","gtx"]
    user_constraint.gpu.priority = 3
    user_constraint.ram.min_value = 8
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 3
    user_constraint.storage.min_value = 0
    user_constraint.storage.max_value = 0
    user_constraint.storage.priority = 0
    user_constraint.screen_size.min_value = 0
    user_constraint.screen_size.max_value = 0
    user_constraint.screen_size.priority = 0
    user_constraint.weight.min_value = 1
    user_constraint.weight.max_value = 2.2
    user_constraint.weight.priority = 1
    user_constraint.price.min_value = 0
    user_constraint.price.max_value = 0
    user_constraint.price.priority = 0

    return user_constraint


if __name__ == "__main__":
    print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_requirements()
    user_constraint = get_test_constraint()

    filtered_notebooks = extract_notebooks(user_constraint)
    print(filtered_notebooks)
    if len(filtered_notebooks) > 0:
        filtered_notebooks = compute_similarity(user_constraint, filtered_notebooks)
    else:
        print("Cannot find notebook")
    print(filtered_notebooks)
