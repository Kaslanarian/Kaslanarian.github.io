---
layout:     post
title:      实变函数与泛函分析
subtitle:   笔记概要
date:       2021-03-02
author:     Welt Xing
header-img: img/matrix_equations.png
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

