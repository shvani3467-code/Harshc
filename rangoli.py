#!/usr/bin/env python3
import sys
import random

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
reset = '\033[0m'

for line in sys.stdin:
    for char in line:
        if char == '\n':
            print(char, end='')
        else:
            print(random.choice(colors) + char + reset, end='')
