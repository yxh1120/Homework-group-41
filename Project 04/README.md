optimize SM3
=
实验简介：
在基本实现的SM3算法的基础上，使用循环展开、多线程等多种技术进行加速，通过比较时间观察加速效果

**关键代码实现如下：**   
在扩展函数计算W以及W`时，我们使用循环展开，分别将3个循环以8，4，4的步长进行计算   
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2004/3.png)

在CF函数中，我们将循环以4个步长进行，同时我发现每次执行循环时，代码都要算几次2**32，因此我们可以将其提到函数一开始，这样避免了计算重复数值，节约了时间    
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2004/5.png)

在最后运行函数时使用多线程技术减少总运行时间，在本次代码中，使用了4个线程进行并行运算来进一步加速  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2004/4.png)

**测试结果如图所示：**    
优化前  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2004/1.png)

优化后  
![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2004/2.png)

运行速度：  
我们对10000次加密进行测试，通过对比可发现，优化效果比较明显，加密时间可实现优化近几十倍的效果。

实验环境：
IDLE (Python 3.10 64-bit)
