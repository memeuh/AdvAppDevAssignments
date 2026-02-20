# Program Name: AppDevAssignment2.py
# Course: IT3883/Section 01
# Student Name: Mina Bayramoglu
# Assignment Number: Assignment 2
# Due Date: xx/xx/ 20XX
# Purpose: Reads txt file, seperates parts of file into diff variables, calculates avg
# https://www.computerhope.com/issues/ch001721.htm#complete-program
# https://www.geeksforgeeks.org/python/python-splitting-text-and-number-in-string/
#https://www.geeksforgeeks.org/python/python-lambda-anonymous-functions-filter-map-reduce/
#https://stackoverflow.com/questions/13013734/string-strip-in-python
#https://www.geeksforgeeks.org/python/python-dictionary-keys-method/
#must open file object then turn each line into str obj
#seperate str from numbers
studentslist = [] #empty list

with open('Assignment2input.txt', 'r') as file: #reads file
    for line in file:
        data = line.strip().split() #splits each line into seperate parts per whitespace

        name = data[0] #first part student name
        scores = list(map(float, data[1:])) #scores; convert to float for avg

        # calc avg
        average = sum(scores) / len(scores)

        # tuple
        studentslist.append((name, average))

    #sort by avg
    studentslist.sort(key=lambda x: x[1], reverse=True)

    # round and print output
    for name, average in studentslist:
        print(f"{name} {average:.2f}")








