xh=input("Enter Hours: ")
xr=input("Enter Rate: ")
try:
    ih=float(xh)
    ir=float(xr)
except:
    print("Bad input:",xh,"&",xr)
otp=(ih-40)*(10*0.5)
xp=ih*ir
gcp=otp+xp

print("Gross computation pay:",gcp)
