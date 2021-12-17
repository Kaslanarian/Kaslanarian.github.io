---
layout:     post
title:      拉普拉斯变换的性质
subtitle:   列举与证明
date:       2021-12-17
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 数字信号处理
---

前篇：[拉普拉斯变换简述 - 邢存远的博客 : Welt Xing's Blog (welts.xyz)](https://welts.xyz/2021/12/16/lt/)

我们在前面介绍了拉普拉斯变换，现在我们对**单边拉普拉斯变换**的性质进行列举和证明。而其中不少特性，我们在[傅里叶变换的性质 - 邢存远的博客 : Welt Xing's Blog (welts.xyz)](https://welts.xyz/2021/12/16/ft_property/)已经做过类似的证明，这里不再过多赘述。

## 线性特性

对于两个时域信号$x_1(t)$和$x_2(t)$，我们有（证明略）

$$
\mathcal{L}[a_1x_1(t)+a_2x_2(t)]=a_1X_1(s)+a_2X_2(s)
$$

设它们的收敛轴分别是$\sigma_1$和$\sigma_2$，那么合成信号的收敛域:

$$
\sigma>\max(\sigma_1,\sigma_2)
$$

比如现在我们要求信号$\delta(t)+e^tu(t)$的拉普拉斯变换:

$$
\begin{aligned}
\mathcal{L}[\delta(t)+e^tu(t)]&=\mathcal{L}[\delta(t)]+\mathcal{L}[e^tu(t)]\\
&=1+\int_{0_{-}}^\infty e^{(1-s)t}\mathrm dt\\
&=1+\frac1{s-1}\\
&=\frac{s}{s-1}&\sigma>1
\end{aligned}
$$

## 展缩特性

和傅里叶变换类似:

$$
\mathcal{L}[x(at)]=\frac{1}{a}X(\frac{s}{a}),\sigma>a\sigma_0,a>0
$$

我们这里证明一下收敛域:

$$
\begin{aligned}
\mathcal{L}[x(at)]
&=\int_{0_{-}}^\infty x(at)e^{-st}\mathrm dt\\
&=\frac1a\int_{0_{-}}^\infty x(at)e^{-\frac sa at}\mathrm dat &\tau=at\\
&=\frac1a\int_{0_{-}}^\infty x(\tau)e^{-\frac{s}{a}\tau}\mathrm d\tau
\end{aligned}
$$

对于$x(t)$，如果收敛条件为$\sigma>\sigma_0$，那么对于新变换，我们有

$$
\begin{aligned}
\frac{\sigma}{a}&>\sigma_0\\{\sigma}&>a\sigma_0\\
\end{aligned}
$$

## 时移特性

对$t_0>0$，如果

$$
X(s)=\mathcal{L}[x(t)],\sigma>\sigma_0
$$

那么

$$
e^{-st_0}X(s)=\mathcal{L}[x(t-t_0)u(t-t_0)]
$$

## 综合运用

假如我们想求下面周期信号的单边LT:

![image-20211217111000688](/img/image-20211217111000688.png)

也就是

$$
x(t)=\sum_{k=0}^\infty x_1(t-k)
$$

其中

$$
x_1(t)=2(u(t)-u(t-1))
$$

运用线性特性和时移特性，我们可以计算出其LT：

$$
\begin{aligned}
\mathcal{L}[x(t)]
&=\mathcal{L}[\sum_{k=0}^\infty x_1(t-2k)]\\
&=\sum_{k=0}^\infty\mathcal{L}[x_1(t-2k)]\\
&=\sum_{k=0}^\infty e^{-2sk}\mathcal{L}[x_1(t)]\\
&=\sum_{k=0}^\infty e^{-2sk}\mathcal{L}[2(u(t)-u(t-1))]\\
&=\sum_{k=0}^\infty2e^{-2sk}\int_{0_{-}}^1e^{-st}\mathrm dt\\
&=2\int_{0_{-}}^1e^{-st}\mathrm dt\sum_{k=0}^\infty e^{-2sk}\\
&=\frac{2}{1-e^{-2s}}\cdot(-\frac{e^{-s}-1}s)\\
&=\frac2{s(1+e^{-s})},\sigma>0
\end{aligned}
$$

再看一个例子，已知$\mathcal{L}[x(t)]=X(s)$，若$a>0,b>0$，求$\mathcal{L}[x(at-b)u(at-b)]$：

我们将信号从$x(t)u(t)$经过一系列变换变成目标信号，先时移再展缩

$$
\begin{aligned}
\mathcal{L}[x(t-b)u(t-b)]&=e^{-bs}X(s)\\
\mathcal{L}[x(at-b)u(at-b)]&=\frac{e^{-\frac{bs}{a}}}aX(\frac sa)\\
\end{aligned}
$$

注意这里的$e^{-bs}$由于是$s$的函数，所以也要进行展缩.

## 卷积特性

和傅里叶变换类似，也就是时域信号的卷积等于复频域信号的乘积，其收敛域满足

$$
\sigma>\max(\sigma_1,\sigma_2)
$$

## 乘积特性

类似的，频域的卷积**正比于**时域的乘积:

$$
\mathcal{L}[x_1(t)x_2(t)]=\frac1{2\pi j}[X_1(s)*X_2(s)]
$$

和上面不同的是，其收敛域为

$$
\sigma>\sigma_1+\sigma_2
$$

这是由乘积信号的拉普拉斯变换决定的:

$$
\mathcal{L}[x_1(t)x_2(t)]=\int_{0_{-}}^\infty x_1(t)x_2(t)e^{-st}\mathrm dt
$$

如果与特殊信号相乘，比如指数信号$e^{-\lambda t}$(指数加权)，效果则是平移(参考上面的时移特性):

$$
\mathcal{L}[e^{-\lambda t}x(t)]=X(s+\lambda)
$$

如果是线性加权，效果则是取微分:

$$
\mathcal{L}[-t x(t)]=\dfrac{\mathrm dX(s)}{\mathrm ds}
$$

## 微分特性

$$
\mathcal{L}[\frac{\mathrm dx(t)}{\mathrm dt}]=sX(s)-x(0_{-}),\sigma>\sigma_0
$$

如果$x(0_{-})=0$，那么微分特性和傅里叶变换中的相同.

不难得出该规律的高阶扩展:

$$
\mathcal{L}[\dfrac{d^nx(t)}{\mathrm d^n t}]=s^nX(s)-\sum_{r=0}^{n-1}s^{n-r-1}x^{(r)}(0_{-})
$$

## 积分特性

$$
\mathcal{L}[\int_{-\infty}^t x(\tau)\mathrm d\tau]=\frac{X(s)}s+\frac1s\int_{-\infty}^{0_{-}}x(\tau)\mathrm d\tau,\sigma>\max(\sigma_0,0)
$$

为了便于书写，我们会将$\int_{-\infty}^{0_{-}} x(\tau)\mathrm d\tau$简写成$x^{-1}(0_{-})$，如果该值为0，上式可以简化成

$$
\mathcal{L}[\int_{-\infty}^t x(\tau)\mathrm d\tau]=\frac{X(s)}s
$$

## 综合运用

对下面的信号进行拉普拉斯变换:

![image-20211217230248656](/img/image-20211217230248656.png)

硬算积分当然是可以的:

$$
\int_{0_{-}}^\infty x(t)e^{-st}\mathrm dt=\int_{0}^1te^t\mathrm dt+\int_{1}^2(2-t)e^{-st}\mathrm dt
$$

但我们想利用上面提到的性质进行快速求解。我们对信号求微分，一阶微分:

![image-20211217231002753](/img/image-20211217231002753.png)

二阶微分:

![image-20211217231017971](/img/image-20211217231017971.png)

利用前面提到的微分性质:

$$
\begin{aligned}
\mathcal{L}[\dfrac{\mathrm d^2x(t)}{\mathrm dt^2}]
&=s^2X(s)-sx(0_{-})-x'(0_{-})\\
\int_{0_{-}}^\infty x''(t)e^{-st}\mathrm dt&=s^2X(s)\\
1-2e^{-s}+e^{-2s}&=s^2X(s)\\
X(s)&=\frac{1-2e^{-s}+e^{-2s}}{s^2},\sigma>-\infty
\end{aligned}
$$

除此之外，我们还可以将信号分解为:

$$
x(t)=r(t)-2r(t-1)+r(t-2),r(t)=tu(t)
$$

而$r(t)$的LT很好求得:

$$
\mathcal{L}[tu(t)]=\frac{1}{s^2}
$$

从而利用线性特性和平移特性，求得$x(t)$的拉普拉斯变换:

$$
\begin{aligned}
\mathcal{L}[x(t)]
&=\mathcal{L}[r(t)-2r(t-1)+r(t-2)]\\
&=\mathcal{L}[r(t)]-2\mathcal{L}[r(t-1)]+\mathcal{L}[r(t-2)]\\
&=(1-2e^{-s}+e^{-2s})\mathcal{L}[r(t)]\\
&=\frac{1-2e^{-s}+e^{-2s}}{s^2},\sigma>-\infty\\
\end{aligned}
$$

## 初值定理和终值定理

对**因果序列**，如果$\mathcal{L}[x(t)]=X(s),\sigma>\sigma_0$，且其导数可进行LT；若$x(t)$在$t=0$不包含**冲激及其各阶导数**，那么

$$
\lim_{t\to0}x(t)=x(0_{+})=\lim_{s\to\infty}sX(s)
$$

初值定理只适用于有理真分式的情况. 若$sX(s)$的收敛域包含$j\omega$轴，也就是收敛轴在负半轴，那么

$$
\lim_{t\to\infty}x(t)=x(\infty)=\lim_{s\to0}sX(s)
$$

## 拉普拉斯变换和傅里叶变换的关系

我们前面提到过，傅里叶变换就是拉普拉斯变换的一种特殊情况，对于任意信号，如果其收敛域包含了零点，那么就是可以进行傅里叶变换的，否则就不是。

我们考虑特殊情况，也就是收敛域的收敛边界位于$j\omega$轴时，两种变换的关系:

$$
X(j\omega)=X(s)\vert_{s=j\omega}+\pi\sum_{n}K_n\delta(\omega-\omega_n)
$$

其中$K_n$是系数。举例来说，信号

$$
x(t)=\cos 2t\;u(t)
$$

的拉普拉斯变换很好计算:

$$
\mathcal{L}[x(t)]=\frac{s}{s^2+4},\sigma>0
$$

因为收敛边界为$j\omega$轴，因此其傅里叶变换不是简单的将$s$替换为$j\omega$，而是多出一项:

$$
\mathcal{F}[x(t)]=\frac{j\omega}{(j\omega)^2+4}+\frac\pi2[\delta(\omega-2)+\delta(\omega+2)]
$$
