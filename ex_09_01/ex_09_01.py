name=input("Enter file name: ")
fhand=open(name)
counts=dict()
for words in fhand:
    sword=words.rstrip()
    counts[sword]=sword
print(counts)
