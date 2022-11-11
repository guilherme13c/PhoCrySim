from components import *
import json
from flask import Flask, request

components.COMPONENTS

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Photonic Crystal API Library</h1><h2>PhoCryAPI</h2>"

@app.route("/components/")
def list_components():
    return json.dumps(components.COMPONENTS)

@app.route("/components/switch_n")
def switch_n():
    args = request.args
    Input = args.get("Input", type=int)
    Control = args.get("Control", type=int)
    
    print()
    
    try:
        ret = components.Switch_N.calculate(float(Input), float(Control))
    except:
        return json.dumps({
            "status": 300
        })
    
    return json.dumps({
        "result":{
            "output": ret[0],
            "drain": ret[1]
        },
        "status": 200
    })
    
@app.route("/components/switch_p")
def switch_p():
    args = request.args
    Input = args.get("Input", type=int)
    Control = args.get("Control", type=int)
    
    try:
        ret = components.Switch_P.calculate(float(Input), float(Control))
    except:
        return json.dumps({
            "status": 300
        })
    
    return json.dumps({
        "result":{
            "output": ret[0],
            "drain": ret[1]
        },
        "status": 200
    })
