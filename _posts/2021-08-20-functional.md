---
layout:     post
title:      泛函分析论
subtitle:   知识梳理
date:       2021-08-20
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

接下来我们会讨论算子，泛函等概念，在此先做一个浅显的介绍。我们之前将“空间”概念从点的集合扩展到函数的集合：只要定义了一个距离就可以生成一个空间，由此引出赋范线性空间，巴拿赫空间等概念。这里，我们将赋范线性空间$X$到赋范线性空间$Y$的映射称作**算子**；如果$Y$是数域，那么则称这个映射为**泛函**。举两个例子，微分算子$D=\dfrac{\mathrm{d}}{\mathrm{d}x}$就是从连续可微函数空间$C[a,b]$到$C[a,b]$的算子；而黎曼积分$\displaystyle\int_a^bf(t)\mathrm{d}t$就是连续函数空间上的泛函。简单地说，函数是数与数之间的对应，算子则是函数与函数间的对应。

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

## <center>谱的概念

这一部分是将矩阵特征值进行衍生，因此理解起来会简单一点（但还是很难！）。

考察$n$个未知数的线性方程组：

$$
\begin{cases}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=y_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=y_2\\
\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\\
a_{n1}x_1+a_{n2}x_2+\cdots+a_{nn}x_n=y_n\\
\end{cases}
$$

根据我们在线性代数中学到的，上式简化成

$$
Ax=y
$$

在这里，我们将其解释成$n$维空间$E^n$上的线性算子$A$满足$Ax=y$. 对复数$\lambda$，若存在$x\neq0$，使得$Ax=\lambda x$，则称$\lambda$为$A$的特征值。它意味着$(A-\lambda I)x=0$有非零解，即**算子$(A-\lambda I)$不存在逆算子**。因此特征值问题和$(A-\lambda I)$是否有逆算子等价。

**定义1**：设$X$是赋范线性空间，$T\in\mathscr{B}(X)$，若$T^{-1}$存在且定义在整个$X$上的有界线性算子，则称$T$是$X$上的**正则算子**。

正则算子性质：

1. $T$是正则算子$\leftrightarrow r\exists$有界算子$B\in\mathscr{B}(X):BT=TB=I$，其中$I$是恒等算子；
2. $A,B$都是正则算子$\to T=AB$也是正则算子，且$(AB)^{-1}=B^{-1}A^{-1}$.

**定义2**：设$T\in\mathscr{B},\lambda\in\mathbb{C}$. 若$(T-\lambda I)$正则，我们称$\lambda$是算子$T$的**正则点**，$T$的正则点全体称作$T$的正则集，或者是豫解集，记为$\rho(T)$，不是正则点的复数称作$T$的**谱点**，其全体构成$T$的**谱**，记为$\sigma(T)$.

**定义3**（谱的分类）：设$\lambda\in\sigma(T)$，即$T-\lambda I$不存在有界逆算子，可分三种情况：

1. 如果$T-\lambda I$不是一对一，此时存在$x\in X,x\neq0$，使得$(T-\lambda I)x=0$，即$Tx=\lambda x$，则称$\lambda$是算子T的特征值，$x$称为响应于$\lambda$的特征向量，$T$的特征值全体称为$T$的点谱，记作$\sigma(T)$;
2. $(T-\lambda I)$是一对一的，但是值域不填满全空间；
3. $(T-\lambda I)$是一对一的，但$(T-\lambda I)^{-1}$不是有界的.

其中(2),(3)类谱点合称$T$的**连续谱**，记为$\sigma_C(T)$.
