---
layout:     post
title:      LIBLINEAR中的多分类
subtitle:   Crammer-Singer方法
date:       2022-02-03
author:     Welt Xing
header-img: img/background.jpg
catalog:    true
tags:
    - LIBLINEAR
---

## 引入

SVM在最开始是二分类器，因此如何将其扩展到多分类问题是很重要的。较为简单和常用的方法是“一对一”和“一对多”方法，这也是很多机器学习的初学者最早接触到的方法。在刘志刚等人的《支持向量机在多类分类问题中的推广》对多分类方法进行了总结，文中指出，多分类SVM大致分为两类:

1. 通过某种方式构造**一系列的两类分类器**并将它们组合在一起来实现多类分类；
2. 将多个分类面的参数求解合并到**一个最优化问题**中， 通过求解该最优化问题“一次性”地实现多类分类。

前面提到的“一对一”和“一对多”显然都属于第一类。除此以外，第一类多分类器还包括有向无环图SVMs、纠错编码SVMs和层次SVMs等。

作为当前流行的软件包之一，LIBSVM采用的是一对多的多分类方案；而LIBLINEAR采用的是Crammer-Singer多分类方案，该方案属于第二种，但我们知之甚少。sklearn中的SVM模块的底层实现是LIBSVM和LIBLINEAR，其中`LinearSVC`是由LBLINEAR实现，`SVC`和`NuSVC`是由LIBSVM实现。用户可通过`LinearSVC`的`multi_class`参数指定多分类方案，其文档如下:

```python
"""
...
multi_class : {'ovr', 'crammer_singer'}, default='ovr'
    Determines the multi-class strategy if `y` contains more than
    two classes.
    ``"ovr"`` trains n_classes one-vs-rest classifiers, while
    ``"crammer_singer"`` optimizes a joint objective over all classes.
    While `crammer_singer` is interesting from a theoretical perspective
    as it is consistent, it is seldom used in practice as it rarely leads
    to better accuracy and is more expensive to compute.
    If ``"crammer_singer"`` is chosen, the options loss, penalty and dual
    will be ignored.
...
"""
```

也就是说`LinearSVC`可以选择“一对多”方案或Crammer-Singer方案，但在`SVC`中，多分类方案只有“一对一”和“一对多”(参考`sklearn.svm.SVC`中的`decision_function_shape`参数)。

## 多分类优化问题

本文的目的是借助LIBLINEAR的文档，对其内部的多分类机制，也就是Crammer-Singer方法进行学习，拓展对线性SVM多分类方法的认识。对于带标签数据集$\\{(\pmb x_i,y_i)\\}_{i=1}^l$，其中$\pmb x_i\in\mathbb{R}^n$，$y_i\in\\{1,\cdots,k\\}$，也就是一共$k$类。 Crammer和Singer提出下面的优化问题来进行多分类

$$
\begin{aligned}
\min_{\{\pmb w_m\},\pmb\xi}\quad&\frac12\sum_{m=1}^k\Vert{\pmb w}_m\Vert^2+C\sum_{i=1}^l\xi_i\\
\text{s.t.}\quad&\pmb w_{y_i}^T\pmb x_i-\pmb w_m^T\pmb x_i\geq e_i^m-\xi_i,\forall m,i
\end{aligned}\tag1
$$

$C$是正则化参数，而$\pmb w_m$是第$m$类对应的权重向量，其中

$$
e_i^m=\begin{cases}
0&\text{if }y_i=m;\\
1&\text{if }y_i\neq m.
\end{cases}
$$

多分类问题的决策函数为

$$
\mathop{\arg\max}\limits_{m=1,\cdots,k}\quad\pmb w_m^T\pmb x
$$

我们来看一下优化问题(1)，这是加入松弛变量后的形式，如果我们将松弛项$\xi_i$忽略，那么问题变成

$$
\begin{aligned}
\min_{\{\pmb w_m\},\pmb\xi}\quad&\frac12\sum_{m=1}^k\Vert{\pmb w}_m\Vert^2\\
\text{s.t.}\quad&\pmb w_{y_i}^T\pmb x_i-\pmb w_m^T\pmb x_i\geq e_i^m,\forall m,i
\end{aligned}\tag2
$$

