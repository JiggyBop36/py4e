file=input("Enter file name: ")
rfile=open(file)
for line in rfile:
    line=line.rstrip()
    print(line.upper())
