#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the export_histogram_numeric")

num_records = 1000
num_groups = 10

print("running the case for " + str(num_records) + " entries")

for i in range(5):
    time.sleep(5)
    range = pow(2, 4 + 2 * i)
    write_configure_info(str(num_records) + " " + str(num_groups) + " " + str(range))
    subprocess.run(["bin/export_histogram_numeric", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    rename_result_file("histogram_numeric_100k_" + str(range))
    move_to_scale_mamba("histogram_numeric_100k_" + str(range))
