def square(x: int | float) -> int | float:
    """
    Returns the square of a number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number.
    """
    result = x * x
    return result


def pow(x: int | float) -> int | float:
    """
    Returns the number raised to the power of itself.

    Args:
        x (int | float): The base number.

    Returns:
        int | float: The result of raising the base number to the
        power of itself.
    """
    result = x ** x
    return result


def outer(x: int | float, function) -> object:
    """
    Creates a closure that applies a function to a value multiple times.

    Args:
        x (int | float): The initial value.
        function (Callable): The function to be applied.

    Returns:
        Callable: A function that applies the given function to the
        value multiple times.
    """
    count = 0

    def inner() -> float:
        """
        Applies the function to the value a number of times equal to the
        count of calls.

        Returns:
            float: The result after applying the function multiple times.
        """
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner
