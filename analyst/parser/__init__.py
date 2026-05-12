import os
from song import Song
import json

def read_history(path = 'history') -> list[Song]:
    if not os.path.isdir(path):
        raise Exception(f'Directory {path} does not exist')

    filenames = [
        os.path.join(path, f) for f in os.listdir(path) 
        if os.path.isfile(os.path.join(path, f)) 
    ]

    raw_json: list[dict] = []

    for name in filenames:
        f = open(name)
        text = f.read()
        res = ''

        try:
            res = json.loads(text)
        except:
            print(f'⚠️ Failed to parse {name}')
            continue
    
        if type(res) == list:
            raw_json = raw_json + res
        
    def try_from_raw(d: dict):
        try:
            return Song.fromRawStats(d)
        except:
            return None

    data: list[Song] = list(filter(lambda r: r != None, map(lambda j : try_from_raw(j), raw_json)))

    return data