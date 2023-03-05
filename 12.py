import easygui

easygui.enterbox("Hi! WHat is your name?")
easygui.integerbox("How old are you?")
easygui.buttonbox("Do you want to continue", "Game Continue", choices=["Yes", "No", "Maybe"])
easygui.msgbox("Kia ora! Welcome to Easygui")

for i in range(100):
    number = random.randint(0,5)
    print(number)

words = ["bat", "cat", "mat"]
my_word = random.choice[words]
print(my_word)

word = "stephanie"
letter = random.choice(word)
print(letter)
print()
