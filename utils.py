import json
import re
from pathlib import Path


def clean_string(str):
    tmp = ("[edit]", "[citation needed]", "[fr]", "[modifier | modifier le code]", "\n")
    for t in tmp:
        str = str.replace(t, "")
    return re.sub(r'\[\d+\]', '', str)

def open_json(filename):
    return json.load(open(filename))

def create_folder(folder_name):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
