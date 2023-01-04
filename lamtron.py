# s1 = input()
# s2 = input()

temp = False
try:
    s11 = float(input())
    s21 = int(input())
    temp = True
except:
    print("Error: No Input")
if temp:
    print("dung format: {0:.{1}f}".format(s11, s21))
    cach2 = round(s11, s21)
    print("dung round:", cach2)
