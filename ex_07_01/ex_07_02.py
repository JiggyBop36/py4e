file=input("Enter file name: ")
try:
    rfile=open(file)
except:
    print("File cannot be opened: ",file)
count=0
total=0
for line in rfile:
    if line.startswith("X-DSPAM-Confidence:"):
        line=line.rstrip()
        num=line.find(":")
        anum=line[num+1:]
        fnum=float(anum)
        count+=1
        total+=fnum
asc=total/count
print("Average spam confidence: ",asc)
