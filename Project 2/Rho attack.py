import hashlib
import random
import time

def left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def sm3(message):
    
    IV = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
    
    message_length = len(message)
    
    message += '\x80'
    while len(message) % 64 != 56:
        message += '\x00'
    message += (message_length * 8).to_bytes(8, 'big').decode()
    
    blocks = [message[i:i+64] for i in range(0, len(message), 64)]
    
    for block in blocks:
        w = [0] * 68
        w[:16] = [int.from_bytes(block[i:i+4].encode(), 'big') for i in range(0, 64, 4)]
        
        for i in range(16, 68):
            w[i] = left(w[i-16] ^ w[i-9] ^ (left(w[i-3], 15)), 1) ^ (left(w[i-13], 7) ^ w[i-6])

        v = IV[:]
        for i in range(64):
            ss1 = left((left(v[0], 12) + v[4] + left(0x79cc4519, i % 32)) % (1 << 32), 7)
            ss2 = ss1 ^ left(v[0], 12)
            tt1 = (v[0] ^ v[1] ^ v[2]) % (1 << 32) + v[3] + ss2 + w[i] + int.from_bytes(b'\x79\xcc\x45\x19', 'big')
            tt2 = (v[4] ^ v[5] ^ v[6]) % (1 << 32) + v[7] + ss1 + w[i]
            v[3], v[2], v[1], v[0], v[7], v[6], v[5], v[4] = v[2], left(v[1], 9), v[0], tt1, v[6], left(v[5], 19), v[4], hashlib.sha256(hex(tt2)[2:].encode()).digest()[0] ^ tt2
        
        IV = [(IV[i] ^ v[i]) % (1 << 32) for i in range(8)]
    
    return ''.join([hex(i)[2:].zfill(8) for i in IV])



def rho(test):
    num = int(test/4)              
    x = hex(random.randint(0, 2**(test+1)-1))[2:]
    a = sm3(x)               
    b = sm3(a)             
    i = 1
    while a[:num] != b[:num]:
        i += 1
        a = sm3(a)              
        b = sm3(sm3(b))    
    b = a           
    a = x            
    for j in range(i):
        if sm3(a)[:num] == sm3(b)[:num]:
            return sm3(a)[:num],a,b
        else:
            a = sm3(a)
            b = sm3(b)


test = 8 #测试
start=time.time()
col, m1, m2 = rho(test)
print("找到碰撞！")
print("消息1:", m1)
print("消息2:", m2)
print("找到",test,"bit的碰撞")
end=time.time()
print('共消耗',end-start,'秒')
