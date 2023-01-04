print("c1 dung if + while")
a = int(input())

sum_of_even = 0
sum_of_odd = 0
while a > 0:
    last_digit = a % 10
    if last_digit % 2 == 0:
        sum_of_even += last_digit
    else:
        sum_of_odd += last_digit
    a = a//10
product_of_sum = sum_of_even * sum_of_odd
print(product_of_sum)


print("c2 dung list string")
try:

    inp = int(input('nhap chu so can tinh: '))

    if inp > 0:

        lst = list(str(inp))

        lst_odd_number = []

        lst_even_number = []

        for i in lst:

            if int(i) % 2 == 0:

                lst_even_number.append(int(i))

            else:

                lst_odd_number.append(int(i))

        print(sum(lst_odd_number)*sum(lst_even_number))

    else:

        print('Vui long nhap so tu nhien!')

except:

    print('Dinh dang dau vao khong hop le!')


print("c3 dung for va mang 1 chieu de quet cac phan tu di qua:")
n = input("moi nhap:")
list_even_number = 0
list_odd_number = 0
for i in range(len(str(n))):
    if int(n[i]) % 2 == 0:
        list_even_number += int((n[i]))
    else:
        list_odd_number += int((n[i]))
kq = list_even_number*list_odd_number
print(kq)
