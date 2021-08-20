---
layout:     post
title:      感知机算法
subtitle:   理论与Python实现
date:       2021-04-25
author:     Welt Xing
header-img: img/venti.png
catalog:    true
tags:
    - 机器学习
---

## 引言

在刚开始阅读《统计学习方法》的感知机部分时，就发现它和支持向量机模型极为相似，因此阅读起来颇为轻松，但两种模型仍存在区别，不能相提并论.

## 感知机模型

### 模型的形式化定义

先来看感知机模型的形式化定义，它就是一个从特征空间$\mathcal{X}\subseteq\mathbb{R}^n$到输入空间$\mathcal{Y}=\\{+1,-1\\}$的一个函数：

$$f(x)=\text{sign}(w\cdot x+b)$$

其中$w,b$为感知机参数，分别叫做权重向量和偏置. $\text{sign}$为符号函数：

$$
\text{sign}(x)=\begin{cases}
+1,x\ge0\\
-1,x\lt0\\
\end{cases}
$$

感知机属于我们之前提到的线性判别模型，它的假设空间是定义在特征空间中的所有分类模型（也叫做线性分类器），即函数集合$\\{f\vert f(x)=w\cdot x+b\\}$。

### 模型的几何解释

线性方程$wx+b=0$对应于特征空间中的一个超平面$S$，其中$w$是超平面的法向量，$b$是超平面的截距。这个超平面将特征空间分为了两个部分。位于两部分的点(即特征向量)分别被分为正、负两类。S也被称之为分离超平面。

![separating htperplane](https://pic3.zhimg.com/80/v2-8d9acfedeb1d3b15f91487fb291d0f6a_1440w.jpg)

## 感知机学习策略

我们先来看一下什么是线性可分，对于给定一个数据集

$$
T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_n,y_n)\}
$$

其中$x_i\in\mathcal{X}\subseteq\mathbb{R}^n,y_i\in\mathcal{Y}=\\{+1,-1\\}$,如果存在一个分离超平面将政府类样本完全分离：

$$y_i(wx_i+b)>0$$

则称样本线性可分. 感知机的任务就是找到这样一个分离超平面.

> 《凸优化》告诉我们，两个不相交的凸集合必有分离超平面，所以一个数据集有分离超平面的充要条件是存在两个不相交的凸集能够分别包含所有的正样本点和负样本点；更进一步，如果所有正样本点构成的凸包和负样本点构成的凸包相交，则一定线性不可分.

接下来我们需要定义一个经验损失函数并将其最小化. 我们当然可以以误分类的样本数作为损失函数，但它既不可导又不连续，遂放弃，改用误分类点到分离超平面的距离：

$$
\dfrac{1}{\Vert w\Vert}\vert wx_0+b\vert
$$

更一般的，误分类点$x_i$到分离超平面的距离为

$$
-\dfrac{1}{\|w\|}y_i(wx_i+b)
$$

设误分类点集合为$M$，从而得到总距离：

$$
-\dfrac{1}{\|w\|}\sum_{x_i\in M}y_i(wx_i+b)
$$

我们将$\frac{1}{\Vert w\Vert}$删去，得到感知机学习的损失函数：

$$
L(w,b)=-\sum_{x_i\in M}y_i(wx_i+b)
$$

## 感知机学习算法

### 算法的原始形式

易证该损失函数为凸，我们尝试用**梯度下降法**去求解. 先获取梯度：

$$
\begin{aligned}
\nabla_wL(w,b)&=-\sum_{x_i\in M}y_ix_i\\
\nabla_bL(w,b)&=-\sum_{x_i\in M}y_i\\
\end{aligned}
$$

从而可以写出算法：

![algorithm](/img/perceptron.png)

直观解释如下：当一个实例点被误分类，就调整参数，使分离超平面向该误分类点的方向移动，减小距离知道越过该点使得可以正确分类.

#### 编程实现

我们尝试用Python代码实现书中的例子：对$((3,3),+1),((4,3),1),((1,1),-1)$计算出对应的感知机.

```python
import numpy as np

train_x = [[3, 3], [4, 3], [1, 1]]
train_y = [[1], [1], [-1]]
eta = 0.5 # 步长

def perceptron(train_x:list, train_y:list, eta:float):
    N = len(train_x)
    n = len(train_x[0])
    w = np.matrix(np.zeros((1, n)))
    b = np.matrix(np.zeros((1, 1)))
    X = np.matrix(train_x)
    Y = np.matrix(train_y)
    while True:
        mistake = False
        for i in range(0, N):
            if Y[i] * (w * X[i].T + b) <= 0:
                w = w + eta * Y[i] * X[i]
                b = b + eta * Y[i]
                mistake = True
                break
        if mistake == False:
            return w, b
```

书中给定数据如下：

```python
train_x = [[3, 3], [4, 3], [1, 1]]
train_y = [[1], [1], [-1]]
```

我们调用函数：

```python
>>> perceptron(train_x, train_y, 0.5)
(matrix([[0.5, 0.5]]), matrix([[-1.5]]))
```

也就是$w=(0.5, 0.5),b=-1.5$，和书中结果相同.

#### 编程改良

我们想观察随着训练次数增加，经验误差的变化趋势，顺便探究和步长的关系，于是加入损失函数模块：

```python
def loss_function(X:list, y:list, w, b):
    X = np.matrix(train_x)
    Y = np.matrix(train_y)
    ret = 0
    for i in range(X.shape[0]):
        loss = y[i] * (w * X[i].T + b)
        if loss < 0:
            ret += loss
    return -ret
```

