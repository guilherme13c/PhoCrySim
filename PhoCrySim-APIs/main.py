import requests

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
        print(Input)
        if Input >= 50:
          return True
        elif Input <= 5:
          return False
        else:
          return None

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

