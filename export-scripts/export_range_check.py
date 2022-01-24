#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the export_range_check")

num_records = 1000
print("running the case for " + str(num_records) + " entries")

for i in range(5):
    time.sleep(5)
    range = pow(2, 8 + 4 * i)
    write_configure_info(str(num_records) + " " + str(range))
    subprocess.run(["bin/export_range_check", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    rename_result_file("range_check_100k_" + str(8 + 4 * i))
    move_to_scale_mamba("range_check_100k_" + str(8 + 4 * i))