目标函数看起来是要同时训练$k$个SVM(参考二分类SVM的原问题)，再看约束条件，针对第$i$条数据，当$y_i=m$，那么约束显然成立，如果不相等，约束则是

$$
\pmb w_{y_i}^T\pmb x_i-\pmb w_{m}^T\pmb x_i\geq1,\forall m\neq y_i 
$$

考虑空间几何，显然约束是让样本点$\pmb x_i$离$y_i$类对应的超平面越远，对应就是分类效果越好；如果联系决策函数，那么约束是想让$\pmb x_i$在正确类上的分数尽可能高。

问题(1)的对偶形式为

$$
\begin{aligned}
\min_{\pmb\alpha}\quad&f(\pmb\alpha)=\frac12\sum_{m=1}^k\Vert\pmb w_{m}\Vert^2+\sum_{i=1}^l\sum_{m=1}^ke_i^m\alpha_i^m\\
\text{s.t.}\quad&\sum_{m=1}^k\alpha_i^m=0,i=1,\cdots,l\\
&\alpha_i^m\leq C_{y_i}^m,i=1,\cdots,l,m=1,\cdots,k
\end{aligned}\tag{3}
$$

其中

$$
\pmb w_m=\sum_{i=1}^l\alpha_i^m\pmb x_i,\forall m,\quad\pmb\alpha=[\alpha_1^1,\cdots,\alpha_1^k,\cdots,\alpha_l^1,\cdots,\alpha_l^k]^T,C_{y_i}^m=\begin{cases}
0&\text{if }y_i\neq m,\\
C&\text{if }y_i=m.
\end{cases}
$$

可以将$\pmb w_{m}$视作$\pmb\alpha$的函数，也就是$\pmb w_m(\pmb\alpha)$。$\pmb\alpha$是长度为$kl$的向量，我们将其分块成$[\bar{\pmb\alpha}_1,\cdots,\bar{\pmb\alpha}_l]$其中

$$
\bar{\pmb\alpha}_i=[\alpha_i^1,\cdots,\alpha_i^k]^T,i=1,\cdots,l
$$

## 坐标下降求解

在LIBLINEAR中，对偶问题(3)的解决是依赖于坐标下降方法实现，这种特定的坐标下降被称作序列对偶方法(Sequential Dual Method, SDM)。那么下面的部分我们来介绍该算法相关。

先来看$f$的梯度

$$
g_{i}^m=\dfrac{\partial f(\pmb\alpha)}{\partial\alpha_i^m}=\pmb w_m(\pmb\alpha)^T\pmb x_i+e_i^m,\forall i,m
$$

和一般的坐标下降方法类似，SDM方法每次选取一个$i$，固定$\bar{\pmb\alpha}_i$以外的所有变量，然后求解子问题:

$$
\begin{aligned}
\min_{\bar{\pmb\alpha}_i}\quad&\sum_{m=1}^k\frac12A(\alpha_i^m)^2+B_m\alpha_i^m\\
\text{s.t.}\quad&\sum_{m=1}^k\alpha_i^m=0,\\
&\alpha_i^m\leq C_{y_i}^m,m=\{1,\cdots,k\}
\end{aligned}\tag{4}
$$

其中

$$
A=\pmb x_i^T\pmb x_i,\quad B_m=\pmb w_m^T\pmb x_i+e_i^m-A\alpha_i^m
$$

这个问题仍然很复杂，这是由于对偶问题本身的复杂度导致的。在LIBLINEAR中，会定期对问题规模进行收缩(Shrink)，对于到边界的变量，也就是$\alpha_i^m=C_{y_i}^m$，我们不会将其考虑进来，设剩下的元素构成的子向量$\bar{\pmb\alpha}_i^{U_i}$，其中变量子集$U_i\subset\\{1,\cdots,k\\}$是我们需要考虑的变量。因此子问题(4)的问题规模缩小:

$$
\begin{aligned}
\min_{\bar{\pmb\alpha}_i}\quad&\sum_{m\in U_i}\frac12A(\alpha_i^m)^2+B_m\alpha_i^m\\
\text{s.t.}\quad&\sum_{m\in U_i}^k\alpha_i^m=-\sum_{m\notin U_i}\alpha_i^m,\\
&\alpha_i^m\leq C_{y_i}^m,m\in U_i
\end{aligned}\tag{5}
$$

