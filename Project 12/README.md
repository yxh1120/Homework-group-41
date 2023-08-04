verify the above pitfalls with proof-of-concept code
=

**k泄露导致d被攻击**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/2.png)

代码实现展示  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/6.png)

**k重用导致d被攻击**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/3.png)

代码实现展示  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/7.png)

**两名用户使用同样的k，可攻击d**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/4.png)

代码实现展示  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/8.png)

**在ECDSA签名中使用相同的d和k，导致d被攻击**  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/5.png)

代码实现展示  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/9.png)

运行结果如图：  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2012/1.png)

实验环境： IDLE (Python 3.10 64-bit)
