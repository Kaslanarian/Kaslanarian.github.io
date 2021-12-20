---
layout:     post
title:      Z变换的性质
subtitle:   列举、证明与比较
date:       2021-12-20
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 数字信号处理
---

这里讨论Z变换的性质。可以预见其性质与拉普拉斯变换性质相似。

## 线性特性

给定两离散信号$x_1[n]$和$x_2[n]$，对应的$Z$变换就是$X_1(z)$和$X_2(z)$，收敛域分别是$R_{x1}$和$R_{x2}$，则我们有

$$
\mathcal{Z}[ax_1[n]+bx_2[n]]=aX_1(z)+bX_2(z),\vert z\vert>\max(R_{x1},R_{x2})
$$

我们现在想求信号$x[n]=\cos(\omega_0 n)u[n]$的Z变换:

$$
\begin{aligned}
\mathcal{Z}\{x[n]\}
&=\mathcal{Z}\{(\frac12e^{j\omega_0n}+\frac12e^{-j\omega_0 n})u[n]\}\\
&=\frac12\mathcal{Z}\{e^{j\omega_0n}u[n]\}+\frac12\mathcal{Z}\{e^{-j\omega_0n}u[n]\}\\
&=\frac12\frac1{1-e^{j\omega_0}z^{-1}}+\frac12\frac1{1-e^{-j\omega_0}z^{-1}}\\
&=\frac12\frac{2-(e^{j\omega_0}+e^{-j\omega_0})z^{-1}}{1-(e^{j\omega_0}+e^{-j\omega_0})z^{-1}+z^{-2}}\\
&=\frac{1-\cos\omega_0 z^{-1}}{1-2z^{-1}\cos\omega_0+z^{-2}},\vert{z}\vert>1
\end{aligned}
$$

类似的

$$
\mathcal{Z}[\sin(\omega_0n)u[n]]=\frac{\sin\omega_0 z^{-1}}{1-2z^{-1}\cos\omega_0+z^{-2}},\vert{z}\vert>1
$$

## 位移特性

已知$\mathcal{Z}[x[n]]=X(z),\vert{z}\vert>R_x$，因果序列的位移满足

$$
\mathcal{Z}\{x[n-k]u[n-k]\}=z^{-k}X(z),\vert{z}\vert>R_x
$$

如果不是因果序列，则

$$
\begin{aligned}
\mathcal{Z}\{x[n+k]u[n]\}&=x^k[X(z)-\sum_{n=0}^{k-1}x[n]z^{-n}],\vert z\vert>R_x\\
\mathcal{Z}\{x[n-k]u[n]\}&=x^{-k}[X(z)+\sum_{n=-k}^{-1}x[n]z^{-n}],\vert z\vert>R_x\\
\end{aligned}
$$

我们尝试证明上面的结论，先看因果序列的位移

$$
\begin{aligned}
\mathcal{Z}\{x[n-k]u[n-k]\}
&=\sum_{n=0}^\infty x[n-k]u[n-k]z^{-n}\\
&=z^{-k}\sum_{n=0}^\infty x[n-k]u[n-k]z^{-(n-k)}\\
&=z^{-k}\sum_{n=k}^\infty x[n-k]u[n-k]z^{-(n-k)}\\
&=z^{-k}\sum_{n=0}^\infty x[n]u[n]z^{-n}\\
&=z^{-k}X(z)
\end{aligned}
$$

现在考虑非因果序列，左移:

$$
\begin{aligned}
\mathcal{Z}\{x[n+k]u[n]\}
&=\sum_{n=0}^\infty x[n+k]u[n]z^{-n}\\
&=z^{k}\sum_{n=0}^\infty x[n+k]u[n]z^{-(n+k)}\\
&=z^{k}\sum_{n=k}^\infty x[n]z^{-n}\\
&=z^{k}\bigg[\sum_{n=0}^\infty x[n]z^{-n}-\sum_{n=0}^{k-1}x[n]z^{-n}\bigg]\\
&=z^k\bigg[X(z)-\sum_{n=0}^{k-1}x[n]z^{-n}\bigg]
\end{aligned}
$$

右移变换的证明与上面类似，这里不做过多赘述。

假如我们现在想求信号

$$
R_N[n]=u[n]-u[n-N]
$$

的Z变换和收敛域，利用线性特性和因果信号位移特性，我们有

$$
\begin{aligned}
\mathcal{Z}\{R_N[n]\}&=\mathcal{Z}\{u[n]\}-\mathcal{Z}\{u[n-N]\}\\
&=\frac1{1-z^{-1}}-z^{-N}\frac{1}{1-z^{-1}}\\
&=\frac{1-z^{-N}}{1-z^{-1}}
\end{aligned}
$$

