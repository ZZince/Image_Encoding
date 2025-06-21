import numpy as np
from PIL import Image
from utils import merge, save_raw_data

def get_raw_data(image: Image) -> list[np.uint8]:
    """Return a generator of pixels in the image

    Args:
        image (Image): RGB image from pillow

    Return: List of uint(0-255) for earch color value in image
    """
    array: np.ndarray = np.asanyarray(image)
    raw_data: list[np.uint8] = []
    def get_generator():
        for pixel in array:
            yield pixel

    for height in get_generator():
        for pixel in height:
            temp_data = [color for color in pixel]
            merge(raw_data, temp_data)

    return raw_data

if __name__ == "__main__":
    image: Image.Image = Image.open("data/images/image_1.jpg")
    raw_data = get_raw_data(image=image)

    save_raw_data(raw_data)