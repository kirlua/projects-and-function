import easygui
combo = {
    "VALUE": {"items": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "CHEEZY": {"items": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "SUPER": {"items": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}
}

def add_combo():
    combo_name = easygui.enterbox("Enter the name of the combo", "New combo!").upper()
    combo[combo_name] = {"items": {}}
    for i in range(3):
        if i == 0:
            order = "burger"
        elif i == 1:
            order = "side menu"
        else:
            order = "drink"

text = "What would you like to do?"
title = "Menu maker options"
button_list = ["add_combo", "find_combo", "Delete_combo", "Output_all", "Exit"]
output = easygui.buttonbox(text, title, button_list)
if output == add_combo:
    add_combo()

print("User selected option: ", end = " ")
print(add_combo)

