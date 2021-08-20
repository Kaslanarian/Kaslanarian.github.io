---
layout:     post
title:      泛函分析论
subtitle:   内积空间和希尔伯特空间
date:       2021-05-25
author:     Welt Xing
header-img: img/functional.png
catalog:    true
tags:
---

## <center>引言

我们之前介绍了赋范线性空间，那里只有长度（范数），但没有角度，因此也就没有内积，正交的概念了。本章就是来解决在赋范线性空间中引入角度和正交等概念。事实上希尔伯特在20世纪初便解决了这个问题，这种空间是赋范线性空间的特例，称作希尔伯特空间。

## <center>内积空间的基本概念

在复欧式空间，我们定义了两个向量的内积运算：

$$
a=(\xi_1,\xi_2,\cdots,\xi_n),b=(\eta_1,\eta_2,\cdots,\eta_n)
$$

则$a,b$内积定义为

$$
\big<a,b\big>=\sum_{i=1}^n\xi_i\bar{\eta}_i
$$

其中$\bar{\eta}_i$是$\eta_i$的复共轭。并且内积和长度有以下关系：

$$
\|a\|=\sqrt{\big<a,a\big>}
$$

内积定义告诉我们$a$正交于$b\leftrightarrow\big<a,b\big>=0$，由此在有限维复欧式空间$\mathbb{E}^n$中，内积有以下性质：

1. $\big<a,a\big>\geqslant0,\big<a,a\big>=0\leftrightarrow a=0$;
2. $\big<\alpha a+\beta b,c\big>=\alpha\big<a,c\big>+\beta\big<b,c\big>,a,b,c\in\mathbb{E}^n,\alpha,\beta\in\mathbb{C}$;
3. $\big<a,b\big>=\overline{\big<a,b\big>},a,b\in\mathbb{E}^n$.

注意上面是**复欧式空间**中的内积，我们在一般的线性空间引入内积概念：

**定义**：$X$是复线性空间，如果对$X$中任意2个向量$x,y$，友谊复数$\big<x,y\big>$与之对应并满足：

1. $\big<x,x\big>\geqslant0,\big<x,x\big>=0\leftrightarrow x=0,x\in X$;
2. $\big<\alpha x+\beta y,z\big>=\alpha\big<x,z\big>+\beta\big<y,z\big>,x,y,z\in X,\alpha,\beta\in\mathbb{C}$;
3. $\big<a,b\big>=\overline{\big<b,a\big>}a,b\in X$.

如果是$X$是式线性空间，那么3的共轭号没有意义；从内积的定义，我们有下面的等式：

$$
\big<x,\alpha y+\beta z\big>=\overline{\alpha}\big<x,y\big>+\overline{\beta}\big<x,z\big>
$$

设$X$是内积空间，令

$$
\|x\|=\sqrt{\big<x,x\big>}\tag{*}
$$

那么$\|\cdot\|$是$X$上的范数，因为不难证明$①\|x\|\geqslant0,\Vert x\Vert=0\leftrightarrow x=0;②\Vert ax\Vert=\vert a\vert\Vert x\Vert$.

接着需要证明三点不等式$\Vert x+y\Vert\leqslant\Vert x\Vert+\Vert y\Vert$，需要用到施瓦茨不等式作为引理：

**引理**（施瓦茨不等式）：设$X$按内积$\big<x,y\big>$成为内积空间，则$\forall x,y\in X$，有

$$
|\big<x,y\big>|\leqslant\|x\|\cdot\|y\|
$$

由施瓦茨不等式：

$$
\begin{aligned}
\|x+y\|^2&=\big<x+y,x+y\big>\\
&=\big<x,x\big>+\big<x,y\big>+\big<y,x\big>+\big<y,y\big>\\
&=\|x\|^2+\|y\|^2+\big<x,y\big>+\big<y,x\big>\\
&\leqslant\|x\|^2+\|y\|^2+2\|x\|\cdot\|y\|\\
&=(\|x\|+\|y\|)^2
\end{aligned}
$$

