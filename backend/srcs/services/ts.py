import json 

def load_ts_var(path): 
    return json.loads(open(path).read().split("=")[1])