def add_combo():
    combo_name = easygui.enterbox("Enter the new name of the combo", "New combo!").upper()
    combo[combo_name] = {"items": {}}
