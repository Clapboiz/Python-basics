# ## https://nguyenlediep.com

# print("Nhập dãy số: ",end='')
# n=input()
# n_len=len(n)
# tong=0
# for i in range(n_len):
#     n_val=n[i]
#     tong=tong+int(n_val)
# print("Tổng của dãy số vừa nhập là: ",tong)

# # Chúc các bạn thành công!


# temp=False
# try:
#     a=input()
#     tachso=a.split()
#     gomso=map(int,tachso)
#     tinhtong=sum(gomso)
#     temp=True
# except:
#     print("input bi loi xin moi chay lai chuong trinh!")

# if temp:
    
#     print(tinhtong)


a=input()
tachso=a.split()
gomso=map(int,tachso)
try:
    tinhtong=sum(gomso)
    print(tinhtong)
except:
    print("input bi loi xin moi chay lai chuong trinh!")
