txt = input("How many coins do you have?: ")

dividedString = (txt.split("and"))
#initializing variables outside loop
numPenny = float(0)
numNickel = float(0)
numDime = float(0)
numQuarter = float(0)
for i in dividedString:
    x =i.split() #creates list
    if x[1] == "penny" or x[1] =="pennies": #if second item in list is pennies it takes in the first item as the number of pennies
        numPenny = x[0]
        numPenny = float(numPenny) #converts list item into float
    elif x[1] == "nickel" or x[1] =="nickels":
        numNickel = x[0]
        numNickel = float(numNickel)
    elif x[1] == "dime" or x[1]=="dimes":
        numDime = x[0]
        numDime = float(numDime)
    elif x[1] == "quarter" or x[1] =="quarters":
        numQuarter = x[0]
        numQuarter = float(numQuarter)

    else:
        print("Invalid input. Please try again.")
#total calculations
penny = 0.01 * numPenny
nickel = 0.05 * numNickel
dime = 0.1 * numDime
quarter = 0.25 * numQuarter

Total = penny + nickel + dime + quarter
print(round(Total,2))