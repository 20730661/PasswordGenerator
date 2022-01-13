#!/bin/python3

import math
import random
import string

import sys

print("------------------------------------------------------------")
print("Password Generator")
print("Made By 20730661")
print("------------------------------------------------------------")

def main():
    charlist = ""
    user_input = input("Do you want uppercase letters? [Y/n] ")
    if user_input != "n":
        charlist += string.ascii_uppercase

    user_input = input("Do you want lowercase letters? [Y/n] ")
    if user_input != "n":
        charlist += string.ascii_lowercase

    user_input = input("Do you want numbers? [Y/n] ")
    if user_input != "n":
        charlist += string.digits

#     user_input = input("do you want numvers? [Y/n] ")
#     if user_input != "n":
#         charlist += string.digits

    user_input = input("Do you want speical characters? [Y/n] ")
    if user_input != "n":
        charlist += string.punctuation

    user_input = input("Do you want to add custom characters? [y/N] ")
    if user_input == "y":
        user_input = input("enter the character(s) that you want do add: ")
        charlist += user_input

    user_input = input("How long do you want the password to be? [10] ")

    # if length of user_input is 0 then default password_length to 10

    password_length = 10
    if len(user_input) > 0 and user_input.isdigit() and int(user_input) > 0:
        password_length = int(user_input)
    else:
        print("your input is invalid, so the password length has been set to the default value which is 10.")

    password_output = ''.join(random.choices(charlist, k=password_length))

    print("")
    print(f"your password with {password_length} characters:")
    print(password_output)
    print("***please record your password somewhere as it is not recorded.***")

if __name__ == "__main__":
    main()

print("------------------------------------------------------------")
