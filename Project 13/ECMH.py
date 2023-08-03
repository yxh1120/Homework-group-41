from gmssl import sm2
from hashlib import sha256
import time

p='FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF'
a='FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC'
b='28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93'
n='FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123'
g='32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7'\
'BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0'

def ECMH(msg):
    hash_msg= sha256(str(msg).encode()).digest()
    pri = int(hash_msg.hex(), 16)
    sm2_c = sm2.CryptSM2(private_key="", public_key="")
    P1 = sm2_c._kg(pri, g)
    return P1

def ECMH_append(hash, msg):

    hash_msg = sha256(str(msg).encode()).digest()
    sm2_c = sm2.CryptSM2(private_key="", public_key="")
    pri = int(hash_msg.hex(), 16)
    P1 = sm2_c._kg(pri, g)
    P = sm2_c._add_point(P1, hash)
    P = sm2_c._convert_jacb_to_nor(P)
    return P


message1 ='abcdefgh'
message2 ='123456789'

start=time.time()
message_hash1 = ECMH(message1)
message_hash2 = ECMH(message2)
append_message2_hash=ECMH_append(message_hash1, message2)
append_message1_hash=ECMH_append(message_hash2, message1)
end=time.time()

print("message1的hash值:\n  ", message_hash1)
print("message2的hash值:\n  ", message_hash2)

print("message1添加message2后的hash值:\n  ", append_message2_hash)
print("message2添加message1后的hash值:\n  ", append_message1_hash)

print('共消耗',end-start,'秒')
