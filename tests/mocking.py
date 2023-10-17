import pytest

class MockFileHandle:
    def __init__(self):
        self.data = ""
        self.__read_index = 0
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def write(self, data):
        self.data += data

    def writelines(self, lines):
        self.data += "\n".join(lines)

    def read(self):
        return self.data

    def readline(self):
        lines = self.data.split("\n")
        ind = 0
        for line in lines:
            if ind == self.__read_index:
                self.__read_index += 1
                return line + "\n"
            else:
                ind += 1
        return None

    def readlines(self):
        lines = self.data.split("\n")
        return [line + "\n" for line in lines if line]

@pytest.fixture
def mock_file_handle():
    return MockFileHandle()
