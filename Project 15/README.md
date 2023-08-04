sm2 2P sign
=
SM2 2P签名协议是一种允许双方使用SM2椭圆曲线公钥加密算法对消息进行安全签名的加密协议。该协议的基本思想是双方交换消息以建立共享密钥，然后使用该密钥对消息进行签名。  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2015/3.png)

**关键代码实现：**  
Alice首先调用S1、S2函数求得P1、Q1、e，之后通过socket发送给用户B，等待用户B计算完成后从它那里接收r、s2、s3，并将这三个数据作为参数传到S5函数中，得到最终签名值。  
Bob从Alice处接收P1、Q1、e，并将其传入Sign函数中，得到r、s2、s3，最后将其传回用户A即可。  
Alice:  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2015/4.png)

Bob:  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2015/5.png)

运行结果如图：  
Alice:
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2015/1.png)

Bob:
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2015/2.png)

实验环境： IDLE (Python 3.10 64-bit)
