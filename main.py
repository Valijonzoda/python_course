def printText():
    print("hello world")
printText()


def sqRing(p):
    s = 3.1415 * (p ** 2)  #git test
    return s
print(sqRing(20))
#git test

def getSqr(w, h):
    return 2*(w+h)
print(getSqr(4, 5)) #up data


def get_args(a, b, c, d):
    print(a, b, c, d)

l = ("hello", 77, [1, "hh", "32"], False)
get_args(*l)


def aaargs(*args, **kwargs):
    print(args)
    print(kwargs)


#notebook123
