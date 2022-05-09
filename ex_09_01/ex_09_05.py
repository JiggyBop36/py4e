file=input("Enter file name: ")
fhand = open(file)
counts=dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' :
        continue
    domain=words[1]
    maindomain=domain.split('@')
    actualdomain=maindomain[1]
    counts[actualdomain]=counts.get(actualdomain,0)+1
print(counts)
