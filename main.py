from Notebook import Notebook
from spec_list import brand_list, cpu_list, gpu_list
from item_extrator import extract_notebooks


def get_requirements():
    user_constraint = Notebook()

    user_constraint.brand.priority = input("Enter brand priority: ")
    if float(user_constraint.brand.priority) > 0:
        temp = input("Enter brand option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.brand.value = [brand_list[t] for t in temp]

    user_constraint.cpu.priority = input("Enter CPU priority: ")
    if float(user_constraint.cpu.priority) > 0:
        temp = input("Enter CPU option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.cpu.value = [cpu_list[t] for t in temp]

    user_constraint.gpu.priority = input("Enter GPU priority: ")
    if float(user_constraint.gpu.priority) > 0:
        temp = input("Enter GPU option: ")
        temp = [int(x) for x in temp.split(",")]
        user_constraint.gpu.value = [gpu_list[t] for t in temp]

    user_constraint.ram.priority = input("Enter RAM priority: ")
    if float(user_constraint.ram.priority) > 0:
        user_constraint.ram.min_value = input("Enter minimum RAM (GB): ")
        user_constraint.ram.max_value = input("Enter maximum RAM (GB): ")

    user_constraint.storage.priority = input("Enter storage priority: ")
    if float(user_constraint.storage.priority) > 0:
        user_constraint.storage.min_value = input("Enter minimum storage (GB): ")
        user_constraint.storage.max_value = input("Enter maximum storage (GB): ")

    user_constraint.screen_size.priority = input("Enter screen size priority: ")
    if float(user_constraint.screen_size.priority) > 0:
        user_constraint.screen_size.min_value = input("Enter minimum screen size (inches): ")
        user_constraint.screen_size.max_value = input("Enter maximum screen size (inches): ")

    user_constraint.weight.priority = input("Enter weight priority: ")
    if float(user_constraint.weight.priority) > 0:
        user_constraint.weight.min_value = input("Enter minimum weight (kg): ")
        user_constraint.weight.max_value = input("Enter maximum weight(kg): ")

    user_constraint.price.priority = input("Enter price priority: ")
    if float(user_constraint.price.priority) > 0:
        user_constraint.price.min_value = input("Enter minimum price (RM): ")
        user_constraint.price.max_value = input("Enter maximum price (RM): ")

    return user_constraint


def get_test_constraint():
    user_constraint = Notebook()

    user_constraint.brand.value = ["hp", "dell"]
    user_constraint.brand.priority = 3
    user_constraint.cpu.value = ["i5", "ryzen 5"]
    user_constraint.cpu.priority = 3
    user_constraint.gpu.value = ["iris"]
    user_constraint.gpu.priority = 0
    user_constraint.ram.min_value = 8
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 0
    user_constraint.storage.min_value = 256
    user_constraint.storage.max_value = 512
    user_constraint.storage.priority = 3
    user_constraint.screen_size.min_value = 14
    user_constraint.screen_size.max_value = 15.6
    user_constraint.screen_size.priority = 3
    user_constraint.weight.min_value = 1.5
    user_constraint.weight.max_value = 2.5
    user_constraint.weight.priority = 2
    user_constraint.price.min_value = 3500
    user_constraint.price.max_value = 4000
    user_constraint.price.priority = 2

    return user_constraint


if __name__ == "__main__":
    print("Refer to notebook-spec-option.md for the available options")

    # user_constraint = get_requirements()
    user_constraint = get_test_constraint()

    filtered_notebooks = extract_notebooks(user_constraint)
    print(filtered_notebooks)
