import random

print('Lets play "Rock Paper Scissors"! What do you wanna go with?')

while True:
    choices = ["rock", "paper", "scissors"]

    computer_input = random.choice(choices)
    user_wins = 0
    computer_wins = 0
    tie = 0

    player_input = None

    while player_input not in choices:
        player_input = input("\nRock, Paper, or Scissors?: ").lower()

    print("\nRock, Papers, Scissors, Shoot!")

    if player_input == computer_input:
        print("Computer went for" , computer_input)
        print("You went with ", player_input)
        print("It's a TIE!")
        tie = tie + 1

    elif player_input == "rock":
        if computer_input == "paper":
            print("Computer went for" , computer_input)
            print("You went with", player_input)
            print("You lose!")
            computer_wins = computer_wins + 1
        if computer_input == "scissors":
            print("Computer went for" , computer_input)
            print("You went with", player_input)
            print("You win!")
            user_wins = user_wins + 1

    elif player_input == "paper":
        if computer_input == "rock":
            print("Computer went for" , computer_input)
            print("You went with", player_input)
            print("You win!")
            computer_wins = computer_wins + 1
        if computer_input == "scissors":
            print("Computer went for" , computer_input)
            print("You went with", player_input)
            print("You lose!")
            user_wins = user_wins + 1

    print('\n')
    print("The current stats for wins are:")
    print("Player:", user_wins)
    print("Computer:", computer_wins)
    print('Draws:', tie)

    if user_wins > computer_wins:
        print("\nYou are being the computer!")
    elif user_wins < computer_wins:
        print("\nThe computer is beating you!")
    else:
        print("\nYou are tied with the Computer!")

    replay = input("\nDo you want to play again? (Yes/No): ").lower()

    if replay != "yes":
        break
    elif replay != 'y':
        break

print("Thanks for playing! Goodbye!")