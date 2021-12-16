---
layout:     post
title:      傅里叶变换的性质
subtitle:   手动推导
date:       2021-12-16
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 数字信号处理
---

对于任意连续信号$x(t)$，其傅里叶变换

$$
X(j\omega)=\mathcal{F}[x(t)]=\int_{-\infty}^{+\infty}x(t)e^{-j\omega t}\mathrm dt
$$

我们在这里对其多种性质进行列举和推导:

## 线性性质

多个信号线性组合的傅里叶变换等于傅里叶变换的线性组合:

$$
\begin{aligned}
\mathcal{F}[ax_1(t)+bx_2(t)]
&=\int_{-\infty}^{+\infty}(ax_1(t)+bx_2(t))e^{-j\omega t}\mathrm dt\\
&=\int_{-\infty}^{+\infty}ax_1(t)e^{-j\omega t}\mathrm dt+\int_{-\infty}^{+\infty}bx_2(t)e^{-j\omega t}\mathrm dt\\
&=a X_1(j\omega)+bX_2(j\omega)
\end{aligned}
$$

## 对称性

如果$\mathcal{F}[x(t)]=X(j\omega)$，那么我们有$\mathcal{F}[X(t)]=2\pi x(-j\omega)$. 证明:

$$
\begin{aligned}
x(t)&=\frac1{2\pi}\int_{-\infty}^{+\infty}X(j\omega)e^{j\omega t}\mathrm d\omega\\
x(-t)&=\frac1{2\pi}\int_{-\infty}^{+\infty}X(j\omega)e^{-j\omega t}\mathrm d\omega\\
将t和\omega互换:\\
x(-j\omega)&=\frac1{2\pi}\int_{-\infty}^{+\infty}(t)e^{-j\omega t}\mathrm dt\\
&=\frac{1}{2\pi}\mathcal{F}[X(t)]
\end{aligned}
$$

如果$x(t)$是偶信号，则有

$$
\mathcal{F}[X(t)]=2\pi x(j\omega)
$$

## 展缩特性

我们考察展缩后的时域信号在傅里叶变换后的频域信号:

$$
\begin{aligned}
\mathcal{F}[x(at)]
&=\int_{-\infty}^{+\infty}x(at)e^{-j\omega t}\mathrm dt\\
&=\frac{1}{\vert a\vert}\int_{-\infty}^{+\infty}x(at)e^{-\frac{j\omega}{a}\cdot a t}\mathrm d(at)\\
&=\frac1{\vert a\vert}X(j\frac{\omega}{a})
\end{aligned}
$$

也就是，时域压缩则频域拉伸，反之亦然.

## 时移特性

考察时移后的时域信号在傅里叶变换后的频域信号:

$$
\begin{aligned}
\mathcal{F}[x(t-t_0)]
&=\int_{-\infty}^{+\infty}x(t-t_0)e^{-j\omega t}\mathrm dt\\
&=\int_{-\infty}^{+\infty}x(t-t_0)e^{-j\omega(t-t_0)}e^{-j\omega t_0}\mathrm dt\\
&=e^{-j\omega t_0}\int_{-\infty}^{+\infty}x(t-t_0)e^{-j\omega(t-t_0)}\mathrm d(t-t_0)\\
&=e^{-j\omega t_0}X(j\omega)
\end{aligned}
$$

## 频移特性

类似的，考察平移后的频域信号在傅里叶逆变换后的表现:


$$
\begin{aligned}
\mathcal{F}^{-1}[X(j(\omega-\omega_0))]
&=\frac{1}{2\pi}\int_{-\infty}^{+\infty}X(j(\omega-\omega_0))e^{j\omega t}\mathrm d\omega\\
&=\frac{1}{2\pi}\int_{-\infty}^{+\infty}X(j(\omega-\omega_0))e^{j(\omega-\omega_0)t}e^{j\omega_0t}\mathrm d\omega\\
&={e^{j\omega_0t}}x(t)\\
\end{aligned}
$$

## 时域卷积特性

对于傅里叶变换，我们有：时域的卷积等于频域的乘积. 证明：

