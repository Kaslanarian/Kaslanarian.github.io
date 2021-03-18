---
layout:     post
title:      智能系统
subtitle:   公式推导
date:       2021-03-18
author:     Welt Xing
header-img:
catalog:    true
tags:
    - 课程
---

## 分类推理

需要求解的是条件概率

$$
P(c\vert o_1,\cdots,o_n)
$$

简写为：

$$
P(c|o_{1:n})
$$

由链式规则，我们推出朴素贝叶斯模型的联合分布：

$$
P(c|o_{1:n})=P(c)\prod_{i=1}^nP(o_1|c)\tag{1}
$$

根据条件概率：

$$
P(c|o_{1:n})=\dfrac{P(c,o_{1:n})}{P(o_{1:n})}\tag{2}
$$

其中上式的分母$P(o_{1:n})=\sum_cP(c,o_{1:n})$是一个归一化常数，使得$\sum_{c}P(c|o_{1:n})=1$，所以令其为$\frac{1}{\chi}$：

$$
P(c|o_{1:n})=\chi P(c,o_{1:n})\tag{3}
$$

所以两者成正比.

## 时序模型的推理

### 滤波

我们需要求解

$$
P(s_t|o_{0:t})
$$

由贝叶斯规则：

$$
P(s_t|o_{0:t})\propto P(o_t|s_t,)
$$
