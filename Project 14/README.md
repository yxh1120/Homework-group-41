PGP_SM2
=
PGP（Pretty Good Privacy）是一种广泛使用的加密程序，可为数据通信提供加密隐私和身份验证。SM2 是一种基于椭圆曲线的加密算法，在中国被广泛使用。PGP 使用两种类型的加密算法来保护数据：对称密钥加密和公钥加密。
对称密钥加密是一种使用相同密钥加密和解密的算法，因此在加密和解密之间需要共享密钥。而公钥加密则是一种使用不同的密钥加密和解密的算法，其中公钥用于加密，而私钥用于解密。  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2014/3.png)

关键代码实现：  
加密函数:
使用SM2加密算法与对应人公钥将密钥K进行加密，之后使用密钥K与对称加密算法SM4加密明文，得到两个密文。  
解密函数:
使用私钥调用SM2进行解密，将密钥K计算出来，之后利用密钥K调用对称加密算法SM4得到明文。  
在主函数中，我们首先调用加密算法得到两个密文消息，之后将其传入解密算法中，即可得到明文与对应的密钥K   
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2014/2.png)

运行结果如图：  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2014/1.png)

实验环境： IDLE (Python 3.10 64-bit)
