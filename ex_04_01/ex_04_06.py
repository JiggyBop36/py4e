def computepay(hours, rate):
    if hours>40:
        #print("Overtime")
        rp=hours*rate
        op=(hours-40)*(rate*0.5)
        #print(rp, op)
        pay=rp+op
        return pay
    else:
        #print("Regular")
        pay=hours*rate
        return pay
sh=input("Enter Hours: ")
sr=input("Enter Rate: ")
try:
    fh=float(sh)
    fr=float(sr)
    #print(fh, fr)
except:
    print("Bad input:",sh,"&",sr)
    quit()
xp=computepay(fh, fr)

print("Pay:",xp)
