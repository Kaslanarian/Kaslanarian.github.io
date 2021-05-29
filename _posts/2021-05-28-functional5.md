---
layout:     post
title:      泛函分析论
subtitle:   线性算子的谱
date:       2021-05-28
author:     Welt Xing
header-img: img/functional.png
catalog:    true
tags:
    - 数学
---

## <center>引言

这一部分是将矩阵特征值进行衍生，因此理解起来会简单一点（但还是很难！）。

## <center>谱的概念

考察$n$个未知数的线性方程组：

$$
\begin{cases}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=y_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=y_2\\
\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\\
a_{n1}x_1+a_{n2}x_2+\cdots+a_{nn}x_n=y_n\\
\end{cases}
$$

根据我们在线性代数中学到的，上式简化成

$$
Ax=y
$$

在这里，我们将其解释成$n$维空间$E^n$上的线性算子$A$满足$Ax=y$. 对复数$\lambda$，若存在$x\neq0$，使得$Ax=\lambda x$，则称$\lambda$为$A$的特征值。它意味着$(A-\lambda I)x=0$有非零解，即**算子$(A-\lambda I)$不存在逆算子**。因此特征值问题和$(A-\lambda I)$是否有逆算子等价。

**定义1**：设$X$是赋范线性空间，$T\in\mathscr{B}(X)$，若$T^{-1}$存在且定义在整个$X$上的有界线性算子，则称$T$是$X$上的**正则算子**。

正则算子性质：

1. $T$是正则算子$\leftrightarrow r\exists$有界算子$B\in\mathscr{B}(X):BT=TB=I$，其中$I$是恒等算子；
2. $A,B$都是正则算子$\to T=AB$也是正则算子，且$(AB)^{-1}=B^{-1}A^{-1}$.

**定义2**：设$T\in\mathscr{B},\lambda\in\mathbb{C}$. 若$(T-\lambda I)$正则，我们称$\lambda$是算子$T$的**正则点**，$T$的正则点全体称作$T$的正则集，或者是豫解集，记为$\rho(T)$，不是正则点的复数称作$T$的**谱点**，其全体构成$T$的**谱**，记为$\sigma(T)$.

**定义3**（谱的分类）：设$\lambda\in\sigma(T)$，即$T-\lambda I$不存在有界逆算子，可分三种情况：

1. 如果$T-\lambda I$不是一对一，此时存在$x\in X,x\neq0$，使得$(T-\lambda I)x=0$，即$Tx=\lambda x$，则称$\lambda$是算子T的特征值，$x$称为响应于$\lambda$的特征向量，$T$的特征值全体称为$T$的点谱，记作$\sigma(T)$;
2. $(T-\lambda I)$是一对一的，但是值域不填满全空间；
3. $(T-\lambda I)$是一对一的，但$(T-\lambda I)^{-1}$不是有界的.

其中(2),(3)类谱点合称$T$的**连续谱**，记为$\sigma_C(T)$.
