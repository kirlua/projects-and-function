import easygui
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
