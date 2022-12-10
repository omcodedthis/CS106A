"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    NUM_RANDOM = 10
    MIN_RANDOM = 0
    MAX_RANDOM = 100
# This is to define and assign values to the constants desired.


    for i in range(NUM_RANDOM):
        num = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(num)

# The random.randint function will pick a random integer between the range denoted by the values of
# MIN_RANDOM & MAX_RANDOM, repeating this process 10 times as 10 integers is desired.





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
