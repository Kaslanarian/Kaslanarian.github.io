---
layout:     post
title:      泛化误差上界定理
subtitle:   证明与解析
date:       2021-04-24
author:     Welt Xing
header-img: img/prove_header.jpg
---

## 问题描述

我们先来看看什么是泛化误差上界定理：

对于二分类问题，当假设空间是有限个函数的集合$\mathcal{F}=\\{f_1,f_2,...,f_d\\}$时，对于任意一个函数$f\in\mathcal{F}$，至少以概率$1-\delta$，以下不等式成立：

$$R(f)\lt\hat{R}(f)+\varepsilon(d,N,\delta)$$

其中，

$$\varepsilon(d,N,\delta)=\sqrt{\dfrac{1}{2N}\big(\log d+\log\dfrac{1}{\delta}\big)}$$

## 证明

先介绍一个不等式作为引理

$\text{Hoeffding}$不等式：设$\mathop{\sum}\limits_{i=1}^nX_i$为独立随机变量$X1,X_2,...,X_n$的和，$X_i\in[a_i,b_i]$，则有

$$\forall t>0,P(S_n-E[S_n]\ge t)\le\exp\big(\dfrac{-2t^2}{\sum_{i=1}^n(b_i-a_i)^2}\big),\\\quad\quad\;\;\; P(E[S_n]-S_n\ge t)\le\exp\big(\dfrac{-2t^2}{\sum_{i=1}^n(b_i-a_i)^2}\big)$$

对于$N$维空间中的二分类问题，即$X =\mathbb{R}^n,Y\in\{−1, +1\}$. 假设空间是函数的有限集合$\{f_1,f_2,...,f_d\}$，其中$d$是函数个数. 我们选取0-1损失作为损失函数，

关于$f$的期望风险和经验风险分别是

$$
R(f)=E[L(Y,f(X))]\\
\hat{R}(f)=\dfrac{1}{N}\sum_{i=1}^NL(y_i,f(x_i))
$$

显然对于任意函数$f\in\mathcal{F}$，$\hat{R}(f)$是$N$个独立随机变量$L(Y,f(X))$的样本均值，$R(f)$则为其期望. 如果损失函数取值于$[0,1]$，即$\forall i,[a_i,b_i]=[0,1]$. 根据引理，我们有$\forall\varepsilon>0$，下面的不等式成立：

$$P(R(f)-\hat{R}(f)\ge\varepsilon)\le\exp(-2N\varepsilon^2)$$

由于$\mathcal{F}$是一个有限集合，故

$$
\begin{aligned}
P(\exists f\in\mathcal{F}:R(f)-\hat{R}(f)\geqslant\varepsilon)
&=P(\mathop{\cup}\limits_{f\in\mathcal{F}}\{R(f)-\hat{R}(f)\geqslant\varepsilon\})\\
&\leqslant\sum_{f\in\mathcal{F}}P(R(f)-\hat{R}(f)\geqslant\varepsilon)\\
&\leqslant d\exp(-2N\varepsilon^2)
\end{aligned}
$$

等价结论是$\forall f\in\mathcal{F},P(R(f)-\hat{R}(f)\lt\varepsilon)\geqslant1-d\exp(-2N\varepsilon^2)$

令$$\delta=d\exp(-2N\varepsilon^2)$$

则$$P(R(f)\lt\hat{R}(f)+\varepsilon)\geqslant1-\delta$$

即至少$1-\delta$的概率$R(f)\lt\hat{R}(f)+\varepsilon$，

$$\varepsilon=\sqrt{\dfrac{1}{2N}\big(\log d+\log\dfrac{1}{\delta}\big)}$$

## 分析

通过不等式我们发现，训练误差越小，泛化误差越小；样本数越大，泛化误差越小，假设空间越大，其值越大. 当然，以上的讨论只是基于假设空间有限的情况，对一般的假设空间找到泛化误差界则没那么简单.