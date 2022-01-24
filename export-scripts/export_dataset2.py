#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("start running benchmark of datasets 2")

time.sleep(5)
subprocess.run(["bin/export_dataset_2", os.getenv("EMP_MY_PARTY_ID"), "5000"])
rename_result_file("dataset_2")
move_to_scale_mamba("dataset_2")
