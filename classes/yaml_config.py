import yaml
from verbosity import *
class YamlConfig():

    # Class for holding configuration of SD Card and CSV file
    config_file_path = "null"
    col_labels_dict = {}
    col_vars_dict = {}
    sd_card_setup_dict = {}
    config_block_info_dict = {}
    data_block_info_dict = {}


    # When constructed, the config_file_path is required
    def __init__(self, config_file_path, verbosity):
        self.config_file_path = config_file_path
        self.verbosity = verbosity

    def readInConfig(self):
        # get column labels (column headers for csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n    Getting Column Labels")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_LABELS'].items():
            self.col_labels_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print(key, value)


        # get column vars (variables that will go in each row of the csv file)
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n    Getting Column Variables")
        for key, value in yaml.safe_load(open(self.config_file_path))['COL_VARS'].items():
            self.col_vars_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print(key, value)

        # get sd card setup
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n    Getting Column SD Card Setup")
        for key, value in yaml.safe_load(open(self.config_file_path))['SDCARD_SETUP'].items():
            self.sd_card_setup_dict[key] = value
            if self.verbosity.value > Verbosity.HIGH.value:
                print(key, value)

        # check to make sure necessary items were set in the yaml config file
        # TODO WRITE IFS

        # get configuration data info
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n    Getting " + str(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]) + " Config Data Blocks Info")
        for i in range(self.sd_card_setup_dict["NUM_CONFIG_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\n    Reading CFG_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['CFG_' + str(i)].items():
                self.config_block_info_dict["CFG_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print(key, value)

        # get actual data info
        if self.verbosity.value > Verbosity.HIGH.value:
            print("\n    Getting " + str(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]) + " Data Blocks Info")
        for i in range(self.sd_card_setup_dict["NUM_DATA_BLOCKS"]):
            if self.verbosity.value > Verbosity.HIGH.value:
                print("\n    Reading DB_" + str(i))
            for key, value in yaml.safe_load(open(self.config_file_path))['DB_' + str(i)].items():
                self.data_block_info_dict["DB_" + str(i) + ":" + key] = value
                if self.verbosity.value > Verbosity.HIGH.value:
                    print(key, value)






