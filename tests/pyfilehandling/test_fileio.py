import pyfilehandling

import pytest
from tests.mocking import mock_file_handle

def test_write_append_mode(monkeypatch, mock_file_handle):
    monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
    data_to_write = "Hello, World!"

    pyfilehandling.write("abc.txt", data_to_write)

    with open("abc.txt", "r") as file:
        content = file.read()

    assert content == data_to_write

def test_write_overwrite_mode(monkeypatch, mock_file_handle):
    monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
    data_to_write = "Hello, World!"

    pyfilehandling.write("abc.txt", data_to_write,"w")

    with open("abc.txt", "r") as file:
        content = file.read()

    assert content == data_to_write

def test_write_invalid_mode(monkeypatch, mock_file_handle):
    monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
    data_to_write = "Hello, World!"

    # Try to write with an invalid mode, expect a ValueError
    with pytest.raises(ValueError, match="Invalid mode 'invalid_mode'. it should be 'w' or 'a'."):
        pyfilehandling.write("abc.txt", data_to_write, mode="invalid_mode")

def test_read_existing_file(monkeypatch, mock_file_handle):
    monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
    data_to_write = "Hello, World!"

    # Write data to the file
    with open("abc.txt", "w") as file:
        file.write(data_to_write)

    # Read the content using the read function
    content = pyfilehandling.read("abc.txt")

    assert content == data_to_write

def test_read_empty_file(monkeypatch, mock_file_handle):
    monkeypatch.setattr('builtins.open', lambda file, mode='r': mock_file_handle)
    open("abc.txt", "w").close()

    # Read the content using the read function, expect an empty string
    content = pyfilehandling.read("abc.txt")
    assert content == ""
