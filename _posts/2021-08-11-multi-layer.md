---
layout:     post
title:      深度神经网络的反向传播
subtitle:   数学推导
date:       2021-08-11
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

从输入到输出依次有三个权重矩阵和三个偏执向量，我们分别设置为矩阵$\{A_{5\times3},B_{4\times5},C_{3\times 4}\}$​​​​和**列向量**$\{a_5,b_4,c_3\}$​​​​。再设激活函数为$f$​​​​​，这里设成带有广播性质的sigmoid函数。从而得到输出端的输出：

$$
\hat{y}_{1\times3}=f\bigg(C\cdot f\big(B\cdot f(Ax-a)-b\big)-c\bigg)
$$

为了表达方便，我们再设中间层输入

$$
f(Ax-a),f\big(B\cdot f(Ax-a)-b\big)
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
\dfrac{\partial E}{\partial c}=(\dfrac{\partial \hat{y}}{\partial c})^\top\dfrac{\partial E}{\partial\hat{y}}
\end{aligned}
$$

我们利用链式法则将梯度拆开，$\partial E/\partial\hat{y}$​是一个长度为3的**列**向量：$(\hat{y}-y)$​​​。我们再看前面一项：

$$
\begin{aligned}
\dfrac{\partial\hat{y}}{\partial c}&=\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial c}\\
&=\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot \text{hidden}_2-c)}\dfrac{\partial{(C\cdot \text{hidden}_2-c)}}{\partial c}\\
\end{aligned}
$$

又被链式法则拆成了两项，第一项是向量对向量求导，变量的独立性使得结果是一个$3\times 3$的对角矩阵，对角元就是对应位置的梯度：

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
\dfrac{\partial E}{\partial C}&=\dfrac{\partial E}{\partial(C\cdot\text{hidden}_2-c)}\cdot\text{hidden}_2^\top\\
&=(\hat{y}-y)\circ\hat{y}\circ(1-\hat{y}) \cdot\text{hidden}_2^\top\\
&=-\dfrac{\partial E}{\partial c}\cdot\text{hidden}_2^\top
\end{aligned}
$$

是一个$3\times 4$矩阵，是和$C$​形状相同。接着往前，对$B$和$b$求偏导：

$$
\begin{aligned}
\dfrac{\partial E}{\partial b}
&=(\dfrac{\partial \hat{y}}{\partial b})^\top\dfrac{\partial E}{\partial\hat{y}}\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot \text{hidden}_2-c)}\cdot\dfrac{\partial{(C\cdot \text{hidden}_2-c)}}{\partial b}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot \text{hidden}_2-c)}\cdot\dfrac{\partial{(C\cdot \text{hidden}_2-c)}}{\partial \text{hidden}_2}\cdot\dfrac{\partial\text{hidden}_2}{\partial{b}}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial\text{hidden}_2}{\partial{b}}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial{b}}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot\dfrac{\partial(B\cdot\text{hidden}_1-b)}{\partial b}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot-\mathbf{I}_4\bigg)^\top\cdot(\hat{y}-y)\\
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

$\text{hidden2}_i$对应$\text{hidden}_2$向量的第$i$​个元素。从而计算出$E$对$B$的梯度：

$$
\begin{aligned}
\dfrac{\partial E}{\partial b}
&=-\bigg(\big(\hat{y}\circ(1-\hat{y})\big)\cdot\big(\text{hidden}_2\circ(1-\text{hidden}_2)\big)^\top\circ C \bigg)^\top\cdot(\hat{y}-y)\\
&=-\text{hidden}_2\circ(1-\text{hidden}_2)\cdot\big((\hat{y}\circ(1-\hat{y})\big)^\top\circ C^\top\cdot(\hat{y}-y)
\end{aligned}
$$

对于$B$​，易得出：

$$
\begin{aligned}
\dfrac{\partial E}{\partial B}
&=-\dfrac{\partial E}{\partial b}\cdot\text{hidden}_1^\top
\end{aligned}
$$

现在反向传播到最后一层，也就是去求$A$和$a$的偏导：

$$
\begin{aligned}
\dfrac{\partial E}{\partial a}
&=\bigg(\dfrac{\partial \hat{y}}{\partial a}\bigg)^\top\dfrac{\partial E}{\partial\hat{y}}\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot\dfrac{\partial(B\cdot\text{hidden}_1-b)}{\partial a}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot B\cdot\dfrac{\partial f(Ax-a)}{\partial a}\bigg)^\top\cdot(\hat{y}-y)\\
&=\bigg(\dfrac{\partial f(C\cdot \text{hidden}_2-c)}{\partial(C\cdot\text{hidden}_2-c)}\cdot C\cdot\dfrac{\partial f(B\cdot\text{hidden}_1-b)}{\partial(B\cdot\text{hidden}_1-b)}\cdot B\cdot\dfrac{\partial f(Ax-a)}{\partial(Ax-a)}\cdot -\mathbf{I}_5\bigg)^\top\cdot(\hat{y}-y)\\
\dfrac{\partial E}{\partial A}&=-\dfrac{\partial E}{\partial a}\cdot x^\top
\end{aligned}
$$

## <center>规律总结

从上面的步骤中，我们可以总结出神经网络的反向传播的通式：对于一个$l$​​​​​​层神经网络（$l$​​​​​​是权重矩阵个数，比如上面的神经网络是3层），对于第$k(k\leq l)$​​​​​​层权重矩阵$W_k$​​​​​​和第$k$​​​​​​层偏置$b_k$​​​​​​（比如上面$k=3$​​​​​​时，$W_k=C$​​​​​​，$b_k=c$​​​​​​​​），则梯度有：

$$
\begin{aligned}
\dfrac{\partial E}{\partial b_k}&=\begin{cases}
-\bigg[\bigg(\prod_{i=l}^{k+1}\dfrac{\partial f(W_ix_i-b_i)}{\partial(W_ix_i-b_i)}\cdot W_i\bigg)\cdot\dfrac{\partial f(W_k x_k-b_k)}{\partial(W_kx_k-b_k)}\bigg]^\top\cdot(\hat{y}-y)\quad\text{if }k<l;\\
-\bigg(\dfrac{\partial f(W_k x_k-b_k)}{\partial(W_kx_k-b_k)}\bigg)^\top\cdot(\hat{y}-y)\quad\text{if }k=l
\end{cases}\\
\dfrac{\partial E}{\partial M_k}&=-\dfrac{\partial E}{\partial b_k}\cdot x_k^\top
\end{aligned}
$$

这里的$\prod$​​​是矩阵乘法，这里$i$​从$l$​减小到$k+1$​（从后往前计算，反向传播）。$x_i$​​为第$i$层神经元的输入，显然输出就是$f(W_ix_i-b_i)$​。

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
