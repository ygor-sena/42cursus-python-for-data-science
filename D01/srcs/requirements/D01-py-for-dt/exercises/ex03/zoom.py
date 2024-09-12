from load_image import ft_load, Image, np
from matplotlib import pyplot as plt


def ft_zoom() -> None:
    """
    Zooms into a specific region of an image, converts it to grayscale,
    and displays it.

    This function performs the following steps:
    1. Loads an image from a specified path.
    2. Crops the image to a specific region.
    3. Converts the cropped image to grayscale.
    4. Prints the new shape of the image.
    5. Displays the grayscale image using Matplotlib.

    Returns:
        None
    """
    img = Image.fromarray(ft_load("imgs/animal.jpeg"))
    img = img.crop((450, 100, 850, 500))
    img = img.convert('L')

    img_width, img_height = img.size

    print("New shape after slicing: ({0}, {1}, {2}) or ({0}, {1})".format(
            img_width, img_height, len(img.getbands())))
    print(np.array(img))

    plt.imshow(img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    ft_zoom()
