a,b,c=map(float, input().split())

if a+b>c and a+c>b and b+c>a:
    print("3 canh nay tao thanh 1 tam giac thuong va ngoai ra")
    if a*a+b*b==c*c:
        print("tam giac nay la mot tam giac vuong")
    elif a==b==c:
        print("tam giac nay la mot tam giac deu")
    elif a==b or b==c or c==a:
        print("tam giac nay la mot tam giac can")
    elif a*a>b*b+c*c or b*b>a*a+c*c or c*c>a*a+b*b:
        print("tam giac nay la mot tam giac tu")        
    else:
        print("tam giac nay la mot tam giac nhon")
    print("3 canh {},{},{} tao thanh 1 tam giac".format(a,b,c))