def product_of_sum_even_odd(n):
    s_even=0
    s_odd=0
    while n>0:
        dig=n%10
        if dig%2==0:
            s_even+=dig
        if dig%2==1:
            s_odd+=dig
        n=n//10
    return s_even*s_odd        

n=int(input())
print(product_of_sum_even_odd(n))

#c2
#Dinh nghia ham

#tuyChon == 0: tinh tong cac chu so chan
#tuyChon == 1: tinh tong cac chu so le
def tong_chu_so(soTuNhien, tuyChon):
   tong = 0
   while soTuNhien > 0:
       #Kiem tra chu so cuoi la chan hay le
       if soTuNhien % 2 == tuyChon:
           tong += soTuNhien % 10
       soTuNhien = soTuNhien // 10
   return tong

def tich_chan_le(soTuNhien):
   return tong_chu_so(soTuNhien, 0) * tong_chu_so(soTuNhien, 1)
  
#Khoi lenh co the phat sinh loi
try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n < 0
   if n < 0:
       print("Vui long nhap so tu nhien!")
   else:
       print(tich_chan_le(n))
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")