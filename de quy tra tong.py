


def dequy(n):
    if n>0:
        return n+dequy(n-1)
    return 0

n=int(input())
print("ket qua la {}".format(dequy(n)))