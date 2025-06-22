import numpy as np
from typing import Sequence
from PIL import Image
from utils import save_raw_data

def convert_image_to_ppm_data(image: Image.Image) -> Sequence[np.uint8]:
    """
    Converts a Pillow RGB image into a list of bytes conforming to the PPM (P6) binary format.

    The output list contains:
    - An ASCII header: "P6\n<width> <height>\n255\n"
    - Followed by binary RGB pixel data (one byte per channel, row-major order)

    Args:
        image (Image.Image): Input image in RGB mode.

    Returns:
        list[np.uint8]: Byte values representing the image in PPM P6 format.
    """
    # Convert the image to a NumPy array
    pixel_array: np.ndarray = np.asarray(image)

    # Build the ASCII header (text portion of the PPM format)
    width, height = image.size
    header: str = f"P6\n{width} {height}\n255\n"
    ppm_data: list[np.uint8] = [ord(char) for char in header]

    # Flatten the pixel array and append raw RGB bytes (3 per pixel)
    for row in pixel_array:
        for pixel in row:
            ppm_data.extend(pixel.tolist())  # pixel = [R, G, B]

    return ppm_data

if __name__ == "__main__":
    image_path = "data/images/image_1.jpg"
    image: Image.Image = Image.open(image_path).convert("RGB")  # Ensure RGB mode

    ppm_binary_data = convert_image_to_ppm_data(image)
    save_raw_data(ppm_binary_data)
