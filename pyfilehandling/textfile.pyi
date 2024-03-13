from typing import Dict, Any


class jsonFile:
    file: Any  # Placeholder for file object, type inferred

    def __init__(self, filename: str, mode: str = "r") -> None:
        """
        Initialize a textFile instance.

        Parameters:
        - filename (str): The name of the TEXT file.
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

    def read(self) -> str:
        """
        Read TEXT data from the file and return it as a string.

        Returns:
        - str: The data.
        """

    def write(self, data: str) -> None:
        """
        Write TEXT data to the file.

        Parameters:
        - data (str): The data to write to the file.

        Returns:
        - None
        """

    def close(self) -> None:
        """
        Close the file.

        Returns:
        - None
        """
