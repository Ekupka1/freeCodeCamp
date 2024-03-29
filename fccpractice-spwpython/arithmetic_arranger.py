#Arithmetic Formatter - Gathers a function then performs mathematics

# Create a function that receives a list of strings that are arithmetic problems 
# and returns the problems arranged vertically and side-by-side. The function should 
# optionally take a second argument. When the second argument is set to True, the answers 
# should be displayed.

#Run first shows the list and if it passes the error check with TRUE then show answer

import sys
import time

def arithmetic_arranger(list, *args):
    checkList(list)
    for line in list:
        line = line.split()
        for firstRow in line[0-2]:
            firstRow = int(line[0])
            print(f"{firstRow:>5}", end='    ')
    print('\n')
    for line in list:
        line = line.split()
        for secRow in line[0+1]:
            secRow = int(line[2])
            print(f"{line[1]:>1} {secRow:>3}", end='    ')
            math(line)
    print('\n')

    # print(bool(list))
    time.sleep(3)
    if not False:
        for line in list:
            line = line.split()
        # print(f"{line[1]:>1} { line[2]:>3}")
            print(f"{math(line):>5}", end='    ')
        # print('\n')
        
# ERRORS - addition and subtraction, multiplication and division will return an error, only digits, max 4 digits, limit is five problems
def checkList(list):
    count = len(list)
    if count > 5:
        sys.exit("Error: Too many problems.") 
    for line in list:   
        line = line.split()
        lenOne = len(line[0])
        lenTwo = len(line[2])
        x = line[0].isnumeric()
        y = line[2].isnumeric()
        if line[1] == "*" or line[1] == "/":
            sys.exit("Error: Operator must be '+' or '-'.")
        elif x == False or y == False: 
            sys.exit("Error: Numbers must only contain digits.") 
        elif lenOne > 4 or lenTwo > 4:
            sys.exit("Error: Numbers cannot be more than four digits.")
        else:
            list = True
            

def math(line):
    sum = 0
    if line[1] == "-":
        sum = int(line[0]) - int(line[2])
        # print("-----\n", f"{sum:>4}")
    elif line[1] == "+":
        sum = int(line[0]) + int(line[2])
        # print("-----\n", f"{sum:>4}")
    return sum


fname = input('Enter a arithmetic question: \n')
if len(fname) < 1 : fname = arithmetic_arranger(["32 - 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49" , "123 - 49"]




