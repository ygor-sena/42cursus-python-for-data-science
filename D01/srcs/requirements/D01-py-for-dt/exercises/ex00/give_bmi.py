import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI for a list of heights and weights.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of BMI values.

    Raises:
        AssertionError: If arguments are not lists.
        AssertionError: If arguments do not have the same number of elements.
        AssertionError: If arguments are not lists of integers or floats.
    """
    if not (isinstance(height, list) and isinstance(weight, list)):
        raise AssertionError("height and weight must be lists")
    if len(height) != len(weight):
        raise AssertionError("height and weight " +
                             "must have the same number of elements")
    if not all(isinstance(h, (int, float)) for h in height) or \
       not all(isinstance(w, (int, float)) for w in weight):
        raise AssertionError("height and weight " +
                             "must be lists of integers or floats")

    height = np.array(height)
    weight = np.array(weight)

    return (weight / (height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check a list of BMI values to determine if they exceed the limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The BMI limit.

    Returns:
        list[bool]: A list of boolean values indicating if
                    each BMI exceeds the limit.

    Raises:
        AssertionError: If bmi is not a list.
        AssertionError: If bmi is not a list of integers or floats.
        AssertionError: If limit is not an integer.
    """
    if not isinstance(bmi, list):
        raise AssertionError("bmi must be a list")
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise AssertionError("bmi must be a list of integers or floats")
    if not isinstance(limit, int):
        raise AssertionError("limit must be an integer")

    bmi_np = np.array(bmi)

    return (bmi_np > limit).tolist()
