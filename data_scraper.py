import os
import os.path
from data_information import notebook_crawl_target, cpu_crawl_target, gpu_crawl_target

OUTPUT_DIRECTORY = "./data/"
OUTPUT_FILE_TYPE = ".csv"


def collect_data(key, url, spider_name):
    # create directory if path does not exist
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    # generate path to store data output
    file_name = OUTPUT_DIRECTORY + key + OUTPUT_FILE_TYPE

    # remove the existing file if there is
    if os.path.exists(file_name):
        os.remove(file_name)

    # generate command to run the spider
    command = f'scrapy crawl {spider_name} -o {file_name} -a url="{url}"'

    # run the command
    os.system(command)


if __name__ == "__main__":
    os.chdir("./scraper")

    for key, url in notebook_crawl_target.items():
        collect_data(key, url, "notebook_spider")
    for key, url in (cpu_crawl_target | gpu_crawl_target).items():
        collect_data(key, url, "notebook_check_spider")

    os.chdir("./..")
