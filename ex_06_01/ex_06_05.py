str = 'X-DSPAM-Confidence: 0.8475'
num=str.find(":")
fnum=(str[num+2:])
ffnum=float(fnum)
print(ffnum)
