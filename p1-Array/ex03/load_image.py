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
    try:
        img = Image.open(p).convert("RGB")
        arr = np.array(img, dtype=np.uint8)
    except Exception as e:
        raise ValueError(f"Could not load image: {e}")
    print(f"The shape of the image is: {arr.shape}")
    return arr
