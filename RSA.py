if __name__=="__main__":

    #private
    p = 709
    q = 719
    # public

    e = 95  # 19 95 5351 26755 101669 508345
    n = p * q # 988027


def encript(e,n,J):
    C = 1
    for i in range(e): C *= J
    return(C % n)

def decript(p,q,e,C):
    k = ((p - 1) * (q - 1) + 1) / e
    J = 1
    for i in range(int(k)): J *= C
    return(J % n)

enc = encript(e,n,int(input("Data: ")))
dec = decript(p,q,e,enc)

print(enc)
print(dec)
