import math
n=int(input())
if n<2:
    print("k phai so nt")
else:    
    #so nguyen to la so chia het cho 1 va chinh no, nen chi can duyet den 
    #sqrt(n+1) la se biet duoc co phai so nguyen to hay ko
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("k phai so nt")
            break
    else:
        print("la so nt")
