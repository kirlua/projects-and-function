import easygui
import random

while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)
    play_again = easygui.buttonbox("Welcome to Rock, Paper, Scissors\n\n"
                                   "Rock beats scissors\n"
                                   "Scissors beats paper\n"
                                   "Paper beats rock\n"
                                   "Do you want to play\n"
                                   "Welcome and Rules", choices=["Yes", "No"])
    if play_again == "No":
        break
    else:
        player = easygui.buttonbox("Choose your weapon", "Choose weapon",
                                   choices=[weapons[0], weapons[1],
                                   weapons[2]])
        easygui.msgbox(f"You chose {player} and the computer "
                       f"chose {computer}", "choice")

        if computer == player:
            result == "This was a draw"
        elif computer == "Paper" and player == "Rock" or \
                computer == "Scissors" and player == "Paper" or \
                computer == "Rock" and player == "Scissors":
            result = "You lose"
        else:
            result = "You win"

        easygui.msgbox(f"{result}")
    print("Goodbye")





