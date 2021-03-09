---
layout:     post
title:      实变函数与泛函分析
subtitle:   笔记概要
date:       2021-03-02
author:     Welt Xing
header-img: img/post-bg-desk.jpg
catalog:    true
tags:
    - 课程
---

# 实变函数与泛函分析

一些重要/陌生知识点的记录以供复习参考

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