temp=True
try:
    s=int(input())
    temp=False
except:
    print("dinh dang k hop le")

if temp==False:
    print('so thap phan la %d, so bat phan la %o' %(s,s))