因此有三点不等式成立，此时称范数$\Vert\cdot\Vert$为由内积导出的范数，所以**内积空间是特殊的赋范线性空间**，若$X$按照*式中范数完备，则称为**希尔伯特空间**.

平行四边形公式（不难证明）：

$$
\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2)
$$

## 内积空间的例子

- $L^2[a,b]$，对其中任意向量$x,y$有
  
  $$
    \big<x,y\big>=\int_a^bx(t)\overline{y(t)}\mathrm{d}t
  $$

  因此由内积导出的范数

  $$
    \|x\|={\bigg(\int_a^b\vert x(t)\vert^2\mathrm{d}t\bigg)}^\frac{1}{2}
  $$

  这个就是$P$方可积函数$p=2$时的范数，因此推出$L^2[a,b]$就是希尔伯特空间.

- $l^2$是希尔伯特空间，$p\neq2$时$l^p$不成为希尔伯特空间.

极化恒等式：

$$
\big<x,y\big>=\dfrac{1}{4}\bigg(\|x+y\|^2-\|x-y\|^2+i\|x+iy\|^2-i\|x-iy\|^2 \bigg)
$$

它表示内积可以用它导出的范数来表示，当$X$是实内积空间，恒等式简化为

$$
\big<x,y\big>=\dfrac{1}{4}\bigg(\|x+y\|^2-\|x-y\|^2\bigg)
$$

由施瓦茨不等式，立刻发现内积其实是双变量的连续函数，即$x_n\to x,y_n\to y$时$\big<x_n,y_n\big>\to\big<x,y\big>(n\to\infty)$.

## <center>投影定理

设$X$是度量空间，$M$是$X$中的非空子集，$x\in X$，称

$$
\inf_{y\in M}d(x,y)
$$

为点到集合的距离，记为$d(x,M)$，在赋范线性空间中

$$
d(x,M)=\inf_{y\in M}\|x-y\|
$$

**定理1**（极小化向量定理）：$X$是内积空间，$M$是$X$中非空凸集，并且按$X$中内积导出距离完备，那么对每个$x\in X$，存在唯一的$y\in M$使得

$$
\|x-y\|=d(x,M)
$$

由于$X$的完备子空间必然是凸集，所以有下面的推论：

**推论**：如果$X$是内积空间，$M$是$X$的完备子空间，那么对每个$x\in X$，存在唯一的$y\in M$使得

$$
\|x-y\|=d(x,M)
$$

> 极小化向量定理是内积空间的一个基本定理.

**定义1**：$X$是内积空间，$x,y\in X$，如果

$$
\big<x,y\big>=0
$$

则称两向量“垂直”或“正交”，记为$x\perp y$，如果$A\subset X,B\subset,\forall x\in A,\forall y\in B,x\perp y$，则称$A$与$B$正交，记为$A\perp B$，特别的，当$A=\\{x\\}$时称$x$与$B$正交，记为$x\perp B$.

容易知道，勾股公式对两个正交向量成立：

$$
\|x+y\|^2=\|x\|^2+\|y\|^2
$$

有了正交概念后我们就可以建立起空间几何学。

**引理1**：设$X$是内积空间，$M$是$X$的线性子空间，$x\in X$，如果存在$y\in M$，使得$\Vert x-y\Vert=d(x,M)$，那么$x-y\perp M$.

**定义2**：设$X$是内积空间，$M$是$X$的子集，称集合

$$
M^\perp=\{x\in X:x\perp M\}
$$

为$M$在$X$中的**正交补**.

**定理2**（投影定理）：设$Y$是希尔伯特空间$X$的闭子空间，那么有

$$
X=Y\dot{+}Y^\perp
$$

