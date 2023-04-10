import easygui
text = "What would you like to do?"
title = "Menu maker options"
button_list = []
button_1: "add_combo"
button_2: "find_combo"
button_3: "delete_combo"
button_4: "output_all"
button_5: "button_list"
output = easygui.buttonbox(button_list, button_1, button_2, button_3, button_4, button_5)
print("user selected option: ", end = " ")
print(output)
