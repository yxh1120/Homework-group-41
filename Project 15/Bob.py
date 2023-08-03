import random
import socket
from gmssl import sm3

HOST = 'localhost'
PORT = 10001



def sm3_hash(message):
    message = message.encode('utf-8')
    msg_list = [i for i in message]
    hash_hex = sm3.sm3_hash(msg_list)

    return hash_hex

    
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

a = 2
b = 2       
p = 17 
G = [5, 1]
n = 19
message='202100460105'
e=hash(message)
k2=11
k3=7
d = 5
Pubk = mul(d, G)
ID='20021225'
ZZ=str(len(ID))+ID+str(a)+str(b)+str(G[0])+str(G[1])+str(Pubk[0])+str(Pubk[1])
Za=sm3_hash(ZZ)


def Sign(P1,Q1,e):
    global n,G,d,p,k2,k3
    P_=mul(gcd(d,n),P1)
    G_=G
    G_[1]= p - G_[1]
    P=add(P_,G_)
    Q2=mul(k2,G)
    R=add(mul(k3,Q1),Q2)
    r=(R[0]+e)%n
    s2=(d*k3)%n
    s3=(d*(r+k2))%n
    return r,s2,s3


    
y=[]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
for i in range(6):
    if i == 5:
        break
    s.sendall('1'.encode('UTF-8'))
    data = s.recv(512)
    y.append(data.decode('utf-8'))
print("连接成功！")
P1=[]
P1.append(int(y[0]))
P1.append(int(y[1]))
Q1=[]
Q1.append(int(y[2]))
Q1.append(int(y[3]))
e=int(y[4])
r,s2,s3=Sign(P1,Q1,e)
x=[]
b=0
x.append(str(r))
x.append(str(s2))
x.append(str(s3))
for i in range(4):
    data = s.recv(512)
    if i == 3:
        s.sendall('0'.encode('UTF-8'))
        break
    s.sendall(x[b].encode('UTF-8'))
    b += 1
s.close()
