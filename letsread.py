fhand=open(r"mytextfile.txt")
x=fhand.read()
print(x)
f.close()

fhand=open(r"mytextfile.txt")
for line in fhand:
    line=line.rstrip()
    if line.startswith('From'):
        print(line)
fhand.close()


fhand=open(r"mytextfile.txt")
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)
fhand.close()

fhand=open("mytextfile.txt")
for line in fhand:
    line=line.rstrip()
    if not "uct.ac.za" in line:
        continue
    print(line)
fhand.close()

fname=input("Enter file name:\n")
try:
    fhand=open(fname)
except:
    print("File cannot be opened:",fname)
    quit()
count=0
for line in fhand:
    if line.startswith("Subject"):
        count+=1
        line=line.rstrip()
        print(line)
print("There were",count,"subject line in",fname)
