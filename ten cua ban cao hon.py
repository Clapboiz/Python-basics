def compare_(caoA, caoB, A,B):
    if caoA>caoB:
        print("A>B")
    elif caoA==caoB:
        print("A=B")
    else:
        print("A<B")
caoA, A=input().split()
caoB, B=input().split()

compare_(caoA, caoB, A, B)


def compare_(caoA, caoB, A, B):
    if caoA>caoB:
        return A
    elif caoA==caoB:
        return A
    else:
        return B
caoA, A=input().split()
caoB, B=input().split()
print("{} la ket qua cua phep so sanh".format(compare_(caoA, caoB, A, B)))