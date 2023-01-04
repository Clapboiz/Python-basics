import math
temp=False
try:
    print("xin moi ban nhap 3 so a,b,c tuong ung ax^2 + bx + c:")
    a,b,c=map(float, input().split())
except:
    print("Loi dau vao")
if temp:
    if a==0 and b!=0:
        x=-c/b
        print("phuong trinh co 1 nghiem la:",round(x,3))
    elif a==0 and b==0 and c==0:
        print("phuong trinh vo so nghiem")
    else:
        denta=pow(b,2)-4*a*c
        if denta<0:
            print("phuong trinh vo nghiem")
        elif denta==0:
            x=-b/2*a
            print("phuong trinh co nghiem kep la:",x)
        else:
            x1=(-b+math.sqrt(denta))/2*a
            x2=(-b-math.sqrt(denta))/2*a
            print("phuong trinh co 2 nghiem la:","\n",x1,"\n",x2)

