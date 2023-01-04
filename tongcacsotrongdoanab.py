#c1 dung for
print("cach 1 dung for")
try:
    a,b=map(int, input().split())
except:
    print("dau vao ko hop le")
tong=0
for i in range(a,b+1):
    tong+=i
print("tong:{}".format(tong))

#c2 dung while
print("cach 2 dung while")
try:
    a,b=map(int, input().split())
except:
    print("dau vao ko hop le")
tong=0
i=a
while(i<=b):
    tong+=i
    i+=1
print("tong:{}".format(tong))