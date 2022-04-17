from Notebook import Notebook
from constraint_processor import set_cpu_gpu_average

def get_test_constraint():
    user_constraint = Notebook()

    user_constraint.brand.value = []
    user_constraint.brand.priority = 0
    user_constraint.cpu.value = ["n4100"]
    user_constraint.cpu.priority = 10
    user_constraint.gpu.value = []
    user_constraint.gpu.priority = 0
    user_constraint.ram.min_value = 16
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 4
    user_constraint.storage.min_value = 0
    user_constraint.storage.max_value = 0
    user_constraint.storage.priority = 0
    user_constraint.screen_size.min_value = 0
    user_constraint.screen_size.max_value = 0
    user_constraint.screen_size.priority = 0
    user_constraint.weight.min_value = 0
    user_constraint.weight.max_value = 0
    user_constraint.weight.priority = 0
    user_constraint.price.min_value = 0
    user_constraint.price.max_value = 0
    user_constraint.price.priority = 0

    return set_cpu_gpu_average(user_constraint)
