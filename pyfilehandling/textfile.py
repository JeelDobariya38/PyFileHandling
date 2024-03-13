from .customerrors import ReadNotPermitted, WriteNotPermitted


class textFile:
    def __init__(self, filename: str, mode: str = "r"):
        if not filename.endswith(".txt"):
            filename += ".txt"
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def read(self) -> str:
        if self.file.readable:
            return self.file.read()
        else:
            raise ReadNotPermitted(self.file.name)

    def write(self, data: str):
        if self.file.writable:
            self.file.write(data)
        else:
            raise WriteNotPermitted(self.file.name)

    def close(self):
        self.file.close()
