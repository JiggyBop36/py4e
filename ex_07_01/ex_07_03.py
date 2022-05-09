file=input("Enter file name: ")
try:
    rfile=open(file)
except:
    if file=="na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punked!")
        quit()
    else:
        print("File cannot be opened: ",file)
        quit()
line_count=0
count=0
total=0
for line in rfile:
    line_count+=1
    if line.startswith("X-DSPAM-Confidence:"):
        line=line.rstrip()
        num=line.find(":")
        anum=line[num+1:]
        fnum=float(anum)
        count+=1
        total+=fnum
asc=total/count
print("Average spam confidence: ",asc)
print("There were",line_count,"subject lines in",file)
