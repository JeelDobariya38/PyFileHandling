# PyFileHandling
[![Run-Tests](https://github.com/JeelDobariya38/pyfilehandling/actions/workflows/Run-Tests.yaml/badge.svg)](https://github.com/JeelDobariya38/pyfilehandling/actions/workflows/Run-Tests.yaml)
## Overview
PyFileHandling is a Python package that provides file handling capabilities and offers various functions for file manipulation operations.

## Installation

You can install PyFileHandling using pip:

```shell
pip install pyfilehandling
```

## Importing the Package

You can import the package in different ways:

```python
import pyfilehandling.FileIO
```

```python
import pyfilehandling.FileIO as file
```

```python
from pyfilehandling import FileIO
```

## Creating a File

You can create a file using the `create` function:

```python
import pyfilehandling.FileIO as file

file.create('abc.txt')
```

The `create` function takes the following arguments:

- `path` (str): The path of the file to be created.

This function creates a file with the specified name in the current directory. If the file already exists, an exception will be thrown.

## Creating a Directory/Folder

You can create a directory/folder using the `create_directory` function:

```python
import pyfilehandling.FileIO as file

file.create_directory('PyFile')
```

The `create_directory` function takes the following argument:

- `path` (str): The path of the directory to be created.

This function creates a directory with the specified name. If the directory already exists, an exception will be thrown.

## Writing to a File

You can write data to a file using the `write` function:

```python
import pyfilehandling.FileIO as file

file.write('abc.txt', 'abcdef')
```

The `write` function takes the following arguments:

- `path` (str): The path of the file.
- `data` (str): The data to be written.
- `mode` (str, optional): The file opening mode. Defaults to "w" (write mode).

This function writes the specified data to the file. By default, it opens the file in write mode. It returns `True` if the write operation is successful, `False` otherwise.

## Appending to a File

You can append data to a file using the `write` function with the append mode:

```python
import pyfilehandling.FileIO as file

file.write('abc.txt', 'abcdef', "a")
```

In this case, the mode "a" represents the append mode.

## Writing to a File with a New Line

You can write data to a file with a new line using the `writeline` function:

```python
import pyfilehandling.FileIO as file

file.writeline('abc.txt', 'abcdef', end='\n', start='start')
```

The `writeline` function takes the following arguments:

- `path` (str): The path of the file.
- `data` (str): The data to be written.
- `mode` (str, optional): The file opening mode. Defaults to "w" (write mode).
- `end` (str, optional): The line ending character. Defaults to '\n' (newline).
- `start` (str, optional): The starting character(s) of each line. Defaults to "".

This function writes the specified data to the file with a new line. It returns `True` if the write operation is successful, `False` otherwise.

## Writing Lines to a File

You can write a list of data to a file, with each element on a new line, using the `writelines` function:

```python
import pyfilehandling.FileIO as file

file.writelines('abc.txt', ['abcdef', 'ghijkl'])
```

The `writelines` function takes the same arguments as `writeline`, except that the `data` argument is taken as a list.

## Reading Data from a File

You can read the contents of a file using the `read` function:

```python
import pyfilehandling.FileIO as file

file.read('abc.txt')
```

The `read` function takes the following argument:

- `path` (str): The path of the file.

This function returns a string containing the contents of the file.

## Reading a Line from a File

You can read a single line from a file using the `readline` function:

```python
import pyfilehandling.FileIO as file

file.readline('abc.txt')
```

The `readline` function takes the following argument:

- `path` (str): The path of the file.

This function returns the first line of the file as a string.

## Reading Lines from a File

You can read all lines from a file and take them as a list using the `readlines` function:

```python
import pyfilehandling.FileIO as file

file.readlines('abc.txt')
```

The `readlines` function takes the following argument:

- `path` (str): The path of the file.

This function returns a list of lines from the file.

## Contributing

Contributions are welcome! To contribute to PyFileHandling, please read the [Contribution Guidelines](CONTRIBUTING.md).

## Code of Conduct

We strive to maintain a positive and inclusive community. We encourage everyone participating in PyFileHandling to read the [Code of Conduct](CODE_OF_CONDUCT.md).
