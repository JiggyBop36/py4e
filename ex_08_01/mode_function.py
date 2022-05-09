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
lst.sort()
List1=[]
a=0
while a<len(lst):
    List1.append(lst.count(lst[a]))
    a+=1
dic1=dict(zip(lst,List1))
dic2=[k for (k, v) in dic1.items() if v==max(List1)]
print("Mode is/are:",str(dic2))
