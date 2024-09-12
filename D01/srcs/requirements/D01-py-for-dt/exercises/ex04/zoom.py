from load_image import ft_load, Image, np


def ft_zoom() -> Image:
    """
    Zooms into a specific region of an image, converts it to grayscale,
    and displays it.

    Returns:
        Image: The processed grayscale image.
    """
    img = Image.fromarray(ft_load("imgs/animal.jpeg"))
    img = img.crop((450, 100, 850, 500))
    img = img.convert('L')

    img_width, img_height = img.size

    print("The shape of the image is: ({0}, {1}, {2}) or ({0}, {1})".format(
            img_width, img_height, len(img.getbands())))
    print(np.array(img))

    return img
