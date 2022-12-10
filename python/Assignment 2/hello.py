"""
File: hello.py
------------------
Prompts user for their name and then says hello!
"""


def main():
    user_name = input("What is your name?: ")
    print("Hello " + str(user_name) + "!")

# This section asks for the user_name and is then stored in the variable user_name, it is then printed after the word
# "Hello" to greet the user.


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
