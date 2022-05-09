numlist=list()
while True:
    inp=input("Enter a number: ")
    if inp=="done":
        break
    try:
        finp=float(inp)
        numlist.append(finp)
    except:
        print('Bad input!')        
print(numlist)
print("Average:",sum(numlist)/len(numlist))
