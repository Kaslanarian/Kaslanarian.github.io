---
layout:     post
title:      实变函数论
subtitle:   知识梳理
date:       2021-08-20
author:     Welt Xing
header-img: img/math_header.jpg
catalog:    true
tags:
    - 数学
---

> 一些重要/陌生知识点的记录以供复习参考

## 集合

### 集合基础

#### 指标集

$\{A_{\alpha}:\alpha\in\Lambda\}$可以理解为`C++`中的数据结构`std::map<int, std::set<T>>`，也就是一族集合。$\Lambda$称作指标集，对应`map`的$key$集合，$A_\alpha$就是从中取出$key$为$\alpha$的集合。

习惯上$\Lambda$就是$\{1,2,3,\cdots\}$，可有限可无限。

#### 有限覆盖定理

设

$$
\{I_{\alpha}:\alpha\in\Lambda\}\tag{1}
$$

是一族开区间，那么有

$$
[a,b]\subset\mathop\cup\limits_{\alpha\in\Lambda} I_{\alpha}\to\exists\{\alpha_1,\alpha_2,\cdots,\alpha_k\}\subset\Lambda,使得[a,b]\subset\mathop\cup\limits_{i=1}^kI_{\alpha_i}\tag{2}
$$

#### 区间套定理

若:

$$
[a_n,b_n]\subset[a_{n-1},b_{n-1}]\tag{1}
$$

且

$$
\lim_{n\to\infty}(b_n-a_n)=0\tag{2}
$$

那么

$$
\exists!a\in\mathbb{R},a\in[a_n,b_n],n=1,2,3,\cdots\tag{3}
$$

即：

$$
\{a\}=\mathop{\cap}\limits_{i=1}^{\infty}[a_n,b_n]\tag{4}
$$

#### $\epsilon-N$语言向集合语言的转换

设$\{f_n(x)\}$是定义在$E$上的函数列，若$x$是使该函数列收敛于$0$的点，则：

$$
\forall\epsilon>0,\exists N\in\mathbb{N},s.t.\;\forall n\ge N,|f_n(x)|<\epsilon\tag{1}
$$

转换：

$$
\{x:\lim_{n\to\infty}f_n(x)=0\}=\mathop\cap\limits_{\epsilon\in\mathbb{R}^+}\mathop\cup\limits_{N=1}^\infty\mathop\cap\limits_{n=N}^\infty\{x:|f_n(x)|<\epsilon\}\tag{2}
$$

运用德摩根公式将上述语句取反：

$$
\{x:\lim_{n\to\infty}f_n(x)\neq0或不存在\}=\mathop\cup\limits_{\epsilon\in\mathbb{R}^+}\mathop\cap\limits_{N=1}^\infty\mathop\cup\limits_{n=N}^\infty\{x:|f_n(x)|\ge\epsilon\}\tag{3}
$$

#### 上极限和下极限

上极限的定义：

$$
\overline{\lim_{n\to\infty}}A_n=\{x:存在无穷多个A_n，使得x\in A_n\}\tag{1}
$$

等价于

$$
\overline{\lim_{n\to\infty}}A_n=\mathop\cap\limits_{N=1}^\infty\mathop\cup\limits_{n=N}^{\infty}\{x:x\in A_n\}\tag{2}
$$

下极限的定义：

$$
\liminf_{n\to\infty}A_n=\{ x:当n充分大以后都有x\in A_n\}\tag{3}
$$

等价于

$$
\mathop\cup\limits_{N=1}^\infty\mathop\cap\limits_{n=N}^{\infty}\{x:x\in A_n\}\tag{4}
$$

显然$\liminf_{n\to\infty}A_n\subset\limsup_{n\to\infty}A_n$

### 对等和基数

#### 对等关系

在集合$A$和集合$B$之间存在一个满射$\phi:A\to B$则两集合对等，此时两者有相同基数：$\overline{\overline{A}}=\overline{\overline{B}}$

## 点集

#### 聚点，内点和界点

若$E是$n$维空间的一个点集，$P_0$是其中一个定点：

* 如果存在$P_0$的某个领域$U(P_0)$，使得$U(P_0)\subset E$，则称$P_0$为$E$的**内点**；
  如果$P_0$是$E^c$的内点，那么$P_0$是$E$的**外点**；
  如果$P_0$即非$E$的内点也不是$E$的外点，则称$P_0$是$E$的**界点**或者是**边界点**。

* 如果$P_0$的任一领域都有$E$中无限多点，则称$P_0$为$E$的一个**聚点**。
  $\to$有限集无聚点；
  $\to E$之内点必是$E$之聚点，但$E$的聚点却不一定是$E$的内点，因为还可能是界点

定理：下面三个称述等价

* $P_0$是$E$的聚点；

* $\forall U(P_0),\exists P\in E\;and\;P\neq P_0$

* $\exists \{P_n\}=\{P_1,P_2,...,P_n\}(P_i\neq P_j),s.t.P_n\to P_0(n\to\infty)$

孤立点：

* $P_0\in E$但不是$E$的聚点，则称为孤立点，充要条件：$\exists U(P_0),s.t. E\cap U(P_0)=\{P_0\}$

开核，全体内点的集合：

$$
\mathring{E}=\{x:\exists U(x)\subset E\}
$$

导集，全体聚点的集合：

$$
E'=\{x:\forall U(x),U(x)\cap E\backslash\{x\}\neq\emptyset\}
$$

边界，全体边界点的集合（$\partial E$）;

闭包：$E\cup E'$，也可以写成$\overline{E}$

我们有：

$$
\overline{E}=E\cup\partial E=\mathring{E}\cup\partial E=E'\cup\{E的孤立点\}
$$

定理：

* $A\subset B\to A'\subset B',\mathring{A}\subset\mathring{B},\overline{A}\subset\overline{B}$

* $(A\cup B)'=A'\cup B'$

* 波尔查诺-维尔斯特拉斯定理：若$E$是有界无限集，则至少有一个聚点。

* 设$E\neq\emptyset,E\neq\mathbf{R}^n\to \partial{E}\neq\emptyset$

#### 开集，闭集和完备集

定义：

* 设$E\subset\mathbf{R}^n$，如果E的每一个点都是E的内点，则称E为**开集**；

