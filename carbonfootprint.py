print ("Welcome to this carbon footprint calculator! Please answer a few questions to quantify an approximation of your contribution to CO2 emissions!")
footprint = 0 #variable to store carboon footprint accumulation
car = input("Does the person picking you up from school leave the car engine running whiley they wait?")
if car == "yes":
    footprint +=4

meat = input("How often do you eat red meat as the main course? Enter 1 for once a week, 2 for twice a week, and 3 for more: ")
if meat == 1:
    footprint += 4
if meat == 2:
    footprint += 4
if meat == 3:
    footprint  += 5

water = input("Does your family purchase bottled water?")
if water == "yes":
    footprint +=1

bags = input("Do you use plastic bags when shopping?")
if bags == "yes":
    footprint +=3
if bags == "no":
    footprint += 0.5

plastic = input("Do you recycle plastic?")
if plastic == "yes":
    footprint += -0.5

glass = input("Do you recycle glass?")
if glass == "yes":
    footprint += -0.5

paper = input("Do you recycle paper?")
if paper == "yes":
    footprint += -1.5

metal = input("Do you recycle metal?")
if metal == "yes":
    footprint += -1

ConversionFactor = footprint *200
print ("Your total contribution is approximatley ")
print(ConversionFactor)
print("lbs!")
