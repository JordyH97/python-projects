import random

print("I'm thinking of a number between 1 and 10...")

#Sets numbers
randNum = random.randrange(1, 11)
guess = input("What's your number? ")
guess = int(guess)

#Uses Loop to Check if Number is correct
if guess <= 0:
    print("Please type another number that is greater than 0 and try again.")

elif guess > 10:
    print("Please type another number that is less than 10 and try again.")

elif guess == randNum :
    print("I picked:", randNum)
    print("You got it right!")

else :
    print("I picked:", randNum)
    print("You got it wrong! Try again next time!")