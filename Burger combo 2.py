import easygui
# dictionary
combo = {"Value": {"Beef Burger": 5.69,
                   "Fries": 1.00,
                   "Fizzy drink": 1.00},

         "Cheezy": {"Cheese Burger": 6.69,
                    "Fries": 1.00,
                    "Fizzy Drink": 1.00},

         "Super": {"Cheese Burger": 6.69,
                   "Fries": 1.00,
                   "Smoothie": 2.00}
         }
#function for burger, side menu and drink order
    for v in range(3):
        if v == 0:
            order = "burger"
        elif v == 1:
            order = "side menu"
        else:
            order = "drink"






# showing the menu
msg = "List of combos:\n"
for burger in combo:
    msg += f"{burger} \n"
    for subitem in combo[burger]:
        msg += f'   {subitem} ${float(combo[burger][subitem]):.2f} \n'
easygui.msgbox(msg, title="Menus")

