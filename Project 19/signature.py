import random
import time

def Cop(a, b):
    while a != 0:
        a, b = b % a, a
    if b != 1 and b != -1:
        return 1
    return 0

def gcd(a, m):
    if Cop(a, m):
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

def add(P,Q):
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

def mul(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = add(t, l)
        n = n - 1
    return t

def Sign(m):
    global n,G,d
    k=random.randint(1,n-1)
    R=mul(k,G)
    r=R[0] % n
    e=hash(message)
    s=(gcd(k, n) * (e + d * r)) % n
    return r,s


def Verify(e,r,s):
    global Pubk,n,G
    w=gcd(s,n)
    S=add(mul((e * w) % n,G),mul((r * w) % n,Pubk))
    if(S!=0):
        if(S[0]%n==r):
            return True
        else: return False
    return False

def forge(r,s):
    global n,G,Pubk
    u=random.randint(1,n-1)
    v=random.randint(1,n-1)
    R1=add(mul(u,G),mul(v,Pubk))
    r1=R1[0]%n
    e1=(r1 * u * gcd(v, n)) % n
    s1 = (r1 * gcd(v, n)) % n
    print('伪造签名为:(',r1,s1,')')
    if(Verify(e1, r1, s1)):
        print('验证成功')
    else: print('验证失败')
    
a = 2
b = 2       
p = 17 
G = [5, 1]
n = 19
message='I am Satoshi'

d = 7
Pubk = mul(d, G)



r,s=Sign(message)
print("原始签名为:(",r,s,')')

if(Verify(hash(message),r,s)):
    print('验证成功')
else: print('验证失败')
start=time.time()
forge(r,s)
end=time.time()
print("共消耗",end-start,"秒")


