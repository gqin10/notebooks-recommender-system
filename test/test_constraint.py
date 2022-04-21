from Constraint import Constraint
from constraint_processor import set_cpu_gpu_average

def get_test_constraint():
    user_constraint = Constraint()

    user_constraint.brand.value = []
    user_constraint.brand.priority = 0
    user_constraint.cpu.value = ["i7"]
    user_constraint.cpu.priority = 5
    user_constraint.gpu.value = ["rtx"]
    user_constraint.gpu.priority = 10
    user_constraint.ram.min_value = 16
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 4
    user_constraint.storage.min_value = 0
    user_constraint.storage.max_value = 0
    user_constraint.storage.priority = 0
    user_constraint.screen_size.min_value = 14
    user_constraint.screen_size.max_value = 17.2
    user_constraint.screen_size.priority = 4
    user_constraint.weight.min_value = 0
    user_constraint.weight.max_value = 0
    user_constraint.weight.priority = 0
    user_constraint.price.min_value = 0
    user_constraint.price.max_value = 0
    user_constraint.price.priority = 0

    return set_cpu_gpu_average(user_constraint)

def get_fail_constraint():
    user_constraint = Constraint()

    user_constraint.brand.value = []
    user_constraint.brand.priority = 0
    user_constraint.cpu.value = ["i5", "ryzen 5", "i7", "ryzen 7"]
    user_constraint.cpu.priority = 8
    user_constraint.gpu.value = ["rtx"]
    user_constraint.gpu.priority = 6
    user_constraint.ram.min_value = 8
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 4
    user_constraint.storage.min_value = 0
    user_constraint.storage.max_value = 0
    user_constraint.storage.priority = 0
    user_constraint.screen_size.min_value = 14
    user_constraint.screen_size.max_value = 16
    user_constraint.screen_size.priority = 4
    user_constraint.weight.min_value = 0
    user_constraint.weight.max_value = 0
    user_constraint.weight.priority = 0
    user_constraint.price.min_value = 2000
    user_constraint.price.max_value = 4000
    user_constraint.price.priority = 5

    return set_cpu_gpu_average(user_constraint)
