lst=list()
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
        inum=float(num)
        lst.append(inum)
    except:
        print("Bad input")
print("Maximum:",max(lst))
print("Minimum",min(lst))
