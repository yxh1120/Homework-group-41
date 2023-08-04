forge a signature
=
**伪造的具体实现方法：**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2019/3.png)

**ECDSA签名过程：**  
1、选择一条椭圆曲线Ep(a,b)，和基点G；  
2、选择私有密钥k（k<n，n为G的阶），利用基点G计算公开密钥K=kG；  
3、产生一个随机整数r（r<n），计算点R=rG；  
4、将原数据和点R的坐标值x,y作为参数，计算SHA1做为hash，即Hash=SHA1(原数据,x,y)；  
5、计算s≡r - Hash * k (mod n)  
6、r和s做为签名值，如果r和s其中一个为0，重新从第3步开始执行  

**ECDSA验证过程：**  
1、接受方在收到消息(m)和签名值(r,s)后，进行以下运算  
2、计算：sG+H(m)P=(x1,y1), r1≡ x1 mod p。  
3、验证等式：r1 ≡ r mod p。  
4、如果等式成立，接受签名，否则签名无效。  

**关键代码实现：**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2019/2.png)

运行结果如图：  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2019/1.png)

运行速度：  伪造一次签名并验证成功约需要0.02秒

实验环境： IDLE (Python 3.10 64-bit)
