---
layout:     post
title:      机器学习导论
subtitle:   记录
date:       2021-03-08
author:     Welt Xing
header-img: img/post-bg-desk.jpg
catalog:    true
tags:
    - 课程
---

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