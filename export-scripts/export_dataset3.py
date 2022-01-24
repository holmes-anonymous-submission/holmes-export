#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("start running benchmark of datasets 3")

time.sleep(5)
subprocess.run(["bin/export_dataset_3", os.getenv("EMP_MY_PARTY_ID"), "5000"])
rename_result_file("dataset_3")
move_to_scale_mamba("dataset_3")