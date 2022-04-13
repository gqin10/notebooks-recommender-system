import re
from difflib import get_close_matches

cpu_clean_list = ["Intel", "Core", "AMD", "®", "processor", "@.*", " ", "Pentium", "Silver", "Athlon", "Gold"]

def search(model, model_list):
    model_length = len(model)

    loop = 0
    similarity = 1
    similar_model = []

    while loop == 0 or (similarity > 0 and len(similar_model) < 1):
        similar_model = get_close_matches(model, model_list, n=1, cutoff=similarity)
        loop += 1
        similarity = (model_length - loop) / model_length

    return similar_model[0]

def search_cpu(notebook, **kwargs):
    cpu = re.sub('|'.join(cpu_clean_list), "", notebook["cpu"]).strip().lower()

    cpu_list = kwargs.get("cpu_list")
    cpu_list = cpu_list["cpu_name"].str.lower()

    return search(cpu, cpu_list)

