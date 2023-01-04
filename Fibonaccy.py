#F(n) with n>3
#F(n)=F(n-1)+F(n-2)
#fibonaccy là dãy số tập hợp các số bắt đầu từ 0 hoặc 1, số tiếp theo là 1 tập hợp số tự nhiên bắt đầu dựa trên tổng 2 số đó

print("dung de quy")
def fibonaccy(n):
    if n==1 or n==2:
        return 1
    return fibonaccy(n-1)+fibonaccy(n-2)
n=int(input())
print(fibonaccy(n))

print("dung binh thuong")
n=int(input())
if n==1 or n==2:
    print("1")
else:
    number_fist=1
    number_second=1
    for i in range(n-2):
        number_fist, number_second=number_second,number_second+number_fist

    print(number_second)



try:

    n = int(input("Nhập vào một số tự nhiên bất kì: "))

    SoThu1 = 0

    SoThu2 = 1

    if n <= 0:

        print("Vui lòng nhập lại")

    else:

        if n == 1 or n == 2:

            print(1)

        else:

            for i in range(2,n+1):

                SoThu3 = SoThu1 + SoThu2

                SoThu1 = SoThu2              

                SoThu2 = SoThu3

        '''

        Day so Fibo: 1 1 2 3 5 8 13 21 34 ...

        2 = 1 + 1                             3 = 1 + 2                                                                   5 = 3 + 2

        1 = 1                    ====>        2 = 2 (So thu nhat chuyen thanh so thu hai) Before:1 -> After: 2  ====>     ... Tiep tuc quy luat ...

        => 1 -> So Thu Hai  = 2               2 -> So Thu Hai = 3

        '''

        print(SoThu3)      

except:

    print("Vui lòng nhập lại đúng định dạng đầu vào! ")


try:
    n = int(input("n = "))
    if n < 0:
        print("Vui lòng nhập một số tự nhiên!")
    else:
        i, j = 0, 1
        f = []
        while len(f) <= n:
            f.append(i)
            f.append(j)
            i += j
            j += i
        print("Số Fibonacci thứ {} là: {}".format(n, f[n]))
except:
    print("Định dạng đầu vào không hợp lệ!")