xh=input("Enter Hours: ")
xr=input("Enter Rate: ")
try:
    xp=float(xh)*float(xr)
except:
    print("Bad inputs:",xh,"&",xr)
    quit()
print("Pay:",xp)
