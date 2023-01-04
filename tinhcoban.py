try:
    s1, dau, s2 = map(float, input().split())

    if dau=="+":
        ketqua=s1+s2
    elif dau=="-":
        ketqua=s1-s2
    elif dau=="*":
        ketqua=s1*s2
    elif dau=="/":
        ketqua=s1/s2
    print("ket qua cua phep tinh {} la ketqua".format(dau))
except:
    print("Error")

# # # # # # # # # # # # # # # # # # # #Nhap bieu thuc tu ban phim
# # # # # # # # # # # # # # # # # # # soThu1, phepTinh, soThu2 = input().split()

# # # # # # # # # # # # # # # # # # # #Ep kieu du lieu sang so thuc
# # # # # # # # # # # # # # # # # # # soThu1 = float(soThu1)
# # # # # # # # # # # # # # # # # # # soThu2 = float(soThu2)

# # # # # # # # # # # # # # # # # # # #Bien luu ket qua cua bieu thuc
# # # # # # # # # # # # # # # # # # # ketQua = None

# # # # # # # # # # # # # # # # # # # #Dung cau lenh re nhanh de phan loai phep tinh
# # # # # # # # # # # # # # # # # # # #Luu ket qua cua loai phep tinh phu hop
# # # # # # # # # # # # # # # # # # # if phepTinh == '+':
# # # # # # # # # # # # # # # # # # #    ketQua = soThu1 + soThu2
# # # # # # # # # # # # # # # # # # # elif phepTinh == '-':
# # # # # # # # # # # # # # # # # # #    ketQua = soThu1 - soThu2
# # # # # # # # # # # # # # # # # # # elif phepTinh == 'x':
# # # # # # # # # # # # # # # # # # #    ketQua = soThu1 * soThu2
# # # # # # # # # # # # # # # # # # # elif phepTinh == ':':
# # # # # # # # # # # # # # # # # # #    #Xu ly truong hop o phep chia va so bi chia bang 0
# # # # # # # # # # # # # # # # # # #    if soThu2 == 0:
# # # # # # # # # # # # # # # # # # #        print("So chia phai khac 0!")
# # # # # # # # # # # # # # # # # # #    else:
# # # # # # # # # # # # # # # # # # #        ketQua = soThu1 / soThu2

# # # # # # # # # # # # # # # # # # # #Neu bien ketQua khac None thi chung to bieu thuc hop le
# # # # # # # # # # # # # # # # # # # if ketQua != None:
# # # # # # # # # # # # # # # # # # #    #In ra man hinh bieu thuc va ket qua
# # # # # # # # # # # # # # # # # # #    print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))