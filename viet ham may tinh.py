def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    return a/b

def computer(a,b,phep_tinh):
    if phep_tinh=="+":
        return cong(a,b)
    if phep_tinh=="-":
        return tru(a,b)
    if phep_tinh=="*":
        return nhan(a,b)
    if phep_tinh=="/":
        if b==0:
            return "ko chia dc"
        return chia(a,b)

a,phep_tinh,b=input().split()
a=float(a)
b=float(b)
ketqua=computer(a,b,phep_tinh)
if ketqua=="ko chia dc":
    print("sai input")
else:
    print("{} la ket qua".format(computer(a,b,phep_tinh)))

#c2

def calculate(a, cal, b):
    def add():
        return a + b
    def sub():
        return a - b
    def mul():
        return a * b
    def div():
        return a / b
    key_value = (("+", add()), ("-", sub()), ("*", mul()), (":", div()))
    for key, value in key_value:
        if cal == key:
            return value
            break
try:
    a, cal, b = input().split()
    a, b = float(a), float(b)
    if cal == ":" and b == 0:
        print("Số chia phải khác 0!")
    else:
        print("{} {} {} = {}".format(a, cal, b, calculate(a, cal, b)))
except:
    print("Định dạng đầu vào không hợp lệ!")

#c3

def Process(cal):
    a, b = map(float, [cal[0], cal[2]])

    if "+" in cal:
        print(f"{a} + {b} = {a.__add__(b)}")     # a.__add__(b)     <=> a + b
    elif "-" in cal:
        print(f"{a} - {b} = {a.__sub__(b)}")     # a.__sub__(b)     <=> a - b
    elif "*" in cal:
        print(f"{a} * {b} = {a.__mul__(b)}")     # a.__mul__(b)     <=> a * b
    else:
        print(f"{a} / {b} = {a.__truediv__(b)}") # a.__truediv__(b) <=> a / b

def Input():
    # input = 1 + 2
    # split(input) = ['1', '+', '2']
    lst_str_cal = input("Enter the calculation: {Num 1} {+ - * /} {Num 2}: ").split()
    return lst_str_cal # -> list

if __name__ == "__main__":
    try:
        cal = Input()
        Process(cal)
        """ Example:
                Enter the calculation: {Num 1} {+ - * /} {Num 2}: 1 + 2
                1.0 + 2.0 = 3.0
        """

    except ValueError:
        print("Value error!")
    except ZeroDivisionError:
        print("Not divisible by 0!")