这里的$\dot{+}$为是直和运算：对于线性空间$X$两个子空间$Y,Z,\forall x\in X$，存在唯一的$y\in Y,z\in Z$使得$x=y+z$，则称$X$是两个子空间的直和，记作$X=Y\dot{+}Z$.

**引理2**：设$Y$是希尔伯特空间$X$的闭子空间，则有

$$
Y=Y^{\perp\perp}
$$

**引理3**：设$M$是希尔伯特空间的非空子集，则$M$的线性包$\text{span}M$在$X$中稠密的充要条件是$M^\perp=\\{0\\}$.

## <center>希尔伯特空间中的规范正交系

这里模仿的是欧式空间中的正交坐标系，我们将其引入内积空间。

**定义1**：设$M$是内积空间$X$的一个不含零的子集，如果其中的向量两两正交，那么称$M$为$X$的正交系，如果它们的范数都是1，则称为**规范正交系**.

举个例子，在空间$L^2[a,b]$中定义内积为

$$
\big<f,g\big>=\dfrac{1}{\pi}\int_0^{2\pi}f(x)g(x)\mathrm{d}x,\qquad f,g\in L^2[a,b]
$$

则三角函数系$\\{\frac{1}{\sqrt{2}},\cos x,\sin x,\cdots,\cos nx,\sin nx,\cdots\\}$是$L^2[a,b]$的规范正交系。所以内积空间中规范正交系是对正交函数系概念的推广.

正交系具有下面的性质：

- 对于正交系中任意有限数量的向量$x_1,\cdots,x_n$有
  $$
    {\|}\sum_{i=1}^nx_i{\|}^2=\sum_{i=1}^n\|x_i\|^2
  $$
- 正交系$M$是$X$中的线性无关子集.

**定义2**：设$X$是赋范线性空间，$x_i,i=1,2,\cdots$是$X$中一列向量，$\alpha_1,\alpha_2$是一系列数，作形式级数

$$
\sum_{i=1}^\infty\alpha_ix_i
$$

称$S_n=\sum_{i=1}^n\alpha_ix_i$为上面无穷级数的$n$项部分和，如果级数收敛，称$x=\sum_{i=1}^\infty\alpha_ix_i$为级数的和.

如果这一列向量是规范正交系，$x=\sum_{i=1}^\infty\alpha_ie_i$，则对每个正整数$j$，由内积连续性：

$$
\big<x,e_j\big>=\sum_{i=1}^\infty\alpha_i\big<e_i,e_j\big>=\alpha_j
$$

所以有

$$
x=\sum_{i=1}^\infty\big<x,e_j\big>e_j.
$$

**定义3**：$M$是内积空间$X$中的规范正交系，$x\in X$，称数集

$$
\{\big<x,e\big>:e\in M\}
$$

为向量$x$关于规范正交系$M$的**傅里叶系数集**，而成$\big<x,e\big>$为$x$关于$e$的傅里叶系数.

例子：就拿我们上面$L^2[a,b]$的例子来说，$X=L^2[a,b],e_0=\frac{1}{\sqrt{2}},e_1(x)=\cos x,e_2=\sin x,\cdots,e_{2n-1}=\cos nx,e_{2n}=\sin nx,\cdots,\forall f\in L^2[0.2\pi]:$

$$
\begin{aligned}
a_0&=\dfrac{1}{\sqrt{2}\pi}\int_0^{2\pi}f(t)\mathrm{d}t=\big<f,e_0\big>,\\
a_n&=\dfrac{1}{\pi}\int_0^{2\pi}f(t)\cos nt\mathrm{d}t=\big<f,e_{2n-1}\big>,n=1,2,\cdots\\
b_n&=\dfrac{1}{\pi}\int_0^{2\pi}f(t)\sin nt\mathrm{d}t=\big<f,e_{2n}\big>,n=1,2,\cdots\\
\end{aligned}
$$

下面讨论傅里叶系数的性质：

