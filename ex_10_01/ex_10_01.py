file=input("Enter file name: ")
fhand = open(file)
counts=dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' :
        continue
    counts[words[1]]=counts.get(words[1],0)+1
#print(counts)
lst=list()
for count, email in counts.items():
    lst.append((email, count))
lst.sort(reverse=True)
for email, count in lst[:1]:
    print(count, email)
