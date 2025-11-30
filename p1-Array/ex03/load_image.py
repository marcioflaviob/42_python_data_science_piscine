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
