from .customerrors import ReadNotPermitted, WriteNotPermitted

import json
from typing import Dict, Any

class jsonFile:
    def __init__(self, filename: str, mode: str = "r"):
        if not filename.endswith(".json"):
            filename += ".json"
        self.file = open(filename, mode)

    def read(self) -> Dict:
        if self.file.readable:
            return json.load(self.file)
        raise ReadNotPermitted(self.file.name)

    def write(self, data: Dict, indent: int = 4):
        if self.file.writable:
            json.dump(data, self.file, indent)
        raise WriteNotPermitted(self.file.name)

    def read_key(self, key) -> Any:
        if self.data == None:
            self.data = self.read()
        else:
            return self.data[key]
