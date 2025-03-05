from typing import Any


def calc_mean(args: Any) -> None:
    """
    Calculate and print the mean of a list of numbers.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    if not args:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    print(f'mean : {mean}')


def calc_median(args: Any) -> None:
    """
    Calculate and print the median of a list of numbers.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    if not args:
        print("ERROR")
        return
    median = sorted(args)[len(args) // 2]
    print(f'median : {median}')


def calc_quartile(args: Any) -> None:
    """
    Calculate and print the first and third quartiles of a list of numbers.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    if not args:
        print("ERROR")
        return
    quartile = []
    quartile.append(sorted(args)[len(args) // 4])
    quartile.append(sorted(args)[3 * len(args) // 4])
    print(f'quartile : {[f'{q:.1f}' for q in quartile]}')


def calc_std(args: Any) -> None:
    """
    Calculate and print the standard deviation of a list of numbers.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    if not args:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    std = (sum([(x - mean) ** 2 for x in args]) / len(args)) ** 0.5
    print(f'std : {std:.11f}')


def calc_var(args: Any) -> None:
    """
    Calculate and print the variance of a list of numbers.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    if not args:
        print("ERROR")
        return
    mean = sum(args) / len(args)
    var = sum([(x - mean) ** 2 for x in args]) / len(args)
    print(f'var : {var:.7f}')


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print various statistical measures for a list of numbers.

    This function calculates and prints the mean, median, quartiles,
    standard deviation, and variance of the provided list of numerical values.

    Args:
        args (list): A list of numerical values.

    Returns:
        None
    """
    get_function = {
        "mean": calc_mean,
        "median": calc_median,
        "quartile": calc_quartile,
        "std": calc_std,
        "var": calc_var
    }

    for value in kwargs.values():
        if value not in ["mean", "median", "quartile", "std", "var"]:
            return
        else:
            get_function[value](args)
