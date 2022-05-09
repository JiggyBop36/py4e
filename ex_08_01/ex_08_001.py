def chop(t):
    x=len(t)
    y=x-1
    del t[y]
    del t[0]
    print(t)

dchbq=[2,3,4,5,5,6,6,7,7,8]
chop(dchbq)

def middle(t):
    x=len(t)
    t=t[1:x-1]
    print(t)

abab=[2,3,4,5,5,6,6,7,7,8]
middle(abab)
