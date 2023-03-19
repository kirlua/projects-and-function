import random

import easygui

player_one = easygui.enterbox("Enter the name of player 1","Yahtzee game")
player_one_dice = ""
player_two = easygui.enterbox("Enter the name of player 2", "Yahtzee game")
player_two_dice = ""
dice = ["1","2","3","4","5","6"]
easygui.msgbox("Please roll the dice", "Error")

while player_one_dice == "" or player_two_dice == "":

        player_one_dice = random.choice(dice)

        player_two_dice = random.choice(dice)
print(f"{player_one} scores {player_one_dice}")
print(f"{player_two} scores {player_two_dice}")
if player_one_dice == player_two_dice:
    result = "This was a draw"
elif player_one_dice > player_two_dice:
    result = (f"{player_one} beats {player_two}")
else:
    result = (f"{player_two} beats {player_one}")

print(result)

