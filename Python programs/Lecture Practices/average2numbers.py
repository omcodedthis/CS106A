"""
File: average2numbers.py
------------------------
This program asks the user for two numbers
and prints their average.
"""

def main():
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))

# This use of shorthand converts the user input to a float as the number the user can input can also be a decimal.

   num3 = (num1 + num2) / 2
   print("The average is " + str(num3) + ".")

# This prints the desired answer, num3 is converted from a float to a string to be printed as text for the user.

if __name__ == '__main__':
    main()
# This calls the main function when the program is running.
