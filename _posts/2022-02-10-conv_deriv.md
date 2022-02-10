---
layout:     post
title:      卷积神经网络的反向传播
subtitle:   卷积与池化的求导推导
date:       2022-02-10
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 卷积神经网络
---

前篇：<https://welts.xyz/2021/08/22/cnn/>，<https://welts.xyz/2021/08/22/code_cnn/>.

我们在前面对卷积神经网络进行了综述，同时对卷积和池化进行探究。我们列举了几种卷积核，当它们作用于图片时，会有不同的效果。但在真正的CNN中，卷积核(或者说卷积核的参数)和全连接层的偏置与权重一样，都是在不断变化的。也就是说，卷积层与池化层也在反向传播中。本文便是从零探索卷积层和池化层的求导，再到反向传播。

## 从一维情况开始

前面提到，图片是一个“三维结构”：图片长、图片宽和通道数。我们将其简化成一维的数据，也就是宽度，通道数均为1的数据，其实就是常见的表格式数据。

### 卷积

我们只令步长stride为1，无padding。对于下面的数据

$$
\pmb x=\begin{bmatrix}
x_1&x_2&\cdots&x_n
\end{bmatrix}
$$

采用长度为$k$的卷积核($k<n$):

$$
\pmb a=\begin{bmatrix}
a_1&\cdots&a_k
\end{bmatrix}
$$

这样输出的尺寸

$$
o=n-k+1
$$

设输出向量为$\pmb y$，所以有

$$
y_i=\sum_{j=1}^k x_{i+j-1} a_j
$$

现在就是求$\pmb y$对卷积核$\pmb a$的导数:

$$
\begin{aligned}
\dfrac{\mathrm d\pmb y}{\mathrm d\pmb a}
&=\bigg[\dfrac{\mathrm dy_i}{\mathrm da_j}\bigg]_{ij}\\
&=\big[x_{i+j-1}\big]_{ij}\\
\end{aligned}
$$

显然形成的是一个$o\times k$的矩阵，也就是雅各比矩阵。比如我们的数据长度为6，卷积核长度为3，那么求导结果是$4\times3$矩阵:

$$
\begin{bmatrix}
x_1&x_2&x_3\\
x_2&x_3&x_4\\
x_3&x_4&x_5\\
x_4&x_5&x_6\\
\end{bmatrix}
$$

### 池化

池化分为平均池化和最大池化，其中最大池化最常用，且效果更好。为了方便处理，我们设池化核长度能够被数据长度整除，先考虑平均池化。对于数据

$$
\pmb x=\begin{bmatrix}
x_1&x_2&\cdots&x_{nk}
\end{bmatrix}
$$

设池化核长度为$k$，那么输出$\pmb y$的长度为$n$:

$$
\pmb y=\begin{bmatrix}
\frac1k\sum_{i=1}^k x_i&\frac1k\sum_{i=k+1}^{2k}x_i&\cdots&\frac1k\sum_{i=(n-1)k+1}^{nk}x_i
\end{bmatrix}
$$

求导，生成的是$n\times nk$的雅各比矩阵$J$。其中

$$
J_{i,(i-1)k+1:ik}=1
$$

也就是第$i$行的第$(i-1)k$到第$ik$列为$\frac1k$，其余元素为0。比如数据长度为6，池化核长度为2，那么

$$
\pmb y=\begin{bmatrix}
\frac12(x_1+x_2)&\frac12(x_3+x_4)&\frac12(x_5+x_6)
\end{bmatrix}
$$

从而求导结果