**引理1**：设$X$是内积空间，$M$是$X$中规范正交系，从$M$中任取有限个向量$e_1,e_2,\cdots e_n$，那么有：

$$
\bigg\Vert x-\sum_{i=1}^n\big<x,e_i\big>e_i\bigg\Vert^2=\|x\|^2-\sum_{i=1}^n\vert\big<x,e_i\big>\vert^2\geqslant0\\
\bigg\Vert x-\sum_{i=1}^n\alpha_ie_i\bigg\Vert^2\geqslant\bigg\Vert x-\sum_{i=1}^n\big<x,e_i\big>e_i\bigg\Vert\\
$$

**定理1**（贝塞尔不等式）：设$\\{e_k\\}$是内积空间$X$中有限或可数规范正交系，$\forall x\in X$:

$$
\sum_{i=1}^\infty\vert\big<x,e_i\big>\vert^2\leqslant\|x\|^2
$$

如果等号成立，则称作**帕塞瓦尔等式**.

**引理2**：设$\\{e_k\\}$是希尔伯特空间$X$的可数规范正交系，那么

1. $\sum_{i=1}^\infty\alpha_ie_i$收敛$\leftrightarrow\sum_{i=1}^\infty\vert\alpha_i\vert^2$收敛；
2. 若$x=\sum_{i=1}^\infty\alpha_ie_i$则$\alpha_i=\big<x,e_i\big>,i=1,2,\cdots$,故
   $$
    x=\sum_{i=1}^\infty\big<x,e_i\big>e_i
   $$
3. $\forall x\in X,\sum_{i=1}^\infty\big<x,e_i\big>e_i$收敛.

**推论1**：设$\\{e_k\\}$是希尔伯特空间$X$的可数规范正交系，则对任何$x\in X$

$$
\lim_{n\to\infty}\big<x,e_n\big>=0
$$

**定义4**：设$M$是希尔伯特空间$X$中的规范正交系，如果

$$
\overline{\text{span }M}=X
$$

则称$M$是$X$中的**完全规范正交系**.

**定理2**：设$M$是希尔伯特空间$X$中的规范正交系，$M$完全$\leftrightarrow M^{\perp}=\\{0\\}$.

**定理3**：$M$是希尔伯特空间中完全规范正交系的充要条件是$\forall x\in X$，成立帕塞瓦尔等式.

也就是说，只要$M$是一个完全规范正交系，那么$\forall x\in X$，我们都有

$$
x=\sum_{e\in M}\big<x,e\big>e
$$

**推论2**（斯捷科洛夫定理）：设$M$是希尔伯特空间$X$中的规范正交系，如果帕塞瓦尔等式在$X$的某个稠密子集$A$上成立，则$M$完全.

**引理3**：（施密特正交化）略

**定理4**：每个非零希尔伯特空间必有完全规范正交系. 

完全规范正交系$M$的基数为$X$的**希尔伯特维数**.

**定义5**：设$X,\tilde{X}$是两个内积空间，如果存在一个$X\to\tilde{X}$的映射$T$使得$\forall x,y\in X,\alpha,\beta\in\mathbb{C}$:

$$
T(\alpha x+\beta y)=\alpha Tx+\beta Ty\\
\big<Tx,Ty\big>=\big<x,y\big>
$$

则称$X,\tilde{X}$同构，$T$为$X\to\tilde{X}$的同构映射.

**定理5**：两个希尔伯特空间$X$与$\tilde{X}$同构的充要条件是$X$与$\tilde{X}$有相同的希尔伯特维数.

**推论3**：任何可分希尔伯特空间必然和某个$\mathbb{R}^n(\mathbb{C}^n)$或$l^2$同构.

## <center>希尔伯特空间上的连续线性泛函

**定理1**：（里斯定理）设$X$是希尔伯特空间，$f$是$X$上的连续线性泛函，那么存在唯一的$z\in X$，使对每一个$x\in X$，有

