---
layout:     post
title:      集中不等式(2)
subtitle:   Concentration
date:       2021-11-17
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 概率论
---

## 矩生成函数

对于随机变量$X$，我们设

$$
M_X(t)=\mathbb{E}(e^{tX})
$$

称$M_X(t)$为$X$的矩生成函数。矩生成函数有这样的性质：

$$
\mathbb{E}[X^n]=M_X^{(n)}(0)
$$

此外，$\forall x,y,\exists\delta>0,t\in(-\delta,\delta)$，我们有

$$
M_X(t)=M_Y(t)
$$

那么$X$和$Y$有相同分布。如果$X,Y$独立，则

$$
M_{X+Y}(t)=M_X(t)M_Y(t)
$$

矩生成函数在后面的集中不等式的证明中有重要的地位。

## Chernoff方法

对于随机变量$X$，其期望为$\mu$，我们想求

$$
\Pr(X-\mu\ge\epsilon)
$$

常常会构造一个随机变量$t$，然后取指数，再利用马尔可夫不等式获得一个上界，上界必然是$t$的函数，然后将函数的最值作为最终的界：

$$
\begin{aligned}
\Pr(X-\mu\ge\epsilon)&=\Pr(e^{t(X-\mu)}\ge e^{t\epsilon}),t\in(0,+\infty)\\
&\leq\dfrac{\mathbb{E}[e^{t(X-\mu)}]}{e^{t\epsilon}}\\
&=\dfrac{\mathbb{E}[e^{tX}]}{e^{t(\epsilon+\mu)}}\\
&\leq\min_{t}\bigg\{\dfrac{\mathbb{E}[e^{tX}]}{e^{t(\epsilon+\mu)}}\bigg\}
\end{aligned}
$$

类似的，如果要求

$$
\Pr(X-\mu\le-\epsilon)
$$

我们会乘上一个负随机变量$t$，将不等号变向，已进行后面的马尔科夫不等式放缩。如果要求

$$
\Pr(\vert X-\mu\vert\ge\epsilon)
$$

我们可以放缩成上面两个概率的和：

$$
\Pr(\vert X-\mu\vert\ge\epsilon)\leq\Pr(X-\mu\ge\epsilon)+\Pr(X-\mu\le-\epsilon)
$$

## 二值Chernoff界

我们以分类问题为例：$n$个独立随机变量$X_i$，$X_i\in\\{0,1\\},\mathbb{E}[X_i]=\mu_i$，实际上就是$X_i\sim Ber(p_i)$，

$$
\mu=\sum_{i=1}^n\mathbb{E}[X_i]=\sum_{i=1}^n p_i
$$

1. $\forall\epsilon>0$，我们有

   $$
   \Pr[\sum_{i=1}^n X_i\ge(1+\epsilon)\mu]\leq\bigg(\dfrac{e^\epsilon}{(1+\epsilon)^{1+\epsilon}}\bigg)^\epsilon
   $$

2. $\forall\epsilon\in(0,1)$，我们有

   $$
   \Pr[\sum_{i=1}^n X_i\ge(1+\epsilon)\mu]\leq e^{-\mu\epsilon^2/3}
   $$

我们来证明这两个上界。根据Chernoff方法：

$$
\begin{aligned}
\Pr[\sum_{i=1}^n X_i\ge(1+\epsilon)\mu]&=\Pr[e^{t\sum_{i=1}^nX_i}\geq e^{t(1+\epsilon)\mu}]\\
&\leq e^{-t(1+\epsilon)\mu}\mathbb{E}[e^{t\sum_{i=1}^n X_i}]\\
&=e^{-t(1+\epsilon)\mu}\prod_{i=1}^n\mathbb{E}[e^{tX_i}]\\
&=e^{-t(1+\epsilon)\mu}\prod_{i=1}^n[(1-p_i)+p_ie^t]&离散期望公式\\
&\leq e^{-t(1+\epsilon)\mu}\prod_{i=1}^ne^{p_i(e^t-1)}&利用了1+x\leq e^x\\
&=e^{-t(1+\epsilon)\mu+\mu(e^t-1)}\\
&\leq\exp(\min_t\{\mu(e^t-1{)}-\mu t(1+\epsilon{)}\})
\end{aligned}
$$

我们现在只需要求函数

$$
f=\mu(e^t-1)-\mu t(1+\epsilon)
$$

关于$t$的最小值：

$$
f'(t)=\mu(e^t-1-\epsilon)
$$

当$t=\ln(1+\epsilon)$，函数取极小

$$
\min_t f=\mu\epsilon-\mu(1+\epsilon)\ln(1+\epsilon)
$$

代入，则不等式1得证。而对于不等式2，我们只需要用简单的微积分证明

$$
e^{-\mu\epsilon^2/3}\leq\bigg(\dfrac{e^\epsilon}{(1+\epsilon)^{1+\epsilon}}\bigg)^\epsilon
$$

即可，这里省略。对于不等式1，我们也有反向的版本：

$$
\Pr[\sum_{i=1}^n X_i\le(1-\epsilon)\mu]\leq\bigg(\dfrac{e^\epsilon}{(1-\epsilon)^{1-\epsilon}}\bigg)^\epsilon
$$

