"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
   T_MAX = 10
# T_MAX is a constant denoting the starting value for counting down to 0.


   for i in range(T_MAX):
       print(T_MAX - i)
# This prints the constant, T_MAX and decreases the value by one each time the process is repeated.

   print("Liftoff!")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
