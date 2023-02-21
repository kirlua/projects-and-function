def check_input(question):
    error = "That was not a valid number"
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)

def welcom(text,symbol):
    print(symbol * len(text))
    print(text)
    print(symbol * len(text))
    print()

# Main routine
bid = 0.0
highest = 0.0
welcom("Andrew's fantastic Auctions", "*")
item = input("What is the auction for? ")
reserve = check_input("What is the reserve price? $")
print()
print("The auction for the", item, "has started! ")

while bid != -1:
    print(f"\n "
          f"The highest bid so far is ${highest:.2f}")
    bid = check_input("What is your bid? (-1 to quit) $")
    if bid > highest:
        highest = bid
    elif bid == -1:
        break
    else:
        print("\nSorry, that bid was not high enough")

if highest >= reserve:
    print()
    print("=============")
    print(f" The {item} sold at auction for ${highest:.2f}")
else:
    print()
    print("=============")
    print(f"The {item} was not sold because the \n"
          f"reserve of ${item} was sold because of the\n"
          f"The highest bid was only ${highest:.2f}")
