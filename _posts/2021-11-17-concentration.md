---
layout:     post
title:      集中不等式(1)
subtitle:   Concentration
date:       2021-11-17
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 概率论
---

笔者在一年前曾学习过相关内容，但当时没有机器学习的相关基础，也没想到自己会在以后的工作中依赖这些知识。幸运的是导师能让我旁听并复习这部分内容，笔者因此也认真对待，本文记录的就是课上内容。

## <center>机器学习与集中不等式

对于数据特征与标记，机器学习的一个基本假设就是独立同分布假设：数据特征$\mathcal{X}$与标记$\mathcal{Y}$服从分布$\mathcal{D}$，而已知数据集$S_n$是从该分布中独立采样得到：

$$
\mathcal{X},\mathcal{Y}\sim\mathcal{D}\\
S_n\sim D,i.i.d
$$

我们研究的问题是分类问题，因此标记空间为$\\{0,1\\}$。给定一个分类器$f$，我们可以写出经验误差与泛化误差：

$$
\begin{aligned}
\hat{R}(f,S_n)&=\frac1n\sum_{i=1}^n\mathbb{I}[f(x_i\neq y_i)]\\
R(f)&=\mathbb{E}_{(x,y)\sim\mathcal{D}}\big[\mathbb{I}[f(x)\neq y]\big]
\end{aligned}
$$

机器学习的核心任务，就是让经验误差尽可能地去逼近泛化误差，也就是对于任意的$t$，令概率

$$
\Pr_{S_n}\big[
\vert\hat{R}(f,S_n)-R(f)\vert\geq t
\big]
$$

足够小，等价于让$\vert\hat{R}(f,S_n)-R(f)\vert<t$的概率很大。

假设我们有一个能使经验误差为0的分类器$f$，现在尝试求泛化误差$R(f)$在$(0,\epsilon)$的概率。刚见到这样的问题会非常困惑，因为不知道如何下手。我们设随机变量

$$
X_i=\mathbb{I}[f(x_i)\neq y_i],i=1,2,\cdots n
$$

显然$X_i\in\\{0,1\\}$. 我们也很容易用随机变量来表示经验误差与泛化误差：

$$
\begin{aligned}
\hat{R}(f,S_n)&=\frac1n\sum_{i=1}^n X_i\\
R(f)&=\mathbb{E}_{x\sim\mathcal{D}}[x]
\end{aligned}
$$

考虑表达上的简便，设$p=R(f)$。因为经验误差为0，我们相当于求

$$
\Pr\big(p\in(0,\epsilon),X_i=0,i=1,\cdots,n\big)
$$

为了简化问题，我们改变不等式方向：

$$
\begin{aligned}
\Pr\big(p\geq\epsilon,X_i=0,i=1,\cdots,n\big)
&\leq\Pr\big(X_i=0,i=1,2,\cdots,n\vert p>\epsilon\big)&条件概率\\
&=\prod_{i=1}^n\Pr(X_i=0\vert p>\epsilon)&独立性假设\\
&\leq\prod_{i=1}^n(1-\epsilon)&条件概率\\
&\leq e^{-n\epsilon}&1-x\leq e^{-x}
\end{aligned}
$$

从而，我们能求出泛化误差$R(f)$在$(0,\epsilon)$的概率:

$$
\Pr(X_i=0,i=1,\cdots,n,p\in(0,\epsilon))\geq1-e^{-n\epsilon}
$$

指数收敛率是很令人欣喜的，因为它比通常的多项式收敛更快。

说到这里，我们似乎并没有接触到有关“集中不等式”的内容，但我们将上面的问题泛化一下就可以瞥见端倪：我们相当于在求解概率

$$
\Pr\big[\big\vert\frac1n\sum_{i=1}^nX_i-\mathbb{E}[X]\big\vert<\epsilon\big]
$$

而通过集中不等式，我们能将该概率收敛到不同的界。

## <center>Markov不等式

马尔科夫不等式：对于非负的随机变量$X$和$\epsilon$，我们有

$$
\Pr(X\geq\epsilon)\leq\dfrac{\mathbb{E}[X]}{\epsilon}
$$

我们可以用全概率去证明该不等式：

$$
\begin{aligned}
\mathbb{E}[X]&=\mathbb{E}[X\vert X\geq\epsilon]\Pr(X\geq\epsilon)+\mathbb{E}[X\vert X<\epsilon]\Pr(X<\epsilon)\\
&\geq\mathbb{E}[X\vert X\geq\epsilon]\Pr(X\geq\epsilon)\\
&\geq\epsilon\Pr(X\geq\epsilon)\\
\dfrac{\mathbb{E}[X]}{\epsilon}&\geq\Pr(X\geq\epsilon)
\end{aligned}
$$

