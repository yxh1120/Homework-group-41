import hashlib
import random

p = 6277101735386680763835789423207666416083908700390324961279
a = 0
b = 7
Gx = 28948022309329048855892746252171976963228307975334815319267288091773240550737
Gy = 25215240129546715419327374937300700509970766929654737037893221091505261823773
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and P[1] != Q[1]:
        return None
    if P[0] == Q[0]:
        l = (3 * P[0] * P[0] + a) * pow(2 * P[1], p - 2, p) % p
    else:
        l = (Q[1] - P[1]) * pow(Q[0] - P[0], p - 2, p) % p
    x = (l * l - P[0] - Q[0]) % p
    y = (l * (P[0] - x) - P[1]) % p
    return (x, y)

def point_mul(n, P):
    R = None
    for i in range(256):
        if (n >> i) & 1:
            R = point_add(R, P)
        P = point_add(P, P)
    return R

def hash_to_point(msg):
    h = hashlib.sha256()
    h.update(msg)
    digest = h.digest()
    x = int.from_bytes(digest, 'big')
    while True:
        candidate = (x % p, 0)
        if point_mul(n, candidate) is not None:
            return candidate
        x += 1

def sign(msg, sk):
    k = random.randint(1, n-1)
    R = point_mul(k, (Gx, Gy))
    e = int.from_bytes(hashlib.sha256(msg + R[0].to_bytes(32, 'big')).digest(), 'big')
    s = (k - sk * e) % n
    return (R[0], s)

def verify(msg, sig, pk):
    e = int.from_bytes(hashlib.sha256(msg + sig[0].to_bytes(32, 'big')).digest(), 'big')
    R = point_add(point_mul(sig[1], (Gx, Gy)), point_mul(e, pk))
    if R is None or R[0] != sig[0]:
        return False
    return True
        

msgs = [b"202100460105",b"yanxiaohan"]
sk = random.randint(1, n-1)
pk = point_mul(sk, (Gx, Gy))
sigs = []
for msg in msgs:
    sigs.append(sign(msg, sk))

print("私钥:", hex(sk))
print("公钥:", hex(pk[0]))
print("消息1:",msgs[0])
print("签名1:",sigs[0])
print("消息2:",msgs[1])
print("签名2:",sigs[1])


pks=[pk] * len(msgs)    
for i in range(len(msgs)):
    if not verify(msgs[i], sigs[i], pks[i]):
        print("验证成功！")
    else:print("验证失败！")




