---
layout:     post
title:      实变函数与泛函分析
subtitle:   笔记概要
date:       2021-03-02
author:     Welt Xing
header-img: img/math_header.jpg
catalog:    true
tags:
    - 课程
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

#### 含极限的运算

在这里，不同于数学分析，$(\pm\infty)-(\pm\infty),(\pm\infty)+(\mp\infty),\frac{\pm\infty}{\pm\infty}$