import subprocess
import os
import time
from pathlib import Path

def configure_network():
    subprocess.run(["./network_setup.sh"])

def write_configure_info(msg):
    f = open("benchmark_input.txt", "w")
    f.write(msg)
    f.close()

def rename_result_file(name):
    if os.environ["EMP_MY_PARTY_ID"] == "1":
        os.rename("./export_script.mpc", name + ".mpc")
        os.rename("./export_input.txt", name + ".txt")

def move_to_scale_mamba(name):
    if os.environ["EMP_MY_PARTY_ID"] == "1":
        Path("/home/ubuntu/SCALE-MAMBA/Programs/" + name).mkdir(parents=True, exist_ok=True)
        os.replace(name + ".mpc", "/home/ubuntu/SCALE-MAMBA/Programs/" + name + "/" + name + ".mpc")