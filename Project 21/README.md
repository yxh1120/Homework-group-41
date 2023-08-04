 Schnorr Bacth
 =
 Schnorr签名算法最初是由德国密码学家ClausSchnorr于2008年提出的，在密码学中，它是一种数字签名方案，以其简单高效著称。  
 Schnorr Batch是指Schnorr签名的批量处理技术。Schnorr Batch的目标是提高生成和验证Schnorr签名的效率。



 **Schnorr数字签名具体流程**  
 ![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2021/2.png)

 **Schnorr Batch具体实现方法**  
 在传统的Schnorr签名方案中，每个签名需要独立进行计算和验证，这可能会导致高昂的计算开销。
 Schnorr Batch通过将多个签名的计算合并为一个集合，然后进行批量处理，从而减少了重复的计算步骤，提高了效率。
 这种批量处理技术尤其在密码学协议和区块链系统中具有潜在的应用，因为它可以显著提高系统的性能和可扩展性。  
 ![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2021/3.png)

 **关键代码实现：**  
 在实现原本的Schnorr签名方案的签名（Sign）函数和验证（Verify）函数基础上，通过将多个签名的计算合并为一个集合，批量进行处理，提高了效率  
 ![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2021/4.png)

 运行结果如图：  
 ![image](https://github.com/yxh1120/Homework-group-41/blob/main/Project%2021/1.png)

实验环境： IDLE (Python 3.10 64-bit)
