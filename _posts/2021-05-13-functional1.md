---
layout:     post
title:      泛函分析论
subtitle:   度量空间和赋范线性空间
date:       2021-05-13
author:     Welt Xing
header-img: img/functional.png
catalog:    true
tags:
    - 数学
---

## 度量空间

我们复习度量空间：设$X$是一个集合，若对于$X$中任意两个元素$x,y$，都有唯一确定的实数$d(x,y)$与之对应，而且这一对应关系满足下列条件：

1. $d(x,y)\geqslant0,d(x,y)=0\leftrightarrow x=y$;
2. $d(x,y)\leqslant d(x,z)+d(y,z)$;

则称$d(x,y)$是$x,y$的距离，称$(X,d)$为**度量空间**或**距离空间**. $X$中元素称为点，条件2为**三点不等式**.

## 度量空间的进一步例子

#### 离散的度量空间

设$X$为任意的非空集合，对$X$中任意两点$x,y\in X$,令

$$
d(x,y)=\begin{cases}
1,x\neq y\\
0,x=y
\end{cases}
$$

#### 序列空间

令$S$表示实数列或复数列的全体，对$S$中任意两点$x=(\xi_1,\xi_2,\cdots,\xi_n,\cdots)$及$y=(\eta_1,\eta_2,\cdots,\eta_n,\cdots)$，令

$$
d(x,y)=\sum_{i=1}^\infty\dfrac{1}{2^i}\dfrac{\vert\xi_i-\eta_i\vert}{1+\vert\xi_i-\eta_i\vert}
$$

#### 有界函数空间

$B(A)$表示$A$上有界实值函数全体，对$B(A)$中任意两点定义

$$
d(x,y)=\sup_{t\in A}|x(t)-y(t)|
$$

#### 可测函数空间

设$X$是$\mathrm{R}^n$中$L$-可测子集. $\mathscr{M}(X)$为其上实值的$L$可测函数全体，$m$为$L$测度，若$m(X)\lt\infty$，对任意两个可测函数$f(t)$和$g(t)$，由于

$$
\dfrac{|f(t)-g(t)|}{1+|f(t)-g(t)|}<1
$$

所以是$X$上可测函数，令

$$
d(f,g)=\int_X\dfrac{|f(t)-g(t)|}{1+|f(t)-g(t)|}\mathrm{d}t
$$

#### $C[a,b]$空间

$C[a,b]$是闭区间$[a,b]$上的实值连续函数全体，对其中任意两点$x,y$定义

$$
d(x,y)=\max_{a\leqslant t\leqslant b}|x(t)-y(t)|
$$

#### $l^2$

记$l^2=\\{x=\\{x_k\\}:\sum_{k=1}^\infty x_k^2<\infty\\}$，设$x=\{x_k\}\in l^2,y=\{y_k\}\in l^2$，定义

$$
d(x,y)=\bigg[\sum_{k=1}^\infty(y_k-x_k)^2\bigg]^{\frac{1}{2}}
$$

## 度量空间的极限、稠密集和可分空间

设$(X,d)$为度量空间，$d$是距离，定义

$$
U(x_0,\varepsilon)=\{x\in X:d(x,x_0)<\varepsilon\}
$$

为$x_0$为半径的开球，亦称$x_0$的$\varepsilon$-邻域.

仿照我们在欧式空间的收敛点列，极限，我们将其扩展到度量空间，其实就是$d$的收敛. 我们将

$$
\delta(M)=\sup_{x,y\in M}d(x,y)
$$

定义为点集$M$的直径. 如果直径有限则$M$为$(X,d)$的有界集.

**定义**：设$X$是度量空间，$E,M$是$X$中两个子集，令$\overline{M}$表示$M$的闭包，如果$E\subset\overline{M}$，则称$M$在$E$中**稠密**，当$E=X$时称$M$为$X$的一个稠密子集。如果$X$有一个可数的稠密空间，则称$X$为**可分空间**.($\mathbb{R}^n$便是一个可分空间，全体有理数便是其可数稠密子集).

## 连续映射

**定义**：设$X=(X,d),Y=(Y,\tilde{d})$是两个度量空间，$T$是$X$到$Y$的映射,$x_0\in X$, 如果对于任意给定的正数$\varepsilon$, 存在正数$\delta$，使得对$X$中任意满足$d(x,x_0)\lt\delta$的$x$都有

