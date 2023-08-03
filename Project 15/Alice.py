import random
import socket
from gmssl import sm3

HOST = ''
PORT = 10001

def sm3_hash(message):
    message = message.encode('utf-8')
    msg_list = [i for i in message]
    hash_hex = sm3.sm3_hash(msg_list)

    return hash_hex

    
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
k=2
d = 7
Pubk = mul(d, G)
ID='20021225'
ZZ=str(len(ID))+ID+str(a)+str(b)+str(G[0])+str(G[1])+str(Pubk[0])+str(Pubk[1])
Za=sm3_hash(ZZ)

def S1():
    global n,G,d
    P1=mul(gcd(d,n),G)
    return P1

def S3():
    global Za,message,k,G
    M_=Za+message
    e=hash(M_)
    Q1=mul(k,G)
    return Q1,e

def S5(r,s2,s3):
    s=((d*k)*s2+d*s3-r)%n
    if(s!=0 or s!=n-r):
        return r,s
    return 0,0

x=[]
P1=S1()
Q1,e=S3()
x.append(str(P1[0]))
x.append(str(P1[1]))
x.append(str(Q1[0]))
x.append(str(Q1[1]))
x.append(str(e))
i=-1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
while True:
    i += 1
    data = conn.recv(2048)
    if data.decode('utf-8') == 0:
        break
    conn.send(x[i].encode('UTF-8'))
    if i == 4:
        break


y=[]

for i in range(4):
    conn.send('1'.encode('UTF-8'))
    data = conn.recv(2048)
    if data.decode('utf-8') == 0:
        break
    y.append(data.decode('utf-8'))
conn.close()

r=int(y[0])
s2=int(y[1])
s3=int(y[2])
r,s = S5(r,s2,s3)
print('Sign：(',r,s,")")
