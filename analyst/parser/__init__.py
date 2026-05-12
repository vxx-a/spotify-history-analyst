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
        res = json.loads(text)

        if type(res) == list:
            raw_json = raw_json + res
        

    data: list[Song] = map(lambda j : Song.fromRawStats(j), raw_json)

    return data