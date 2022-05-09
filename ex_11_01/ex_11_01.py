import re
hand = open('mbox-short.txt')
regex=input("Enter a regular expression: ")
count=0
for line in hand:
    line = line.rstrip()
    if re.search(regex, line):
        count+=1
        #print(line)
print("mbox-short.txt had", count, "lines that matched", regex)
