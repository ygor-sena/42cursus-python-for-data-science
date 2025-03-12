from typing import Any


def callLimit(limit: int):
    """
    Limits the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the function can be called.

    Returns:
        Callable[[Callable], Callable]: A decorator that limits the number
        of calls to the function.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of calls to the function. It
        creates a closure around the original function.

        Args:
            function (Callable): The function to be limited.

        Returns:
            Callable: The wrapped function that enforces the call limit.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            The wrapped function that enforces the call limit.

            Args:
                *args (Any): Positional arguments for the function.
                **kwds (Any): Keyword arguments for the function.

            Returns:
                Any: The result of the function call if within limit,
                otherwise None.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1

            return function(*args, **kwds)
        return limit_function
    return callLimiter
