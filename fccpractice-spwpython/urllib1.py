#12 EX pfe - Makes a socket communication easier, only gets the contents

from logging import FileHandler
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #Has to do the decode the data

#word count code

count = 0 
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)