在两种情况下，我们不需要求解问题(5):

1. $\vert U_i\vert<2$，此时线性约束会让变量无法移动；
2. $A=0$，也就是$\pmb x_i=0$，此时$\alpha_i^m$不会对$\pmb w_m$造成影响。

假设求解前的变量值为$\hat{\alpha}_i^m$，更新后的变量值为$\alpha_i^m$，那么我对$\pmb w_m$进行更新

$$
\pmb w_m\gets\pmb w_m+(\alpha_i^m-\hat{\alpha}_i^m)y_i\pmb x_i
$$

算法框架如下：

<img src="/img/image-20220203191114542.png" alt="image-20220203191114542" style="zoom:67%;" />

在算法的内部循环中，我们采用随机排列的方式选择$i$，这是一种能加速收敛的启发式方法。剩下的问题就是子问题(5)的求解。

问题(5)是经典的凸优化问题，这意味着它的最优性要满足KKT条件，也就是存在$\beta,\rho_m,m\in U_i$使得

$$
\begin{cases}
\sum_{m\in U_i}^k\alpha_i^m=-\sum_{m\notin U_i}\alpha_i^m,&等式约束\\
\alpha_i^m\leq C_{y_i}^m,m\in U_i,&不等式约束\\
\rho_m\geq0,m\in U_i&不等式乘子约束\\
\rho_m(C_{y_i}^m-\alpha_i^m)=0,m\in U_i,&对偶互补条件\\
A\alpha_i^m+B_m-\beta=-\rho_m,m\in U_i.&梯度约束
\end{cases}
$$

通过不等式约束，后三个约束条件等价于

$$
\begin{aligned}
A\alpha_i^m+B_m-\beta&=0,\text{if }\alpha_i^m<C_{y_i}^m,m\in U_i\\
A\alpha_i^m+B_m-\beta&=AC_{y_i}^m+B_m-\beta\leq 0,\text{if }\alpha_i^m=C_{y_i}^m,m\in U_i
\end{aligned}\tag6
$$

因此KKT条件等价于等式约束+不等式约束+(6)。定义

$$
D_m=B_m+AC_{y_i}^m,m=1,\cdots,k
$$

如果$\beta$已知，$\alpha_i^m$的闭式解

$$
\alpha_i^m\equiv\min(C_{y_i}^m,\frac{\beta-B_m}{A})
$$

满足处理等式约束以外的所有KKT条件，因此下面我们要找到满足等式约束的$\beta$。我们有

$$
\sum_{m:m\in U_i\text{ and }\alpha_i^m<C_{y_i}^m}(\beta-B_m)=-(\sum_{m:m\notin U_i}AC_{y_i}^m+\sum_{m:m\in U_i\text{ and }\alpha_i^m=C_{y_i}^m}AC_{y_i}^m)
$$

从而

$$
\begin{aligned}
\sum_{m:m\in U_i\text{ and }\alpha_i^m<C_{y_i}^m}\beta&=\sum_{m:m\in U_i\text{ and }\alpha_i^m=C_{y_i}^m}D_m-\sum_{m=1}^kAC_{y_i}^m\\
&=\sum_{m:m\in U_i\text{ and }\alpha_i^m=C_{y_i}^m}D_m-AC
\end{aligned}
$$

因此

$$
\beta=\dfrac{\sum_{m\in U_i,\alpha_i^m<C_{y_i}^m}D_m-AC}{\vert\{m\vert m\in U_i,\alpha_i^m<C_{y_i}^m\}\vert}
$$

令$\Phi=\emptyset$，然后按$D_m$递减的顺序将序列数$m$加入到$\Phi$中，其中$m=1,\cdots,k,m\neq y_i$，直到

$$
h=\dfrac{\sum_{m\in\Phi}D_m-AC}{\vert\Phi\vert}\geq\max_{m\notin\Phi}D_m
$$

此时令$\beta=h$。下面是求解子问题算法的详细过程:

<img src="/img/image-20220203191137049.png" alt="image-20220203191137049" style="zoom:67%;" />

可以证明上面的操作能够使得

$$
\Phi=\{m\vert m\in U_i,\alpha_i^m<C_{y_i}^m\}
$$

这里省略证明步骤。
