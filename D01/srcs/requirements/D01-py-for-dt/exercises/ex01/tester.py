from array2D import slice_me

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Subject test cases
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(f"{GREEN}TEST 01 - Successful case:{RESET}")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")

try:
    print(f"{RED}TEST 02 - Start/end is not an integer:{RESET}")
    print(slice_me(family, "0", 7))
except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")

# Test case where list is not a 2D list
bad_family = [[1.80, 78.4, 75.5],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

try:
    print(f"{RED}TEST 03 - Family list is not a 2D list:{RESET}")
    print(slice_me(bad_family, 0, 2))
except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")

# Test case where list is not of list type
t_family = ([1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2])

try:
    print(f"{RED}TEST 04 - Family list is not of list type:{RESET}")
    print(slice_me(t_family, 0, 2))
except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")
