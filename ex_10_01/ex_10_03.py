import string
name=input("Enter file name: ")
try:
    fname=open(name)
except:
    print("Bad input")
counts=dict()
lst=list()
count=0
for line in fname:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words=line.split()
    #print(words)
    for word in words:
        for letter in word:
            count+=1
            if letter not in counts:
                counts[letter]=1
            else:
                counts[letter]+=1
for key, value in counts.items():
    lst.append((value, key))
lst.sort(reverse=True)
for key, value in lst:
    print(value, key)
