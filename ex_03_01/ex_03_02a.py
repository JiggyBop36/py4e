xh=input("Enter Hours: ")
try:
    ih=float(xh)
except:
    ih=-1
    print('Error, please enter numeric input')
    quit()
xr=input("Enter Rate: ")
try:
    ir=float(xr)
except:
    ih=-1
    print('Error, please enter numeric input')
    quit()
otp=(ih-40)*(10*0.5)
xp=ih*ir
gcp=otp+xp

print("Gross computation pay:",gcp)
