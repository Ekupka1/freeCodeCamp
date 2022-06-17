#07-01 EX pfe - Opens a file and upper case it

from itertools import count

fLower = open('ex_07_textfile.txt')
# fSize = fLower.read() 

for word in fLower:
    #print(word)
    fh = word.rstrip()
    print(fh.upper())

count = 0 #Only works with fSize code
for character in fSize:
    count = count + 1

print(count)

print(len(fSize))