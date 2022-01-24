#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the export_variance_check")

fixed_point_shift = 100
print("running the case for entries with a fixed-point shift of " + str(fixed_point_shift))

time.sleep(5)
for i in range(5):
    num_records = 1000 + i * 1000
    write_configure_info(str(num_records) + " " + str(fixed_point_shift))
    subprocess.run(["bin/export_variance_check", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    rename_result_file("variance_check_100p_" + str(i + 1))
    move_to_scale_mamba("variance_check_100p_" + str(i + 1))