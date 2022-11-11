import pandas as pd
import numpy as np

# TODO: Add more complex logic gates

# region Constants
TABLE_SW = pd.read_csv("/mnt/c/Users/Guilherme/Desktop/projetos/PhoCrySim/PhoCryAPI/PhoCrySim-APIs/backend/components/LumericalValues/switchValuesV2.csv")
TABLE_Y = pd.read_csv("/mnt/c/Users/Guilherme/Desktop/projetos/PhoCrySim/PhoCryAPI/PhoCrySim-APIs/backend/components/LumericalValues/yConnectorValues.csv")

COMPONENTS = {
    "Switch N": {
        "InputCol": "Input",
        "ControlCol": "Control",
        "OutputCol": "SWNOutput",
        "DrainCol": "SWNDrain"
    },
    "Switch P": {
        "InputCol": "Input",
        "ControlCol": "Control",
        "OutputCol": "SWPOutput",
        "DrainCol": "SWPDrain"
    },
    "Junction Y": {
        "Input1Col": "Input1",
        "Input2Col": "Input2",
        "OutputCol": "JunctionOutput"
    },
    "Split Y": {
        "InputCol": "Input1",
        "Output1Col": "SplitOutput1",
        "Output2Col": "SplitOutput2"
    }
}
# endregion

# region Switch N 
class Switch_N:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = TABLE_SW[(TABLE_SW['Control']==int(Control))&(TABLE_SW['Input']==int(Input))].head(1)
        return float(line["SWNOutput"]), float(line["SWNDrain"])

# endregion

# region Switch P
class Switch_P:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = TABLE_SW[(TABLE_SW['Control']==int(Control))&(TABLE_SW['Input']==int(Input))].head(1)
        return (float(line["SWPOutput"]), float(line["SWPDrain"]))

# endregion

# FIXME
# region Y Junction
class Junction_Y:
    @staticmethod
    def calculate(Input1: int, Input2: int):
        line = TABLE_Y[(TABLE_Y['Input1']==Input1)&(TABLE_Y['Input2']==Input2)].head(1)
        return (float(line["JunctionOutput"]))

# endregion

# FIXME
# region Y Split
class Split_Y:
    @staticmethod
    def calculate(Input: int):
        line = TABLE_Y[TABLE_Y['Input1']==Input].head(1)
        print(line["SplitOutput1"])
        print(line)
        return (float(line["SplitOutput1"]), float(line["SplitOutput2"]))

# endregion

