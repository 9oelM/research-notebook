import json
from typing import Dict, Any

def getJson(file : str) -> Dict[str, Any]:
    with open(file) as f:
        data = json.load(f)
    return data