$$
f(x)=\big<x,z\big>
$$

且$\Vert f\Vert=\Vert z\Vert$.

对每个$y\in X$，令$Ty=f_y$，其中$f_y$为$X$上如下定义的泛函：

$$
f_y(x)=\big<x,y\big>,x\in X
$$

> 个人理解：一个元素对应了一个连续线性泛函. 正对应里斯定理.

显然$f_y$是$X$上的连续线性泛函，并且由里斯定理，$T$是$X\to X'$的映射，其中$X'$表示由$X$上连续线性泛函全体所成的巴拿赫空间，又$\Vert Ty\Vert=\Vert y\Vert$，容易看出对任何$x,y\in X$以及任何数$\alpha,\beta$有

$$
T(\alpha x+\beta y)=\overline{\alpha}Tx+\overline{\beta}Ty
$$

事实上，对于任意$z\in X$有

$$
\begin{aligned}
T(\alpha x+\beta y)(z)
&=\big<z,\alpha x+\beta y\big>\\
&=\overline{\alpha}\big<z,x\big>+\overline{\beta}\big<z,y\big>\\
&=\overline{\alpha}Tx(z)+\overline{\beta}Ty(z)\\
&=(\overline{\alpha}Tx+\overline{\beta}Ty)(z)
\end{aligned}
$$

称满足上式的映射$T$是**复共轭线性映射**，所以映射$Ty=f_y$是$X\to X'$上保持范数不变的复共轭线性映射，称为**复共轭同构映射**，如果两希尔伯特空间间存在这样的复共轭同构映射，则称它们**复共轭同构**，并不加以区别视为同一，写成$X=X'$。因此当$X$是希尔伯特空间时，$X=X'$，即$X$是**自共轭**的.

设$X$是$n$维内积空间，$e_1,e_2,\cdots,e_n$为$X$中规范正交系，$A$为$X\to X$的线性算子，事实上$A$与$n$阶矩阵$(a_{ij})$相对应，其中$a_{ij}=\big<Ae_j,e_i\big>,i,j=1,2,\cdots,n$，令$(b_{ij})$表示矩阵$(a_{ij})$的共轭转置矩阵，即$b_{ij}=\overline{a_{ji}}$，记$(b_{ij})$对应的算子为$A^\star$，则

$$
\big<A^\star e_j,e_i\big>=b_{ij}=\overline{a_{ji}}=\overline{\big<Ae_i,e_j\big>}=\big<e_j,Ae_i\big>
$$

也就是

$$
\big<Ae_i,e_j\big>=\big<e_i,A^\star e_j\big>
$$

因此对$X$中任意向量

$$
x=\sum_{i=1}^nx_ie_i,y=\sum_{i=1}^ny_ie_i
$$

有

$$
\big<Ax,y\big>=\big<x,A^\star y\big>
$$

推广到内积空间：
**定理2**：设$X,Y$是两个希尔伯特空间，$A\in\mathscr{B}(X,Y)$，那么存在唯一的$A^\star\in\mathscr{B}(Y,X)$，使得$\forall x\in X,y\in Y$，有

$$
\big<Ax,y\big>=\big<x,A^\star y\big>
$$

并且$\Vert A\Vert=\Vert A\Vert$.

**定义**：设$A$是希尔伯特空间$X\to Y$的有界线性算子，则称定理2中的算子$A^\star$为$A$的**希尔伯特共轭算子**，或简称为共轭算子。

共轭算子有下面的性质：

1. $(A+B)^*=A^*+B^*$
2. $(\alpha A)^*=\overline{\alpha}A^*$
3. $(A^*)^*=A$
4. $\Vert A^*A\Vert=\Vert AA^*\Vert=\Vert A\Vert^2$，由此可知$A^*A=0\leftrightarrow A=0$
5. 当$X=Y,(AB)^*=B^*A^*$.
