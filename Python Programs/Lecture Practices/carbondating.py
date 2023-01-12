"""
File: calculateage.py
------------------
This program runs carbon dating (how cool!)
The ratio of normal carbon (carbon-12) to carbon-14 in the air
and in all living things at any given time is nearly constant.
Maybe one in a trillion carbon atoms are carbon-14. Carbon-12 is
stable, but Carbon-14 decays with a half-life of approximately
5,730 years. After the organism dies it stops taking in new carbon.
"""
import math

HALF_LIFE = 5730
HALF_LIFE_CONSTANT = HALF_LIFE / math.log(0.5)


def main():
    print("This program calculates the age of a single sample using the percentage of C-14.")
    while True:
        calculate_sample_age()

# main() lets the user know that it is able to calculate the age of a sample using the percentage of C-14.

def calculate_sample_age():
    age1 = float(input("Enter the percentage of Carbon-14 in the sample: "))
    age2 = HALF_LIFE_CONSTANT * (math.log(age1/100))
    print("The age of the sample is " + str(age2) + ".")

# calculate_sample_age uses the given percentage and inputs in a given formula of age = K * log(%age/100) to calculate
# the expected age of the sample.



if __name__ == '__main__':
    main()