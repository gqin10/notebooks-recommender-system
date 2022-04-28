"""
All attributes of notebooks
['Brand', 'Model', 'Product Type', 'Processor Brand', 'Processor Model',
'CPU Cores', 'Processor Speed (GHz)', 'Processor Max Speed', 'RAM (GB)',
'RAM Type', 'Storage Type', 'Storage Size (GB)', 'Operating System',
'Screen Size (inches)', 'Screen Definition', 'Resolution',
'Graphics Card Type', 'Camera Resolution (MP)', 'Type', 'Bluetooth',
'Ethernet', 'HDMI', 'USB', 'Wireless Ready', 'Weight (kg)',
'Product Height (cm)', 'Product Width (cm)', 'Product Depth (cm)',
'Price (RM)']
"""
notebook_required_attributes = [
    "Brand", "Model", "Processor Model", "RAM (GB)",
    "Storage Size (GB)", "Operating System", "Screen Size (inches)", "Graphics Card Type",
    "Camera Resolution (MP)", "Weight (kg)", "Price (RM)"
]

notebook_update_attribute_names = [
    "brand", "model", "cpu", "ram",
    "storage", "os", "screen_size", "gpu",
    "camera", "weight", "price"
]

notebook_crawl_target = {
    "notebook": "https://www.harveynorman.com.my/computing/computers-en/laptops-en"
}

cpu_crawl_target = {
    "cpu_cinebenchR15_single_64bit": "https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html?type=&sort=&deskornote=2&gpubenchmarks=1&or=0&cinebench_r15_single=1&cpu_fullname=1",
    "cpu_cinebenchR15_multi_64bit": "https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html?type=&sort=&deskornote=2&gpubenchmarks=1&or=0&cinebench_r15_multi=1&cpu_fullname=1",
    "cpu_geekbench_single_64bit": "https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html?type=&sort=&deskornote=2&gpubenchmarks=1&or=0&geekbench5_1_single=1&cpu_fullname=1",
    "cpu_geekbench_multi_64bit": "https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html?type=&sort=&deskornote=2&gpubenchmarks=1&or=0&geekbench5_1_multi=1&cpu_fullname=1"
}

gpu_crawl_target = {
    "gpu_icestorm": "https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html?type=&sort=&gpubenchmarks=1&or=0&3dmark13_ice_gpu=1&gpu_fullname=1",
    "gpu_mark11P": "https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html?type=&sort=&gpubenchmarks=1&or=0&3dmark11_gpu=1&gpu_fullname=1",
    "gpu_firestrike": "https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html?type=&sort=&gpubenchmarks=1&or=0&3dmark13_fire_gpu=1&gpu_fullname=1",
    "gpu_mark06": "https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html?type=&sort=&gpubenchmarks=1&or=0&3dmark06=1&gpu_fullname=1"
}
