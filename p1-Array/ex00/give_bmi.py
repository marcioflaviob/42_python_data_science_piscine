
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI
    """
    results = []
    if len(height) != len(weight):
        raise ValueError("arrays must have the same length")
    for i in range(len(height)):
        h = height[i]
        w = weight[i]
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("height and weight must be numbers")
        if h == 0 or w == 0:
            raise ValueError("values must be non-zero")
        results.append(w / (h * h))
    return results


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if numbers in an array are higher than limit
    """
    if type(limit) is not int:
        raise TypeError("limit must be a number")
    results = []
    for i in range(len(bmi)):
        value = bmi[i]
        if not isinstance(value, (int, float)):
            raise TypeError("bmi values must be numbers")
        results.append(value > limit)
    return results
