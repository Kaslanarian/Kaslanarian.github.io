---
layout:     post
title:      软阈值函数的推导
subtitle:   由来、推导和在优化上的应用
date:       2022-01-22
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 机器学习
    - 数字信号处理
---

软阈值函数(Soft-thresholding function)是一种降噪函数，常用在数字信号处理领域。本文是受[一篇Note](https://eeweb.engineering.nyu.edu/iselesni/lecture_notes/SoftThresholding.pdf)的启发，介绍软阈值函数的由来与推导，同时介绍它在优化问题上的一个简单应用。

## 背景

考虑一个信号被加上噪声:

$$
y=x+n
$$

其中$n$是零均值高斯分布噪声，独立于$x$。我们需要尽可能从带噪信号$y$还原出原始信号$x$。在一些领域，比如小波分析(wavelet)，短时距傅里叶变换(STFT)，该问题被表达成

$$
y=w+n
$$

其中$y$是带噪声系数(noisy coefficient)，$w$是无噪声系数(noisy-free coefficient)，$n$是噪声，还是一个零均值高斯变量。我们想利用最大后验分布，通过观察$y$，估计出最有可能的$w$，也就是求条件概率分布的极值:

$$
\hat{w}(y)=\mathop{\arg\max}\limits_{w}\Pr(w\vert y)
$$

由贝叶斯公式:

$$
\Pr(w\vert y)=\dfrac{\Pr(w)\Pr(y\vert w)}{\Pr(y)}
$$

由于我们是求概率关于$w$的极值，而$\Pr(y)$与$w$不相关，因此问题可简化为

$$
\hat{w}(y)=\mathop{\arg\max}\limits_{w}\Pr(w)\Pr(y\vert w)
$$

考虑

$$
y=w+n\sim\mathcal{N}(w,\sigma_n^2)
$$

令$p_n(n)$为零均值高斯随机变量的概率密度函数，从而有

$$
\Pr(y\vert w)=p_n(y-w)
$$

也就是上式的$\mathcal{N}(w,\sigma_n^2)$，因此优化问题等价于

$$
\hat{w}(y)=\mathop{\arg\max}\limits_{w}[p_n(y-w)\cdot\Pr(w)]
$$

加上对数(不影响最优解):

$$
\begin{aligned}
\hat{w}(y)
&=\mathop{\arg\max}\limits_{w}[p_n(y-w)\cdot\Pr(w)]\\
&=\mathop{\arg\max}\limits_{w}[\log p_n(y-w)+\log \Pr(w)]\\
&=\mathop{\arg\max}\limits_{w}[-\frac{(y-w)^2}{2\sigma_n^2}+\log \Pr(w)]\\
\end{aligned}
$$

定义$f(w)=\log \Pr(w)$，也就是概率密度函数的对数，因此优化问题的最优解满足

$$
\frac{y-\hat{w}}{\sigma_n^2}+f'(\hat w)=0
$$

现在的问题是无噪声系数$w$服从何种概率分布模型。在自然图像的小波分析领域，$p_w(w)$通常被建模成广义高斯分布(generalized):

$$
p_w(w)=K(s,p)\exp(-\bigg\vert\dfrac{w}{s}\bigg\vert^p)
$$

其中$s,p$是分布的系数，$K(s,p)$是归一化常数，用于控制$p_w(w)$的积分为1，符合概率分布要求。可以看到当$p=2$时，$p_w(w)$正是高斯分布。广义高斯分布都有重尾(heavy-tailed)的特征。我们假设$p=1$，也就是服从拉普拉斯分布:

$$
p_w(w)=\frac{1}{\sqrt2\sigma}\exp(-\frac{\sqrt2}{\sigma}\vert w\vert)
$$

尽管拉普拉斯分布不是最准确的概率模型，但它很简单且具有信号的基本特性。下图是零均值，不同方差的拉普拉斯分布概率密度函数:

<img src="/img/dsp/laplace.png" alt="laplace" style="zoom:67%;" />

在这样的假设下

$$
f(w)=-\log(\sigma\sqrt2)-\frac{\sqrt2}{\sigma}\vert w\vert\\
f'(w)=-\frac{\sqrt2}{\sigma}\cdot\text{sign}(w)
$$

因此最优条件(求导为0)等价于满足下面的等式

$$
\frac{y-\hat{w}}{\sigma_n^2}-\frac{\sqrt2}{\sigma}\text{sign}(\hat{w})=0
$$

我们想找出函数$\hat{w}(y)$，也就是给定$y$，返回合理的$\hat{w}$，但显然不容易得到，我们决定先求$y(\hat{w})$:

$$
y=\hat{w}+\frac{\sqrt2\sigma_n^2}{\sigma}\text{sign}(\hat w)
$$

图像是这样的

<img src="/img/dsp/y_w.png" alt="y" style="zoom: 80%;" />

这里的$y(\hat w)$已经不是严格意义上的函数了。之所以$\hat w=0$时$y$有多个取值，是“次梯度”对导数进行推广:不可微点的导数不是一个值，而是一个集合（可参考<https://welts.xyz/2021/09/30/lasso/>）。现在要求$\hat{w}(y)$，也就是反函数，关于直线$y=\hat{w}$作轴对称即可:

<img src="/img/dsp/w_y.png" alt="w" style="zoom:80%;" />

也就是

$$
\hat{w}(y)=\begin{cases}
y+T,&y<-T\\
0,&-T\leq y\leq T\\
y-T,&T<y
\end{cases}\tag{*}
$$

对于该问题，$T=\sqrt2\sigma_n^2/\sigma$，上面的$\hat{w}(y)$便是**软阈值函数**，对输入的信号$y$，$\hat{w}(y)$会将较小的输入置为0，而将较大输入减小输出，可用于降噪的场景。

我们将上面的*式写作

$$
\hat{w}(y)=\text{sign}(y)\cdot(\vert{y}\vert-T)_+
$$

其中$(a)_+$被定义为

$$
(a)_+=\begin{cases}
0&\text{if }a\leq0\\
a&\text{if }a>0.
\end{cases}
$$

定义软阈值算子(soft operator)为

$$
\text{soft}(g,\tau)=\text{sign}(g)\cdot(\vert g\vert-\tau)_+
$$

因此上面的最大对数似然问题的解可写作

$$
\hat{w}(y)=\text{soft}(y,\frac{\sqrt2\sigma_n^2}\sigma)
$$

## 在优化问题上的应用

考虑一元优化问题

$$
\min\quad\frac a2(x-b)^2+\lambda\vert x\vert,a>0
$$

求导得到

$$
b=\hat{x}+\frac\lambda a\text{sign}(\hat{x})
$$

显然$\hat{x}(b)$是软阈值函数，也就是$\text{soft}(b,\frac\lambda{a})$。所以该问题的最优解就是

$$
\hat{x}=\begin{cases}
b-\frac\lambda a,&b<-\frac\lambda a\\
0,&-\frac\lambda a\leq b\leq\frac\lambda a\\
b+\frac\lambda a,&\frac\lambda a<b
\end{cases}
$$

将问题扩展到多元优化问题，也就是

$$
\min_{X}\quad\frac12\Vert X-B\Vert_2^2+\lambda\Vert X\Vert_1
$$

这样的拓展成立是因为

$$
\begin{aligned}
\Vert X-B\Vert_2^2&=\sum_i\sum_{j}(X_{ij}-B_{ij})^2\\
\Vert X\Vert_1&=\sum_{i}\sum_{j}\vert X_{ij}\vert
\end{aligned}
$$

因此优化问题可分解为独立的多个子问题。因此最优解还是软阈值函数，也就是$\text{soft}(B,\lambda)$，注意此时的$B+\lambda$是将矩阵$B$的每一个元素都加上$\lambda$。

但是软阈值函数无法一步解决Lasso回归问题:

$$
\min\quad\Vert A\pmb x-\pmb b\Vert_2^2+\lambda\Vert\pmb x\Vert_1
$$

近端梯度下降法将该问题在每次迭代中转化成独立的子问题，而每个子问题可以用软阈值函数求解，可参考<https://welts.xyz/2021/09/30/lasso/>.
