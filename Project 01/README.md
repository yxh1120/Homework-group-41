Birthday attack
=

实验简介：
首先利用Python实现了简化的sm3算法，通过对随机生成的固定长度的字符串进行sm3加密，对加密的结果进行birthday攻击，为了展示运行效果，只让找到前4bit的碰撞进行演示，由于是自己编写的sm3算法，在效率上可能达不到最理想的情况。


测试实验结果如下图所示：

![image](https://github.com/yxh1120/project/blob/main/Project%201/1.png)

运行速度：
测试找到前4bit的碰撞约需要0.5秒。

实验环境：
IDLE (Python 3.10 64-bit)
