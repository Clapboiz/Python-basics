#c1 dung de quy
from re import I


def giaithua(n):
    if n == 0:
        return 1
    return n*giaithua(n-1)

n=int(input())
print(giaithua(n))

#c2 dung for

def giaithuac2(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

n=int(input())
print(giaithuac2(n))  

