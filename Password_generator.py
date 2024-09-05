import random
import string


def password_generator(min_lenth, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenth:
        new_character = random.choice(characters)
        pwd += new_character

        if new_character in digits:
            has_number = True
        if new_character in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        elif special_char:
            meets_criteria = meets_criteria and has_special

    return pwd


lenth = int(input("Enter the minimum lenth: "))
has_number = input("Do you want to add number?(y/n): ").lower() == "y"
has_special = input("Do you want to add special characters?(y/n): ").lower() == "y"
pwd = password_generator(lenth, has_number, has_special)
print(pwd)
