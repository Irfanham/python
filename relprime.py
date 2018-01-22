def fpb(x,y):
	if(x==0):
		return(y)
	elif(y==0):
		return(x)
	else:
		return fpb(y,x%y)	
while (1) :
	a=int(input("Bilangan 1= "))
	b=int(input("Bilangan 2= "))
	print ("FPB dari "+str(a)+" dan "+str(b)+" = "+str(fpb(a,b)))
	if fpb(a,b)==1:
		print("Bilangan relatif prima")
	else:
		print("Bukan bilangan relatif prima")
	break 
