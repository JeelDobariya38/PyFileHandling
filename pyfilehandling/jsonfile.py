import json

class jsonFile():
    def __init__(self, filename: str, mode: str):
        if not filename.endswith(".json"):
            filename += ".json"
        self.file = open(filename, mode)

