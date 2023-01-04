# num = 1

# while num <= 3 :
#     print(num)
#     num += 1
# print("END")
# #> 1
# #> 2
# #> 3
# #> END


num = 0
total = 0

while num < 4:
    if num == 2:
        print('!!BREAK!!')
        break
    print(num)
    total+=num
    num += 1
print("Tổng =",total)
n=5
while n>0:
    n=n-1
    if n==2:
        continue
    print(n)
print("done!")
