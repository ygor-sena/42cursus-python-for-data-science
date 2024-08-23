import sys


def is_even_or_odd(nbr) -> None:
    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    args = len(sys.argv)
    if args < 2:
        sys.exit(0)
    if args > 2:
        raise AssertionError("more than one argument is provided")

    # If argv[1] is a string, it will raise ValueError exception
    nbr = int(sys.argv[1])
    is_even_or_odd(nbr)

except ValueError:
    print(f"{AssertionError.__name__}: argument is not an integer")
    sys.exit(1)
except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")
    sys.exit(1)
