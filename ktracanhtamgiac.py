try:
    a,b,c=map(float, input().split())

    if a+b>c and a+c>b and b+c>a:
        print("3 canh tao thanh tam giac")
    else:
        print("3 canh {}, {}, {}, ko tao thanh tam giac".format(a,b,c)) 
except:
    print("Error")
