---
layout:     post
title:      深度神经网络的反向传播
subtitle:   数学推导
date:       2021-08-14
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 深度学习
---

## <center>引言

我们在之前已经推导出简单神经网络中数据传播（前向，反向传播）的公式，这里我们希望从头推导，并总结出多层反向传播的通式，从而构建多层的深度神经网络。

## <center>问题构建

我们这里以下面的四层神经网络为例：

![image-20210810153837384](/img/image-20210810153837384.png)

从输入到输出依次有三个权重矩阵和三个偏执向量，我们分别设置为矩阵$\{A_{3\times5},B_{5\times4},C_{4\times3}\}$​​​​和**行向量**$\{a_5,b_4,c_3\}$​​​​。再设激活函数为$f$​​​​​，这里设成带有广播性质的sigmoid函数。从而得到输出端的输出：

$$
\hat{y}_{1\times3}=f\bigg(f\big(f(xA-a)B-b\big)C-c\bigg)
$$

为了表达方便，我们再设中间层输入

$$
f(xA-a),f\big(f(xA-a)B-b\big)
$$

为$\text{hidden}_1$​和$\text{hidden}_2$​，表示两个隐藏层的输出，显然都是列向量。

以上是前向传播，而对于给定数据$x$​，反向传播的核心就是求解误差函数

$$
E=\dfrac12\|\hat{y}-y \|^2
$$

对各个参数的梯度，进而实现梯度下降。这里$y$是训练集的标签数据。

## <center>反向传播

我们先求$E$​对$c$​和$C$​的梯度：

$$
\begin{aligned}
\dfrac{\partial E}{\partial c}=\dfrac{\partial E}{\partial\hat{y}}\dfrac{\partial \hat{y}}{\partial c}
\end{aligned}
$$

我们利用链式法则将梯度拆开，$\partial E/\partial\hat{y}$​是一个长度为3的**行**向量：$(\hat{y}-y)$​​​。我们再看后面一项：

$$
\begin{aligned}
\dfrac{\partial\hat{y}}{\partial c}&=\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial c}\\
&=\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\dfrac{\partial{(\text{hidden}_2\cdot C-c)}}{\partial c}\\
\end{aligned}
$$

又被链式法则拆成了两项，第一项是向量对向量求导，对于Sigmoid函数，变量的独立性使得结果是一个$3\times 3$的对角矩阵，对角元就是对应位置的梯度：

$$
\dfrac{\partial f(x)}{\partial x}=\begin{bmatrix}
f(x)_1\big(1-f(x)_1\big)\\
&f(x)_2\big(1-f(x)_2\big)\\
&&f(x)_3\big(1-f(x)_3\big)
\end{bmatrix}
$$

后一项求导算出一个$3\times3$的负单位矩阵$-I_{3}$​​，和前面的矩阵乘起来，转置，再与$(\hat{y}-y)$相乘，从而得到梯度：

$$
\dfrac{\partial E}{\partial c}=-(\hat{y}-y)\circ\hat{y}\circ(1-\hat{y})
$$

这里的$\circ$是哈达玛积，也就是逐项乘积：$C=A\circ B\to C_{ij}=A_{ij}B_{ij}$​，这是由于激活函数是对矩阵元素独立计算。​​

我们接着求$E$对$C$的梯度：

$$
\begin{aligned}
\dfrac{\partial E}{\partial C}
&=\bigg(\dfrac{\partial(\text{hidden}_2\cdot C-c)}{\partial C}\bigg)^\top\cdot\dfrac{\partial E}{\partial(\text{hidden}_2\cdot C-c)}\\
&=\text{hidden}_2^\top\cdot\dfrac{\partial E}{\partial(\text{hidden}_2\cdot C-c)}\\
&=\text{hidden}_2^\top\cdot(\hat{y}-y)\circ\hat{y}\circ(1-\hat{y})\\
&=-\text{hidden}_2^\top\cdot\dfrac{\partial E}{\partial c}
\end{aligned}
$$

是一个$4\times3$矩阵，是和$C$​形状相同。接着往前，对$B$和$b$求偏导：

