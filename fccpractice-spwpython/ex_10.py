#10 EX pfe - Opens a file and finds biggest word

from audioop import reverse
from os import times_result
from time import clock_getres, time
from xmlrpc.client import TRANSPORT_ERROR


fname = input('Enter File: ')
if len(fname) < 1 : fname = 'ex_10_text.txt'
hand = open(fname)

count = dict()

for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print("reg list: ", count)

sortList = sorted(count.items())
print("sorted reg list:", sortList)

tmp = list()
for k,v in count.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)
print("reverse list: ", tmp)

tmp = sorted(tmp, reverse=True)
print("sorted reversed list: ", tmp)

for v,k in tmp [:2]:
    print(k,v)
