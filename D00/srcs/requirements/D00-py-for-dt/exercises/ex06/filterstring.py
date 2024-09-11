import sys


def get_input() -> str:
    """
    Get input from the user or command line arguments.

    Returns:
        str: The input message.
    Raises:
        AssertionError: If the number of arguments is invalid.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    elif sys.argv[1].isdigit():
        raise AssertionError("the arguments are bad")
    else:
        msg = sys.argv[1]
    return msg


def main() -> None:
    """
    Filter words from a string based on the length of the word.

    Raises:
        SystemExit: If there is an assertion error in getting input.
    """
    try:
        msg = get_input().split()
    except AssertionError as e:
        print(f'{AssertionError.__name__}: {e}')
        sys.exit(1)

    print([word for word in msg if len(word) > int(sys.argv[2])])


if __name__ == '__main__':
    main()
