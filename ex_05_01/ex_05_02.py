maximum=None
minimum=None
total=0
count=0
print("Before:", maximum)
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
        inum=int(num)
        total=total+inum
        count=count+1
        if maximum is None:
            maximum=minimum
        elif inum>maximum:
            maximum=inum

        if minimum is None:
            minimum=inum
        elif inum<minimum:
            minimum=inum

    except:
        print("Bad input")
print("Maximum:", float(maximum))
print("Minimum:", float(minimum))
print("Total:", float(total))
print("Count:", float(count))
print("Average:", int(total/count))
