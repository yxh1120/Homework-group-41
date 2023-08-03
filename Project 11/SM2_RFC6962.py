import random
import string
import math
from collections import Counter
import time

Bits_len=32

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
def TC(m):
    by = bytes(m,'UTF-8')
    message = by.hex()
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
    for j in range(16):
        W.append(int(M[n][0+8*j:8+8*j],16))
    for j in range(16,68):
        W.append(P1(W[j-16]^W[j-9]^ROL(W[j-3],15))^ROL(W[j-13],7)^W[j-6])
    for j in range(64):
        W_.append(W[j]^W[j+4])
    Wstr = ''
    W_str = ''
    for x in W:
        Wstr += (hex(x)[2:] + ' ')
    for x in W_:
        W_str+= (hex(x)[2:] + ' ')
    return W,W_

def CF(V,M,i):
    A,B,C,D,E,F,G,H = V[i]
    W,W_ = Expand(M,i)
    for j in range(64):
        SS1 = ROL((ROL(A,12)+E+ROL(T_(j),j%32))%(2**32),7)
        SS2 = SS1 ^ ROL(A,12)
        TT1 = (FF(A,B,C,j)+D+SS2+W_[j])%(2**32)
        TT2 = (GG(E,F,G,j)+H+SS1+W[j])%(2**32)
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
    for i in range(n):
        V.append(CF(V,M,i))
    return V[n]


def SM3_test(PP):
    m = TC(PP)
    M = Group(m)
    Vn=SM3(M)
    aa=""
    for x in Vn:
        aa += hex(x)[2:]
    return aa

def Coprime(a, b):
    while a != 0:
        a, b = b % a, a
    if b != 1 and b != -1:
        return 1
    return 0

def gcd(a, m):
    if Coprime(a, m):
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m

def T_add(P,Q):
    if (P == 0):
        return Q
    if (Q == 0):
        return P
    if P == Q:
        aaa=(3*pow(P[0],2) + a)
        bbb=gcd(2*P[1],p)
        k=(aaa*bbb)%p 
    else:
        aaa=(P[1]-Q[1])
        bbb=(P[0]-Q[0])
        k=(aaa*gcd(bbb,p))%p 

    Rx=(pow(k,2)-P[0] - Q[0]) %p
    Ry=(k*(P[0]-Rx) - P[1])%p
    R=[Rx,Ry]
    return R



def T_mul(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = T_add(t, l)
        n = n - 1
    return t

def Sign(M,k):
    global n,G,d,Za
    M_=Za+M
    e = SM3_test(M_)
    R=T_mul(k,G)
    r=(R[0]+int(e,16)) % n
    e=hash(message)
    s=(gcd(1+d, n) * (k - d * r)) % n
    return r,s

def Verify(r,s):
    global Pubk,n,G,message,Za
    M_=Za+message
    e =SM3_test(M_)
    t=(r+s)%n
    S=T_add(T_mul(s,G),T_mul(t,Pubk))
    R=(int(e,16)+S[0])%n
    if(R==r):
        return True
    else: return False
    
a = 2
b = 2       
p = 17 
G = [5, 1]
n = 19
message='yanxiaohan'
e=hash(message)
d = 7
Pubk = T_mul(d, G)
ID='202100460105'
ZZ=str(len(ID))+ID+str(a)+str(b)+str(G[0])+str(G[1])+str(Pubk[0])+str(Pubk[1])
Za=SM3_test(ZZ)


k=int(SM3_test(str(d)+SM3_test(Za+message)+'SM2'),16)
k=k%n
r,s=Sign(message,k)
print('消息：',message)
print("签名:(",r,s,')')

if(Verify(r,s)):
    print('验证成功')
else: print('验证失败')
