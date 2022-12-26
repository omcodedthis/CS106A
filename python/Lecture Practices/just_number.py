def main():
   user_string = input("This function extracts just the number from a piece of text, please enter some text: ")
   just_number_string = find_number(user_string)
   print(just_number_string)
# main() takes in the user input and assigns it to user_string, it is then passed when find_number(user_string) is
# called and just_number_string is printed.


def find_number(string):
    only_number = ''
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            only_number += ch
    return only_number
# find_number(string) creates a new string, only_number. A for loop goes through all the characters in user_string, if
# the character is a number, it gets added to only_number. This repeats for all characters and then is returned to
# just_number_string in main().

if __name__ == '__main__':
    main()