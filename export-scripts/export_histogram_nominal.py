#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the export_histogram_nominal")

num_records = 1000
print("running the case for " + str(num_records) + " entries")

for i in range(5):
    time.sleep(5)
    num_groups = 10 + 10 * i
    write_configure_info(str(num_records) + " " + str(num_groups))
    subprocess.run(["bin/export_histogram_nominal", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    rename_result_file("histogram_nominal_100k_" + str(8 + 4 * i))
    move_to_scale_mamba("histogram_nominal_100k_" + str(8 + 4 * i))