$$
\tilde{d}(Tx,Tx_0)\lt\varepsilon
$$

则称$T$在$x_0$连续.

> 其实就是我们所学的函数在定义域上的扩充.

**定理1**：设$T$是度量空间$(X,d)\to(Y,\tilde{d})$的映射，那么$T$在$x_0\in X$连续的充要条件为当$x_n\to x_0(n\to\infty)$时必有$Tx_n\to Tx_0(n\to\infty)$.

如果映射$T$在$X$上的每一点都连续，则称其为$X$上的**连续映射**. 称集合

$$
\{x\in X:Tx\in M\subset Y\}
$$

为集合$M$在映射$T$下的原像，简记为$T^{-1}M$.

**定理2**：度量空间$X\to Y$的映射$T$是$X$上连续映射的充要条件是$Y$中任意开集$M$的原像$T^{-1}M$是$X$中的开集.

> 上面的开集改成闭集，结论仍然成立.

## 柯西点列和完备度量空间

**定义**：设$X=(X,d)$是度量空间，$\\{x_n\\}$是$X$中点列，如果对任意给定的正数$\varepsilon>0$，存在正整数$N=N(\varepsilon)$，当$n,m>N$时，必有

$$
d(x_n,x_m)\leqslant\varepsilon
$$

则称$\\{x_n\\}$为$X$中的柯西点列和基本点列，如果$(X,d)$中的每一个柯西点列都在$(X,d)$中收敛，那么称其为**完备的度量空间**.

> 可以知道有理数全体按绝对值构成的度量空间是不完备的，但$\mathbb{R}^n$完备. 在一般度量空间中，柯西点列不一定收敛，但在度量空间中每一个收敛点列都是柯西点列.

**定理**：完备度量空间$X$的子空间$M$是完备空间的充要条件为$M$是$X$中的闭子空间.

## 度量空间的完备化

**定义**：设$(X,d),(\tilde{X},\tilde{d})$是两个度量空间，如果存在$X$到$\tilde{X}$上的保距映射，即$\tilde{d}(Tx,Ty)=d(x,y)$，则称$(X,d)$与$(\tilde{X},\tilde{d})$**等距同构**. 此时称$T$为$X\to X'$的等距同构映射.

定理1（**度量空间的完备化定理**） 设$X=(X,d)$是度量空间，那么一定存在一完备度量空间$\tilde{X}=(\tilde{X},\tilde{d})$，使得$X$与$\tilde{X}$的某个稠密子空间$W$等距同构，并且$\tilde{X}$在等距同构意义下是唯一的，即若$(\hat{X},\hat{d})$也是一完备度量空间，且$X$与$\hat{X}$的某个稠密子空间等距同构，则$(\hat{X},\hat{d})$与$(\tilde{X},\tilde{d})$等距同构.

定理1’：设$X=(X,d)$是度量空间，那么存在唯一的完备度量空间$(\tilde{X},\tilde{d})$使得$X$是$X‘$的稠密子空间.

## 压缩映射原理

定义：$T$是度量空间$X$到自身的映射，如果存在一个数$\alpha(0\lt\alpha\lt1)$，使得对所有的$x,y\in X$：

$$
d(Tx, Ty)\leqslant\alpha d(x,y)
$$

则称$T$是压缩映射.

定理1（压缩映射原理）：设$T$是$X$上的压缩映射，那么$T$有且只有一个不动点，即$Tx=x$只有一个解.

此处略去隐函数存在定理和常微分方程解的存在性和唯一性定理.

## 线性空间

定义1：在非空集合$X$中定义元素的加法运算和实数（或者复数）与$X$中元素的乘法运算，对于加法我有以下限制：

1. $x+y=y+x$;
2. $(x+y)+z=x+(y+z)$;
3. $\exists!\theta\in X,\forall x\in X,x+\theta=x,\theta$称为零元素;
4. $\forall x\in X,\exists!x'\in X,x+x'=\theta,x'$称为$x$的负元素，记为$-x$.

而对乘法我们有下面的限制：

1. $1x=x$;
2. $a(bx)=(ab)x$;
3. $(a+b)x=ax+bx,a(x+y)=ax+ay$.

则称$X$按上述加法和数乘运算成为**线性空间**或**向量**空间，其中的元素称作向量，如果数积运算只对实数（复数）有意义，则称$X$是实（复）线性空间.

