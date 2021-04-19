---
layout:     post
title:      机器学习导论
subtitle:   绪论
date:       2021-03-08
author:     Welt Xing
header-img: img/post-bg-desk.jpg
catalog:    true
tags:
    - 机器学习
---

> 西瓜书训练营课程导学

1997book, 统计学习方法；PRML，ESL，MLAPP，UML

Artificial Intelligence is Intelligence-inspired computing.

经典定义：利用经验改善系统自身性能。

PAC（概率近似正确）：

$$
\Pr(|f({x})-y|\le\epsilon)\ge1-\delta
$$

机器学习处理的问题往往在$\bold{NP}$之外，导致公式无法是：

$$
\Pr(|f({x})-y|=0)=1
$$

机器学习最优解：能实现的最优解，而不是理论最优解

- 数据集；训练，测试
- 示例，样例：示例无结果，样例有结果，都是训练集中的样本
- 样本
- 属性，特征；属性值
- 属性空间，样本空间，输入空间
- 特征向量
- 标记空间，输出空间
- 假设（模型的输出的是假设），真相，学习器
- 分类，回归
- 二分类，多分类
- 正类，反类
- 监督/无监督学习
- 未见样本（一个重要假设：样本来源于同一个未知分布）
- 所有的数据都是独立同分布（$i.i.d.$）
- 泛化：学习器处理新数据，也就是一般数据的能力
假设空间：

$$
(n_1+1)\times(n_2+1)\times...\times(n_k+1)\textbf{+1}
$$

学习，搜索和规划

- 版本空间
有限的点能学习出无限个模型。
- 归纳偏好
奥卡姆剃刀：若非必要，勿增实体
- 简单的定义：

$$
y=ax^2+bx+c\\
y=ax^3+c
$$

从不同角度上会有不同的简单定义。

- [可微分编程](https://zh.wikipedia.org/wiki/%E5%8F%AF%E5%BE%AE%E5%88%86%E7%BC%96%E7%A8%8B)
- $\text{NFL}$定理：前提，证明和结论
- 查准率，查全率和$F_1$，以及带权的$F_\beta$
- PR图：移动阈值画图，离散数据导致图像不平滑
- 分类，排序和回归
- $t$检验：过高估计（$k$折交叉验证样本存在重复性），solution：$5\times2$交叉验证，只算第一折均值，但方差都要算。
- 多学习器下，算法优度没有传递性.
- 偏差-方差分解只能用于以平方误差为评价标准的回归问题，对分类不适用

### 线性模型

- 离散属性的处理（无序的离散属性不能转成数字，而是$k$维向量）.
- $w$多解：加入归纳偏好（正则化）.
- $\text{Logistic}(对数几率函数)\in\text{Sigmoid}$
- 似然：$y_ip(y_i^+)+y_jp(y_j^-)$

### SVM

- $\kappa(x_i,x_j)$定义了一个距离，从而

  $$
  K=\begin{bmatrix}
  \kappa(\pmb{x}_1,\pmb{x}_1)&\cdots\\
  \vdots&\kappa(\pmb{x}_n,\pmb{x}_n)
  \end{bmatrix}
  $$

  定义了一个空间.

- 文本数据常用线性核，情况不明先用高斯核.
- 正则化$\leftrightarrow$先验