$$
\begin{aligned}
\mathcal{F}[x_1(t)*x_2(t)]
&=\mathcal{F}[\int_{-\infty}^{+\infty}x_1(\tau)x_2(t-\tau )\mathrm d\tau]\\
&=\int_{-\infty}^{+\infty}\bigg(\int_{-\infty}^{+\infty}x_1(\tau)x_2(t-\tau )\mathrm d\tau\bigg)e^{-j\omega t}\mathrm dt\\
&=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x_1(\tau)x_2(t-\tau)e^{-j\omega t}\mathrm dt\mathrm d\tau\\
&=\int_{-\infty}^{+\infty}x_1(\tau)\int_{-\infty}^{+\infty}x_2(t-\tau)e^{-j\omega t}\mathrm dt\mathrm d\tau\\
&=\int_{-\infty}^{+\infty}x_1(\tau)X_2(j\omega)e^{-j\omega\tau}\mathrm d\tau\\
&=X_2(j\omega)\int_{-\infty}^{+\infty}x_1(\tau)e^{-j\omega\tau}\mathrm d\tau\\
&=X_1(j\omega)X_2(j\omega)
\end{aligned}
$$

## 频域卷积特性

对于傅里叶变换，我们还有：频域的卷积**正比于**时域的乘积. 证明：

$$
\begin{aligned}
\mathcal{F}^{-1}[X_1(j\omega)*X_2(j\omega)]
&=\frac{1}{2\pi}\int_{-\infty}^{+\infty}X_1(j\omega)*X_2(j\omega)\cdot e^{j\omega t}\mathrm d\omega\\
&=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}X_1(j\omega_0)X_2(j(\omega-\omega_0))\mathrm d \omega_0\cdot e^{j\omega t}\mathrm d\omega\\
&=\frac1{2\pi}\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}X_1(j\omega_0)X_2(j(\omega-\omega_0))e^{j\omega t}\mathrm d\omega_0\mathrm d\omega\\
&=\int_{-\infty}^{+\infty}X_1(j\omega_0)\bigg(\frac1{2\pi}\int_{-\infty}^{+\infty}X_2(j(\omega-\omega_0))e^{j\omega t}\mathrm d\omega\bigg)\mathrm d\omega_0\\
&=\int_{-\infty}^{+\infty}X_1(j\omega_0)x_2(t)e^{j\omega_0t}\mathrm d\omega_0\\
&=x_2(t)\int_{-\infty}^{+\infty}X_1(j\omega_0)e^{j\omega_0t}\mathrm d\omega_0\\
&=2\pi\;x_1(t)x_2(t)
\end{aligned}
$$

**注意到频域卷积和时域乘积之间有一个比例系数**$2\pi$.

## 时域微分特性

我们考虑时域信号对时间微分后的傅里叶变换:

$$
\begin{aligned}
x(t)
&=\frac1{2\pi}\int_{-\infty}^{+\infty}X(j\omega)e^{j\omega t}\mathrm d\omega\\
\dfrac{\mathrm dx(t)}{\mathrm dt}
&=\dfrac{\mathrm d}{\mathrm dt}\frac1{2\pi}\int_{-\infty}^{+\infty}X(j\omega)e^{j\omega t}\mathrm d\omega\\
&=\frac1{2\pi}\int_{-\infty}^{+\infty}X(j\omega)\frac{\mathrm de^{j\omega t}}{\mathrm dt}\mathrm d\omega\\
&=\frac1{2\pi}\int_{-\infty}^\infty j\omega X(j\omega)e^{j\omega t}\mathrm d\omega\\
&=\mathcal{F}[j\omega X(j\omega)]\\
\mathcal{F}[\dfrac{\mathrm dx(t)}{\mathrm dt}]&=j\omega X(j\omega)
\end{aligned}
$$

我们可以进一步推导出$n$阶微分下的傅里叶变换:

$$
\begin{aligned}
\dfrac{\mathrm d^nx(t)}{\mathrm dt^n}
&=\frac{1}{2\pi}\int_{-\infty}^{+\infty}X(j\omega)\frac{\mathrm d^ne^{j\omega t}}{\mathrm dt^n}\mathrm d\omega\\
&=\mathcal{F}[(j\omega)^nX(j\omega)]\\
\mathcal{F}[\dfrac{\mathrm d^nx(t)}{\mathrm dt^n}]&=(j\omega)^nX(j\omega)
\end{aligned}
$$

## 频域微分特性

类似的，我们也可以考虑频域信号对频率微分下的傅里叶变换:

$$
\begin{aligned}
X(j\omega)&=\int_{-\infty}^{+\infty}x(t)e^{-j\omega t}\mathrm dt\\
\dfrac{\mathrm d^nX(j\omega)}{\mathrm d\omega^n}&=\int_{-\infty}^{+\infty}x(t)\frac{\mathrm de^{-j\omega t}}{\mathrm d\omega}\mathrm dt\\
&=\mathcal{F}[(-jt)^n x(t)]\\
&=(-j)^n\mathcal{F}[t^n x(t)]\\
j^n\dfrac{\mathrm d^nX(j\omega)}{\mathrm d\omega^n}&=\mathcal{F}[t^n x(t)]
\end{aligned}
$$
