
def slice_me(family: list, start: int, end: int) -> list:
    """
    Slide a 2D array
    """
    if (not isinstance(family, list) or not isinstance(start, int) or
            not isinstance(end, int)):
        raise TypeError("argument types are not correct")
    if len(family) == 0:
        rows, cols = 0, 0
    else:
        rows = len(family)
        cols = len(family[0])
        if not all(isinstance(row, list) for row in family):
            raise TypeError("argument types are not correct")
        if not all(len(row) == cols for row in family):
            raise TypeError("argument types are not correct")
    print(f"My shape is : ({rows}, {cols})")
    new = family[start:end]
    new_rows = len(new)
    print(f"My new shape is : ({new_rows}, {cols})")
    return new
