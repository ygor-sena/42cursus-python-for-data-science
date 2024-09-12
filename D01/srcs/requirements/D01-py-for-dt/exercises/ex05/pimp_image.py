from load_image import np
from matplotlib import pyplot as plt


def ft_invert(array) -> None:
    """
    Inverts the colors of the image received.
    """
    img = np.array(array)
    inverted = 255 - img

    plt.imshow(inverted)
    plt.show()


def ft_red(array) -> None:
    """
    Applies a red filter to the image received.
    """
    red = np.zeros_like(array)

    red[..., 0] = array[..., 0]

    plt.imshow(red)
    plt.show()


def ft_green(array) -> None:
    """
    Applies a green filter to the image received.
    """
    green = np.zeros_like(array)

    green[..., 1] = array[..., 1]

    plt.imshow(green)
    plt.show()


def ft_blue(array) -> None:
    """
    Applies a blue filter to the image received.
    """
    blue = np.zeros_like(array)

    blue[..., 2] = array[..., 2]

    plt.imshow(blue)
    plt.show()


def ft_grey(array) -> None:
    """
    Applies a grey filter to the image received.
    """
    weighted = array / 3
    grey = weighted.sum(axis=2)

    plt.imshow(grey, cmap="gray")
    plt.show()
