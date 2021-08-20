---
layout:     post
title:      泛函分析论
subtitle:   有界线性算子和连续线性泛函
date:       2021-05-22
author:     Welt Xing
header-img: img/functional.png
catalog:    true
tags:
    - 数学
---

## <center>引言

我们这里会讨论算子，泛函等概念，在此先做一个浅显的介绍。我们之前将“空间”概念从点的集合扩展到函数的集合：只要定义了一个距离就可以生成一个空间，由此引出赋范线性空间，巴拿赫空间等概念。这里，我们将赋范线性空间$X$到赋范线性空间$Y$的映射称作**算子**；如果$Y$是数域，那么则称这个映射为**泛函**。举两个例子，微分算子$D=\dfrac{\mathrm{d}}{\mathrm{d}x}$就是从连续可微函数空间$C[a,b]$到$C[a,b]$的算子；而黎曼积分$\displaystyle\int_a^bf(t)\mathrm{d}t$就是连续函数空间上的泛函。简单地说，函数是数与数之间的对应，算子则是函数与函数间的对应。

## <center>有界线性算子和连续线性泛函

### 线性算子和线性泛函

**定义1** 如果$X,Y$是两个同为实（复）的线性空间，$\mathscr{D}$是$X$的线性子空间，$T$是$\mathscr{D}\to Y$的映射，$\forall x,y\in\mathscr{D},\alpha\in\mathbb{R}$:

$$
\begin{cases}
T(x+y)=Tx+Ty\\
T(\alpha x)=\alpha Tx
\end{cases}
$$

则称$T$为$\mathscr{D}\to Y$的**线性算子**，$\mathscr{D}$为$T$的定义域，记为$\mathscr{D}(T)$，$T\mathscr{D}$为值域，记为$\mathscr{R}(T)$，$T$取值于实/复数域时则被称为实/复线性泛函。我们定义

$$
\mathscr{N}(T)=\{x:Tx=0\vert x\in\mathscr{D}(T)\}
$$

为算子$T$的零空间.

#### 例子

1. 设$X$是线性空间，$\alpha$是一个给定的数，令$Tx=\alpha x$，显然$T$是$X\to X$的线性算子，称为**相似算子**，$\alpha=1$：恒等算子，$\alpha=0$：零算子，记为$O$.
2. 定义$[0,1]$上的多项式全体$\mathscr{P}[0,1]$,$\forall x\in\mathscr{P}[0,1],定义(Tx)(t)=\dfrac{\mathrm{d}}{\mathrm{d}t}x(t)$，，可知$T$也是线性算子，称作微分算子。如果指定$t0$，则是线性泛函。
3. 对任意$x\in C[a,b]$，定义$(Tx)(t)=tx(t)$，这也是线性算子，称作乘法算子。

### 有界线性算子和连续线性泛函

**定义2**：承接上面线性算子定义，如果存在常数$c$，对任意$x\in\mathscr{D}(T)$有

$$
\|Tx\|\leqslant c\|x\|
$$

则称T是定义域上的**有界线性算子**，当定义域等于$X$时，称$T$是$X\to Y$的有界线性算子，简称有界算子，如果不存在这样的$c$则是无界算子。

**定理1**：承接线性算子定义，$T$为有界算子的充要条件是$T$是$X$上的连续算子。
**定理2**：设$X$是赋范线性空间，$f$是$X$上的线性泛函，那么$f$是其上的连续泛函的充要条件是$f$的零空间是$X$中的闭子空间。

**定义3**：我们称

$$
\|T\|=\sup_{x\neq 0,x\in\mathscr{D}(T)}\dfrac{\|Tx\|}{\|x\|}
$$

为算子$T$在$\mathscr{D}(T)$上的**范数**。

**引理**：设$T$是有界线性算子，那么

$$
\|T\|=\sup_{x\in\mathscr{D}(T),\|x\|=1}\|Tx\|=\sup_{x\in\mathscr{D}(T),\|x\|\leqslant1}\|Tx\|
$$

#### 例子

设$X\in C[0,1],K[t,\tau]$是矩形域$[0,1]^2$上的二元连续函数，则对每一个$x\in C[0,1]$，定义

$$
(Tx)(t)=\int_0^1K(t,\tau)x(\tau)\mathrm{d}\tau
$$

易知$T$是$C[0,1]\to C[0,1]$的线性算子，称作**积分算子**，函数$K(t,\tau)$称作$T$的**核**。因为

$$
|x(t)|\leqslant\max_{0\leqslant t\leqslant1}|x(t)|=\|x\|
$$

所以

$$
\begin{aligned}
\|Tx\|&=\max_{t\in[0,1]}|\int_0^1K(t,\tau)x(\tau)\mathrm{d}\tau|\\
&\leqslant\max_{t\in[0,1]}\int_0^1|K(t,\tau)||x(\tau)|\mathrm{d}\tau\\
&\leqslant\max_{t\in[0,1]}\int_0^1|K(t,\tau)|\mathrm{d}\tau\cdot\|x\|
\end{aligned}
$$

从而算子有界的，如果记

