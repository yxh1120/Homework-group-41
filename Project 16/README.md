sm2 2P decrypt
=
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2016/1.png)

**关键代码实现：**  
Alice：编写加密函数，求出C1,C2,C3,得到一组密文C1||C2||C3,
Alice求解出T1并发送给Bob，等待Bob。  
从Bob那里接收T2，求出相关参数，得到M"和u，若u==C3，则消息就是M"。  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2016/4.png)

Bob:接收Alice传来的T1，之后由T1计算T2，将T2传输回Alice。  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2016/5.png)

运行结果如图：  
Alice：  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2016/2.png)

Bob：  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2016/3.png)

实验环境： IDLE (Python 3.10 64-bit)
