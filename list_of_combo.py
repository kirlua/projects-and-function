import easygui
# dictionary
combo = {
    "VALUE": {"items": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "CHEEZY": {"items": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}},
    "SUPER": {"items": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}
}
def display_combo():
    msg = "List of combos:\n"
    for item in combo:
        msg += f"{item} \n"
        for subitem in combo[item]["items"]:
            msg += f'   {subitem} ${float(combo[item]["items"][subitem]):.2f} \n'
    easygui.msgbox(msg, title="Menus")
display_combo()
