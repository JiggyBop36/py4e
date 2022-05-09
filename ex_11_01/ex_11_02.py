import re
hand = open('mbox-short.txt')
lst=list()
for line in hand:
    line = line.rstrip()
    x= re.findall('^N.+: ([0-9]+)', line)
    if len(x) > 0:
        lst.append(int(x[0]))
print(int(sum(lst)/len(lst)))
