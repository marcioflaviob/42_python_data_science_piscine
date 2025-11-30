from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def zoom_and_gray(arr_rgb: np.ndarray, crop_size=(400, 400)) -> np.ndarray:
    """
    Crop the center region from arr_rgb and convert to grayscale.
    Returns a 2D array.
    """
    h, w = arr_rgb.shape[:2]
    crop_h, crop_w = crop_size

    start_y = max(0, (h - crop_h) // 2)
    start_x = max(0, (w - crop_w) // 2)

    cropped = arr_rgb[start_y:start_y + crop_h, start_x:start_x + crop_w]

    pil = Image.fromarray(cropped)
    gray = pil.convert("L")
    arr_gray = np.array(gray, dtype=np.uint8)

    return arr_gray


def main():
    path = "../animal.jpeg"
    arr = ft_load(path)
    print(f"The shape of the image is: {arr.shape}")
    print(arr)

    newArr = zoom_and_gray(arr, crop_size=(400, 400))
    print(f"New shape after slicing: (400, 400, 1) or {newArr.shape}")
    print(newArr)

    plt.imshow(newArr, cmap="gray", vmin=0, vmax=255)
    plt.show()


if __name__ == "__main__":
    main()
