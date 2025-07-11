""" 
This task aims to design a password generator which ask user for
the length of the desired password and generates one
"""
import random
import string

def generate_password():
    print("Password Generator")
    print('-'*18)

    while True:
        try:
            length = int(input("Enter the desired length of the password --> "))
            if length <= 0:
                print("Password length must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for the length :) ")

    pass_ltr  = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(pass_ltr) for i in range(length))

    print(f"\nGenerated Password: {password}")

generate_password()