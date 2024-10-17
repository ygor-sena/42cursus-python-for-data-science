import sys


def get_input() -> str:
    """
    Get input from the user or command line arguments.

    Returns:
        str: The input message.
    Raises:
        AssertionError: If the number of arguments is invalid.
    """
    args = len(sys.argv)
    if args > 2:
        raise AssertionError("invalid number of arguments")
    if args < 2:
        print("What is the text to count?")
        msg = sys.stdin.readline()
    else:
        msg = sys.argv[1]
    return msg


def main() -> None:
    """
    Main function to count different types of characters in the input message.

    Raises:
        AssertionError: If the number of arguments is invalid.
    """
    try:
        msg = get_input()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        sys.exit(1)

    PUNCT_MARKS = "!\"'-()./:,;?…"

    upper = sum(1 for c in msg if c.isupper())
    lower = sum(1 for c in msg if c.islower())
    punct = sum(1 for c in msg if c in PUNCT_MARKS)
    space = sum(1 for c in msg if c.isspace())
    digit = sum(1 for c in msg if c.isdigit())

    print(f'\nThe text contains {len(msg)} characters:\n' +
          f'{upper} upper letters\n' +
          f'{lower} lower letters\n' +
          f'{punct} punctuation marks\n' +
          f'{space} spaces\n' +
          f'{digit} digits')


if __name__ == "__main__":
    main()
