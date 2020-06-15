# NWW
def NWW(a, b):
    if a >= b:
        pass
    elif b > a:
        c = b
        b = a
        a = c
    c = b
    m = a*b
    while m >= b:
        if b % a == 0:
            return(b)
        else:
            b += c


print(NWW(6, 932))


# pierwsza
def pierwsza(x):
    x = abs(x)
    if x == 1 or x == 0:
        return(False)
    else:
        for i in range(x-2):
            if x % (i+2) == 0:
                return(False)
        return(True)


print(pierwsza(5))