$$
\dfrac{\partial\pmb{y}}{\partial\pmb{x}}=\frac12\begin{bmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1\\
\end{bmatrix}
$$

上面是平均池化的结果，现在考虑最大池化，还是保持数据长度为$nk$，池化核长度为$k$，那么最大池化的结果为

$$
\pmb{y}=\begin{bmatrix}
\max_{i=1,\cdots,k} x_i&\max_{i=k+1,\cdots,2k}x_i&\cdots&\max_{(n-1)k+1,\cdots,nk}x_i
\end{bmatrix}
$$

因此进行求导后，生成的是$n\times nk$的雅各比矩阵$J$。其中每一行都有且仅有一个元素为1，其余为0。1所在的位置与子向量的最大值所在位置相关。比如数据长度为6，池化核长度为2，我们设数据为

$$
\pmb x=\begin{bmatrix}
5&4&8&10&3&1
\end{bmatrix}
$$

那么输出为

$$
\pmb y=\begin{bmatrix}
5&10&3
\end{bmatrix}
$$

因此求导结果为

$$
\dfrac{\partial\pmb{y}}{\partial\pmb{x}}=\begin{bmatrix}
1&0&0&0&0&0\\
0&0&0&1&0&0\\
0&0&0&0&1&0\\
\end{bmatrix}
$$

### 举例

考虑一个卷积+ReLU激活+池化的“网络“，但我们在池化输出后就停止，而不是通过全连接网络。我们设置输入数为**5**，卷积核尺寸为2，池化核尺寸也为2，采取最大池化，这样输出数为2。输入

$$
\pmb x=\begin{bmatrix}
1&4&0&2&7
\end{bmatrix}
$$

卷积核为

$$
\pmb a=[-1\quad1]
$$

那么数据通过卷积核作用后，输出为

$$
\pmb o_1=\begin{bmatrix}
3&-4&2&5
\end{bmatrix}
$$

通过ReLU层

$$
\pmb o_2=\begin{bmatrix}
3&0&2&5
\end{bmatrix}
$$

再通过池化层:

$$
\pmb o_3=[3\quad5]
$$

前向传播完成，现在考虑反向传播。先是$\pmb o_3$对$\pmb o_2$求导，参照我们前面的分析，有

$$
\dfrac{\partial\pmb o_3}{\partial\pmb o_2}=\begin{bmatrix}
1&0&0&0\\
0&0&0&1\\
\end{bmatrix}
$$

再考虑$\pmb o_2$对$\pmb o_1$求导，也就是ReLU层的求导

$$
\dfrac{\partial\pmb o_2}{\partial\pmb o_1}=\begin{bmatrix}
1&0&0&0\\
0&0&0&0\\
0&0&1&0\\
0&0&0&1\\
\end{bmatrix}
$$

最后考虑$\pmb o_1$对卷积核参数求导，还是参照前面的分析，有

$$
\dfrac{\partial\pmb o_1}{\partial\pmb a}=\begin{bmatrix}
1&4\\
4&0\\
0&2\\
2&7\\
\end{bmatrix}
$$

因此对最后的输出对卷积核参数的导数:

$$
\begin{aligned}
\dfrac{\partial\pmb o_3}{\partial\pmb{a}}&=\dfrac{\partial\pmb o_3}{\partial\pmb o_2}\dfrac{\partial\pmb o_2}{\partial\pmb o_1}\dfrac{\partial\pmb o_1}{\partial\pmb{a}}\\
&=\begin{bmatrix}
1&0&0&0\\
0&0&0&1\\
\end{bmatrix}\begin{bmatrix}
1&0&0&0\\
0&0&0&0\\
0&0&1&0\\
0&0&0&1\\
\end{bmatrix}\begin{bmatrix}
1&4\\
4&0\\
0&2\\
2&7\\
\end{bmatrix}\\
&=\begin{bmatrix}
1&4\\
2&7
\end{bmatrix}
\end{aligned}
$$

## 二维情况

### 卷积

考虑我们的数据是二维的，也就是矩阵类型数据:

$$
\pmb X=\begin{bmatrix}
x_{11}&\cdots&x_{1n}\\
\vdots&\ddots&\vdots\\
x_{n1}&\cdots&x_{nn}
\end{bmatrix}
$$

同样，卷积核也是方形的

$$
\pmb A=\begin{bmatrix}
a_{11}&\cdots&a_{1k}\\
\vdots&\ddots&\vdots\\
a_{k1}&\cdots&a_{kk}
\end{bmatrix}
$$

所以输出是$(n-k+1)\times(n-k+1)$的矩阵$\pmb Y$，对应元素满足

$$
Y_{ij}=\sum_{m=1}^k\sum_{n=1}^k x_{i+m-1,j+n-1}a_{m,n}
$$

我们现在想求卷积结果对卷积核参数的导数，也就是矩阵对矩阵的导数，形成的是一个4维张量，其中

$$
\dfrac{\partial\pmb Y_{ij}}{\partial\pmb A_{mn}}=\begin{cases}
x_{i+m-1,j+n-1}&\text{if } \\
0&\text{otherwise}
\end{cases}
$$

举个例子，假如我们的数据是$4\times4$矩阵，卷积核为$3\times3$，从而输出为$2\times 2$矩阵

$$
\pmb Y=\begin{bmatrix}
\sum_{i=1}^3\sum_{j=1}^3x_{ij}a_{ij}&\sum_{i=1}^3\sum_{j=1}^3x_{i,j+1}a_{ij}\\
\sum_{i=1}^3\sum_{j=1}^3x_{i+1,j}a_{ij}&\sum_{i=1}^3\sum_{j=1}^3x_{i+1,j+1}a_{ij}\\
\end{bmatrix}
$$

那么

$$
\dfrac{\partial\pmb Y_{11}}{\partial\pmb A}=\begin{bmatrix}
x_{11}&x_{12}&x_{13}\\
x_{21}&x_{22}&x_{23}\\
x_{31}&x_{32}&x_{33}\\
\end{bmatrix},
\dfrac{\partial\pmb Y_{12}}{\partial\pmb A}=\begin{bmatrix}
x_{12}&x_{13}&x_{14}\\
x_{22}&x_{23}&x_{24}\\
x_{32}&x_{33}&x_{34}\\
\end{bmatrix},\\
\dfrac{\partial\pmb Y_{21}}{\partial\pmb A}=\begin{bmatrix}
x_{21}&x_{22}&x_{23}\\
x_{31}&x_{32}&x_{33}\\
x_{41}&x_{42}&x_{43}\\
\end{bmatrix},
\dfrac{\partial\pmb Y_{22}}{\partial\pmb A}=\begin{bmatrix}
x_{22}&x_{23}&x_{24}\\
x_{32}&x_{33}&x_{34}\\
x_{42}&x_{43}&x_{44}\\
\end{bmatrix}.
$$

因此

$$
\dfrac{\partial\pmb Y}{\partial\pmb A}=\begin{bmatrix}
\dfrac{\partial\pmb Y_{11}}{\partial\pmb A}&\dfrac{\partial\pmb Y_{12}}{\partial\pmb A}\\
\dfrac{\partial\pmb Y_{21}}{\partial\pmb A}&\dfrac{\partial\pmb Y_{22}}{\partial\pmb A}
\end{bmatrix}
$$

### 池化

类似于与二维卷积，二维池化求导也是一个4维张量。还是以$4\times4$数据为例，我们采用$2\times2$池化。若是平均池化，则结果为

$$
\begin{bmatrix}
\frac14\sum_{i=1}^2\sum_{i=1}^2x_{ij}&\frac14\sum_{i=1}^2\sum_{i=1}^2x_{i,j+2}\\
\frac14\sum_{i=1}^2\sum_{i=1}^2x_{i+2,j}&\frac14\sum_{i=1}^2\sum_{i=1}^2x_{i+2,j+2}\\
\end{bmatrix}
$$

那么输出对输入的导数

$$
\dfrac{\partial\pmb Y_{11}}{\partial\pmb X}=\begin{bmatrix}
\frac14&\frac14&0&0\\
\frac14&\frac14&0&0\\
0&0&0&0\\
0&0&0&0\\
\end{bmatrix},\dfrac{\partial\pmb Y_{12}}{\partial\pmb X}=\begin{bmatrix}
0&0&\frac14&\frac14\\
0&0&\frac14&\frac14\\
0&0&0&0\\
0&0&0&0\\
\end{bmatrix},\\\dfrac{\partial\pmb Y_{21}}{\partial\pmb X}=\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
\frac14&\frac14&0&0\\
\frac14&\frac14&0&0\\
\end{bmatrix},\dfrac{\partial\pmb Y_{22}}{\partial\pmb X}=\begin{bmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&\frac14&\frac14\\
0&0&\frac14&\frac14\\
\end{bmatrix}.
$$

也就是

$$
\dfrac{\partial\pmb Y}{\partial\pmb X}=\begin{bmatrix}
\dfrac{\partial\pmb Y_{11}}{\partial\pmb X}&\dfrac{\partial\pmb Y_{12}}{\partial\pmb X}\\
\dfrac{\partial\pmb Y_{21}}{\partial\pmb X}&\dfrac{\partial\pmb Y_{22}}{\partial\pmb X}
\end{bmatrix}
$$

## 总结

我们这里简单地对卷积池化尤其是一维的情况进行了推导，方法还是数学推导那一套。我们在后面会尝试用这里推导的结果进行实践。
