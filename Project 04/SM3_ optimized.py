import random
import threading
import time


IV = [0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600, 0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E]
T = [0x79cc4519, 0x7a879d8a]

def ROL(X,i):
    i = i % 32
    return ((X<<i)&0xFFFFFFFF) | ((X&0xFFFFFFFF)>>(32-i))
def FF(X,Y,Z,j):
    if j>=0 and j<=15:
        return X ^ Y ^ Z
    else:
        return ((X & Y) | (X & Z) | (Y & Z))
def GG(X,Y,Z,j):
    if j>=0 and j<=15:
        return X ^ Y ^ Z
    else:
        return ((X & Y) | (~X & Z))
def P0(X):
    return X^ROL(X,9)^ROL(X,17)
def P1(X):
    return X^ROL(X,15)^ROL(X,23)
def T_(j):
    if j>=0 and j<=15:
        return T[0]
    else:
        return T[1]
def TC(message):
    m = bin(int(message,16))[2:]
    if len(m) != len(message)*4:
        m = '0'*(len(message)*4-len(m)) + m
    l = len(m)
    l_bin = '0'*(64-len(bin(l)[2:])) + bin(l)[2:]
    m = m + '1'
    m = m + '0'*(448-len(m)%512) + l_bin
    m = hex(int(m,2))[2:]
    return m
def Group(m):
    n = len(m)/128
    M = []
    for i in range(int(n)):
        M.append(m[0+128*i:128+128*i])
    return M
def Expand(M,n):
    W = []
    W_ = []
    for j in range(0,16,8):
        W.append(int(M[n][0+8*j:8+8*j],16))
        W.append(int(M[n][0+8*(j+1):8+8*(j+1)],16))
        W.append(int(M[n][0+8*(j+2):8+8*(j+2)],16))
        W.append(int(M[n][0+8*(j+3):8+8*(j+3)],16))
        W.append(int(M[n][0+8*(j+4):8+8*(j+4)],16))
        W.append(int(M[n][0+8*(j+5):8+8*(j+5)],16))
        W.append(int(M[n][0+8*(j+6):8+8*(j+6)],16))
        W.append(int(M[n][0+8*(j+7):8+8*(j+7)],16))
    for j in range(16,68,4):
        W.append(P1(W[j-16]^W[j-9]^ROL(W[j-3],15))^ROL(W[j-13],7)^W[j-6])
        W.append(P1(W[j-15]^W[j-8]^ROL(W[j-2],15))^ROL(W[j-12],7)^W[j-5])
        W.append(P1(W[j-14]^W[j-7]^ROL(W[j-1],15))^ROL(W[j-11],7)^W[j-4])
        W.append(P1(W[j-13]^W[j-6]^ROL(W[j-0],15))^ROL(W[j-10],7)^W[j-3])
    for j in range(0,64,4):
        W_.append(W[j]^W[j+4])
        W_.append(W[j+1]^W[j+5])
        W_.append(W[j+2]^W[j+6])
        W_.append(W[j+3]^W[j+7])
    Wstr = ''
    W_str = ''
    for x in W:
        Wstr += (hex(x)[2:] + ' ')
    for x in W_:
        W_str+= (hex(x)[2:] + ' ')
    return W,W_

def CF(V,M,i):
    aa=2**32
    A,B,C,D,E,F,G,H = V[i]
    W,W_ = Expand(M,i)
    for j in range(0,64,4):
        SS1 = ROL((ROL(A,12)+E+ROL(T_(j),j%32))%(aa),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j)+D+SS2+W_[j])%(aa)
        TT2 = (GG(E,F,G,j)+H+SS1+W[j])%(aa)
        D = C
        C = ROL(B,9)
        B = A
        A = TT1
        H = G
        G = ROL(F,19)
        F = E
        E = P0(TT2)
        #
        SS1 = ROL((ROL(A,12)+E+ROL(T_(j+1),(j+1)%32))%(aa),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j+1)+D+SS2+W_[j+1])%(aa)
        TT2 = (GG(E,F,G,j+1)+H+SS1+W[j+1])%(aa)
        D = C
        C = ROL(B,9)
        B = A
        A = TT1
        H = G
        G = ROL(F,19)
        F = E
        E = P0(TT2)
        #
        SS1 = ROL((ROL(A,12)+E+ROL(T_(j+2),(j+2)%32))%(aa),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j+2)+D+SS2+W_[j+2])%(aa)
        TT2 = (GG(E,F,G,j+2)+H+SS1+W[j+2])%(aa)
        D = C
        C = ROL(B,9)
        B = A
        A = TT1
        H = G
        G = ROL(F,19)
        F = E
        E = P0(TT2)
        #
        SS1 = ROL((ROL(A,12)+E+ROL(T_(j+3),(j+3)%32))%(aa),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j+3)+D+SS2+W_[j+3])%(aa)
        TT2 = (GG(E,F,G,j+3)+H+SS1+W[j+3])%(aa)
        D = C
        C = ROL(B,9)
        B = A
        A = TT1
        H = G
        G = ROL(F,19)
        F = E
        E = P0(TT2)

    a,b,c,d,e,f,g,h = V[i]
    V_ = [a^A,b^B,c^C,d^D,e^E,f^F,g^G,h^H]
    return V_

def SM3(M):
    n = len(M)
    V = []
    V.append(IV)
    for i in range(0,n):
        V.append(CF(V,M,i))
    return V[n]


def SM3_test():
    list_r = random.randint(0, pow(2,64))
    m = TC(str(list_r))
    M = Group(m)
    Vn=SM3(M)
    aa=""
    for x in Vn:
        aa += hex(x)[2:]
    #print(aa)

def fun():
    for i in range(2500):
        SM3_test()

num=10000
t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=fun)
t3 = threading.Thread(target=fun)
t4 = threading.Thread(target=fun)
start = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
end_time = time.time()
print('运行',num,"次共消耗",(time.time()-start),'秒')
