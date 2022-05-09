def mode_function(counts):
    bigcount=None
    bigword=None
    for word,count in counts.items():
        if bigcount is None or count>bigcount:
            bigword=word
            bigcount=count
    print(bigword, bigcount)

counts=dict()
lst=list()
while True:
    number=input("Enter a number: ")
    if number=="done":
        break
    try:
        inum=int(number)
        lst.append(inum)
    except:
        continue
for num in lst:
    counts[num]=counts.get(num,0)+1

mode_function(counts)
