i=int(input("banyak : "))
n=0
p=2
while n<i:
    while p<n:
        x=2
        while (x <=(p/x)):
            if (p%x==0):break
            x=x+1
        if (x>(p/x)):print (p)
        p=p+1
    n=n+1
