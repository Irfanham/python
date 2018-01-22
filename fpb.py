a=int(input("Bilangan 1 : "))
b=int(input("Bilangan 2 : "))
x=a*b
while b<>0 :
	c=a%b
	a=b
	b=c
print("FPB = " + str(a) + "\nKPK = " + str(x/a)) 