**因为该信号是有限长序列，所以收敛域为整个Z平面**。也就是说，线性加权后序列z变换的收敛域可能比原序列z变换的收敛域大。

## 指数加权

$$
\begin{aligned}
\mathcal{Z}\{a^nx[n]\}&=\sum_{n=0}^\infty a^nz^{-n}\\
&=\sum_{n=0}^\infty(\frac{z}{a})^{-n}\\
&=X(\frac za),\vert z\vert>\vert a\vert R_x
\end{aligned}
$$

所以信号

$$
x[n]=a^n\cos(\omega_0 n)u[n]
$$

的Z变换就是

$$
\begin{aligned}
\mathcal{Z}\{x[n]\}
&=\frac{1-\cos\omega_0 {(z/a)}^{-1}}{1-2{(z/a)}^{-1}\cos\omega_0+{(z/a)}^{-2}}\\
&=\frac{1-a\cos\omega_0 {z}^{-1}}{1-2a{z}^{-1}\cos\omega_0+a^2{z}^{-2}}\\
\end{aligned}
$$

## Z域微分特性

$$
\begin{aligned}
\mathcal{Z}\{nx[n]\}
&=\sum_{n=0}^\infty nx[n]z^{-n}\\
&=-z\sum_{n=0}^\infty -nx[n]z^{-n-1}\\
&=-z\sum_{n=0}^\infty x[n]\frac{\mathrm d z^{-n}}{\mathrm dz}\\
&=-z\frac{\mathrm d}{\mathrm dz}\sum_{n=0}^\infty x[n]z^{-n}\\
&=-z\frac{\mathrm dX(z)}{\mathrm dz},\vert{z}\vert>R_x
\end{aligned}
$$

比如我们现在要求$x[n]=(n+1)a^nu[n]$的Z变换和收敛域，考虑到

$$
\mathcal{Z}[a^nu[n]]=\frac1{1-az^{-1}},\vert z\vert>\vert a\vert
$$

利用上面的性质，我们有

$$
\mathcal{Z}\{na^nu[n]\}=-z\frac{\mathrm d}{\mathrm dz}\frac1{1-az^{-1}}=\frac{az^{-1}}{(1-az^{-1})^2},|z|>|a|
$$

然后利用线性特性得到最终结果：

$$
\mathcal{Z}\{(n+1)a^nu[n]\}=\mathcal{Z}\{na^nu[n]\}+\mathcal{Z}\{a^nu[n]\}=\frac1{(1-az^{-1})^2},|z|>|a|
$$

## 序列卷积

我们考察Z变换是否仍然有序列卷积的性质：

$$
\begin{aligned}
\mathcal{Z}\{x_1[n]*x_2[n]\}
&=\sum_{n=0}^{\infty}x_1[n]*x_2[n]z^{-n}\\
&=\sum_{n=0}^\infty\sum_{k=0}^\infty x_1[k]x_2[n-k]z^{-n}\\
&=\sum_{k=0}^\infty x_1[k]\sum_{n=0}^\infty x_2[n-k]z^{-n}\\
&=\sum_{k=0}^\infty x_1[k]z^{-k} X_2(z)\\
&=X_1(z)X_2(z)
\end{aligned}
$$

我们证明出卷积的Z变换等于Z变换的乘积。至于收敛域，显然我们上式的两次Z变换都需要满足，因此收敛域$\vert z\vert\in R_{x_1}\cap R_{x_2}$。

## 初值定理与终值定理

与拉普拉斯变换类似，Z变换也有对应的初值定理和终值定理。

$$
x[0]=\lim_{z\to\infty}X(z)
$$

若$(z-1)X(z)$的收敛域包含单位圆，则

$$
x[\infty]=\lim_{z\to 1}(z-1)X(z)
$$

比如，已知

$$
X(z)=\frac1{1-az^{-1}},|z|>|a|
$$

那么

$$
\begin{aligned}
x[0]&=\lim_{z\to\infty}X(z)=1\\
x[1]&=\lim_{z\to\infty}\mathcal{Z}\{x[n+1]\}\\
&=\lim_{z\to\infty}z(X(z)-x[0])\\
&=a\\
x[\infty]&=\lim_{z\to1}(z-1)X(z)\\
&=\lim_{z\to1}\frac{z-1}{1-az^{-1}}\\
&=0
\end{aligned}
$$

## 总结

我们对Z变换的性质进行总结：

![image-20211220174637079](/img/image-20211220174637079.png)

可以发现Z变换的很多性质继承自拉普拉斯变换，下图是两种变换的性质比较：

![image-20211220174739776](/img/image-20211220174739776.png)
