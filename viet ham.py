def inp(name, age):
    print("ten cua ban la:{},{}".format(name, age))
try:    
    name=input()
    age=input()
    inp(name, age)
except:
    print("sai")