import pandas as pd
import numpy as np

# region Constants
COMPONENTS = {
    "Switch N": {
        "OutputCol": "SWNOutput",
        "DrainCol": "SWNDrain"
    },
    "Switch P": {
        "OutputCol": "SWPOutput",
        "DrainCol": "SWPDrain"
    },
}

TABLE_SW = pd.read_csv("/mnt/c/Users/Guilherme/Desktop/projetos/PhoCrySim/PhoCrySim-APIs/backend/components/LumericalValues/switchValuesV2.csv")
# endregion

# region Switch N 
table = TABLE_SW

class Switch_N:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = table[(table['Control']==Control)&(table['Input']==Input)]
        return float(line.head()["SWNOutput"]), float(line.head()["SWNDrain"])

# endregion

# region Switch P
table = TABLE_SW

class Switch_P:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = table[(table['Control']==Control)&(table['Input']==Input)]
        return (float(line.head()["SWPOutput"]), float(line.head()["SWPDrain"]))

# endregion
