from Constraint import NOTEBOOK_LIST


def set_cpu_gpu_average(user_constraint):
    if user_constraint.cpu.priority > 0 and len(user_constraint.cpu.value) > 0:
        filtered_notebooks = NOTEBOOK_LIST.dropna(subset=["cpu"])
        filter = filtered_notebooks["cpu"].str.contains("|".join(user_constraint.cpu.value), regex=True, case=False)
        filtered_notebooks = filtered_notebooks[filter]
        user_constraint.cpu_average.min_value = min(filtered_notebooks["cpu_average"])
        user_constraint.cpu_average.max_value = max(filtered_notebooks["cpu_average"])

    if user_constraint.gpu.priority > 0 and len(user_constraint.gpu.value) > 0:
        filtered_notebooks = NOTEBOOK_LIST.dropna(subset=["gpu"])
        filter = filtered_notebooks["gpu"].str.contains("|".join(user_constraint.gpu.value), regex=True, case=False)
        filtered_notebooks = filtered_notebooks[filter]
        user_constraint.gpu_average.min_value = min(filtered_notebooks["gpu_average"])
        user_constraint.gpu_average.max_value = max(filtered_notebooks["gpu_average"])

    return user_constraint


def use_cpu_average(user_constraint):
    user_constraint.cpu_average.priority = user_constraint.cpu.priority
    user_constraint.cpu.priority = 0
    return user_constraint


def use_gpu_average(user_constraint):
    user_constraint.gpu_average.priority = user_constraint.gpu.priority
    user_constraint.gpu.priority = 0
    return user_constraint