* 设$E\subset\mathbf{R}^n$，如果E的每一个聚点都属于E，则称E是**闭集**；

判定条件：

* $E为开集\leftrightarrow E\subset\mathring{E}，亦即E=\mathring{E}$

* $E为闭集\leftrightarrow E'\subset E,亦即\partial E\subset E$

定理1：$\forall E\subset\mathbf{R}^n,\mathring{E}是开集,E'和\overline{E}都是闭集.$

定理2：$E$是开集，则$E^c$是闭集；$E$是闭集，则$E^c$是开集.

定理3：任意个开集的并仍是开集，有限个开集的交是开集；

定理4：任意个闭集的交仍是闭集，有限个闭集的并是闭集；

海涅-伯雷尔有限覆盖定理：设$F$是一个有界闭集，$\mathscr{M}$是一族开集$\{U_i\}_{i\in\Lambda}$，它覆盖了$F$，则$\mathscr{M}$中必存在有限多个开集$U_1.U_2,...,U_m$，它们同样覆盖了$F$

定义：设$M$是度量空间$X$中的一个集合，$\mathscr{M}$是$X$中任一族覆盖了$M$的开集，如果币可以从$\mathscr{M}$中选出有限个开集仍然覆盖$M$，则称$M$是$X$中的**紧集**.

定理：

$$
M是\mathbf{R}^n中的紧集\to M是\mathbf{R}^n中的有界闭集.
$$

定义：

* 设$E\subset\mathbf{R}^n$，如果$E\subset E'$，那么$E$就是**自密集**，也就是说，集合中每一个点都是聚点的集合是自密集，或者说没有孤立点的集合就是自密集.
  
* 设$E\subset\mathbf{R}^n$，如果$E=E'$，那么$E$就是**完备集**或**完全集**，完备集就是自密闭集，也就是没有孤立点的闭集.
  
#### 直线上开集闭集及完备集的构造

定义：设$G$是直线上开集，如果开区间$(\alpha,\beta)\subset G$，而且端点$\alpha,\beta$都不属于$G$，那么称$(\alpha,\beta)$为$G$的**构成区间**

定理（开集构造定理）：直线上任一个非空开集都可以表示成有限个或可数个互不相交的构成区间的和集.

定义：设$A$是直线上的闭集，称$A$的余集$A^c$的构成区间为$A$的**余区间**或**邻接区间**.

我们又可以得到闭集的构造如下：

定理：直线上的闭集$F$或者是全直线，或者是从直线上挖掉有限个或可数个互不相交的开区间（即$F$的余区间）所得到的集.

#### 康托尔三分集

即康托尔疏朗集.

定义：设$E\subset\mathbf{R}^n$

* $F\subset\mathbf{R}^n$，若对任意$x\in F$和任意领域$U(x)$，$U(x)\cap E\neq\emptyset$，则称$E$在$F$中**稠密**.

* 若对任意$x\in\mathbf{R}^n$和任意邻域$U(x)$，存在$U(y)\subset U(x)\cup E^c$，则称$E$是**疏朗集**或**无处稠密集**.

如有限点集或收敛可数列都是疏朗集，有理点$\mathbf{Q}^n$在$\mathbf{R}^n$中稠密

> 直观上，如果$X$中的任一点$x$可以被$A$中的点很好的逼近，则称$A$在$X$中稠密.

![康托尔集](/img/kantor.png)

性质：

* $P$是完备集（自密的闭集是完备的）

* $P$没有内点（区间集都是相互隔离的闭区间）

* $[0,1]\backslash P$是可数个互不相交的开区间，其长度为$1$:

  $$
  \sum_{n=1}^\infty\dfrac{2^{n-1}}{3^n}=1
  $$

  这导致$P$的长度只能是$0$.

* $P$的基数为$c$.

总结：**康托尔集是一个测度为0且基数为$c$的疏朗完备集。**

## 测度论

### 外侧度

定义：设$E$为$\mathbf{R}^n$中任一点集，对于每一列覆盖$E$的开区间$E\subset\mathop{\cup}\limits_{i=1}^\infty I_i$，作出它的体积总和$\mu=\sum_{i=1}^\infty\|I_i\|$（$\mu$可以是$\infty$，不同的列有不同的$\mu$），所有这一切的$\mu$组成了一个下方有界的数集，它的下确界（完全由$E$决定）称为$E$的<u>勒贝格外测度</u>，简称<u>$L$外侧度</u>或<u>外测度</u>，记为$m^*E$，即：

$$
m^*E=\inf_{E\subset\mathop{\cup}\limits_{i=1}^\infty I_i}\sum_{i=1}^\infty|I_i|.
$$

性质：

1. $m^\star E\geqslant 0$，当$E=\emptyset$时，$m^\star E=0$.

2. 设$A\subset B$，则$m^\star A\leqslant m^*B$.

3. $$
    m^*(\mathop{\cup}\limits_{i=1}^\infty A_i)\leqslant\sum_{i=1}^\infty m^*A_i
    $$（次可数可加性）

### 可测集

外侧度的优点是任何集合都有外侧度，但是外侧度只具有次可数可加性，不具有可数可加性.

我们想对外侧度$m^*$的定义域加以限制，设法在$\mathbf{R}^n$中找一个集合类$\mathscr{M}$，在$\mathscr{M}$上能够满足**测度公理**。

定义：设$E$为$\mathbf{R}^n$中的点集，如果对任意点集$T$都有

$$
m^*T=m^*(T\cap E)+m^*(T\cap E^c)
$$

则称$E$是$L$可测的，此时$E$的外测度$m^*E$就是$E$的$L$测度，记为$mE$. $L$可测集全体记为$\mathscr{M}$.

定理1：集合$E$可测的充分必要条件是$\forall A\subset E,B\subset E^c$，总有

$$
m^*(A\cup B)=m^*A+m^*B
$$

（该定理将定义进行了简化）

定理2：$S$可测的充要条件是$S^c$可测.

定理3：设$S_1,S_2$都可测，则$S_1\cup S_2$可测，并且当$S_1\cap S_2=\emptyset$时，对于任意集合$T$总有：

$$
m^*[T\cap(S_1\cup S_2)]=m^*(T\cap S_1)+m^*(T\cap S_2)
$$

（即分配律）

