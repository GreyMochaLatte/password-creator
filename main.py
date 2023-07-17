import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
options = [lowercase, uppercase, numbers, symbols]

def save_standard_password(account):
    length = 0
    password = ""
    while length < 30:
        character_type = random.choice(options)
        character = random.choice(character_type)
        password += character
        length += 1
    password_file = open("Papa's Apple Pie Recipe.txt", "a")
    password_file.write(account + ": " + password + "\n")
    print(f"Your password for {account} has successfully been saved")
    password_file.close()
    print(find_password(account))
    return password

def save_custom_password(account):
    length = 0
    password = ""
    requirements = []
    max_length = int(input("How long does the password need to be? "))
    if max_length == 0:
        print("A password with zero length cannot be created. ")
    min_lowercase = int(input("What's the minimum number of lowercase letters required? "))
    if min_lowercase > 0:
        requirements.append(lowercase)
    min_uppercase = int(input("What's the minimum number of uppercase letters required? "))
    if min_uppercase > 0:
        requirements.append(uppercase)
    min_numbers = int(input("What's the minimum number of numbers required? "))
    if min_numbers > 0:
        requirements.append(numbers)
    min_symbols = int(input("What's the minimum number of symbols required? "))
    if min_symbols > 0:
        requirements.append(symbols)
    if min_lowercase + min_uppercase + min_numbers + min_symbols > max_length:
        print("total minimum requirements exceed the maximum password length. ")
    else:
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
        password_file = open("Papa's Apple Pie Recipe.txt", "a")
        password_file.write(account + ": " + password + "\n")
        print(f"Your password for {account} has successfully been saved")
        password_file.close()
        print(find_password(account))
        return password

def update_standard_password(account):
    lines = []
    password_list = open("Papa's Apple Pie Recipe.txt", "r")
    for line in password_list:
        lines.append(line)
    password_list.close()
    password_file = open("Papa's Apple Pie Recipe.txt", "w")
    indx = 0
    for line in lines:
        if account in line:
            save_custom_password(account)
        else:
            password_file.write(lines[indx])
        indx += 1
    password_file.close()

def update_custom_password(account):
    lines = []
    password_list = open("Papa's Apple Pie Recipe.txt", "r")
    for line in password_list:
        lines.append(line)
    password_list.close()
    password_file = open("Papa's Apple Pie Recipe.txt", "w")
    indx = 0
    for line in lines:
        if account in line:
            save_standard_password(account)
        else:
            password_file.write(lines[indx])
        indx += 1
    password_file.close()

def find_password(account):
    password_file = open("Papa's Apple Pie Recipe.txt", "r")
    for line in password_file:
        if line.startswith(account):
            return line
    password_file.close()


task = input("Would you like to 'save', 'update', or 'find' a password?  ")
if task == "save" or "s":
    account = input("What account is the password for?  ")
    account = account.capitalize()
    password_exists = find_password(account)
    if password_exists is not None:
        print("There already exists a password for that account. ")
        print(find_password(account))
    password_type = input("Would you rather create a 'standard' or 'custom' password?  ")
    password_type.lower()
    if password_type == "standard" or "s":
        save_standard_password(account)
    elif password_type == "custom" or "c":
        save_custom_password(account)
    else:
        print("That's not an available response")
elif task == "update" or "u":
    account = input("What account is the password for?  ")
    account = account.capitalize()
    password_not_exists = find_password(account)
    if password_not_exists is None:
        print("A password for that account does not exist yet. ")
    update_type = input("Would you like to update it with a 'standard' or 'custom' password?  ")
    if update_type == "standard" or "s":
        update_standard_password(account)
        print(f"Your password for {account} has successfully been updated")
        print(find_password(account))
    elif update_type == "custom" or "c":
        update_custom_password(account)
        print(f"Your password for {account} has successfully been updated")
        print(find_password(account))
    else:
        print("That's not an available response")
elif task == "find" or "f":
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
# for custom check if password length and total of characters match
