import os.path
import pandas as pd
from sklearn import preprocessing

from data_information import notebook_required_attributes, notebook_update_attribute_names
from search_model import search_cpu, cpu_clean_list, search_gpu, gpu_clean_list

OUTPUT_DIRECTORY = "data/"
OUTPUT_FILE_TYPE = ".csv"


def process_notebook_data():
    # read notebook data
    notebook_data = pd.read_csv("scraper/data/notebook.csv")

    # retrieve the required columns in notebook data
    notebook_data = notebook_data[notebook_required_attributes]

    # rename columns
    notebook_data.columns = notebook_update_attribute_names

    # remove notebooks that do not have information about cpu, ram, and storage
    notebook_data = notebook_data.dropna(subset=["cpu", "ram", "storage"])

    notebook_data["ram"] = (notebook_data["ram"].str.replace("GB", "", regex=True)).str.strip()
    notebook_data["storage"] = (notebook_data["storage"].str.replace("GB", "", regex=True)).str.strip()
    notebook_data["storage"] = (notebook_data["storage"].str.replace("1 TB", "1024", regex=True)).str.strip()

    notebook_data["gpu"] = notebook_data["gpu"].str.replace("ᵉ", "e", regex=True)
    notebook_data["screen_size"] = notebook_data["screen_size"].str.replace(",", ".", regex=True)
    notebook_data["screen_size"] = notebook_data["screen_size"].str.replace("\"|″", "", regex=True)

    notebook_data['weight'] = notebook_data['weight'].replace("< 1", "1", regex=True)

    return notebook_data


def process_cpu_data():
    cpu1_data = pd.read_csv("scraper/data/cpu_cinebenchR15_single_64bit.csv")
    cpu2_data = pd.read_csv("scraper/data/cpu_cinebenchR15_multi_64bit.csv")
    cpu3_data = pd.read_csv("scraper/data/cpu_geekbench_single_64bit.csv")
    cpu4_data = pd.read_csv("scraper/data/cpu_geekbench_multi_64bit.csv")

    cpu1_data.columns = ["name", "cpu_mark_1"]
    cpu2_data.columns = ["name", "cpu_mark_2"]
    cpu3_data.columns = ["name", "cpu_mark_3"]
    cpu4_data.columns = ["name", "cpu_mark_4"]

    cpu_data = pd.merge(cpu1_data, cpu2_data, how="outer", on="name")
    cpu_data = pd.merge(cpu_data, cpu3_data, how="outer", on="name")
    cpu_data = pd.merge(cpu_data, cpu4_data, how="outer", on="name")

    cpu_data[['cpu_mark_1', 'cpu_mark_2', 'cpu_mark_3', 'cpu_mark_4']] = preprocessing.MinMaxScaler().fit_transform(
        cpu_data[['cpu_mark_1', 'cpu_mark_2', 'cpu_mark_3', 'cpu_mark_4']])
    cpu_data['average'] = (cpu_data[['cpu_mark_1', 'cpu_mark_2', 'cpu_mark_3', 'cpu_mark_4']]).mean(axis=1)

    return cpu_data[['name', 'average']]


def process_gpu_data():
    gpu1_data = pd.read_csv("scraper/data/gpu_firestrike.csv")
    gpu2_data = pd.read_csv("scraper/data/gpu_mark11P.csv")
    gpu3_data = pd.read_csv("scraper/data/gpu_firestrike.csv")
    gpu4_data = pd.read_csv("scraper/data/gpu_mark06.csv")

    gpu1_data.columns = ["name", "gpu_mark_1"]
    gpu2_data.columns = ["name", "gpu_mark_2"]
    gpu3_data.columns = ["name", "gpu_mark_3"]
    gpu4_data.columns = ["name", "gpu_mark_4"]

    gpu_data = pd.merge(gpu1_data, gpu2_data, how="outer", on="name")
    gpu_data = pd.merge(gpu_data, gpu3_data, how="outer", on="name")
    gpu_data = pd.merge(gpu_data, gpu4_data, how="outer", on="name")

    gpu_data[['gpu_mark_1', 'gpu_mark_2', 'gpu_mark_3', 'gpu_mark_4']] = preprocessing.MinMaxScaler().fit_transform(
        gpu_data[['gpu_mark_1', 'gpu_mark_2', 'gpu_mark_3', 'gpu_mark_4']])
    gpu_data['average'] = (gpu_data[['gpu_mark_1', 'gpu_mark_2', 'gpu_mark_3', 'gpu_mark_4']]).mean(axis=1)

    return gpu_data[['name', 'average']]


def clean_cpu_model(cpu):
    return (((cpu.replace(regex=cpu_clean_list, value="")).str.strip()).str.lower())


def clean_gpu_model(gpu):
    return (((gpu.replace(regex=gpu_clean_list, value="")).str.strip()).str.lower())


def merge_data(notebook, cpu, gpu):
    cpu['name'] = clean_cpu_model(cpu['name'])
    cpu = cpu.drop_duplicates(subset='name')
    gpu['name'] = clean_gpu_model(gpu['name'])
    gpu = gpu.drop_duplicates(subset='name')

    notebook = pd.merge(notebook, cpu, how="left", left_on=clean_cpu_model(notebook["cpu"]),
                        right_on=clean_cpu_model(cpu["name"]))
    unmatched_notebook = notebook[notebook["name"].isnull()]
    result = unmatched_notebook.apply(search_cpu, axis=1, cpu_list=cpu)
    notebook.loc[notebook["name"].isnull(), "average"] = result
    notebook.drop(columns=["key_0", "name"], inplace=True)

    notebook = pd.merge(notebook, gpu, how="left", left_on=clean_gpu_model(notebook["gpu"]),
                        right_on=clean_gpu_model(gpu["name"]))
    unmatched_notebook = notebook[notebook["name"].isnull() & notebook["gpu"].notnull()]
    result = unmatched_notebook.apply(search_gpu, axis=1, gpu_list=gpu)
    notebook.loc[notebook["name"].isnull() & ~notebook["gpu"].isnull(), "average_y"] = result
    notebook.drop(columns=["key_0", "name"], inplace=True)

    notebook.drop_duplicates(subset=["brand", "model", "cpu", "gpu"])
    notebook.rename(columns = {"average_x": "cpu_average", "average_y": "gpu_average"},inplace=True)

    return notebook


if __name__ == "__main__":
    notebook_data = process_notebook_data()
    cpu_data = process_cpu_data()
    gpu_data = process_gpu_data()

    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    cpu_data.to_csv(OUTPUT_DIRECTORY + "cpu" + OUTPUT_FILE_TYPE, index=False)
    gpu_data.to_csv(OUTPUT_DIRECTORY + "gpu" + OUTPUT_FILE_TYPE, index=False)

    notebook_data = merge_data(notebook_data, cpu_data, gpu_data)
    notebook_data.to_csv(OUTPUT_DIRECTORY + "notebook_data" + OUTPUT_FILE_TYPE, index=False)
