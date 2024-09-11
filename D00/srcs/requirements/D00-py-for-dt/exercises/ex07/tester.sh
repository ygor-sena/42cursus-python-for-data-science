#!/usr/bin/env bash

python3 sos.py "sos" | cat -e

python3 sos.py "SOS" | cat -e

python3 sos.py 'hell$o'
