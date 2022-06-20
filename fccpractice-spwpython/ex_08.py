#08 EX pfe - Opens a file removes white space and fixes bugs

han = open('ex_07_textfile.txt')

for line in han:
    line = line.rstrip()
    words = line.split()
    # print('Words:', words)
    # if line == '':
    #     print("Skipped Blank")
    #     continue
    #Guardian code
    # if len(words) < 1: # Can combine the code
    #     continue
    if len(words) < 3 or words[0] != 'From': #Danger code with guardian in compound statement
        # print('Ignore')
        continue
    print(words[2])


    # for line in han:
    # line = line.rstrip()
    # words = line.split()
    # if words[0] != 'From':
    #     continue
    # print(words[2])