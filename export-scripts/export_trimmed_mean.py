#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the export_trimmed_mean")

fixed_point_shift = 100
num_records = 1000
print("running the case for " + str(num_records) + " entries with a fixed-point shift of " + str(fixed_point_shift))

time.sleep(5)
for i in range(5):
    range = pow(2, 8 + 4 * i)
    write_configure_info(str(num_records) + " " + str(fixed_point_shift) + " " + str(range))
    subprocess.run(["bin/export_trimmed_mean", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    rename_result_file("trimmed_mean_100k_" + str(8 + 4 * i))
    move_to_scale_mamba("trimmed_mean_100k_" + str(8 + 4 * i))