import os
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import subprocess
import re


def checker():
    print("!!!! Checking the gpu support with tensorflow is working or not ......")
    print("!!!! Checking the installed python packages in current python environment .......")
    returned = subprocess.getoutput('pip list')
    # checking the tensorflow is installed or not

    splitted = [i.lstrip(" " or "......" or '\n').lstrip(" "or"\n").replace(" ",":",1).removesuffix("\n") for i in returned.splitlines(True)]
    splitted = ["".join(s.split(" ")) for s in splitted]

    # Regex to match 'tensorflow:0.12.20' or similar
    tf_regex = re.compile(r'^tensorflow:\d+\.\d+\.\d+$')

    print("Checking Tensflow installed or not: ........................... ")

    # Use regex to check for tensorflow
    tf_installed = any(tf_regex.match(pkg) for pkg in splitted)
    if tf_installed:
        print(f"TensorFlow installed: {tf_installed}")
        print("Checking configured for GPU or not..... ")
        res = tf.config.list_physical_devices('GPU')
        val=""
        print(f"Device Name:{res[0].name}\nDevice Type:{str(val:=res[0].device_type)}")
        if val == "GPU":
            print("congratulations ! GPU is Supported 🐦‍🔥🔥")
    else:
        print("please install tensorflow")


if __name__ == '__main__':
    checker()