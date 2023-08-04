AES
=
AES为高级加密标准，属于分组密码，把明文分成一组一组的，每组长度相等，每次加密一组数据，直到加密完整个明文。在AES标准规范中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位）。密钥的长度可以使用128位、192位或256位。

**AES算法流程**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/2.png)

**关键函数代码实现：**  
异或密钥  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/3.png)

行移位  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/4.png)

列混淆  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/6.png)

S盒变换  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/5.png)

测试结果如图  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2009/1.png)

运行速度：  
实现一次AES加密约消耗0.02秒

实验环境： IDLE (Python 3.10 64-bit)
