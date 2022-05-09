name=input("Enter file name: ")
try:
    fname=open(name)
except:
    print("Bad input")
counts=dict()
for line in fname:
    words=line.split()
    print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1
#print(list(counts))
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword, bigcount)
