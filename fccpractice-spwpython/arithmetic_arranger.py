#Arithmetic Formatter - Gathers a function then performs mathematics

#  Create a function that receives a list of strings that are arithmetic problems 
# and returns the problems arranged vertically and side-by-side. The function should 
# optionally take a second argument. When the second argument is set to True, the answers 
# should be displayed.

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# addition and subtraction. Multiplication and division will return an error. only didgets, max 4 didgets, limit is five problems

# fname = input('Enter File: ')
# if len(fname) < 1 : arithmetic_arranger(list)

def arithmetic_arranger(list, **TRUE):
    for line in list:
        line = line.split()
        for firstRow in line[0-2]:
            firstRow = int(line[0])
            print(f"{firstRow:>5}", end='    ')
            # math(line)
    print('\n')
    for line in list:
        line = line.split()
        for secRow in line[0+1]:
            secRow = int(line[2])
            print(f"{line[1]:>1} {secRow:>3}", end='    ')
            math(line)
    print('\n')
    for line in list:
        line = line.split()
        # print(f"{line[1]:>1} { line[2]:>3}")
        print(f"{math(line):>5}", end='    ')
        # print('\n')
        

def math(line):
    if line[1] == "-":
        sum = int(line[0]) - int(line[2])
        # print("-----\n", f"{sum:>4}")
    elif line[1] == "+":
        sum = int(line[0]) + int(line[2])
        # print("-----\n", f"{sum:>4}")
    return sum

arithmetic_arranger(list)

