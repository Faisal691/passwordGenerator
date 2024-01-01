import random
import string

def generate_password(min_length, numbers = True, special_chars = True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    a = [1,2,3]
    pwd = ''
    while  len(pwd) < min_length:
        choice = random.choice(a)
        if choice == 1:
            char = random.choice(letters)
        elif choice == 2 and numbers == True:
            char = random.choice(digits)
        elif choice == 3 and special_chars == True:
            char = random.choice(special_characters)
        pwd += char
    return pwd
min_length = int(input('Enter the min. length for your Password :   '))
num = input('Do you want numbers in your Password -  (Y/N)').lower() == 'y'
char = input('Do you wnat special characters in your Password -  (Y/N)').lower() == 'y'
print()
print(generate_password(min_length,num,char))