kata=input("masukkan kata :").lower()
panjang=len(kata)
cek=''
for x in range(panjang-1,-1,-1):
     cek+=kata[x]

if cek==kata:
    for x in range(panjang-1,-1,-1):
        print (cek[x])
        print (kata[x])
    print ("Palindrome")
else:
    print("Bukan")
