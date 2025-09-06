# unique about this code is that it stores all the previously generated passwords.....
# also it askes for the length of password from user

import random
import string

passwords = []

while True:
    length = input("\n Enter the password length (or type 'q' to quit) : ")
    if length == "q":
        break
    length = int(length)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)

    passwords.append(password)
    print("\n New Password Generated \n :", password )
    print("\n All previous passwords so far \n :", passwords )
