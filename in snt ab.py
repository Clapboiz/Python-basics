a=int(input())
b=int(input())
import math
if a<0 or b<0:
    print("nhap lai")
if a>b:
    print("nhap lai")
else:
    for n in range(a,b+1):
        if n<2:
            continue
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            print(n,end=" ")