推论1：设$S_i(i=1,2,...,n)$都可测，则$\cup_{i=1}^n S_i$也可测，并且当集合两两互不相交时，对于任意集合$T$都有：

$$
m^*\big(T\cap(\mathop{\cup}\limits_{i=1}^nS_i) \big)=\sum_{i=1}^nm^*(T\cap S_i).
$$

定理4：设$S_1$和$S_2$都可测，则$S_1\cap S_2$可测。

推论2：设...可测，则$\cap_{i=1}^nS_i$也可测。

定理5：设$S_1$和$S_2$可测，那么$S_1\backslash S_2$可测。

定理6：设$\{S_i\}$是一列互不相交的可测集，则$\cup_{i=1}^\infty S_i$也是可测集，且：

$$
m(\mathop{\cup}\limits_{i=1}^\infty S_i)=\sum_{i=1}^\infty mS_i.
$$

（即可数可加性）

推论3：设$\{S_i\}$是一列可测集，即使相交，它们的并也是可测集合.

定理7：设$\{S_i\}$是一列可测集，它们的交也是可测集合

定理8：设$\{S_i\}$是一列递增的可测集：

$$
S_1\subset S_2\subset\cdots\subset S_n\subset\cdots,
$$

令$S=\cup_{i=1}^\infty S_i=\lim_{n\to\infty}S_n$，则：

$$
mS=\lim_{n\to\infty}mS_n
$$

定理9：设$\{S_i\}$是一列递降的可测集：

$$
S_1\supset S_2\supset...\supset S_n\supset ...,
$$

令$S=\cup_{i=1}^\infty S_i=\lim_{n\to\infty}S_n$，则当$mS_1<\infty$时：

$$
mS=\lim_{n\to\infty}mS_n.
$$

注意这里$mS_1<\infty$，也就是：

测度有限不一定集合有界，但集合有界必有测度有限。

### 可测集类

背景：我们已经定义了可测集合，但哪些集合是可测的我们不知道。

定理1：

* 凡外侧度为零之集皆可测，称为**零刻度集**；

* 零测度集之任何子集仍为零测度集；

* 有限个或可数个零测度集之和集仍未零测度集.

> 第三点类似与无穷级数：$\sum_{i=1}^\infty0=0$在可数无穷成立，但不可数无穷不然。

定理2：区间$I$（不论开，闭或半开半闭区间）都是可测集合，且$mI=\|I\|$.

定理3：凡开集，闭集皆可测（表示为区间之并）

定义1：设$\varOmega$是由$\mathbf{R}^n$的一些子集类组成的集合类，如果$\varOmega$满足条件：

1. $\emptyset\in\varOmega$.

2. 若$E\in\varOmega$，则$E^c\in\varOmega$.

3. 若$E_n\in\varOmega,n=1,2,...,$则

    $$
    \mathop{\cup}\limits_{n=1}^\infty E_n\in\varOmega
    $$

则称$\varOmega$是$\mathbf{R}^n$的一个$\sigma$代数.

我们可以发现$\mathbf{R}^n$中可测集全体所成的集合类$L_n$是一$\sigma$代数.

定义2：设$\varOmega$是$\mathbf{R}^n$上的一个$\sigma$代数，如果定义在$\varOmega$上的一个非负值集合函数$\mu$满足：

1. $\mu(\emptyset)=0$

2. 若$E_n\in\varOmega,n=1,2,...,$且任意$n\neq m$，$E_n\cap E_m=\emptyset$，有

  $$
  \mu(\mathop{\cup}\limits_{n=1}^\infty E_n)=\sum_{n=1}^\infty\mu(E_n)
  $$

则称$\mu$是$\varOmega$上的正测度.

所以我们可以说：勒贝格测度$m$是定义在$\sigma$代数$L$上的测度.

定义3：设$\varSigma$是$\mathbf{R}^n$的一个子集族，则称所有包含$\varSigma$的$\sigma$代数的交集为$\Sigma$产生的$\sigma$代数.

定义4：当上述$\varSigma$为$\mathbf{R}^n$中全体子集组成的子集类，则记为$\mathscr{B}$，称为伯雷尔代数.

定理4：凡伯雷尔集都是勒贝格可测集.

定义5：若$\varOmega$是$\mathbf{R}^n$上的一个$\sigma$代数，$\mu$是$\varOmega$上的测度，则称$(\mathbf{R}^n,\Omega,\mu)$为**测度空间**.

定义6：设集合$G$可以表示称一系列开集的交：

$$
G=\mathop{\cap}\limits_{i=1}^\infty G_i
$$

则称$G$为$G_\delta$型集；

设集合$F$可以表示称一系列闭集的并：

$$
F=\mathop{\cup}\limits_{i=1}^\infty F_i
$$

则称$F$为$F_\sigma$型集.

> 以上两者都是伯雷尔集

定理5：设$E$是任意可测集，则一定存在$G_\delta$型集$G$，使得$G\supset E$，且$m(G\backslash E)=0$

定理6：设$E$是任一可测集，则一定存在$F_\sigma$型集$F$，使得$F\subset E$，且$m(E\backslash F)=0$

定理7：若$E$是一个可测集，则：

1. $mE=\inf\{mG:G是开集，E\subset G\}$（外正规性）

2. $mE=\sup\{mK:K是紧集，K\subset E\}$（内正规性）

> 区间都是可测的，但集合不一定

## 可测函数

我们考虑一种新的积分，是将横轴进行切割：

$$
A=y_0\lt y_1\lt y_2\lt\cdots\lt y_n=B,
$$

然后考虑积分和

$$
\sum_{i=1}^nf(\xi)i)mE_i
$$

的极限，其中$E_i$由函数值落在区间$[y_{i-1},y_i]$中那些$x$组成。于是我们要研究的函数必须使得集合

$$
E_i=\{x\in[a,b]:y_{i-1}\le f(x)\lt y_i\}
$$

都是可测集，本章中我们称这样的函数为可测函数，并研究它的性质.

### 可测函数及其性质

有界和有限：函数值都是有限实数（$-\infty<a<\infty$）的函数都是有限函数，有界函数必是有限函数，反之不真.

在这里，不同于数学分析，$(\pm\infty)-(\pm\infty),(\pm\infty)+(\mp\infty),\frac{\pm\infty}{\pm\infty}$,包括除以零都认为是**无意义**的.

