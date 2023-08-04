import random
import socket
from gmssl import sm3

HOST = ''
PORT = 10110


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
message='20021225'
e=hash(message)
k=2
d = 7
Pubk = mul((gcd(d*5,n)-1), G)
ID='202100460105'
ZZ=str(len(ID))+ID+str(a)+str(b)+str(G[0])+str(G[1])+str(Pubk[0])+str(Pubk[1])
Za=sm3_hash(ZZ)

def Enc(message):
    global k,Pubk
    C1=mul(k,G)
    R=mul(k,Pubk)
    t=sm3_hash(str(R[0])+str(R[1]))
    C2=int(message)^int(t,16)
    C3=hash(str(R[0])+message+str(R[1]))
    return C1,C2,C3


C1,C2,C3=Enc(message)
assert C1!=0
T1=mul(gcd(d,n),C1)
x=[]
x.append(str(T1[0]))
x.append(str(T1[1]))
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
    if i == 1:
        break


y=[]

for i in range(3):
    conn.send('1'.encode('UTF-8'))
    data = conn.recv(2048)
    if data.decode('utf-8') == 0:
        break
    y.append(data.decode('utf-8')) 
conn.close()
T2=[0,0]
T2[0]=int(y[0])
T2[1]=int(y[1])
C1_=C1
C1_[1]=p-C1_[1]
R=add(T2,C1_)
t=sm3_hash(str(R[0])+str(R[1]))
M__=C2^int(t,16)
u=hash(str(R[0])+str(M__)+str(R[1]))
print('解密得到的消息:',M__)
print('原始消息:',int(message))
if M__==int(message):
    print("解密成功！")
else:
    print("解密失败！")
