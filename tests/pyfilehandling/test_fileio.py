from pyfilehandling import fileio

import pytest
from tests.mocking import mock_file_handle

class TestWrite:
    def test_write_append_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        fileio.write("abc.txt", data_to_write, "a")

        assert mock_file_handle.data == data_to_write

    def test_write_overwrite_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        fileio.write("abc.txt", data_to_write, "w")

        assert mock_file_handle.data == data_to_write

    def test_write_invalid_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        # Try to write with an invalid mode, expect a ValueError
        with pytest.raises(ValueError, match="Invalid mode 'invalid_mode'. it should be 'w' or 'a'."):
            fileio.write("abc.txt", data_to_write, mode="invalid_mode")


class TestRead:
    # TODO: add testcases to check whether function raises `ValueError(f"Error reading from '{path}': {e}")` when path to file is broken.
    # TODO: add testcases to check whether function return a empty string when file is not found.
    def test_read_existing_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        with open("abc.txt", "w") as file:
            file.write(data_to_write)

        content = fileio.read("abc.txt")

        assert content == data_to_write

    def test_read_empty_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        open("abc.txt", "w").close()

        content = fileio.read("abc.txt")
        assert content == ""

class TestReadline:
    # TODO: add testcases to check whether function raises `ValueError(f"Error reading from '{path}': {e}")` when path to file is broken.
    # TODO: add testcases to check whether function return a empty string when file is not found.
    def test_readline_existing_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Line 1\nLine 2\nLine 3"

        with open("abc.txt", "w") as file:
            file.write(data_to_write)

        lines = fileio.readline("abc.txt", 1)

        assert lines == "Line 2"

    def test_readline_invalid_lineNo_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        open("abc.txt", "w").close()

        with pytest.raises(IndexError):
            fileio.readline("abc.txt", 5)

class TestReadlines:
    # TODO: add testcases to check whether function raises `ValueError(f"Error reading from '{path}': {e}")` when path to file is broken.
    # TODO: add testcases to check whether function return a empty list when file is not found.
    def test_readlines_existing_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Line 1\nLine 2\nLine 3"

        with open("abc.txt", "w") as file:
            file.write(data_to_write)

        lines = fileio.readlines("abc.txt")

        assert lines == ["Line 1", "Line 2", "Line 3"]

    def test_readlines_empty_file(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        open("abc.txt", "w").close()

        lines = fileio.readlines("abc.txt")
        assert lines == []

class TestWriteline:
    def test_writeline_append_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Line 1"

        fileio.writeline("abc.txt", data_to_write, "a")

        assert mock_file_handle.data == data_to_write + "\n"

    def test_writeline_overwrite_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Line 1"

        fileio.writeline("abc.txt", data_to_write, "w")

        assert mock_file_handle.data == data_to_write + "\n"
    
    def test_writeline_invalid_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        with pytest.raises(ValueError, match="Invalid mode 'invalid_mode'. it should be 'w' or 'a'."):
            fileio.writeline("abc.txt", data_to_write, mode="invalid_mode")

class TestWritelines:
    def test_writelines_append_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = ["Line 1", "Line 2", "Line 3"]

        fileio.writelines("abc.txt", data_to_write, "a")

        assert mock_file_handle.data == "Line 1\nLine 2\nLine 3\n"

    def test_writelines_overwrite_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = ["Line 1", "Line 2", "Line 3"]

        fileio.writelines("abc.txt", data_to_write, "w")

        assert mock_file_handle.data == "Line 1\nLine 2\nLine 3\n"

    def test_writelines_invalid_mode(self, monkeypatch, mock_file_handle):
        monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
        data_to_write = "Hello, World!"

        with pytest.raises(ValueError, match="Invalid mode 'invalid_mode'. it should be 'w' or 'a'."):
            fileio.writelines("abc.txt", data_to_write, mode="invalid_mode")