> 我们把零元素$\theta$记作$0$.
> $\mathbb{R}^n$,$C[a,b]$都是线性空间

对于空间$l^p(p>0)$，设$x=(\xi_1,\xi_2,\cdots,\xi_n,\cdots)$，如果$\sum_{i=1}^\infty\vert \xi_i\vert^p<\infty$，则称$\xi$数列是**p次收敛数列**. 我们可以证明$p$次收敛数列也是线性空间.

一些相关定义：子空间，平凡子空间，真子空间，线性组合，$\text{span}$线性包，线性相关，线性无关，线性无关子集，维数，基，无限维/零维线性空间，标准积。

## 赋范线性空间和巴拿赫空间

定义1：对于线性空间的每一个向量$x\in X$，都有一个实数$\Vert x\Vert$与之对应：

1. $\Vert x\Vert\geqslant0,\Vert x\Vert=0\leftrightarrow x=0$;
2. $\Vert ax\Vert=\vert a\vert\Vert x\Vert$;
3. $\Vert x+y\Vert\leqslant\Vert x\Vert +\Vert y\Vert$.

则称$\Vert x\Vert$为向量$x$的范数，称$X$按范数$\|\cdot\|$为赋范线性空间.

对$X$中点列$\\{x_n\\}$,如存在$x$使得$\Vert x_n-x\Vert\to0(n\to\infty)$，那么称点列**依范数收敛**. 记$x_n\to x(n\to\infty)$或$\mathop{\lim}\limits_{n\to\infty}x_n=x$.

如果令

$$
d(x,y)=\|x-y\|
$$

以证范数也是距离. 赋范线性空间实际上是特殊的度量空间. 如果$d$是由$\Vert\Vert$导出的距离，那么这种距离和线性运算有以下关系：

1. $d(x-y,0)=d(x,y)$;
2. $d(\alpha x,0)=\vert\alpha\vert d(x,0)$.

完备的赋范线性空间称作**巴拿赫空间**. $\mathbb{R}^n,C[a,b],l^\infty,L^p[a,b],l^p$都是巴拿赫空间.

其中$L^p[a,b]$称作P方可积函数：$f(x),x\in[a,b],\vert f(x)\vert^p$是$[a,b]$上的可积函数. 它可以按函数通常的加分和数乘运算成为线性空间，我们接下来定义范数：

$$
\|f\|_p=\big(\int_a^b|f(t)|^p\mathrm dt\big)^\frac{1}{p}
$$

定理1：当$p\geqslant1$时$L^p[a,b]$按$\|\cdot\|_p$成为赋范线性空间.

定理2：当$p\geqslant1$时$L^p[a,b]$按$\|\cdot\|_p$成为巴拿赫空间.

定理3：设$X$是$n$维赋范线性空间$\\{e_1,e_2,\cdots,e_n\\}$是$X$的一组基，则存在常数$M,M'$使得对一切

$$
x=\sum_{i=1}^n\xi_ie_i
$$

成立

$$
M\|x\|\leqslant\big(\sum_{k=1}^n|\xi_k|^2\big)^\frac{1}{2}\leqslant M'\|x\|
$$

推论1：设在有限维线性空间上定义了两个范数$\Vert\cdot\Vert$和$\Vert\cdot\Vert_1$，那么必存在常数$M$和$M'$，使得对任意$x\in X$，有：

$$
M\|x\|\leqslant\|x\|_1\leqslant M'\|x\|.
$$

定义2：设$(R_1.\|\cdot\|_1)$和$(R_2.\|\cdot\|_2)$是两个赋范线性空间，如果存在从$R_1$到$R_2$的映射$\varphi$满足条件：对任意$x,y\in R_1$以及数$\alpha,\beta$有$\varphi(\alpha x+\beta y)=a\varphi(x)+\beta\varphi(y)$以及正数$c_1,c_2$，使得对一切$x\in R_1$有

$$
c_1\|\varphi(x)\|_2\leqslant\|x\|_1\leqslant c_2\|\varphi(x)\|_2
$$

则称两个赋范空间是**拓扑同构**的.

推论2：任何有限维赋范线性空间都和同维数欧式空间（或某个$\mathbb{C}^n$）拓扑同构. 同数域上相同维数的有限赋范空间彼此拓扑同构.
