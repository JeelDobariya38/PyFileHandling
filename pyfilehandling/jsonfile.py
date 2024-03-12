import json
from typing import Dict


class jsonFile():
    def __init__(self, filename: str, mode: str = "r"):
        if not filename.endswith(".json"):
            filename += ".json"
        self.file = open(filename, mode)

    def read(self) -> Dict:
        if self.file.readable:
            return json.load(self.file)
        raise Exception("")

    def write(self, data: Dict, indent: int = 4):
        if self.file.writable:
            json.dump(data, self.file, indent)
