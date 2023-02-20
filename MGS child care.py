list_of_child = []
total_child = len(list_of_child)

def drop_off():
    child_name = input(" Child name: ")
    list_of_child.append(child_name)
def pick_up():
    name = input("Child name: ")
    if name in list_of_child:
        list_of_child.remove(name)
        print("Name has been removed from the roll.")
    else:
        print("That child isn't on the role.")
def print_roll():
    for name in list_of_child:
        print(name)
def cost(num):
   pass









while True:
    print("What would you like to do? Please choose one of the items below")
    choice = input("Press 1 to drop off\n"
                   "Press 2 to pick up\n"
                   "Press 3 to print the roll\n"
                   "Press 4 to calculate the cost\n"
                   "Press 5 to exit")

    if choice == "1":
        drop_off()
    elif choice == "2":
        pick_up()
    elif choice == "3":
        print_roll()
    elif choice == "4":
        cost(total_child)
    elif choice == "5":
        exit("GoodBye")
    else:
        print("That isn't a valid choice")




