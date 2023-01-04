print("bt")
n=int(input())
#a la tong cac uoc so cua n
a=0
for i in range(1,n//2+1):
    if n%i==0:
        a+=i
if n==a:
    print("hoan thien")

print("list")
n=int(input())
list_n=[]

#Do ước của một số không bao giờ lớn hơn số đó chia 2 (trừ chính nó).
# Vd: số 10 không có ước nào lớn hơn 5 (trừ chính nó là số 10).
for i in range(1,n//2+1):
    if n%i==0:
        list_n.append(i)
if n==sum(list_n):
    print("hoan thien")

#test inp=6 => hoan thien

