# print("Nhập vào số N lớn hơn 1: ")
 
# # Lấy dữ liệu
# n = int(input())
# flag = True
 
# # Kiểm tra SNT
# if (n < 2):
#     flag = False
# elif (n == 2):
#     flag = True
# elif (n % 2 == 0):
#     flag = False
# else:
#     # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
#     for i in range(3, n, 2):
#         if (n % i == 0):
#             flag = False
 
 
# # In kết quả
# if flag == True:
#     print(n, " là số nguyên tố")
# else:
#     print(n, " không phải là số nguyên tố")


                            #############################################################


# a= 'em oi bong toi truoc %s %s' %('se cuop', 'em di ahahahahah')
# print (a)
# b=list('cccc')
# print(b)


                             ###########################       list      ##################################

# a=[[1,2,3,4], [5,6,7,8,9], [10,11,1,11]]
# b=list(a)

# print(a)
# print(b)
# b[0]='pham cong lap'
# print(a)
# print(b)

                             #############################  tuple   ################################

# tup=(i for i in range(10) if i%2==0)
# a= tuple(tup)
# print(a)

                             #############################     set   ################################

# set_1= {12,13}
# print(set_1)
# print(type(set_1))       

                             #############################     dict  P1 ################################

# #c1
# name = 'SpaceX'
# member = 696969
# dic = dict(name='Kteam', member=69)
# print(dic)

# #c2
# name = 'SpaceX'
# member = 696969
# dic = dict(name='Kteam', member=69)
# print(dic)

                             #############################     dict  P1 ################################

# d={'ten':'lap','tuoi':19}
# print(d)

# dic={'name': 'Kteam', 'member': 69}
# print(dic['name'])

# a={'1': 1, '2': 2} | {3: '3', 4: '4'}
# print(a)
# b={1: '1', 2: '2'} | {2: 'Two'}
# print(b)

                             #############################     iterable ################################
itor = (x for x in range(3)) # sử dụng () cho ra một generator expression – một iterator
print(itor)
print(next(itor))
print(next(itor))
print(next(itor))

a=sorted([1, 6, 7, 2])
b=sorted([1, 6, 7, 2], reverse=True)
print(a)
print(b)