$$
\begin{aligned}
\dfrac{\partial E}{\partial b}
&=\dfrac{\partial E}{\partial\hat{y}}\dfrac{\partial \hat{y}}{\partial b}\\
&=(\hat{y}-y)\cdot\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot\dfrac{\partial{(\text{hidden}_2\cdot C-c)}}{\partial b}\\
&=(\hat{y}-y)\cdot\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot\dfrac{\partial{(\text{hidden}_2\cdot C-c)}}{\partial \text{hidden}_2}\cdot\dfrac{\partial\text{hidden}_2}{\partial b}\\
&=(\hat{y}-y)\cdot\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial\text{hidden}_2}{\partial b}\\
&=(\hat{y}-y)\cdot\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(\text{hidden}_1\cdot B-b)}{\partial(\text{hidden}_1\cdot B-b)}\cdot\dfrac{\partial(\text{hidden}_1\cdot B-b)}{\partial b}\\
&=(\hat{y}-y)\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot-\mathbf{I}\\
&=-(\hat{y}-y)\dfrac{\partial f(\text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}
\end{aligned}
$$

转置项中是四个矩阵乘积，其中

$$
\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}=\begin{bmatrix}
\text{hidden2}_{1}(1-\text{hidden2}_{1})\\
&\ddots\\
&&\text{hidden2}_{4}(1-\text{hidden2}_{4})\\
\end{bmatrix}
$$

$\text{hidden2}_i$对应$\text{hidden}_2$向量的第$i$​个元素。从而计算出$E$对$B$的梯度。

对于$B$​，易得出：

$$
\begin{aligned}
\dfrac{\partial E}{\partial B}
&=-\text{hidden}_1^\top\cdot\dfrac{\partial E}{\partial b}
\end{aligned}
$$

现在反向传播到最后一层，也就是去求$A$和$a$的偏导：

$$
\begin{aligned}
\dfrac{\partial E}{\partial a}
&=\dfrac{\partial E}{\partial\hat{y}}\dfrac{\partial \hat{y}}{\partial a}\\
&=(\hat{y}-y)\bigg(\dfrac{\partial f( \text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(\text{hidden}_1\cdot B-b)}{\partial(\text{hidden}_1\cdot B-b)}\cdot\dfrac{\partial(\text{hidden}_1\cdot B-b)}{\partial a}\bigg)\\
&=(\hat{y}-y)\bigg(\dfrac{\partial f( \text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(\text{hidden}_1\cdot B-b)}{\partial(\text{hidden}_1\cdot B-b)}\cdot B^\top\cdot\dfrac{\partial f(xA-a)}{\partial a}\bigg)\\
&=(\hat{y}-y)\bigg(\dfrac{\partial f( \text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(\text{hidden}_1\cdot B-b)}{\partial(\text{hidden}_1\cdot B-b)}\cdot B^\top\cdot\dfrac{\partial f(xA-a)}{\partial (xA-a)}\cdot-\mathbf{I}\bigg)\\
&=-(\hat{y}-y)\dfrac{\partial f( \text{hidden}_2\cdot C-c)}{\partial(\text{hidden}_2\cdot C-c)}\cdot C^\top\cdot\dfrac{\partial f(\text{hidden}_1\cdot B-b)}{\partial(\text{hidden}_1\cdot B-b)}\cdot B^\top\cdot\dfrac{\partial f(xA-a)}{\partial (xA-a)}\\
\dfrac{\partial E}{\partial A}&=-x^\top\cdot\dfrac{\partial E}{\partial a}
\end{aligned}
$$

## <center>规律总结

从上面的步骤中，我们可以总结出神经网络的反向传播的通式：对于一个$l$​​​​​​层神经网络（$l$​​​​​​是权重矩阵个数，比如上面的神经网络是3层），对于第$k(k\leq l)$​​​​​​层权重矩阵$W_k$​​​​​​和第$k$​​​​​​层偏置$b_k$​​​​​​（比如上面$k=3$​​​​​​时，$W_k=C$​​​​​​，$b_k=c$​​​​​​​​），则梯度有从后往前的递归关系：

$$
\begin{aligned}
\dfrac{\partial E}{\partial b_k}&=\begin{cases}
-(\hat{y}-y)\cdot\dfrac{\partial f(x_kW_k-b_k)}{\partial(x_kW_k-b_k)}\quad\text{if }k=l\\
\dfrac{\partial E}{\partial b_{k+1}}W_{k+1}^\top\dfrac{\partial f(x_kW_k-b_k)}{\partial(x_kW_k-b_k)}\quad\text{if }k<l\\
\end{cases}\\
\dfrac{\partial E}{\partial W_k}&=-x_k^\top\dfrac{\partial E}{\partial b_k}\\
\end{aligned}
$$

$x_i$​​为第$i$层神经元的输入，显然输出就是$f(W_ix_i-b_i)$​。

这里出现最多的项就是

$$
\dfrac{\partial f(W_ix_i-b_i)}{\partial(W_ix_i-b_i)}
$$

在真正实现时，我们实际上储存的是$f(W_ix_i-b_i)$，因为sigmoid函数和一些激活函数，比如tanh函数能够更快利用函数值求出导数值：

$$
\text{Sigmoid}'(x)=\text{Sigmoid}(x)\big(1-\text{Sigmoid}(x)\big)\\
\tanh'(x)=1-\tanh^2(x)
$$

至此，我们扫清了实现深度神经网络的数学障碍。
