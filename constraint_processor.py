from Constraint import NOTEBOOK_LIST


def set_cpu_gpu_average(user_constraint):
    if user_constraint.cpu.priority > 0 and len(user_constraint.cpu.value) > 0:
        filtered_notebooks = NOTEBOOK_LIST.dropna(subset=["cpu"])
        filter = filtered_notebooks["cpu"].str.contains("|".join(user_constraint.cpu.value), regex=True, case=False)
        filtered_notebooks = filtered_notebooks[filter]
        user_constraint.cpu_average.value = filtered_notebooks["cpu_average"].mean()

    if user_constraint.gpu.priority > 0 and len(user_constraint.gpu.value) > 0:
        filtered_notebooks = NOTEBOOK_LIST.dropna(subset=["gpu"])
        temp = "|".join(user_constraint.gpu.value)
        filter = filtered_notebooks["gpu"].str.contains("|".join(user_constraint.gpu.value), regex=True, case=False)
        filtered_notebooks = filtered_notebooks[filter]
        user_constraint.gpu_average.value = filtered_notebooks["gpu_average"].mean()

    return user_constraint


def use_cpu_average(user_constraint):
    user_constraint.cpu_average.priority = user_constraint.cpu.priority
    user_constraint.cpu.priority = 0
    return user_constraint


def use_gpu_average(user_constraint):
    user_constraint.gpu_average.priority = user_constraint.gpu.priority
    user_constraint.gpu.priority = 0
    return user_constraint


def is_using_cpu_average(user_constraint):
    return user_constraint.cpu_average.priority > 0


def is_using_gpu_average(user_constraint):
    return user_constraint.gpu_average.priority > 0
