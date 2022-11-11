import requests
import pandas as pd

# region Paths
BaseURL = "http://127.0.0.1:5000/"
Components = BaseURL+"components/"
SWN = Components+"switch_n"
SWP = Components+"switch_p"
# endregion

# region Classes
class SignalReceiver:
    @staticmethod
    def read(Input):
        if Input >= 50:
          return 1
        elif Input <= 25:
          return 0
        else:
          return -1

class SwN:
    @staticmethod
    def calculate_outputs(Input, Control):
        r = requests.get(SWN, params={"Input":int(Input),"Control":int(Control)})
        
        if r.json()['status'] == 200:
            return r.json()['result']['output'], r.json()['result']['drain']
        else:
            return None, None

class SwP:
    @staticmethod
    def calculate_outputs(Input, Control):
        r = requests.get(SWP, params={"Input":int(Input),"Control":int(Control)})
        
        if r.json()['status'] == 200:
            return r.json()['result']['output'], r.json()['result']['drain']
        else:
            return None, None

class WaveGuide:
    @staticmethod
    def calculate_outputs(Input):
        return 0.8 * Input
    
class Nor:
    @staticmethod
    def calculate_outputs(Control, Input1, Input2):
        T1, D1 = SwP.calculate_outputs(Control, Input1)
        T2, D2 = SwP.calculate_outputs(T1, Input2)
        return T2, D2
# endregion


S = [1, 0, 0, 0, 1, 0]
R = [0, 0, 1, 0, 1, 0]

Q = 0
Q_ = 0

E = 0

if len(R) != len(S):
    raise

SIMULATION_DURATION = len(R)

states = {
    "S":  S,
    "R":  R,
    "Q":  [],
    "Q_": []
}

for t in range(SIMULATION_DURATION):
    if E:
        i = t-1
        Qt = SwN.calculate_outputs(Q, E)
        Q_t = SwP.calculate_outputs(Q_, E)
        Q = Nor.calculate_outputs(80, R[i], Q_t[0])[0]
        Q_ = Nor.calculate_outputs(80, S[i], Qt[0])[0]

    states["Q_"].append(Q_)
    states["Q"].append(Q)
    
    E = not E
    
print(pd.DataFrame(states))
