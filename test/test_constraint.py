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
    user_constraint.ram.value = 16
    user_constraint.ram.priority = 4
    user_constraint.storage.value = 0
    user_constraint.storage.priority = 0
    user_constraint.screen_size.value = 14
    user_constraint.screen_size.priority = 4
    user_constraint.weight.value = 0
    user_constraint.weight.priority = 0
    user_constraint.price.value = 0
    user_constraint.price.priority = 0

    return set_cpu_gpu_average(user_constraint)

def get_fail_constraint():
    user_constraint = Constraint()

    user_constraint.brand.value = []
    user_constraint.brand.priority = 0

    user_constraint.cpu.value = ["i5"]
    user_constraint.cpu.priority = 10

    user_constraint.gpu.value = ["mx"]
    user_constraint.gpu.priority = 6

    user_constraint.ram.value = 8
    user_constraint.ram.priority = 3

    user_constraint.os.value = "10"
    user_constraint.os.priority = 3

    user_constraint.camera.value = True
    user_constraint.camera.priority = 8

    user_constraint.storage.value = 512
    user_constraint.storage.priority = 10

    user_constraint.screen_size.value = 14
    user_constraint.screen_size.priority = 5

    user_constraint.weight.value = 0.8
    user_constraint.weight.priority = 0

    user_constraint.price.value = 5000
    user_constraint.price.priority = 2

    return set_cpu_gpu_average(user_constraint)
