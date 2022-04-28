import random
import string

print('Welcome to the Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@&#$%^&*().,?0123456789'

passwordAmount = input("Enter the amount of passwords to generate:")
passwordAmount = int(passwordAmount)

length = input("Enter the length of your password(s):")
length = int(length)
passwords = ''

if passwordAmount == 1:
    for pwd in range(passwordAmount):
        print('\nHere is your password:')
        for x in range(length):
            passwords += random.choice(chars)
        print(passwords)

else :
    print('\nHere are your passwords')
    for pwd in range(passwordAmount):
        for x in range(length):
            passwords += random.choice(chars)
        passwords += "\n"
        print(passwords)