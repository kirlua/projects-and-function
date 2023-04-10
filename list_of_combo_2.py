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
def display_combo():
    msg = "List of combos:\n"
    for items in combo:
        msg += f"{items} \n"
        for otheritems in combo["Value"]:
            msg += f'   {otheritems} ${float(combo["Value"][otheritems]):.2f} \n'

    easygui.msgbox(msg, title="Menus")
display_combo()


