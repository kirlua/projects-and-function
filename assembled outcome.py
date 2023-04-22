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

        combo_item = easygui.enterbox(f"Enter name of the {order} to add to the combo:")
        price = float(easygui.enterbox(f'Enter the price of {combo_item}:'))
        combo[combo_name]["items"][combo_item] = price

def display_combo():
    msg = "List of combos:\n"
    for item in combo:
        msg += f"{item} \n"
        for subitem in combo[item]["items"]:
            msg += f'   {subitem} ${float(combo[item]["items"][subitem]):.2f} \n'

    easygui.msgbox(msg, title="Menus")


add_combo()
display_combo()
