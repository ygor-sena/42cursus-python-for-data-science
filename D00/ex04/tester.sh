#!/usr/bin/env bash

GREEN="\033[0;32m"
RESET="\033[0m"

commands=(
    "python3 whatis.py 14"
    "python3 whatis.py -5"
    "python3 whatis.py"
    "python3 whatis.py 0"
    "python3 whatis.py Hi!"
    "python3 whatis.py 13 5"
)

for cmd in "${commands[@]}"; do
    echo $cmd
    output=$(eval $cmd)
    echo -e "${GREEN}${output}${RESET}"
done
