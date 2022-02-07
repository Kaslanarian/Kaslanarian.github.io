---
layout:     post
title:      有限假设空间下的样本复杂度
subtitle:   可分情形与不可分情形
date:       2022-02-07
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 机器学习
---

## 引入

样本复杂度是满足PAC学习算法$\mathfrak{L}$所需的$m\geq\text{poly}(\frac1\epsilon,\frac1\delta,\text{size}(\pmb x),\text{size}(c))$的最小的$m$，称其为算法$\mathfrak{L}$的样本复杂度。关于PAC学习的一些基本定义，比如PAC辨识、PAC可学、PAC学习算法等概念，由于网上资料很多，我们不做介绍，直接入正题。对于样本复杂度，我们关注下面四种场景:

1. 有限假设空间的可分(realizable)情形；
2. 无限假设空间的可分情形；
3. 有限假设空间的不可分情形(agnostic)；
4. 无限假设空间的不可分情形.

下面的表格列出了上述四种情况的样本复杂度

|        Sample Complexity         |                          Realizable                          |                           Agnostic                           |
| :------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  Finite $\vert\mathcal{H}\vert$  | $m\geq\frac1\epsilon[\log(\vert\mathcal{H}\vert)+\log(\frac1\delta)]$ | $m\geq\frac1{2\epsilon^2}[\log(\vert\mathcal{H}\vert)+\log(\frac2\delta)]$ |
| Infinite $\vert\mathcal{H}\vert$ | $m=O(\frac1\epsilon[d\log(\frac1\epsilon)+\log(\frac1\delta)])$ |       $m=O(\frac1{\epsilon^2}[d+\log(\frac1\delta)])$        |

其中$d$是无限假设空间$\mathcal{H}$的VC维。不需要考虑VC维无穷的情况，因为可以证明VC维无穷等价于样本复杂度无穷，如此问题就失去了讨论意义。

无限假设空间的样本复杂度是一个旷日持久的问题，它的上界一直在被刷新，形式也更加复杂，上表提供的是较为简洁且普适的上界。本文要讨论的东西简单得多，即有限假设空间的样本复杂度证明。

## 可分情形

给定从分布$\mathcal{D}$中独立同分布采样得到的训练数据集$D$，算法$\mathfrak{L}$所考虑的假设空间$\mathcal{H}$中的假设$h$可分为三类:

1. 在$D$上的经验误差大于0；
2. 在$D$上的经验误差为0，但在$\mathcal{D}$上的泛化误差大于0；
3. 在$D$上的经验误差为0，但在$\mathcal{D}$上的泛化误差也为0.

由于是可分情形，第二类和第三类必存在。根据已有的$D$，我们只能排除第一类，而无法辨识第二类和第三类。给定$\epsilon\in(0,1)$，PAC学习框架将第二类与第三类的假设重新分类成：泛化误差大于$\epsilon$的假设，和泛化误差不大于$\epsilon$的假设。显然当训练集数目$m$越大，算法输出前一种假设的概率越小，输出泛化误差不大于$\epsilon$的假设的概率越大。给定$\delta\in(0,1)$，我们希望算法$\mathfrak{L}$以$1-\delta$的概率输出后一种假设即可。即，令**在训练集上表现完美且泛化误差大于$\epsilon$的假设出现概率之和不大于$\delta$**。

设$h$的泛化误差$E(h)>\epsilon$，那么对于从分布$\mathcal{D}$上独立同分布采样的任意数据$(\pmb x,y)$，有

$$
\begin{aligned}
P(h(\pmb x)=y)
&=1-P(h(\pmb x)\neq y)\\
&=1-E(h)\\
&<1-\epsilon
\end{aligned}
$$

训练数据集$D$正是$m$个从分布$\mathcal{D}$中独立同分布采样的样例，因此$h$在训练集上表现完美，即训练误差为0的概率是

$$
\begin{aligned}
P(\wedge_{i=1}^m(h(\pmb x_i)=y_i))
&=(1-P(h(\pmb x)\neq y_i))^m\\
&<(1-\epsilon)^m
\end{aligned}
$$

我们想让它们出现的概率和不大于$\delta$，也就是

$$
P(h\in\mathcal{H}:E(h)>\epsilon\wedge\hat{E}(h)=0)<\vert\mathcal{H}\vert(1-\epsilon)^m<\vert\mathcal{H}\vert e^{-m\epsilon}\leq\delta
$$

所以

$$
m\geq\frac1\epsilon(\ln\vert\mathcal{H}\vert+\ln\frac1\delta)
$$

正是表格中有限假设空间且可分情形的样本复杂度。

## 不可分情形

不可分，也就是对训练集不可分：$\forall h\in\mathcal{H}$，$h$的经验误差都大于0，任意一个假设在训练集上都会出现或多或少的错误。所以我们希望算法$\mathfrak{L}$以$1-\delta$的概率输出经验误差与泛化误差相差小于$\epsilon$的假设。即**算法输出经验误差与泛化误差相差不小于$\epsilon$的假设的概率不大于$\delta$**。

由Hoeffding不等式：

$$
\begin{aligned}
P(E(h)-\hat{E}(h)\geq\epsilon)&\leq\exp(-2m\epsilon^2)\\
P(\hat{E}(h)-E(h)\geq\epsilon)&\leq\exp(-2m\epsilon^2)\\
P(|E(h)-\hat{E}(h)|\geq\epsilon)&\leq2\exp(-2m\epsilon^2)\\
\end{aligned}
$$

得到单个假设满足上述条件的概率。类似的，我们想让它们出现的概率和不大于$\delta$，所以

$$
\begin{aligned}
2|\mathcal{H}|\exp(-2m\epsilon^2)&\leq\delta\\
m&\geq\frac1{2\epsilon^2}[\ln|\mathcal{H}|+\ln\frac2\delta]
\end{aligned}
$$

正是表格中的结果。