同时在`perceptron`中加入画图功能：

```python
def perceptron(train_x, train_y, eta):
    N = len(train_x)
    n = len(train_x[0])
    w = np.matrix(np.random.rand(1, n)) # 这里我们将起始点进行随机化
    b = np.matrix(np.random.rand(1, 1))
    X = np.matrix(train_x)
    Y = np.matrix(train_y)
    epoch = 1
    loss = []
    while True:
        mistake = False
        for i in range(0, N):
            if Y[i] * (w * X[i].T + b) <= 0:
                w = w + eta * Y[i] * X[i]
                b = b + eta * Y[i]
                mistake = True
                break
        if mistake == False:
            plt.plot(range(1, epoch), loss)
            return w, b
        epoch += 1
        loss.append(float(loss_function(train_x, train_y, w, b)))
```

我们来看看步长对算法的影响，由于数据量过小，我们将数据集进行扩充：

```python
train_x = [[3, 3], [4, 3], [1, 1], [2, 2], [3, 1], [5, 2]]
train_y = [[1], [1], [-1], [-1], [-1], [1]]
```

然后绘制不同步长时下降次数-损失函数的关系图：

```python
plt.subplot(2, 2, 1)
perceptron(train_x=train_x, train_y=train_y, eta=1)
plt.subplot(2, 2, 2)
perceptron(train_x=train_x, train_y=train_y, eta=0.1)
plt.subplot(2, 2, 3)
perceptron(train_x=train_x, train_y=train_y, eta=0.01)
plt.subplot(2, 2, 4)
perceptron(train_x=train_x, train_y=train_y, eta=0.001)
```

结果如下：

![img](/img/perceptron_algo.png)

<center>左上、右上、左下和右下的步长分别是1,0.1,0.01和0.001</center>

我们显然有下面的结论，步长越小，收敛速度越慢越稳定；此外，收敛速度先快后慢，启示我们对于大量数据可以提前结束以介绍资源消耗.

最后，不同的迭代起始点，会导致不同的收敛结果，原因是该问题有多个最优解.

### 算法收敛性

下面我们将从理论上去证明上面提到的收敛性. 为了方便，我们将两个参数进行融合：

$$
w\cdot x+b=\begin{bmatrix}
w&b
\end{bmatrix}\begin{bmatrix}
x&1
\end{bmatrix}^\top=\hat{w}\cdot\hat{x}
$$

我们有$\text{Novikoff}$定理：对于我们的感知机问题，我们有

1. 存在满足条件$\Vert\hat w_\text{opt}\Vert=0$的超平面
   $$
   \Vert\hat{w}_{\text{opt}}\Vert\cdot\hat{x}=w_{\text{opt}}+b_{\text{opt}}=0
   $$将数据集完全正确分开；且存在$\gamma>0$，对所有$i=1,2,...,N,y_i(\hat{w}_{\text{opt}}\cdot\hat{x}_i)\geqslant\gamma$.
2. 令$R=\mathop{\max}\limits_{1\leqslant i\leqslant N}\Vert\hat{x}_i\Vert$，则感知机算法在训练数据集上的误分类次数$k$满足

$$
k\leqslant(\dfrac{R}{\gamma})^2
$$

定理表明，误分类的次数$k$是有上界的，算法确实是收敛的，但我们之前提到，收敛后的解有许多解，为了得到唯一的解，我们需要增加约束条件，这就引出我们的**支持向量机**；此外，当数据集线性不可分时，则会发生震荡.

### 算法的对偶形式

我们来看看前面我们进行梯度下降时的策略

$$
\begin{aligned}
w&\gets w+\eta y_ix_i\\
b&\gets b+\eta y_i
\end{aligned}
$$

加入我们把初始态全部设置为0，就会发现$w,b$都可以表示为实例$x_i$和$y_i$的线性组合，这就是对偶形式的基本思想. 学习到最后，两参数分别表示为

$$
\begin{aligned}
w&=\sum_{i=1}^N\alpha_iy_ix_i\\
w&=\sum_{i=1}^N\alpha_iy_i\\
\alpha&\geqslant0
\end{aligned}
$$

当$\eta=1$，$\alpha_i$就是实例点$x_i$的更新次数，越大说明更新次数越多，意味着它距离分离超平面越近，也就越难正确分类. 换句话说，这样的实例对学习效果影响最大.

感知机算法的对偶形式：我们将感知机模型转换为

$$
f(x)=\text{sign}\bigg(\sum_{j=1}^N\alpha_jy_jx_j\cdot x+b \bigg)
$$

其中$\alpha=(\alpha_1,\alpha_2,...,\alpha_N)^\top$，我们的对偶算法如下：

![duality](/img/duality_perception.png)

由于我们要多次使用内积运算，所以可以预先将内积算出来储存在一个矩阵中，也就是$\text{Gram}$矩阵：

$$
\boldsymbol{}{G}=[x_i\cdot x_j]_{N\times N}
$$

2.25 相关Python代码没有实现，先挖个坑.<br>
2.27 基础算法和对偶算法都已经实现：<https://github.com/Kaslanarian/MSLCode/blob/main/perceptron.py>，支持特征为2时的图形表示，但由于没有设置$\text{Novikoff}$定理中提到的上界，所以无法应对线性不可分的情况.

## 相关

[线性支持向量机的推导](https://welts.xyz/2021/04/12/svm/)<br>
[Numpy的计算和维数问题](https://welts.xyz/2021/04/26/numpy_dim/)