我们将$\{x:x\in E,f(x)>a\}$简记为$E[f>a]$，以此我们有定义1：

定义1：设$f(x)$是定义在可测集$E\subset\mathbb{R}^n$上的实函数，如果

$$
\forall a<\infty,E[f>a]可测
$$

则城$f(x)$是$E$上的可测函数.

定理1：可测的充要条件：

1. $\forall a<\infty,E[f\ge a]$可测；
2. $\forall a<\infty,E[f<a]$可测；
3. $\forall a<\infty,E[g\le a]$可测；
4. $\forall a<b<\infty,E[a\lt f\le a]$可测.(充分性要假定$f(x)$是有限函数)

推论：设$f(x)$在$E$上可测，则$E[f=a]$总可测，不管$a$是有限实数还是无穷.

定义2：$y_0=f(x_0)<\infty,\forall\varepsilon>0, V=[y_0-\varepsilon,y_0+\varepsilon],\exists \delta>0,U=[x_0-\delta,x_0+\delta],f(U\cap E)\subset V$，则称$f(x)$在$E$上**连续**.

> 一个函数的每一个孤立点都是连续的.

定理2：可测集$E\subset\mathbb{R}^n$上的连续函数都是可测函数.

定理3：

1. $f(x)$是可测集$E$上的可测函数，则$f(x)$看做$E$子集上的函数式，他是$E_1$上的可测函数；
2. $f(x)$定义在有限个可测集的并集$E=\mathop{\cup}\limits_{i=1}^{s}E_i$上，且$f(x)$在每个子集上都可测，那么$f(x)$在$E$上可测.

定义3：$E$上的可测函数$f(x)$为**简单函数**当且仅当：

