from typing import Dict, Any


class jsonFile:
    file: Any  # Placeholder for file object, type inferred

    def __init__(self, filename: str, mode: str = "r") -> None:
        """
        Initialize a jsonFile instance.

        Parameters:
        - filename (str): The name of the JSON file.
        - mode (str): The mode to open the file in (default is 'r' for read-only).

        Returns:
        - None
        """

    def __enter__(self) -> Any:
        """
        Enter the context manager and return the file object.

        Returns:
        - Any: The file object.
        """

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """
        Exit the context manager and close the file.

        Parameters:
        - exc_type: The exception type.
        - exc_value: The exception value.
        - exc_traceback: The traceback.

        Returns:
        - None
        """

    def read(self) -> Dict:
        """
        Read JSON data from the file and return it as a dictionary.

        Returns:
        - Dict: The JSON data.
        """

    def write(self, data: Dict, indent: int = 4) -> None:
        """
        Write JSON data to the file.

        Parameters:
        - data (Dict): The data to write to the file.
        - indent (int): The number of spaces to use for indentation (default is 4).

        Returns:
        - None
        """

    def read_key(self, key: str) -> Any:
        """
        Read a specific key from the JSON data.

        Parameters:
        - key (str): The key to read from the JSON data.

        Returns:
        - Any: The value associated with the key.
        """

    def close(self) -> None:
        """
        Close the file.

        Returns:
        - None
        """
