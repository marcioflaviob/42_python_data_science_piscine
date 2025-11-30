import numpy as np
import matplotlib.pyplot as plt


def display_image(array: np.ndarray, title: str = "Image"):
    """
    Display the image and print its shape and array values.
    """
    print(f"The shape of image is: {array.shape}")
    print(array)
    plt.imshow(array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    Uses operators: =, +, -, *
    """
    inverted = 255 - array
    display_image(inverted, "Inverted")
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel, zeros out green and blue.
    Uses operators: =, *
    """
    red = array * [1, 0, 0]
    display_image(red, "Red Channel")
    return red


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel, zeros out red and blue.
    Uses operators: =, -
    """
    green = array - array * [1, 0, 1]
    display_image(green, "Green Channel")
    return green


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel, zeros out red and green.
    Uses operators: =
    """
    blue = array.copy()
    blue[:, :, 0] = 0  # Red channel
    blue[:, :, 1] = 0  # Green channel
    display_image(blue, "Blue Channel")
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale using average method.
    Uses operators: =, /
    """
    grey = (array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3)
    grey = np.stack([grey, grey, grey], axis=2).astype(array.dtype)
    display_image(grey, "Greyscale")
    return grey
