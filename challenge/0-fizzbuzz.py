#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: ./0-fizzbuzz.py <max_number>")
    sys.exit(1)

try:
    max_number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid number.")
    sys.exit(1)

for i in range(1, max_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

print()  # for a newline at the end