如果我们有一个非负的单增映射，我们可以得到马尔科夫不等式的拓展形式：

$$
\Pr(X\geq\varepsilon)\leq\dfrac{\mathbb{E}[g(X)]}{g(\epsilon)}
$$

该不等式也很好证明：

$$
\Pr(X\geq\varepsilon)=\Pr(g(X)\geq g(\epsilon))\leq\dfrac{\mathbb{E}[g(X)]}{g(\epsilon)}
$$

## <center>Chebyshev不等式

切比雪夫不等式：对于一个随机变量$X$，其期望为$\mu$，那么

$$
\Pr(\vert{X-\mu}\vert>\epsilon)\leq\dfrac{\sigma^2}{\epsilon^2}
$$

证明：

$$
\begin{aligned}
\Pr(\vert{X-\mu}\vert>\epsilon)&\leq\Pr(({X-\mu})^2>\epsilon^2)\\
&\leq\dfrac{\mathbb{E}[(X-\mu)^2]}{\epsilon^2}&\text{Markov inequality}\\
&=\dfrac{\sigma^2}{\epsilon^2}
\end{aligned}
$$

这里的第一行是遵从这样的规律：如果命题产生这样的关系：$A\to B$，那么$P(A)\leq P(B)$

### Cantelli不等式

也称单边的切比雪夫不等式，保留切比雪夫不等式的条件：

$$
\begin{aligned}
\Pr(X-\mu\geq\epsilon)&\leq\dfrac{\sigma^2}{\sigma^2+\epsilon^2}\\
\Pr(X-\mu\leq-\epsilon)&\leq\dfrac{\sigma^2}{\sigma^2+\epsilon^2}\\
\end{aligned}
$$

可以发现，单边切比雪夫不等式能更紧地进行约束。证明该不等式用到了一个很巧妙的方法，我们只证明第一个：设随机变量$Y=X-\mu$，那么有

$$
\mathbb{E}[Y]=0\\
Var(Y)=\sigma^2
$$

再**设一个随机变量**$t\in[0,+\infty)$，从而

$$
\begin{aligned}
\Pr(Y\geq\epsilon)&=\Pr(Y+t\geq\epsilon+t)\\
&\leq\Pr((Y+t)^2\geq(\epsilon+t)^2)\\
&\leq\dfrac{\mathbb{E}[(Y+t)^2]}{(\epsilon+t)^2}&\text{Markov inequality}\\
&=\dfrac{\sigma^2+t^2}{(\epsilon+t)^2}
\end{aligned}
$$

我们接下来需要证明函数

$$
f(t)=\dfrac{\sigma^2+t^2}{(\epsilon+t)^2}
$$

的最小值不大于原不等式的上界，因为这样我们就可以找到合适的$t$使原不等式得到满足。因为

$$
t^*=\mathop{\arg\min}\limits_{t}\;f=\dfrac{\sigma^2}{\epsilon}
$$

代入到$f(t)$，恰好是$\frac{\sigma^2}{\epsilon^2+\sigma^2}$，因此不等式得到证明。

### Chebyshev不等式的一个推论

对于$n$个独立同分布的随机变量，$E[X]=\mu,Var(X)\leq\sigma^2$，则$\forall\epsilon>0$，我们有

$$
\Pr\big[
\big\vert\frac1n\sum_{i=1}^nX_i-\mu\big\vert\geq\epsilon
\big]\leq\dfrac{\sigma^2}{n\epsilon^2}
$$

证明：设随机变量$Y=\frac1n\sum_{i=1}^n X_i$，那么其期望$\mathbb{E}(Y)=\mu$，由切比雪夫不等式

$$
\begin{aligned}
\Pr\big[\vert{Y-\mu}\vert\geq\epsilon\big]&\leq\dfrac{Var(Y)}{\epsilon^2}\\
&=\frac1{\epsilon^2n^2}Var(\sum_{i=1}^nX_i)\\
&=\frac1{\epsilon^2n^2}\cdot n\sigma^2&独立同分布\\
&=\frac{\sigma^2}{n\epsilon^2}
\end{aligned}
$$

## <center>总结

本文以机器学习任务为引入，介绍了集中不等式在机器学习以及概率论中的重要意义，同时介绍了两种集中不等式：马尔科夫不等式和切比雪夫不等式，它们的证明以及推广。
