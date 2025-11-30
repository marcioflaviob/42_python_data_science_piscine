from pathlib import Path
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image and print its shape and rgb values
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: {path}")
    img = Image.open(p).convert("RGB")
    return np.array(img, dtype=np.uint8)


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
