from flask import Flask, request
from components import *
import json

app = Flask(__name__)

# returns home page
@app.route("/")
def welcome():
    return "<h1>Photonic Crystal API Library</h1><h2>PhoCryAPI lib.</h2>"

# returns list of components
@app.route("/components/")
def list_components():
    try:
        ret = components.COMPONENTS
    except Exception as e:
        return json.dumps({
            "status": 300,
            "exception": str(type(e))
        })
        
    print(ret)
    return json.dumps({
        "components": ret, 
        "status": 200
    })

@app.route("/components/switch_n")
def switch_n():
    args = request.args
    Input = args.get("Input", type=int)
    Control = args.get("Control", type=int)
    
    try:
        ret = components.Switch_N.calculate(float(Input), float(Control))
    except Exception as e:
        return json.dumps({
            "status": 300,
            "exception": str(type(e))
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
    except Exception as e:
        return json.dumps({
            "status": 300,
            "exception": str(type(e))
        })
    
    return json.dumps({
        "result":{
            "output": ret[0],
            "drain": ret[1]
        },
        "status": 200
    })
    
@app.route("/components/junction_y")
def junction_y():
    args = request.args
    Input1 = args.get("Input1", type=int)
    Input2 = args.get("Input2", type=int)
    
    try:
        ret = components.Junction_Y.calculate(float(Input1), float(Input2))
    except Exception as e:
        return json.dumps({
            "status": 300,
            "exception": str(type(e))
        })
    
    return json.dumps({
        "result":{
            "output": ret[0],
        },
        "status": 200
    })
    
@app.route("/components/split_y")
def split_y():
    args = request.args
    Input = args.get("Input", type=int)
    print(Input)
    
    try:
        ret = components.Split_Y.calculate(float(Input))
    except Exception as e:
        return json.dumps({
            "status": 300,
            "exception": str(type(e))
        })
    
    return json.dumps({
        "result":{
            "output1": ret[0],
            "output2": ret[1]
        },
        "status": 200
    })
