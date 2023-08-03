from gmssl import sm2
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

key = b'abcdefgh12345678'
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
crypt_sm4 = CryptSM4()

private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)


def Enc(msg,k):
    global iv,crypt_sm4,sm2_crypt
    data = sm2_crypt.encrypt(k)
    crypt_sm4.set_key(k, SM4_ENCRYPT)
    value = crypt_sm4.crypt_cbc(iv , msg)
    return value,data

def Dec(value,data):
    global crypt_sm4,sm2_crypt
    k =sm2_crypt.decrypt(data)
    crypt_sm4.set_key(k, SM4_DECRYPT)
    decrypt_value = crypt_sm4.crypt_ecb(value)
    return decrypt_value,k

message=b'202100460105'
value,data=Enc(message,key)
print("加密结果：")
print(value)
print(data)
decrypt_value,k=Dec(value,data)
print("解密结果：")
print(decrypt_value)
print(k)

    
