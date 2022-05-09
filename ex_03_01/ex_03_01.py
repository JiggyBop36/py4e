sh=input("Enter Hours: ")
sr=input("Enter Rate: ")
try:
    fh=float(sh)
    fr=float(sr)
    #print(fh, fr)
except:
    print("Bad input:",sh,"&",sr)
    quit()
if fh>40:
    #print("Overtime")
    rp=fh*fr
    op=(fh-40)*(fr*0.5)
    #print(rp, op)
    xp=rp+op
else:
    #print("Regular")
    xp=fh*fr
print("Pay:",xp)
