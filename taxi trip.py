"""Program to keep track of details for a taxi"""

name = input("What is the driver's name?: ")

tripCount = 0
totalTime = 0.0 # Setting these up to take floats
totalIncome = 0.0
baseCost = 10.00 # Using constants rather than literals for
minuteCost = 2.00 # these two costs
startNewTrip = "Yes" # Set the loop to true

while startNewTrip == "Yes":
    # Float allows for half minutes
    tripTime = float(input("How many minutes did the trip take? "))
    tripCount += 1
    totalTime += tripTime
    tripCost = (tripTime * minuteCost) + baseCost
    totalIncome += tripCost
    print(f"This trip cost ${tripCost:.2f}")
    print()
    startNewTrip = input("Do you want to enter a new trip? Yes or No: ")
    # "No" above will break the loop

print("==========================")
print(f" Driver {name} had {tripCount} trips totalling {round(totalTime)}"
      f"minutes \n")
      # the "round" function above rounds up down from .5
      # however, the two below round to 2dp
      f"The averge time of all trips was {round(totalTime / tripCount, 2)}\n"
      f"minutes\n"
      f"The total income for the day was ${totalIncome:.2f}\n" \
      f"The average cost of all trips was ${totalIncome / tripCount:.2f}")


