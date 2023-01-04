import math

def menu():
    print("moi ban nhap 1 hoac 2")

menu()

def ptb1(a,b):
   if a == 0:
       if b == 0:
           return "Phuong trinh co vo so nghiem"
       return "Phuong trinh vo nghiem"
   return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

def ptb2(a,b,c):
   if a == 0:
       return ptb1(b, c)
   #Tinh delta
   delta = b * b - 4 * a * c
   #Kiem tra cac truong hop cua delta
   if delta > 0:
       x1 = float((-b + math.sqrt(delta)) / (2 * a))
       x2 = float((-b - math.sqrt(delta)) / (2 * a))
       return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
   if delta == 0:
       x = -b / (2 * a)
       return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
   return "Phuong trinh vo nghiem"

chuc_nang=int(input())
while chuc_nang<1 or chuc_nang>2:
    menu()
    chuc_nang=int(input())

#để ý lúc nhập phải có khoảng trắng vì có split() . vd 1 2 . 1 2 3 
if chuc_nang==1:
    a,b=map(float, input().split())
    print(ptb1(a,b))
if chuc_nang==2:
    a,b,c=map(float, input().split())
    print(ptb2(a,b,c))
