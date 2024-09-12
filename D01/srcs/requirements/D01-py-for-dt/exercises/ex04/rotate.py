from load_image import Image, np
from zoom import ft_zoom
from matplotlib import pyplot as plt


def tranpose_matrix(np_img: list) -> list:
    """
    Transposes a 2D list (matrix) representing an image.

    This function rotates the image 90 degrees clockwise by transposing
    the matrix.

    Args:
        np_img (list): A 2D list representing the image to be transposed.

    Returns:
        list: A 2D list representing the transposed image.
    """
    rows = len(np_img)
    cols = len(np_img[0])

    rotated_image = [[[0, 0, 0] for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_image[cols - 1 - j][i] = np_img[i][j]

    return rotated_image


def ft_rotate() -> None:
    """
    Rotates an image 90 degrees clockwise and displays it.

    This function performs the following steps:
    1. Loads and processes an image using the ft_zoom function.
    2. Converts the image to a numpy array and then to a list (matrix).
    3. Transposes the matrix to rotate the image 90 degrees clockwise.
    4. Converts the rotated matrix back to an image.
    5. Displays the rotated image using Matplotlib.

    Returns:
        None
    """
    img = ft_zoom()
    np_img = np.array(img).tolist()

    rotated_image = tranpose_matrix(np_img)
    new_img = Image.fromarray(np.array(rotated_image, dtype=np.uint8))

    print(f"New shape after Transpose: ({img.size[0]}, {img.size[1]})")
    print(np.array(img))

    plt.imshow(new_img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    ft_rotate()
