#!/usr/bin/env python

from ft_filter import ft_filter

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

strings = ["Hello", "", "Python", "is", "fun"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("------------------------ [PART 1: FT_FILTER] -------------------------")
# Test with both None and lambda function as first parameter
print(f'{RED}[PYTHON3]{RESET}', end="\n")
print(list(filter(None, strings)))
print(list(filter(lambda x: x % 2 == 0, numbers)), end="\n\n")

print(f'{GREEN}[RECODED]{RESET}', end="\n")
print(list(ft_filter(None, strings)))
print(list(ft_filter(lambda x: x % 2 == 0, numbers)), end="\n\n")

# Test output docs of the original and recoded function
print(f'{RED}[PYTHON3]{RESET}\n{filter.__doc__}', end="\n\n")
print(f'{GREEN}[RECODED]{RESET}\n{ft_filter.__doc__}', end="\n\n")
