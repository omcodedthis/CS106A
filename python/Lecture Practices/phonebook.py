"""
File: phonebook.py
------------------
Program to show an example of using dictionaries to maintain
a phonebook.
"""


def main():
    phonebook = get_user_numbers()
    print_phonebook(phonebook)
    user_lookup(phonebook)
# main() gets the names & number from the users, forming pairs in a dictionary. This is then assigned to phonebook.
# The pairs are printed for the user. The user then can look up any name in the list to retrieve its respective
# number.



def get_user_numbers():
    print("Enter the name and its corresponding number to add your phone book, enter a space after you are done.")
    phonebook ={}
    while True:
        name = input("Enter a name: ")
        if name == " ":
            break
        number = input("Enter the number: ")
        phonebook[name] = number
    return phonebook
# get_user_numbers() creates an empty dictionary, named phonebook. The names and numbers are inputted which are stored
# as pairs in phonebook. When a space is entered, the while True loop ends and phonebook returns to main().



def print_phonebook(phonebook):
    for key in phonebook.keys():
        print(str(key) + " -> " + str(phonebook[key]))
# print_phonebook(phonebook) prints the key & its respective value for the user to see.




def user_lookup(phonebook):
    while True:
        find = input("Enter the name to get their number or a space to end the program: ")
        if find == " ":
            break
        if find in phonebook:
            print(phonebook.get(find))

        if find not in phonebook:
            print("This contact is not in your phone book.")
# user_lookup(phonebook) assigns the users input to find. If find is a key in phonebook, its respective value is
# printed. Otherwise, "This contact is not in your phone book." is printed. Once a space is entered, the program ends.











# Python boilerplate.
if __name__ == '__main__':
    main()
