'''
script: functionMess
action: varied
author: Dylan
date: 03SEP24

'''

# define some functions

def addTen (inputInt):
    
    #add 10 to input
    inputInt += 10
    
    print("inside addTen, inputInt is", inputInt)

def addElement(inputList):
    
    #append element to list
    inputList.append("Farmer")

# define main
def main():
    
    mainInt = 47
    mainList = ["Patrick", "Joesph"]
    
    print("mainInt before add10:", mainInt)
    addTen(mainInt)    
    print("maintInt is:", mainInt)
    
    print("\n\nChecking list\n\n")
    
    print("My list contains: ", mainList)
    addElement(mainList)
    print("After addElement, my list is :", mainList)

# call main
main()

'''
CLASS NOTES

- queue First In First Out
- stack First In Last Out

- Pass By Value vs Pass By Reference

'''
