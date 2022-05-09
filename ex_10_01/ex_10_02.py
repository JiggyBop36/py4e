file=input("Enter file name: ")
fhand = open(file)
counts=dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' :
        continue
    tl=words[5]
    spl_tl=tl.split(":")
    time=spl_tl[0]
    counts[time]=counts.get(time, 0)+1
lst=list()
for time, freq in counts.items():
    lst.append((time, freq))
lst.sort()
for time, freq in lst:
    print(time, freq)
