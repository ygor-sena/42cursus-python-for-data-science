from give_bmi import give_bmi, apply_limit

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Subject test cases
height = [2.71, 1.15]
weight = [165.3, 38.4]

try:
    print(f"{GREEN}TEST 01 - Successful case:{RESET}")
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")


height = [2.71, 1.15, 4.5]
weight = [165.3, 38.4]

try:
    print(f"{RED}TEST 02 - Different length lists:{RESET}")
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")


height = (2.71, 1.15)
weight = [165.3, 38.4]

try:
    print(f"{RED}TEST 03 - height is a tuple:{RESET}")
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")


height = [2.71, 1.15, 1.70]
weight = [165.3, 38.4, "40.0"]

try:
    print(f"{RED}TEST 04 - weight has a string element:{RESET}")
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")


height = [2.71, 1.15]
weight = [165.3, 38.4]

try:
    print(f"{RED}TEST 05 - Limit is a string:{RESET}")
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, "26"))

except AssertionError as e:
    print(f"{AssertionError.__name__}: {e}")
