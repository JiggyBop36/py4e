count=0
total=0.0
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
        fnum=float(num)
    except:
        print("Invalid input")
        continue
        #print(fnum)
    count=count+1
    total=total+fnum
#print("All done!")
print(total,count,total/count)
