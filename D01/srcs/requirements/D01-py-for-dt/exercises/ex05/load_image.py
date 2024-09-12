import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified file path and convert it to a NumPy array.

    Args:
        path (str): The file path to the image. Must be a string ending
        with '.jpg' or '.jpeg'.

    Returns:
        np.ndarray: The image as a NumPy array.

    Raises:
        AssertionError: If the path is not a string or does not end with
                        '.jpg' or '.jpeg'.
        FileNotFoundError: If the file at the specified path does not exist.
        IOError: If the file cannot be opened or read.
    """
    if not isinstance(path, str):
        raise AssertionError("path must be of string type")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise AssertionError(f"invalid file format: '{path}'")
    try:
        with Image.open(path) as img:
            im_array = np.array(img)
    except FileNotFoundError:
        raise FileNotFoundError(f"no such file: '{path}'")
    except IOError:
        raise IOError(f"cannot open or read the file: '{path}'")

    print(f"The shape of image is: {im_array.shape}")
    print(im_array)

    return im_array
