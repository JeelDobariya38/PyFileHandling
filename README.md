# PyFileHandling
pyfilehandling is a python package. Which help user in handling there file and give necessary function to user for some file manipulation operation.

# CONTRIBUTION
contribution are welcome in pyfilehandling project for getting start please read the [CONTRIBUTING.md](CONTRIBUTING.md)

# Code of Conduct
here is code of conduct for the repository [code_of_conduct](CODE_OF_CONDUCT.md)

## For installation

```python
pip install pyfilehandling
```

## Import a package
```python
import pyfilehandling.FileIO
```
```python
import pyfilehandling.FileIO as file
```
```python
from pyfilehandling import FileIO
```

## Create a file

```python
import pyfilehandling.FileIO as file

file.create('abc.txt')
#this will create a file with name abc.txt in current directory.
```
Creates a directory

takes the following arguments:

- path (str): The path of Directory

Doens't return anything but will throw an exception if file already exist

## Create a folder/Directory
```python
import pyfilehandling.FileIO as file

file.create_directory('PyFile')
```

Same as create function but it will create a directory instead of file.  Will throw an exception if directory already exist  

Args:

- path (str): The path of Directory


## Write in a file
```python
import pyfilehandling.FileIO as file

file.write('abc.txt','abcdef')
```
Writes data to a file.

Takes the following arguments:

- path (str): The path of the file.

- data (str): The data to be written.

- mode (str, optional): The file opening mode. Defaults to "w" (write mode).

Returns:

- bool: True if the write operation is successful, False otherwise.


## appending into a file
```python
import pyfilehandling.FileIO as file

file.write('abc.txt','abcdef',"a")
```
Here "a" is the mode of file opening, which in this context is append mode.

## write in a file with new line
```python
import pyfilehandling.FileIO as file

file.writeline('abc.txt','abcdef', end = '\n', start = 'start')
```
Writes data to a file in a new line.

Args:

- path (str): The path of the file.

- data (str): The data to be written.

- mode (str, optional): The file opening mode. Defaults to "w" (write mode).

- end (str, optional): The line ending character. Defaults to '\n' (newline).

- start (str, optional): The starting character(s) of each line. Defaults to "".

Returns:

- bool: True if the write operation is successful, False otherwise.

## Writelines in a file
```python
import pyfilehandling.FileIO as file

file.writelines('abc.txt',['abcdef','ghijkl'])
```
Writes a list of data to a file. Each element of the list is written in a new line. The arguments are same as writeline function except data is taken as list.

## Read data from a file
```python
import pyfilehandling.FileIO as file

file.read('abc.txt')
```

Reads the contents of a file.

takes the following arguments:

- path (str): The path of the file.

Returns:

- string : The contents of the file.

## Read Line from a file
```python
import pyfilehandling.FileIO as file

file.readline('abc.txt')
```
Reads a single line from a file.

Args:

- path (str): The path of the file.

Returns:

- str: The first line of the file.


## Read Lines from a file
```python
import pyfilehandling.FileIO as file

file.readlines('abc.txt')
```
Reads all lines from a file and returns them as a list.

Args:

- path (str): The path of the file.

Returns:

- list: A list of lines from the file.

