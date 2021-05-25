---
layout:     post
title:      泛函分析论
subtitle:   内积空间和希尔伯特空间
date:       2021-05-25
author:     Welt Xing
header-img: img/functional.png
catalog:    true
tags:
---

## <center>引言

我们之前介绍了赋范线性空间，那里只有长度（范数），但没有角度，因此也就没有内积，正交的概念了。本章就是来解决在赋范线性空间中引入角度和正交等概念。事实上希尔伯特在20世纪初便解决了这个问题，这种空间是希尔伯特空间的特例，称作希尔伯特空间。

## <center>内积空间的基本概念

在复欧式空间，我们定义了两个向量的内积运算：

$$
a=(\xi_1,\xi_2,\cdots,\xi_n),b=(\eta_1,\eta_2,\cdots,\eta_n)
$$

则$a,b$内积定义为

$$
\big<a,b\big>=\sum_{i=1}^n\xi_i\bar{\eta}_i
$$

其中$\bar{\eta}_i$是$\eta_i$的复共轭。并且内积和长度有以下关系：

$$
\|a\|=\sqrt{\big<a,a\big>}
$$

内积定义告诉我们$a$正交于$b\leftrightarrow\big<a,b\big>=0$，由此在有限维复欧式空间$\mathbb{E}^n$中，内积有以下性质：

1. $\big<a,a\big>\geqslant0,\big<a,a\big>=0\leftrightarrow a=0$;
2. $\big<\alpha a+\beta b,c\big>=\alpha\big<a,c\big>+\beta\big<b,c\big>,a,b,c\in\mathbb{E}^n,\alpha,\beta\in\mathbb{C}$;
3. $\big<a,b\big>=\overline{\big<a,b\big>},a,b\in\mathbb{E}^n$.

注意上面是**复欧式空间**中的内积，我们在一般的线性空间引入内积概念：

**定义**：$X$是复线性空间，如果对$X$中任意2个向量$x,y$，友谊复数$\big<x,y\big>$与之对应并满足：

1. $\big<x,x\big>\geqslant0,\big<x,x\big>=0\leftrightarrow x=0,x\in X$;
2. $\big<\alpha x+\beta y,z\big>=\alpha\big<x,z\big>+\beta\big<y,z\big>,x,y,z\in X,\alpha,\beta\in\mathbb{C}$;
3. $\big<a,b\big>=\overline{\big<b,a\big>}a,b\in X$.

如果是$X$是式线性空间，那么3的共轭号没有意义；从内积的定义，我们有下面的等式：

$$
\big<x,\alpha y+\beta z\big>=\overline{\alpha}\big<x,y\big>+\overline{\beta}\big<x,z\big>
$$

设$X$是内积空间，令

$$
\|x\|=\sqrt{\big<x,x\big>}\tag{*}
$$

那么$\|\cdot\|$是$X$上的范数，因为不难证明$①\|x\|\geqslant0,\Vert x\Vert=0\leftrightarrow x=0;②\Vert ax\Vert=\vert a\vert\Vert x\Vert$.

接着需要证明三点不等式$\Vert x+y\Vert\leqslant\Vert x\Vert+\Vert y\Vert$，需要用到施瓦茨不等式作为引理：

**引理**（施瓦茨不等式）：设$X$按内积$\big<x,y\big>$成为内积空间，则$\forall x,y\in X$，有

$$
|\big<x,y\big>|\leqslant\|x\|\cdot\|y\|
$$

由施瓦茨不等式：

$$
\begin{aligned}
\|x+y\|^2&=\big<x+y,x+y\big>\\
&=\big<x,x\big>+\big<x,y\big>+\big<y,x\big>+\big<y,y\big>\\
&=\|x\|^2+\|y\|^2+\big<x,y\big>+\big<y,x\big>\\
&\leqslant\|x\|^2+\|y\|^2+2\|x\|\cdot\|y\|\\
&=(\|x\|+\|y\|)^2
\end{aligned}
$$

因此有三点不等式成立，此时称范数$\Vert\cdot\Vert$为由内积导出的范数，所以**内积空间是特殊的赋范线性空间**，若$X$按照*式中范数完备，则称为**希尔伯特空间**.

平行四边形公式（不难证明）：

$$
\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2)
$$

## 内积空间的例子

- $L^2[a,b]$，对其中任意向量$x,y$有
  
  $$
    \big<x,y\big>=\int_a^bx(t)\overline{y(t)}\mathrm{d}t
  $$

  因此由内积导出的范数

  $$
    \|x\|={\bigg(\int_a^b\vert x(t)\vert^2\mathrm{d}t\bigg)}^\frac{1}{2}
  $$

  这个就是$P$方可积函数$p=2$时的范数，因此推出$L^2[a,b]$就是希尔伯特空间.

- $l^2$是希尔伯特空间，$p\neq2$时$l^p$不成为希尔伯特空间.

极化恒等式：

$$
\big<x,y\big>=\dfrac{1}{4}\bigg(\|x+y\|^2-\|x-y\|^2+i\|x+iy\|^2-i\|x-iy\|^2 \bigg)
$$

它表示内积可以用它导出的范数来表示，当$X$是实内积空间，恒等式简化为

$$
\big<x,y\big>=\dfrac{1}{4}\bigg(\|x+y\|^2-\|x-y\|^2\bigg)
$$

由施瓦茨不等式，立刻发现内积其实是双变量的连续函数，即$x_n\to x,y_n\to y$时$\big<x_n,y_n\big>\to\big<x,y\big>(n\to\infty)$.

## <center>投影定理

设$X$是度量空间，$M$是$X$中的非空子集，$x\in X$，称

$$
\inf_{y\in M}d(x,y)
$$

为点到集合的距离，记为$d(x,M)$，在赋范线性空间中

$$
d(x,M)=\inf_{y\in M}\|x-y\|
$$

**定理1**（极小化向量定理）：$X$是内积空间，$M$是$X$中非空凸集，