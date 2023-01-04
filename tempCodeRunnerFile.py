#cao sieu .2
def Sum(*args):
    # Ex = map(str, [1, 2, 3, ...]) = ['1', '2', '3', ...]
    # ' + '.join(Ex) = 1 + 2 + 3 ...
    return f"{' + '.join(map(str, args))} = {sum(args)}"

def Input():
    n = -1
    while n < 0:
        n = int(input("Enter the number: "))
        if n < 0:
            print("n >= 0")

    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return lst
