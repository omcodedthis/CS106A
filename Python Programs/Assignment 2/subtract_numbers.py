"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from the other.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The result is " + str(result) + ".")

# main() takes the input of two numbers, converting to type float from the user assigning them to num1 & num2
# respectively. The variable named "result" is the result of the subtraction of num2 from num1. It is then printed, by
# converting the result to a str type.



if __name__ == '__main__':
    main()
