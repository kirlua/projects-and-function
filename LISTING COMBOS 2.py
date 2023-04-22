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
