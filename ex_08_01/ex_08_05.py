file=input("Enter file name: ")
try:
    rfile=open(file)
except:
    print("File cannot be opened: ",file)
    quit()
from_count=0
for line in rfile:
    if line.startswith("From"):
        from_count+=1
        if len(line)<1:
            continue
        line=line.rstrip()
        word=line.split()
        print(word[1])
print("There were",from_count,"lines beginning with from.")
