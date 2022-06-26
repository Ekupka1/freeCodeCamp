#09 EX pfe - Opens a file and finds biggest word

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'ex_07_textfile.txt'
hand = open(fname)

count = dict()

for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        # print(word)
        count[word] = count.get(word, 0) + 1
        # print(word, "new", count[word])

        # oldCount = count.get(word, 0) #Another way to update count
        # print(word, "old", oldCount)
        # newCount = oldCount + 1
        # count[word] = newCount
        # print(word, "new", newCount)

        # if word in count: #Another way to update count
        #     count[word] = count[word] + 1
        #     # print('old')
        # else:
        #     count[word] = 1
        #     # print("new")
        # # print(word, count[word])

print(count)

#find most common word
largest = -1
comWord = None
for k, v in count.items():
    # print(k,v)
    if v > largest :
        largest = v
        comWord = k
print("Most common", largest, comWord )

# Clean code by removing print testers