我们在前面提到，利用负随机变量$t$即可证明。

## Rademacher随机变量下的Chernoff界

先介绍Rademacher随机变量：$X\in\\{-1,+1\\}$，且变量取$\pm1$的概率都是0.5。对于$n$个独立的Rademacher随机变量下，我们有这样的不等式界：

$$
\begin{aligned}
\Pr[\frac1n\sum_{i=1}^nX_i\ge\epsilon]\leq&e^{-n\epsilon^2/2}\\
\Pr[\frac1n\sum_{i=1}^nX_i\le-\epsilon]\leq&e^{-n\epsilon^2/2}\\
\end{aligned}
$$

该不等式的证明颇为巧妙，我们来仔细分析。

$$
\begin{aligned}
\Pr[\frac1n\sum_{i=1}^nX_i\ge\epsilon]&\leq\frac{1}{e^{tn\epsilon}}\mathbb{E}[e^{t\sum_{i=1}^nX_i}]\\
&=\frac{1}{e^{tn\epsilon}}\prod_{i=1}^n\mathbb{E}[e^{tX_i}]\\
&=\frac{1}{e^{tn\epsilon}}\prod_{i=1}^n(\frac12e^t+\frac12 e^{-t})\\
&=\frac{1}{e^{tn\epsilon}}\prod_{i=1}^n(\frac12\sum_{k=0}^\infty\frac{t^k}{k!} +\frac12\sum_{k=0}^\infty\frac{(-t)^k}{k!} )&Taylor展开\\
&=\frac1{e^{tn\epsilon}}\prod_{i=1}^n\sum_{k=0}^{\infty}\dfrac{t^{2k}}{2k!}&奇数项抵消\\
&\leq\frac1{e^{tn\epsilon}}\prod_{i=1}^n\sum_{k=0}^\infty\dfrac{(\frac{t^2}2)^k}{k!}&2k!\geq 2^k\cdot k!\\
&=\frac1{e^{tn\epsilon}}\prod_{i=1}^ne^{\frac{t^2}2}\\
&=e^{\frac{n}2t^2-nt\epsilon}\\
&\leq e^{-\frac n2\epsilon^2}&求导
\end{aligned}
$$

我们由此得到一个推论，若随机变量$P(X_i=0)=P(X_i=1)=\frac12$，那么

$$
\begin{aligned}
\Pr[\frac1n\sum_{i=1}^nX_i-\frac12\ge\epsilon]&\leq e^{-2n\epsilon^2}\\
\Pr[\frac1n\sum_{i=1}^nX_i-\frac12\le-\epsilon]&\leq e^{-2n\epsilon^2}\\
\end{aligned}
$$

只需要对随机变量$X$做一个映射

$$
Y_i=2X_i-1
$$

此时$Y$就是Rademacher随机变量，回到上面的不等式。

## 有界的Chernoff不等式

### Chernoff引理

先介绍切尔诺夫引理：$X\in[0,1]$, $\mu=E[X]$, $\forall t>0$，我们有

$$
\mathbb{E}[e^{tX}]\leq e^{t\mu+\frac{t^2}8}
$$

如果进行变量替换，X法范围变成$[a,b]$，那么不等式变成

$$
\mathbb{E}[e^{tX}]\leq e^{t\mu+\frac{t^2}8(b-a)^2}
$$

我们来证明该引理：

$$
\begin{aligned}
e^{tX}&=e^{tX+(1-x)0}&变成一个分布\\
&\leq xe^t+(1-x)&Jensen不等式\\
\mathbb{E}[e^{tX}]&\leq\mu e^t+1-\mu\\
&=e^{\ln(1-\mu+\mu e^t)}\\
\end{aligned}
$$

然后我们只需要证明

$$
f(t)=1-\mu+\mu e^t\leq t\mu+\frac{t^2}8,t>0
$$

因为

$$
\begin{aligned}
f(0)&=0\\
f'(0)&=\mu\\
f''(0)&\leq\frac14
\end{aligned}
$$

由泰勒中值定理，$\forall t>0,\exists\xi>0$

$$
f(t)=f(0)+tf'(0)+\frac12t^2f''(0)\leq \mu t+\frac{t^2}8
$$

由此引理得证。

### Chernoff不等式

$n$个独立随机变量$X_i\in[a,b]$，$\forall\epsilon>0$，我们有

$$
\Pr[\frac1n\sum_{i=1}^nX_i-\frac1n\sum_{i=1}^n\mathbb{E}[X_i]\ge\epsilon]\leq e^{-\frac{2n\epsilon^2}{(b-a)^2}}
$$

证明：先用切尔诺夫方法，获得其概率的上界：

$$
\dfrac{\mathbb{E}[e^{t\sum_{i=1}^nX_i}]}{e^{t\sum_{i=1}^n\mathbb{E}[X_i]+nt\epsilon}}
$$

然后对分子使用引理，进一步放缩，将问题转换成证明

$$
\frac{(b-a)^2}8t^2-t\epsilon\leq-\frac{2\epsilon^2}{(b-a)^2}
$$

即可。
