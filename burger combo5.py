import easygui
from collections import OrderedDict

combos = OrderedDict([
    ("VALUE", {
        "items": OrderedDict([
            ("Burger", {"price": 5.69, "name": "Beef burger"}),
            ("Side menu", {"price": 1.00, "name": "Fries"}),
            ("Drink", {"price": 1.00, "name": "Fizzy drink"})
        ])
    }),
    ("CHEEZY", {
        "items": OrderedDict([
            ("Burger", {"price": 6.69, "name": "Cheeseburger"}),
            ("Side menu", {"price": 1.00, "name": "Fries"}),
            ("Drink", {"price": 1.00, "name": "Fizzy drink"})
        ])
    }),
    ("SUPER", {
        "items": OrderedDict([
            ("Burger", {"price": 6.69, "name": "Cheeseburger"}),
            ("Side menu", {"price": 2.00, "name": "Large fries"}),
            ("Drink", {"price": 2.00, "name": "Smoothie"})
        ])
    })
])


def add_combo():
    combo_name = easygui.enterbox("Enter the name of the combo", "New combo!").upper()
    combos[combo_name] = {"items": {}}

    for i in range(3):
        if i == 0:
            order = "Burger"
        elif i == 1:
            order = "Side menu"
        else:
            order = "Drink"

        while True:
            combo_item = easygui.enterbox(f"Enter name of the {order} to add to the combo:").capitalize()
            if combo_item:
                break

        while True:
            price = easygui.enterbox(f'Enter the price of {combo_item}:')
            if price:
                price = float(price)
                break

        combos[combo_name]["items"][order] = {"name": combo_item, "price": price}

    confirm_combo(combo_name)
    return combo_name


def confirm_combo(combo_name):
    while True:
        choices = ["Confirm", "Change Combo Name"]
        for order, items in combos[combo_name]["items"].items():
            choices.append(f"Change {order}")

        msg = f"Combo '{combo_name}' added successfully!\n\n {display_combos()} \n\n What would you like to do?"
        selection = easygui.buttonbox(msg, title="Confirmation", choices=choices)

        if selection == "Confirm":
            if all(v["name"] and v["price"] for v in combos[combo_name]["items"].values()):
                break
            else:
                easygui.msgbox("Please fill in all the fields", title="Error")
        elif selection == "Change Combo Name":
            new_combo_name = easygui.enterbox("Enter the new name for the combo:", title="Change Combo Name",
                                              default=combo_name).upper()
            if new_combo_name and new_combo_name != combo_name:
                combos[new_combo_name] = combos.pop(combo_name)
                combo_name = new_combo_name
        else:
            order = selection[7:]
            new_menu = easygui.enterbox(f"Enter the new name for '{combos[combo_name]['items'][order]['name']}':",
                                        title="Change Item Name",
                                        default=combos[combo_name]['items'][order]['name']).capitalize()
            new_price = float(easygui.enterbox(f"Enter the new price for '{new_menu}':", title="Change Item Price",
                                               default=combos[combo_name]['items'][order]['price']))
            combos[combo_name]["items"][order]["name"] = new_menu
            combos[combo_name]["items"][order]["price"] = new_price

    easygui.msgbox("Thank you for using our system!", title="Exit")


def display_combos():
    msg = "List of combos:\n\n"
    for combo_name, combo_details in combos.items():
        msg += f"{combo_name}\n"
        for order in ["Burger", "Side menu", "Drink"]:
            items = combo_details["items"].get(order)
            if items:
                msg += f"   {order}:\n"
                if isinstance(items, dict):
                    if 'name' in items:
                        msg += f"       {items['name']}: {items['price']:.2f}\n"
                else:
                    for item_name, item_details in items.items():
                        msg += f"   {item_name}: {item_details['price']:.2f}\n"
        msg += "\n"

    return msg


add_combo()