$$
M=\max_{t\in[0,1]}\int_0^1|K(t,\tau)|\mathrm{d}\tau
$$

则显然有$\|T\|\leqslant M$. 现在想证明范数就是$M$，那么我们需要找到一列$x_n\in C[0,1]$，使得$\|x_n\|\leqslant1$并且$\|Tx\|\to M(n\to\infty)$，因为这个含参变量积分连续，所以存在一个$t_0$使得这个积分在此处最，也就是

$$
\int_0^1|K(t_0,\tau)|\mathrm{d}\tau=M
$$

设$x(\tau)$是$K(t_0,\tau)$的符号函数，那么$x(\tau)$在$[0,1]$可测，并且$\sup_{\tau\in[0,1]}\vert x(\tau)\vert\leqslant1$，由卢津定理，$\forall n\in\mathbb{N},\exists x_n\in C[0,1],\Vert x_n\Vert\leqslant1$，使得除去$[0,1]$中一个测度小于$\dfrac{1}{2nL}$的集合$E_n$外都有$x_n(\tau)=x(\tau)$，其中$L=\max_{[t,\tau]\in[0,1]^2}\vert K(t,\tau)\vert$.

因为对所有$[0,1]$上的$t$，都有

$$
\begin{aligned}
\vert\int_0^1K(t,\tau)x(\tau)\mathrm{d}\tau\vert
&\leqslant\int_0^1|K(t,\tau)||x(\tau)-x_n(\tau)|\mathrm{d}\tau+\bigg\vert\int_0^1K(t,\tau)x_n(t,\tau)\bigg\vert\\
&=\int_0^1|K(t,\tau)||x(\tau)-x_n(\tau)|\mathrm{d}\tau+|Tx_n(t)|\\
&\lt L\cdot2\cdot\dfrac{1}{2nL}+\|Tx_n(t)\|\\
&\leqslant \dfrac{1}{n}+\|T\|
\end{aligned}
$$

特别的，当$t\gets t_0$，$M\lt\dfrac{1}{n}+\Vert T\Vert$. 取极限，$M\leqslant\Vert T\Vert$，从而$M=\Vert T\Vert$.

再举一个无界算子的例子：上一节的$\mathscr{P}[0,1]$和微分算子，空间范数继承了$C[0,1]$，令$x_n(t)=t^n,\|x_n\|=1$，但$\|Tx_n\|=\max_{t\in[0,1]}\vert nt^{n-1}\vert=n$，所以$\Vert T\Vert\geqslant\Vert Tx_n\Vert=n$.

## <center>有界线性算子空间和共轭空间

### 有界线性算子全体所成空间

设两个赋范线性空间$X,Y$，设$\mathscr{B}(X,Y)$表示$X\to Y$的有界线性算子的全体，并用$\mathscr{B}(X)$表示$\mathscr{B}(X,X)$. 当$A,B\in\mathscr{B}(X,Y),\alpha$为所讨论数域内的数的时候，我们定义$\mathscr{B}(X,Y)$中的加法和数乘：$\forall x\in X$

$$
\begin{cases}
(A+B)x=Ax+Bx\\
(\alpha A)x=\alpha Ax
\end{cases}
$$

我们可以证明（略），加法和数乘运算，加上我们之前定义的算子范数，$\mathscr{B}(X,Y)$是赋范线性空间。

**定理1**：当$Y$是巴拿赫空间时，$\mathscr{B}(X,Y)$也是巴拿赫空间。

设$A\in\mathscr{B}(Z,Y),B\in\mathscr{X,Z}$，令

$$
(AB)x=A(Bx),x\in X
$$

显然$AB$是线性算子，称为$B$与$A$的乘积，$AB\in\mathscr{B}(X,Y)$.

### 共轭空间

**定义1**：设$X$是赋范线性空间，令$X'$为$X$上连续线性泛函全体所成的空间，称为$X$的**共轭空间**.

由于实数域和复数域完备，由定理一推出：

**定理2**：任何赋范线性空间的共轭空间一定是巴拿赫空间。

**定义2**：两个赋范线性空间$X,Y$，$T$是$X\to Y$的算子，并且$\forall x\in X$:

$$
\|Tx\|=\|x\|
$$

则称$T$是$X\to Y$的保距算子，如果$T$又是映射到$Y$上的(?)，则称$T$是同构映射，此时称$X$与$Y$同构。

## 有限秩算子

**定义**：设$X,Y$是巴拿赫空间，$T\in\mathscr{B}(X,Y)$. 如果$\mathscr{R}(T)$是一个有限维的子空间，则称$T$是一个**有限秩算子**.

记$\mathscr{F}(X,Y)$为$\mathscr{B}(X,Y)$中的有限秩算子全体，并记$\mathscr{F}(X)=\mathscr{F}(X,X)$.

**定理1**：设$X$是巴拿赫空间，$S,T\in\mathscr{F}(X),A\in\mathscr{B}(X)$，则$\mathscr{F}(X)$是$\mathscr{B}(X)$的一个理想，即

$$
S+T\in\mathscr{F}(X),AS,SA\in\mathscr{F}.
$$

后面的定理过于艰深，在此省略.