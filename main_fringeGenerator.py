import argparse
import os.path
import sys

import yaml
from src.process import process


# ---------FUNC--------------------
# This func load the config file
def get_param_file(path_file):

    if os.path.exists(path_file):
        with open(path_file) as file:
            config_param_ = yaml.load(file, Loader=yaml.FullLoader)

    else:
        print("Configuration file doesn't exist")
        sys.exit(-1)

    return config_param_


# ---------------------------------


# --------- MAIN --------------------
def main(config_param):

    process(config_param)


# ---------------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-conf", "--configFile", help="configuration file")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        print(
            "Configuration file missing\n  usage:\n\t python3 main_fringeGenerator.py -conf <path to conf file>/<config_file_name>.yaml\n"
        )

        sys.exit(-1)

    config_param = get_param_file(args.configFile)
    main(config_param)
