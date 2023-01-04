print("bai tap tinh n!")

n=int(input())
giaithua=1
for i in range(1, n+1):
    giaithua=giaithua*i
print("giai thua cua n la:{}".format(giaithua))



print("bai tap tinh S(n)= 1-x+...x^(2n-1)/(2n-1)!+x^(2n)/(2n)!")
#nhìn x^1/1!
    #   x^2/2!
    #   x^(2n-1)/(2n-1)!

    #nhìn tổng quát thì ta thấy đây là giai thừa của (x^(2n)/(2n)!)!
try:
    x=float(input())
    n=int(input())

    tusogiaithua=pow(x,2*n)
    giaithua=1
    for j in range(1,2*n+1):
        giaithua=giaithua*j
    mausogiaithua=giaithua
    ps=tusogiaithua/mausogiaithua

    giaithuafinal=1
    for i in range(1, ps+1):
        giaithuafinal=giaithuafinal*i
    print ("tong s nay la:{}".format(1-giaithuafinal))
except:
    print("ko co dau")
    #vẫn đang sai và chưa biết fix


# # Dựa trên gợi ý và ví dụ đã được nêu, bạn hoàn toàn có thể tự viết chương trình tính S(n) = 1 - x + x^2/2! - x^3/3! + … - x^(2n-1)/(2n-1)! + x^(2n)/(2n)

#     #Khoi lenh co the phat sinh loi
# try:
#     #Nhap gia tri tu ban phim
#     #Ep kieu du lieu sang so nguyen
#     x = float(input())
#     n = int(input())
   
#     #Su dung cau truc re nhanh xu ly truong hop n < 0
#     if n<0:
#         print("Vui long nhap n la so tu nhien!")
#     elif n == 0:
#         print(1)
#     else:
#         ketQua = 1
#         giaiThua = 1
#         #Su dung vong lap for duyet cac so tu 1 toi n
#         for i in range(1, 2*n+1):
#             giaiThua *= i
#             if i % 2 == 0:
#                 ketQua += pow(x, i)/giaiThua
#             else:
#                 ketQua -= pow(x, i)/giaiThua 
#         print('{:.5f}'.format(ketQua))
        
# #Khoi lenh duoc thuc thi khi loi xay ra
# except:
#     print("Dinh dang dau vao khong hop le!")