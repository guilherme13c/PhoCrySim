import pandas as pd
import numpy as np

# region Constants
TABLE_SW = pd.read_csv("/mnt/c/Users/Guilherme/Desktop/projetos/PhoCrySim/PhoCryAPI/PhoCrySim-APIs/backend/components/LumericalValues/switchValuesV2.csv")
TABLE_Y = pd.read_csv("/mnt/c/Users/Guilherme/Desktop/projetos/PhoCrySim/PhoCryAPI/PhoCrySim-APIs/backend/components/LumericalValues/yConnectorValues.csv")

COMPONENTS = {
    "Switch N": {
        "InputCol": "Input",
        "ControlCol": "Control",
        "OutputCol": "SWNOutput",
        "DrainCol": "SWNDrain",
        "table": TABLE_SW
    },
    "Switch P": {
        "InputCol": "Input",
        "ControlCol": "Control",
        "OutputCol": "SWPOutput",
        "DrainCol": "SWPDrain",
        "table": TABLE_SW
    },
    "Junction Y": {
        "Input1Col": "Input1",
        "Input2Col": "Input2",
        "OutputCol": "JunctionOutput",
        "table": TABLE_Y
    },
    "Split Y": {
        "InputCol": "Input1",
        "Output1Col": "SplitOutput1",
        "Output2Col": "SplitOutput2",
        "table": TABLE_Y
    }
}
# endregion

# region Switch N 
class Switch_N:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = TABLE_SW[(TABLE_SW['Control']==int(Control))&(TABLE_SW['Input']==int(Input))]
        return float(line.head()["SWNOutput"]), float(line.head()["SWNDrain"])

# endregion

# region Switch P
class Switch_P:
    @staticmethod
    def calculate(Input: int, Control:int):
        line = TABLE_SW[(TABLE_SW['Control']==int(Control))&(TABLE_SW['Input']==int(Input))]
        return (float(line.head()["SWPOutput"]), float(line.head()["SWPDrain"]))

# endregion

# region Y Junction
class Junction_Y:
    @staticmethod
    def calculate(Input1: int, Input2: int):
        line = TABLE_Y[(TABLE_Y['Input1']==Input1)&(TABLE_Y['Input2']==Input2)]
        return (float(line.head()["JunctionOutput"]))

# endregion

# region Y Split
class Split_Y:
    @staticmethod
    def calculate(Input: int):
        line = TABLE_Y[TABLE_Y['Input']==Input]
        return (float(line.head()["SplitOutput1"]), float(line.head()["SplitOutput2"]))

# endregion

