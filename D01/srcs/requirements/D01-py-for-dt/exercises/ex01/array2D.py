import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list (family) from start to end indices.

    Args:
        family (list): A 2D list to be sliced.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: The sliced 2D list.

    Raises:
        AssertionError: If family is not a list.
        AssertionError: If start and end are not integers.
        AssertionError: If family is not a 2D list with equal-length sublists.
    """
    if not isinstance(family, list):
        raise AssertionError("family must be of list type")
    if not (isinstance(start, int) and isinstance(end, int)):
        raise AssertionError("start and end must be of int type")
    if not all(len(f) == len(family[0]) for f in family):
        raise AssertionError("family must be a 2D list")

    family = np.array(family)
    print(f"My shape is : {family.shape}")

    sliced = family[start:end]
    print(f"My new shape is : {sliced.shape}")

    return sliced.tolist()
