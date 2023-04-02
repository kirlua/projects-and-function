import easygui
import random

players = []

player1 = easygui.enterbox(f"Enter the name of player 1:", "Player 1")
player2 = easygui.enterbox(f"Enter the name of player 2:", "Player 2")

# Add player names to player list with a score of 0
players.append([player1,0])
players.append([player2,0])

# continuous loop which runs rounds until player elects not to play again
while True:
    for player in players:
        # Initialise the score and roll count for current round
        dice_rolls = 0
        score = 0

        # Keep rolling dice up to 3 times
        while dice_rolls < 3:

            # Create list to record the numbers on 5 dice for each roll
            dice = []

            dice_rolls += 1
            # Generate the 5 random numbers representing each dice
            for dice_roll in range (5):
                dice.append(random.randint(1, 6))

            # Sort dice to make it easy to compare results
            dice.sort()

            # Check and republish results
            # 5 dice are the same if 1st dice matches last dice
            if dice[0] == dice[4]:
                result = "Yahtzee!"
                score += 50

            # 4 are the same if either of these combinations is true
            elif dice [0] == dice [2] or dice[1] == dice[3] or dice[2] \
                == dice[4]:
                result = "Three of a kind!"
                score += 10

            # otherwise
            else:
                result = "Better luck next time!\"

