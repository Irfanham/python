def kaskus(n):
    if(n%5==0 and n%6==0):
        return print("KASKUS")
    elif(n%5==0):
        return print("KAS")
    elif(n%6==0):
        return print("KUS")
    else:
        return print(n)
x=int(input("Banyak Nilai : "))
i=1
while i<=x*3:
    if(i%3==0):
        kaskus(i)
    i=i+1




