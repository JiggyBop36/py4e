def computegrade():
    if fs>0.9 or fs<0.5:
        print("Bad score")
        quit()
    else:
        0.9>=fs>=0.0
        #Proceed with the grading
    if fs==0.9:
            print("A")
            quit()
    elif fs==0.8:
            print("B")
            quit()
    elif fs==0.7:
            print("C")
            quit()
    elif fs==0.6:
            print("D")
            quit()
    elif fs==0.5:
            print("F")
            quit()
    else:
        print("Bad score")
        quit()
score=input('Enter score: ')
try:
    fs=float(score)
except:
    fs=-1
    print("Bad score")
    quit()
computegrade()
