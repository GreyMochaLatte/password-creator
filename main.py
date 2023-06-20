import random
import string
# from tkinter import *

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
options = [lowercase, uppercase, numbers, symbols]


def save_standard_password():
    length = 0
    password = ""
    while length < 30:
        character_type = random.choice(options)
        character = random.choice(character_type)
        password += character
        length += 1
    return password


def save_custom_password():
    length = 0
    password = ""
    requirements = []
    max_length = input("How long does the password need to be? ")
    max_length = int(max_length)
    min_lowercase = input("What's the minimum number of lowercase letters required? ")
    min_lowercase = int(min_lowercase)
    if min_lowercase > 0:
        requirements.append(lowercase)
    min_uppercase = input("What's the minimum number of uppercase letters required? ")
    min_uppercase = int(min_uppercase)
    if min_uppercase > 0:
        requirements.append(uppercase)
    min_numbers = input("What's the minimum number of numbers required? ")
    min_numbers = int(min_numbers)
    if min_numbers > 0:
        requirements.append(numbers)
    min_symbols = input("What's the minimum number of symbols required? ")
    min_symbols = int(min_symbols)
    if min_symbols > 0:
        requirements.append(symbols)
    while length < max_length:
        if len(requirements) > 0:
            character_type = random.choice(requirements)
            character = random.choice(character_type)
            password += character
            length += 1
            if character_type == lowercase:
                min_lowercase -= 1
                if min_lowercase == 0:
                    requirements.remove(lowercase)
            elif character_type == uppercase:
                min_uppercase -= 1
                if min_uppercase == 0:
                    requirements.remove(uppercase)
            elif character_type == numbers:
                min_numbers -= 1
                if min_numbers == 0:
                    requirements.remove(numbers)
            else:
                min_symbols -= 1
                if min_symbols == 0:
                    requirements.remove(symbols)
        else:
            character_type = random.choice(options)
            character = random.choice(character_type)
            password += character
            length += 1
    return password


def update_standard_password(account):
    password_file = open("Papa's Apple Pie Recipe.txt", "a+")
    for line in password_file:
        if line.startswith(account):
            password = save_standard_password()
            password_file.write(account + ": " + password + "\n")
            return password
    password_file.close()


def update_custom_password(account):
    password_file = open("Papa's Apple Pie Recipe.txt", "a+")
    for line in password_file:
        if line.startswith(account):
            password = save_custom_password()
            password_file.write(account + ": " + password + "\n")
            return password
    password_file.close()


def find_password(account):
    password_file = open("Papa's Apple Pie Recipe.txt", "r")
    for line in password_file:
        if line.startswith(account):
            return line
    password_file.close()


task = input("Would you like to 'save', 'update', or 'find' a password?  ")
if task == "save":
    account = input("What account is the password for?  ")
    account = account.capitalize()
    password_type = input("Would you rather create a 'standard' or 'custom' password?  ")
    password_type.lower()
    if password_type == "standard":
        password_file = open("Papa's Apple Pie Recipe.txt", "a")
        password_file.write(account + ": " + save_standard_password() + "\n")
        print(f"Your password for {account} has successfully been saved")
        password_file.close()
        print(find_password(account))
    elif password_type == "custom":
        password_file = open("Papa's Apple Pie Recipe.txt", "a")
        password_file.write(account + ": " + save_custom_password() + "\n")
        print(f"Your password for {account} has successfully been saved")
        password_file.close()
        print(find_password(account))
    else:
        print("That's not an available response")
elif task == "update":
    account = input("What account is the password for?  ")
    account = account.capitalize()
    update_type = input("Would you like to update it with a 'standard' or 'custom' password?  ")
    if update_type == "standard":
        update_standard_password(account)
        print(f"Your password for {account} has successfully been updated")
        print(find_password(account))
    elif update_type == "custom":
        update_custom_password(account)
        print(f"Your password for {account} has successfully been updated")
        print(find_password(account))
    else:
        print("That's not an available response")
elif task == "find":
    account = input("What account do you want the password for? ")
    account = account.capitalize()
    print(find_password(account))
else:
    print("That's not an available response")

# create class for password and use class for to initialize each new password
# intercept repeated accounts when creating password
# allow program to update passwords
# add system with access to website storage. leave file system as backup
# check file system to ensure website system correct
