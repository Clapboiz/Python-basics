def sum_(*args):
    tong=0
    for i in args:
        tong+=i
    return tong

args=map(int, input().split())
print("{} la ket qua cua sum".format(sum_(*args)))

#cach nay cao sieu qua !!!
# Hàm tính tổng

def tong(*arg): 
    s = 0
    for i in arg:
        s += i
    return s
try:
    print('Nhap cac so:')
    n = input().split()
    lst = list(map(int, n))
    for i in range(len(lst)-1):
        print('{}'.format(lst[i]), end = ' + ')
    print(lst[len(lst)-1], end = ' = ')
    print(tong(*lst))
except:
    print('Ban nhap sai du lieu dau vao!')

#cao sieu .2
def tinh_tong(*args):
    tong = 0
    for i in args:
        tong += i
    return tong
# Bien kiem tra loi du lieu dau vao
kt = True
while kt:
    try:
        # Neu thuc hien thi thoat chuong trinh voi kt = False
        kt = False
        # Tao 1 list chua cac tham so dau vao voi cac phan tu kieu str
        tham_so = list(input('Nhap vao cac so can tinh tong: ').split())
        # Vong lap dung de ep kieu str sang int
        for i in range(len(tham_so)):
            # Ep tham so tu kieu str sang int
            tham_so[i] = int(tham_so[i])
        for i in range(len(tham_so)):
            # Khi vong lap chay den vong lap cuoi thi hien thi 'tham_so cuoi = '
            if i == len(tham_so) - 1:
                print(tham_so[i],end=' = ')
                break
            # Sau moi vong lap thi hien thi 'tham_so[i] + '
            print(f'{tham_so[i]}',end=' + ')
        # In ket qua o cuoi dong 
        print(tinh_tong(*tham_so))
    except:
        # Tiep tuc thuc hien lai chuong trinh
        kt = True
        print('\nLoi thong so dau vao xin nhap lai!\n')