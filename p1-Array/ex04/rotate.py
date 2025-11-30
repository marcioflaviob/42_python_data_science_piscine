from load_image import ft_load, zoom_and_gray
import numpy as np
import matplotlib.pyplot as plt


def rotate(arr: np.ndarray) -> np.ndarray:
    """
    Rotate the image 90 degrees counter-clockwise using transpose.
    """
    return np.transpose(arr)[::-1]


def main():
    path = "../animal.jpeg"
    arr = ft_load(path)
    zoomArr = zoom_and_gray(arr, crop_size=(400, 400))
    print(f"New shape after slicing: (400, 400, 1) or {zoomArr.shape}")
    print(zoomArr)

    transposedArr = rotate(zoomArr)
    print(f"New shape after Transpose: {transposedArr.shape}")
    print(transposedArr)

    plt.imshow(transposedArr, cmap="gray", vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()