1. $E=\mathop{\cup}\limits_{i=1}^sE_i$;
2. $E_{i}\cap E_{j}=\emptyset,(i\neq j;0<i,j\lt s$;
3. $f(x)=c_i,x\in E_i$.

> 显然，$[0,1]$上的狄利克雷函数就是就是简单函数.
> 简单函数必可测，因此狄利克雷函数可测**但不连续**.

定理4：$f(x),g(x)$在$E$上可测，则下列函数皆可测：

$f(x)+g(x),\vert f(x)\vert,\dfrac{1}{f(x)},f(x)\cdot g(x)$.

定理5：设$\{f_n(x)\}$是$E$上的可测函数列，那么$\mu(x)=\inf_{n}f_n(x)$与$\lambda(x)=\sup_{n}f_n(x)$都可测.

定理6：设$\{f_n(x)\}$是$E$上的可测函数列，则$F(x)=\underline{\lim}f_n(x)$和$G(x)=\overline{\lim}f_n(x)$也在$E$上可测，如果$F(x)=\lim_nf_n(x)$存在时，那么它也可测.

**定理7**：（可测函数与简单函数之间的关系）

1. 如果$f(x)$在$E$上非负可测，则存在可测的简单函数列$\{\varphi_k(x)\}$，使得对任意的$x\in E,\varphi_k(x)\le\varphi_{k+1}(x)$，且$\lim_{k\to\infty}\varphi_k(x)=f(x)$(逐点收敛).
2. 如果$f(x)$在$E$上可测，则存在可测的简单函数列$\{\phi_k(x)\}$，使得对于任意的$x\in E$，$\lim_{k\to\infty}\varphi_k(x)=f(x)$，如果$f(x)$还在$E$上有界，上述收敛就是**一致**的.

定义4：设$\pi$是一个与集合$E$的点$x$有关的命题，如果存在$E$的子集$M$，满足$mM=0$（零测集），使得$\pi$在$E\backslash M$恒成立（差了一个零测集成立），那么我们称$\pi$在$E$上**几乎处处成立**，也写为$\pi\text{ a.e. }$于$E$.

> 我们可以说狄利克雷函数$D(x)=0\text{ a.e.}$于$[0,1]$.

### 叶戈罗夫定理

定理（叶戈罗夫定理）：设$mE\lt\infty$,$\{f_n\}$是$E$上一列$\text{a.e.}$收敛于一个$\text{a.e.}$有限的函数$f$的可测函数,则$\forall\delta>0,\exists E_\delta\subset E$, 使得$\{f_n\}$在$E_\delta$上**一致收敛**, 且$m(E\backslash E_\delta)<\delta$.

这个定理告诉我们，凡是满足定理假设的$\text{a.e.}$收敛的可测函数列，即使不一致收敛，也是“基本上”（去掉一个测度可以任意小的某点集）一致收敛的.

> 当$mE=\infty$时，定理不成立，而逆定理$mE\le\infty$成立.

### 可测函数的构造

定理1（卢津定理）：设$f(x)$是$E$上$\text{a.e.}$有限的可测函数，则$\forall\delta>0,\exists$闭子集$F_\delta\subset E$，使$f(x)$在$F_\delta$上是连续函数，且$m(E\backslash F_\delta)<\delta$.

> 连续必可测，可测不一定连续.

另一种形式的卢津定理：

**定理2**：设$f(x)$是$E\subset\mathbb R$上几乎处处有限的可测函数，则$\forall\delta>0$，存在闭集$F\subset E$及整个$\mathbb{R}$上的连续函数$g(x)$使得在$F$上$g(x)=f(x)$，且$m(E\backslash F)<\delta$. 此外还可以要求：

$$
\mathop{\sup}\limits_{\mathbb R}g(x)=\mathop{\sup}\limits_{F}f(x),\mathop{\inf}\limits_{\mathbb R}g(x)=\mathop{\inf}\limits_{F}f(x).
$$

### 依测度收敛

定义：设$\{f_n\}$是$E\subset\mathbb{R}^q$上的一列$\text{a.e.}$有限的可测函数，若有$E$上$\text{a.e.}$有限的可测函数$f$满足下列关系：

$$
\forall\sigma>0,\mathop{\lim}\limits_{n}mE[\vert f_n-f\vert\ge\sigma]=0
$$

则称函数列$\{f_n\}$**依测度收敛**于$f$，或者**度量收敛**于$f$.记为$f_n(x)\Rightarrow f(x)$.

> 几乎处处收敛可以不依测度收敛，反之亦然.

但两者存在联系：

定理1（里斯定理）：设$E$上$\{f_n\}$依测度收敛于$f$，则存在子列$\{f_{n1}\}$在$E$上$\text{a.e.}$收敛于$f$.

定理2（勒贝格）：设

1. $mE\lt\infty$；
2. $\{f_n\}$是$E$上几乎处处有限的可测函数列；
3. $\{f_n\}$是$E$上$\text{a.e.}$收敛于$\text{a.e.}$有限的函数$f$.

则

$$
f_n(x)\Rightarrow f(x)
$$

定理3：设$f_n(x)\Rightarrow f(x),f_n(x)\Rightarrow g(x)$，则$f(x)=g(x)$在$E$上几乎处处成立.

## 积分论

### 黎曼积分的局限性和勒贝格积分

我们将黎曼积分记作$R$积分，它存在着局限性：

1. 积分与极限的交换太严格：

    $$
        \int_{a}^{b}\lim_{n\to\infty} f_n(x)\mathrm{d}x=\lim_{n\to\infty}\int_{a}^{b}f_n(x)\mathrm{d}x
    $$

    成立常常要$\{f_n(x)\}$一致收敛.
2. 积分运算不完全是微分运算的逆运算.

我们将勒贝格积分记作$L$积分，采取和黎曼积分相反的切割方式进行求和：

$$
\sum_{i=1}^ny_iE[y_i\le f\le y_{i+1}]\\
$$

### 非负简单函数的勒贝格积分

定义：设$E\subset\mathbb{R}^n$为零测集，$\varphi(x)$为$E$上一个非负简单函数，即$E$表示为有限个互不相交的可测集之并，而每个可测集上函数取非负常数：

$$
\varphi(x)=\sum_{i=1}^kc_i\chi_{E_i}(x).
$$

这里的$\chi$是对应集合的特征函数.

$\varphi(x)$在$E$上的勒贝格积分定义为：

$$
\int_E\varphi(x)\mathrm{d}x=\sum_{i=1}^kc_imE_i.
$$

设可测子集$A\subset E$，$\varphi(x)$在$A$上的勒贝格积分定义为$\varphi$在$A$上的限制$\varphi\vert_A$:

$$
\int_A\varphi(x)\mathrm{d}x=\sum_{i=1}^kc_im(A\cup E_i)
$$

定理1：对于可测集$E\subset\mathbb{R}^n$上的非负简单函数$\varphi(x)$，我们有：

- $\forall c>0$:

$$\int_Ec\varphi(x)\mathrm{d}x=c\int_E\varphi(x)\mathrm{d}x$$

- 对于2个互不相交的可测子集：

$$\int_{A\cup B}\varphi(x)\mathrm{d}x=\int_A\varphi(x)\mathrm{d}x+\int_B\varphi(x)\mathrm{d}x$$

- 设$\{A_n\}^\infty_{n=1}$为严格单调增的集合序列且$\mathop{\cup}\limits_{n=1}^\infty A_n=E$:

$$\lim_{n\to\infty}\int_{A_n}\varphi(x)\mathrm{d}x=\int_E\varphi(x)\mathrm{d}x$$

定理2：设$\varphi(x)$和$\psi(x)$都是$E\subset\mathbb{R}^n$上的非负简单函数：

- $$\int_E\varphi(x)\mathrm{d}x+\int_E\psi(x)\mathrm{d}x=\int_E(\varphi(x)+\psi(x))\mathrm{d}x$$

- 对于任意非负实数$\alpha$和$\beta$

$$\alpha\int_E\varphi(x)\mathrm{d}x+\beta\int_E\psi(x)\mathrm{d}x=\int_E(\alpha\varphi(x)+\beta\psi(x))\mathrm{d}x$$

### 非负可测函数的勒贝格积分

定义：设$f(x)$是定义在$E\subset\mathbb{R}^n$的非负可测函数，我们定义它的勒贝格积分：

$$
\int_Ef(x)\mathbb{d}x=\sup\{\int_{E}\varphi(x)\mathrm{d}x:\varphi(x)是E上的简单函数,且x\in{E}时,0\le\varphi(x)\le f(x)\}
$$

显然$0\le\int_Ef(x)\mathrm{d}x\le\infty$，若$\int_Ef(x)\mathrm{d}x\lt\infty$，则函数在定义域上勒贝格可积.

类似于上面，可测子集$A\subset E$上$f(x)$的积分就是

$$
\int_Af(x)\mathrm{d}x=\int_Ef(x)\chi_A(x)\mathrm{d}x
$$

定理1：设$f(x)$是$E\subset\mathbb{R}^n$上的非负可测函数，我们有：

- $mE=0\to\int_Ef(x)\mathrm{d}x=0$;
- $\int_Ef(x)\mathrm{d}x=0\to f(x)=0\text{a.e.}于E$;
- 两个$E$的互不相交的可测子集满足：

$$\int_{A\cup B}f(x)\mathrm{d}x=\int_Af(x)\mathrm{d}x+\int_Bf(x)\mathrm{d}x$$

定理2：如果$f(x)$和$g(x)$是$E\subset\mathbb{R}^n$上的可测函数：

1. $f(x)\le g(x)\text{a.e.}$于$E\to\int_Ef(x)\mathrm{d}x\le\int_Eg(x)\mathrm{d}x$，这时，如果$g(x)$在$E$上$L$可积，那么$f(x)$也是
2. $f(x)=g(x)\text{a.e.}$于$E\to\int_Ef(x)\mathrm{d}x=\int_Eg(x)\mathrm{d}x$，特别的，若$f(x)=0\text{a.e.}$于$E$，那么$\int_Ef(x)\mathrm{d}x=0$.

定理3（莱维定理）设$E\subset\mathbb{R}^n$是可测集，有一列非负可测函数，当$x\in E$时对任一正整数有$f_n(x)\le f_{n+1}(x)$，令

$$
f(x)=\lim_{n\to\infty}f_n(x),x\in E
$$

则

$$
\lim_{n\to\infty}\int_Ef_n(x)\mathrm{d}x=\int_Ef(x)\mathrm{d}x
$$

定理4：对于任意非负实数$\alpha$和$\beta$，我们有：

$$\alpha\int_E\varphi(x)\mathrm{d}x+\beta\int_E\psi(x)\mathrm{d}x=\int_E(\alpha\varphi(x)+\beta\psi(x))\mathrm{d}x$$

推论：非负函数$f,g$都可积，推出$\alpha f+\beta g$也可积.

定理5（逐项积分定理）对于一列非负可测函数

$$
\int_E(\sum_{i=1}^\infty f_n(x))\mathrm{d}x=\sum_{i=1}^\infty\int_E f_n(x)\mathrm{d}x
$$

定理6（法图引理）对于一列非负可测函数

$$
\int_E\mathop{\underline{\lim}}\limits_{n\to\infty}f_n(x)\mathrm{d}x\le\mathop{\underline{\lim}}\limits_{n\to\infty}\int_Ef_n(x)\mathrm{d}x
$$

### 一般可测函数的勒贝格积分

对于$E$上的可测函数$f(x)$,设

$$
f^+(x)=\max\{f(x),0\},f^-(x)=\max\{-f(x),0\}
$$

则两函数都是可测函数，且

$$
f^++f^-=f,f+-f^-=|f|
$$

若$\int_Ef^+(x)\mathrm{d}x$和$\int_Ef^-(x)\mathrm{d}x$至少一个有限，则称$f$在$E$上积分确定，称

$$
\int_Ef^+(x)\mathrm{d}x-\int_Ef^-(x)\mathrm{d}x
$$

为$f$在$E$上的勒贝格积分.

若正部积分和负部积分都有限，那么$f$在$E$上勒贝格可积，简称$L$可积.

定理1：

- 若$E\neq\emptyset$但$mE=0$，那么$E$上的所有实函数都在$E$上可积且积分为0;
- $f\in L(E)\to mE[\vert f\vert=\infty]=0$，即$\vert f(x)\vert\lt\infty\text{a.e.}$于$E$;
- $f$在$E$上积分确定，则$f$在$E$的可测子集上积分确定，若$E=A\cup B$且$A\cap B=\emptyset$：

$$\int_Ef(x)\mathrm{d}x=\int_Af(x)\mathrm{d}x+\int_Bf(x)\mathrm{d}x$$

- 设$f$在$E$上积分确定且$f(x)=g(x)\text{a.e. in }E$,则$g(x)$也在$E$上积分确定且

$$\int_Ef(x)\mathrm{d}x=\int_Eg(x)\mathrm{d}x$$

- 设$f$和$g$都在$E$上积分确定且$f(x)\le g(x)\text{ a.e. in E}$，则

$$\int_Ef(x)\mathrm{d}x\le\int_Eg(x)\mathrm{d}x$$

特别的，如果定义域有限，且$b\le f(x)\le B$，我们就有：

$$bmE\le\int_Ef(x)\mathrm{d}x\le BmE$$

- 设$f$在$E$上可积，则$\vert f(x)\vert$也在$E$上$L$可积，且

$$\vert\int_Ef(x)\mathrm{d}x\vert\le\int_E\vert f(x)\vert\mathrm{d}x$$

- 设$f$是$E$上可测函数，$g$是$E$上非负$L$可积函数且$\vert f(x)\vert\le g(x)\text{ a.e. in E}$，则$f$也在$E$上$L$可积，且

$$\big\vert\int_Ef(x)\mathrm{d}x\big\vert\le\int_E\vert f(x)\vert\mathrm{d}x\le\int_Eg(x)\mathrm{d}x$$

定理2：

$$
\begin{aligned}
\int_E\lambda f(x)\mathrm{d}x&=\lambda\int_Ef(x)\mathrm{d}x\\
\int_E\big(f(x)+g(x)\big)\mathrm{d}x&=\int_Ef(x)\mathrm{d}x+\int_Eg(x)\mathrm{d}x\\
\int_E\big(\alpha f(x)+\beta g(x)\big)\mathrm{d}x&=\alpha\int_Ef(x)\mathrm{d}x+\beta\int_Eg(x)\mathrm{d}x\\
\end{aligned}
$$

这里的系数可以使任意实数.

定理3（积分的绝对连续性）设$E\subset\mathbb{R}^n$是可测集，$f\in L(E)$，则对任意$\varepsilon>0$，存在一个$\delta>0$，使得对于任意的可测集$A\subset E$，只要$mA\lt\delta$，就有

$$
\big\vert\int_Af(x)\mathrm{d}x\big\vert\le\int_A\vert f(x)\vert\mathrm{d}x<\varepsilon
$$

定理4（积分可数可加性）对于$E$中不不相交的可测子集，如果$f$积分确定：

$$
\int_Ef(x)\mathrm{d}x=\sum_{i=1}^\infty\int_{E_i}f(x)\mathrm{d}x
$$

定理5（勒贝格控制收敛定理）设$E\subset\mathrm{R}^n$为可测集，有一列可测函数$f_n$. $F$为$E$上非负勒贝格可积函数，如果对于任意正整数$n$有$\vert f_n(x)\vert\le F(x)\text{ a.e. in E}$且$\mathop{\lim}\limits_{n\to\infty}f_n(x)=f(x)\text{ a.e. in E}$，则：

$$
\lim_{n\to\infty}\int_E\vert f_n(x)-f(x)\vert\mathrm{d}x=0\tag{1}
$$

$$
\lim_{n\to\infty}\int_E f_n(x)\mathrm{d}x=\int_E f(x)\mathrm{d}x\tag{2}
$$

定理6：设$E\subset\mathrm{R}^n$为可测集，有一列可测函数$\{f_n(x)\}_{n=1}^\infty$. $F$为$E$上非负勒贝格可积函数，如果对于任意正整数$n$有$\vert f_n(x)\vert\le F(x)\text{ a.e. in E}$且$n\to\infty$时，$f_n\Rightarrow f$，则：

$$
\lim_{n\to\infty}\int_E\vert f_n(x)-f(x)\vert\mathrm{d}x=0\tag{1}
$$

$$
\lim_{n\to\infty}\int_E f_n(x)\mathrm{d}x=\int_E f(x)\mathrm{d}x\tag{2}
$$

从而推出有界收敛：

推论：设$E$是有限的可测集，有一列可测函数$\{f_n(x)\}_{n=1}^\infty$. $F$为$E$上非负勒贝格可积函数. 如果存在$M>0$使得对于任意正整数$n$,$\vert f(x)\vert\le M\text{ a.e. in E}$，且$n\to\infty$时

$$
f_n(x)\to f(x)\text{ a.e. in }E或f_n\Rightarrow f
$$

则：

$$
\lim_{n\to\infty}\int_E\vert f_n(x)-f(x)\vert\mathrm{d}x=0\tag{1}
$$

$$
\lim_{n\to\infty}\int_E f_n(x)\mathrm{d}x=\int_E f(x)\mathrm{d}x\tag{2}
$$

定理7：可测集$E\subset\mathbb{R}^n$上一列勒贝格可积函数，如果正项级数

$$
\sum_{i=1}^\infty\int_E\vert f_n(x)\vert\mathrm{d}x
$$

收敛，则函数项级数

$$
\sum_{i=1}^\infty f_n(x)
$$

在$E$上几乎处处收敛，其和函数在$E$上$L$可积，且

$$
\int_E\big(\sum_{i=n}^\infty f_n(x)\big)\mathrm{d}x=\sum_{n=1}^\infty\int_Ef_n(x)\mathrm{d}x
$$

定理8：设可测集$E$，$f(x,t)$是$E\times(a,b)$上的实函数，如果$\forall t\in(a,b)$，$f(x,t)$作为$x$的函数在$E$上勒贝格可积，对于$\text{a.e. }x\in E$，$f(x,t)$作为$t$的函数在$(a,b)$上可导且$\big\vert\dfrac{\partial}{\partial t}f(x,t) \big\vert\le F(x)$，$F$是$E$上某个非负勒贝格可积函数，那么$\int_Ef(x,t)\mathrm{d}x$作为$t$的函数在$(a,b)$上可导，且

$$
\dfrac{\mathrm{d}}{\mathrm{d}t}\int_Ef(x,t)\mathrm{d}x=\int_E\dfrac{\partial}{\partial t}f(x,t)\mathrm{d}x
$$

### 黎曼积分和勒贝格积分

> 勒贝格积分是黎曼积分的推广但不是黎曼反常积分的推广.

定理1：设$f(x)\in[a,b]$且是有界函数，则$f(x)$在$[a,b]$上可积的充要条件是$f(x)$在$[a,b]$上几乎处处连续，即$f(x)$上不连续点全体构成一个**零测集**.

定理2：设$f(x)$是$[a,b]$上的有界函数，若$f(x)$在$[a,b]$上可积，则$f(x)$在$[a,b]$上$L$可积，qie

$$
(L)\int_{[a,b]}f(x)\mathrm{d}x=(R)\int_a^bf(x)\mathrm{d}x
$$

定理3：设$f(x)$是$[a,\infty]$上的一个非负实函数，如果$\forall A>a$，$f(x)$在$[a,A]$上$R$可积且$R$反常积分$(R)\displaystyle{\int}_a^\infty f(x)\mathrm{d}x$收敛，则$f(x)$在$[a,\infty]$上$R$可积且

$$
(L)\int_{[a,\infty]}f(x)\mathrm{d}x=(R)\int_a^\infty f(x)\mathrm{d}x
$$

### 勒贝格积分的集合意义和富比尼定理

定理1（截面定理）设$E\subset\mathbb{R}^{p+q}$是可测集，则

1. 对于$\mathbb{R}^p$中几乎所有的点$x$，$E_x$是$\mathbb{R}^q$中的可测集.
2. $mE_x$作为$x$的函数，它是$\mathbb{R}^p$上几乎处处有定义的可测函数.
3. $mE=\displaystyle\int_{\mathbb{R^p}}mE_x\mathrm{d}x$

定理2：设$A,B$分别是$\mathbb{R}^p,\mathbb{R}^q$中的可测集，则$A\times B$是$\mathbb{R}^{p+q}$中的可测集且$m(A\times B)=mA\cdot mB$

定义1：设$f(x)$是$E\subset\mathbb{R}^n$上的非负可测函数，则$\mathbb{R}^{n+1}$上的点集

$$
\{(x,z):x\in E,0\le z\lt f(x) \}
$$

称为$f(x)$在$E$上的**下方图形**，记为$G(E,f)$.

定理3：设$f(x)$为可测集$E\subset\mathbb{R}^n$上的非负函数，则：

1. $f(x)$是$E$上的可测函数$\leftrightarrow G(E,f)$是$\mathbb{R}^{n+1}$上的可测集；
2. 当$f(x)$在$E$上可测时

$$
\int_Ef(x)\mathbb{d}x=mG(E,f)
$$

推论1：设$f(x)$是$E$上可测函数，那么

$$
\int_Ef(x)\mathrm{d}x=mG(E,f^+)-mG(E,f^-).
$$

推论2：可测函数可积的充要条件是$mG(E,f^+)<\infty,mG(E,f^-)<\infty$

定理4（富比尼定理）

- 设$f(P)=f(x,y)$在$A\times B\subset\mathbb{R}^{p+q}$上非负可测，则对几乎处处的$x\in A$，$f(x,y)$作为$y$的函数在$B$上可测，且

$$
\int_{A\times B}f(P)\mathrm{d}P=\int_A\mathrm{d}x\int_Bf(x,y)\mathrm{d}y\tag{1}
$$

- 设$f(P)=f(x,y)$在$A\times B\subset\mathbb{R}^{p+q}$上可积，则对几乎处处的$x\in A$，$f(x,y)$作为$y$的函数在$B$上可积，又$\int_Bf(x,y)\mathbb{d}y$作为$x$的函数在$A$上可积且$(1)$成立.

## 维塔利定理

定义：设$E\subset\mathbb{R},\mathscr{V}=\{I\}$是长度为正的区间族，如果对于任意$x\in E$及任意$\varepsilon>0$，存在区间$I_x\in\mathscr{V}$使得$x\in I_x$且$mI_x<\varepsilon$，则称$\mathscr{V}$以维塔利意义覆盖$E$，简称$E$的$V$-覆盖.

易证明其定义的等价形式为:对于任意$x\in E$，存在一列区间$\{I_n\}\subset\mathscr{V}$，使得$x\in I_n,n=1,2,...,$且$mI_x\to0(n\to\infty)$.

定理（维塔利覆盖定理）设$E\subset\mathbb{R}$且$m^*E<\infty,\mathscr{V}$是$E$的$V$-覆盖，则可选出区间列$\{I_n\}\subset\mathscr{V}$使得各$I_n$互不相交且

$$
m(E\backslash\cup_kI_k)=0
$$

推论：设$E\subset\mathbb{R}$且$m^*E<\infty,\mathscr{V}$是$E$的$V$覆盖，则对任何$\varepsilon>0$，可以从$\mathscr{V}$中选出互不相交的有限区间$I_1,I_2,...,I_n$，使

$$
m^*(E\backslash\mathop{\cup}\limits_{i=1}^nI_i)\lt\varepsilon
$$

## 单调函数的可微性

定义：设$f(x)$为$[a,b]$上的有限函数，$x_0\in[a,b]$，如果存在数列$h_n\to0(h_n\to0)$使极限

$$
\lim_{n}\dfrac{f(x_0+h_n)-f(x_0)}{h_n}=\lambda
$$

存在（可以为无穷），则称$\lambda$为$f(x)$在点$x_0$处的一个**列导数**，记作$Df(x_0)=\lambda$

要注意的是列导数与数列的取法有关，例如$f(x)$是迪利克雷函数，设$x_0$是有理数，那么$h_n$是否是有理数会影响列导数的取值.

引理：设$f(x)$为$[a,b]$上的严格增函数，

1. 如果对于$E\subset[a,b]$中每一点$x$，至少有一个列导数$Df(x)\leqslant p(p\geqslant0)$，则$m^\star f(E)\leqslant pm^\star E$;
2. 如果对于$E\subset[a,b]$中每一点$x$，至少有一个列导数$Df(x)\geqslant q(q\geqslant0)$，则$m^\star f(E)\geqslant pm^\star E$;

定理（勒贝格）：设$f(x)$为$[a,b]$上的单调函数，则

1. $f(x)$在$[a,b]$上几乎处处存在$f'(x)$;
2. $f'(x)$在$[a,b]$上可积;
3. 如果$f(x)$为增函数，有$\int_a^bf'(x)\mathrm{d}x\leqslant f(b)-f(a)$.

## 有界变差函数

定义1（弧长）设$C$是平面上一条连续弧，$x=\varphi(t),y=\psi(t),\alpha\leqslant t\leqslant\beta$是它的参数表示. 两函数都是$[\alpha,\beta]$上的连续函数，相应于区间$[\alpha,\beta]$的任一分划

$$
T:\alpha=t_0\lt t_1\lt\cdots\lt t_n=\beta
$$

得到$C$上一组分点$P_i=(\varphi(t_i),\psi(t_i)),i=0,1,2,...,n,$设依次联结各分点$P_i$所得内接折线的长为$L(T)$. 如果对于$[\alpha,\beta]$的一切分划$T$，$\\{L(T)\\}$成一个有界数集，则称$C$是**可求长**的，并称其上确界

$$
L=\sup_{r}L(T)
$$

为$C$的**长**.

定义2：设$f(x)$为$[a,b]$上的有限函数，如果对于$[a,b]$的任一分划$T$，使$\\{\sum_{i=1}^n\vert f(x_i)-f(x_{i-1})\vert\\}$成有界数集，则称$f(x)$为$[a,b]$上的有界变差函数，并称该有界数集的上确界为$f(x)$在$[a,b]$上的全变差，记为$\mathop{\text V}\limits_{a}^{b}$. 用一个分划做成的和数

$$
V=\sum_{i=1}^n\vert f(x_i)-f(x_{i-1})\vert
$$

称为$f(x)$在此分划下的**变差**.

定理1：连续弧可求长的充要条件是$\varphi(t)$和$\psi(t)$都是$[\alpha,\beta]$上的有界变差函数.

定理2：

- 有界变差有可加性：

$$
\mathop{\text{V}}\limits_{a}^b(f)=\mathop{\text{V}}\limits_{a}^c(f)+\mathop{\text{V}}\limits_{c}^b(f)
$$

- $f(x)$在$[a,b]$上有界变差$\to f(x)$在$[a,b]$上有界.
- 两个有界变差函数的加减乘还是有界变差.

定理3：$[a,b]$上任一有界变差函数都可以表示为两个增函数之差.

定理三和前一节的勒贝格定理可以共同导出下面的推论：设$f(x)$是$[a,b]$上的有界变差函数，则$f(x)$几乎处处存在导数$f'(x)$，且导数在$[a,b]$上可积.

## 不定积分

定义1（不定积分）：设$f(x)$在$[a,b]$上$L$可积，则$[a,b]$上的函数

$$
F(x)=\int_a^xf(t)\mathrm{d}t+C
$$

称为$f(x)$的一个不定积分.

定义2（绝对连续函数）：设$F(x)$为$[a,b]$上的有限函数，如果对任意的$\varepsilon>0$，存在$\delta>0$，使得对$[a,b]$中互不相交的任意有限个开区间$(a_i,b_i),i=1,2,...,n$，只要

$$
\sum_{i=1}^n(b_i-a_i)\lt\delta
$$

就有

$$
\sum_{i=1}^n\vert F(b_i)-F(a_i)\vert\lt\varepsilon
$$

则称$F(x)$是$[a,b]$上的**绝对连续函数**.

定理1：设$f(x)$在$[a,b]$上可积，则其不定积分为绝对连续函数(几乎处处可导).

> 绝对连续函数是一致连续函数，也是有界变差函数.

定理2：设$F(x)$是区间上的绝对连续函数，且$F'(x)=0\text{ a.e. in }[a,b]$，则$F(x)=C$.

定理3：设$f(x)$在区间上可积，则存在绝对连续函数$F(x)$使得$F'(x)=f(x)\text{ a.e. in }[a,b]$(只需取$F(x)=\int_a^xf(t)\mathrm{d}t$).

定理4：设$F(x)$是$[a,b]$上的绝对连续函数，则$\text{a.e.}$有定义的$F'(x)$在$[a,b]$上可积且

$$
F(x)=F(a)+\int_a^xF'(t)\mathrm{d}t
$$

即$F(x)$总是$[a,b]$上可积函数的不定积分.

> $F(x)$是绝对连续函数的充要条件是，它是一个可积函数的不定积分.
