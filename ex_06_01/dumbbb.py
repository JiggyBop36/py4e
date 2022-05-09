n="the name of my school is kings college lagos"
index=0
while index<len(n):
    letter=n[index]
    print(index,letter)
    index+=1


n="the name of my school is kings college lagos"
index=-1
for letter in n:
    #print(letter)
    index+=1
    print(index,letter)

n="the name of my school is kings college lagos"
count=0
for letter in n:
    if letter=="o":
        count+=1
print("Count is",count)

j='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=j.find("@")
print(atpos)
sppos=j.find(" ",atpos)
print(sppos)
host=j[atpos+1:sppos]
print(host)
x=j.find(host)
print(x)
