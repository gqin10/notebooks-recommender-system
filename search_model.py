import re
from difflib import get_close_matches

cpu_clean_list = ["Intel", "Core", "AMD", "®", "processor", "@.*", " ", "Pentium", "Silver", "Athlon", "Gold"]
gpu_clean_list = ["nvidia", "intel", "amd", " ", "®", "laptop", "gpu", "graphics", "design", "mobile",
                  "\(laptop\)", "with", "\(.*\)"]


def search(model, model_list):
    model_length = len(model)

    loop = 0
    similarity = 1
    similar_model = [m for m in model_list if model in m]

    if len(similar_model) <= 0:
        while loop == 0 or (similarity > 0 and len(similar_model) < 1):
            similar_model = get_close_matches(model, model_list, n=1, cutoff=similarity)
            loop += 1
            similarity = (model_length - loop) / model_length

    return similar_model[0]


def search_cpu(notebook, **kwargs):
    cpu = re.sub('|'.join(cpu_clean_list), "", notebook["cpu"]).strip().lower()

    cpu_list = kwargs.get("cpu_list")
    cpu_list = cpu_list["name"].str.lower()

    return search(cpu, cpu_list)


def search_gpu(notebook, **kwargs):
    gpu = re.sub('|'.join(gpu_clean_list), "", notebook["gpu"]).strip().lower()

    gpu_list = kwargs.get("gpu_list")
    gpu_list = (gpu_list["name"].str.replace(" ", "")).str.lower()
    gpu_list = gpu_list.str.replace("|".join(gpu_clean_list), "", regex=True)

    return search(gpu, gpu_list)
