from typing import Optional, List, Generator

def create_dir(path: str) -> None:
    """
    Create a directory at the given path.

    Parameters:
    - path (str): The path for the directory.

    Raises:
    - ValueError: If the path is invalid or a directory already exists at the given path.

    Returns:
    - None
    """

def remove_dir(path: str) -> None:
    """
    Remove a directory at the given path.

    Parameters:
    - path (str): The path to the directory to be removed.

    Raises:
    - ValueError: If the path is invalid.

    Returns:
    - None
    """

def create_file(path: str) -> None:
    """
    Create a file at the given path.

    Parameters:
    - path (str): The path for the file.

    Raises:
    - ValueError: If the path is invalid or a file already exists at the given path.

    Returns:
    - None
    """

def remove_file(path: str) -> None:
    """
    Remove a file at the given path.

    Parameters:
    - path (str): The path to the file to be removed.

    Raises:
    - ValueError: If the path is invalid.

    Returns:
    - None
    """

def write(path: str, data: str, mode: Optional[str] = 'a') -> None:
    """
    Write data to a file.

    Parameters:
    - path (str): The path to the file.
    - data (str): The data to be written to the file.
    - mode (str, optional): The mode in which the file is opened. 
      Defaults to 'a' (append). Other valid modes are 'w' (write).

    Raises:
    - ValueError: If an invalid mode is provided.

    Returns:
    - None
    """

def writeline(path: str, data: str, mode: Optional[str] = 'a') -> None:
    """
    Write data to a file on a new line.

    Parameters:
    - path (str): The path to the file.
    - data (str): The data to be written to the file.
    - mode (str, optional): The mode in which the file is opened. 
      Defaults to 'a' (append). Other valid modes are 'w' (write).

    Raises:
    - ValueError: If an invalid mode is provided.

    Returns:
    - None
    """

def writelines(path: str, data_list: List[str], mode: Optional[str] = 'a') -> None:
    """
    Write a list of data to a file with each item on a new line.

    Parameters:
    - path (str): The path to the file.
    - data_list (List[str]): The list of data to be written to the file.
    - mode (str, optional): The mode in which the file is opened. 
      Defaults to 'a' (append). Other valid modes are 'w' (write).

    Raises:
    - ValueError: If an invalid mode is provided.

    Returns:
    - None
    """

def read(path: str) -> str:
    """
    Read data from a file.

    Parameters:
    - path (str): The path to the file.

    Returns:
    - str: The content of the file.

    If the file is not found, an empty string is returned.
    """

def readline(path: str) -> List[str]:
    """
    Read lines from a file.

    Parameters:
    - path (str): The path to the file.

    Returns:
    - List[str]: A list of lines from the file with newline characters removed.

    If the file is not found, an empty list is returned.
    """

def readlines(path: str) -> List[str]:
    """
    Read lines from a file.

    Parameters:
    - path (str): The path to the file.

    Returns:
    - List[str]: A list of lines from the file with newline characters removed.

    If the file is not found, an empty list is returned.
    """

def get_reader(path: str) -> Generator[str, None, None]:
    """
    Return a generator for reading lines from a file.

    Parameters:
    - path (str): The path to the file.

    Yields:
    - str: Lines from the file with newline characters removed.

    If the file is not found, the generator is empty.
    """
