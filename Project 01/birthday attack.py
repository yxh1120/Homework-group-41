import struct
import random
import time

def left(x, n):
    return ((x << (n & 31)) | (x >> (32 - (n & 31)))) & 0xFFFFFFFF

def padding(message):
    length = len(message) * 8
    message += b'\x80'
    message += b'\x00' * ((56 - len(message) % 64) % 64)
    message += struct.pack('>Q', length)
    return message

def sm3_compress(block, h):
    w = [0] * 68
    for i in range(16):
        w[i] = struct.unpack('>I', block[i*4:i*4+4])[0]
    for i in range(16, 68):
        w[i] = (left(w[i-16] ^ w[i-9], 3) ^ left(w[i-3], 15) ^ (w[i-13] ^ w[i-6])) & 0xFFFFFFFF
    a, b, c, d, e, f, g, hh = h  
    for i in range(0, 64):
        ss1 = (left((left(a, 12) + e + left(0x79CC4519, i)), 7)) & 0xFFFFFFFF
        ss2 = (ss1 ^ left(a, 12)) & 0xFFFFFFFF
        tt1 = (sm3_ffj(a, b, c) + d + ss2 + w[i]) & 0xFFFFFFFF
        tt2 = (sm3_ggj(e, f, g) + hh + ss1 + w[i]) & 0xFFFFFFFF
        d = c
        c = left(b, 9) & 0xFFFFFFFF
        b = a
        a = tt1
        hh = g 
        g = left(f, 19) & 0xFFFFFFFF
        f = e
        e = sm3_p0(tt2)
    h[0] ^= a
    h[1] ^= b
    h[2] ^= c
    h[3] ^= d
    h[4] ^= e
    h[5] ^= f
    h[6] ^= g
    h[7] ^= hh  
    return h

def sm3(message):
    h = [0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600, 0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E]
    message = padding(message)
    blocks = [message[i:i+64] for i in range(0, len(message), 64)]
    for block in blocks:
        h = sm3_compress(block, h)
    hash_value = ''.join([format(num, '08x') for num in h])
    return hash_value

def sm3_ffj(x, y, z):
    return (x ^ y ^ z)

def sm3_ggj(x, y, z):
    return ((x & y) | (x & z) | (y & z))

def sm3_p0(x):
    return (x ^ (left(x, 9)) ^ (left(x, 17)))

def birthday_attack():
    hash_dict = {}
    while True:
        message = get_random_message()
        hash_value = sm3(message)
        if hash_value[:4] in hash_dict:
            original_message = hash_dict[hash_value[:4]]
            print("找到碰撞！")
            print("哈希值:", hash_value)
            print("消息1:", original_message)
            print("消息2:", message)
            break
        hash_dict[hash_value[:4]] = message

def get_random_message():
    #测试128bit
    random_message = bytes(''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=128 )), 'utf-8')
    return random_message

start=time.time()
birthday_attack()
end=time.time()
print('共消耗',end-start,'秒')
