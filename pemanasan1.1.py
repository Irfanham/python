def kaskus(n):
    i=1
    if (i<=n*3):
        i=i+1
        if(i%3==0):      
            if(i%5==0 and i%6==0):
                return print("KASKUS")
            elif(i%5==0):
                return print("KAS")
            elif(i%6==0):
                return print("KUS")
            else:
                return print(n)
        
print(kaskus(10))

    
    
    
    
