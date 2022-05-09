fname=input("Enter file name: ")
fh=open(fname)
lst=list()
word_count=0
for line in fh:
    words=line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
        word_count+=1
print(sorted(lst))
print("There are",word_count,"words in",fname)
