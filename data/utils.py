import os
from typing import Sequence
from numpy import uint8

def save_raw_data(raw_data: Sequence[uint8], file_path: str = "data/raw_data/image.ppm") -> None:
    """
    Saves a list of raw bytes (uint8 values) to a binary file.

    This function is typically used to save image data in binary formats such as PPM (P6).
    It ensures that the output is written as pure binary, without encoding transformations.

    Args:
        raw_data (Sequence[uint8]): A flat sequence of uint8 values representing raw data (e.g., image).
        file_path (str): Path to the output file. Defaults to "data/raw_data/image.ppm".

    Raises:
        ValueError: If raw_data is empty or contains invalid types.
        OSError: If the file or directory cannot be written.
    """
    if not raw_data:
        raise ValueError("raw_data is empty. Cannot save an empty file.")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "wb") as file:
            file.write(bytes(raw_data))
    except OSError as e:
        raise OSError(f"Failed to write file: {file_path}") from e
