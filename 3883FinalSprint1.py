txt = input("How many coins do you have?: ")

dividedString = (txt.split("and")) #split input string

numPenny = float(0)
numNickel = float(0)
numDime = float(0)
numQuarter = float(0)

counter = 0
#counter is used to account for the spaces in between
for i in dividedString:
    if "penny" or "pennies" in i:
        characters = list(i)
        if counter == 0: #if this is the first time the string is being iterated, it takes in the first character
            numPenny = characters[0]
        else:
            numPenny = characters[1] #if it's the second time the string is being iterated, it takes in the second character in the list
        numPenny = float(numPenny)

    elif "nickel" or "nickels" in i:
        characters = list(i)
        if counter == 0:
            numNickel = characters[0]
        else:
            numNickel = characters[1]
        numNickel = float(numDime)

    elif "dime" or "dimes" in i:
        characters = list(i)
        if counter == 0:
            numDime = characters[0]
        else:
            numDime = character[1]
        numDime = float(numDime)
    elif "quarter" or "quarters" in i:
        characters = list(i)
        if counter == 0:
            numQuarter = characters[0]
        else:
            numQuarter = characters[1]
        numQuarter = float(numQuarter)
    counter +=1 #adds one to counter after it loops the first time
#calculating totals
penny = 0.01 * numPenny
nickel = 0.05 * numNickel
dime = 0.1 * numDime
quarter = 0.25 * numQuarter

Total = penny + nickel + dime + quarter
print(round(Total,2))
