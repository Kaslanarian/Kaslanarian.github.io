---
layout:     post
title:      智能系统
subtitle:   公式推导
date:       2021-03-18
author:     Welt Xing
header-img: img/agent_header.jpeg
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

其中上式的分母$P(o_{1:n})=\sum_cP(c,o_{1:n})$是一个归一化常数，使得$\sum_{c}P(c\vert o_{1:n})=1$，所以令其为$\frac{1}{\chi}$：

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

我们有：

$$
\begin{aligned}
P(s_t|o_{0:t})
&=\dfrac{P(s_t,o_t|o_{0:t-1})}{P(o_t|o_{0:t-1})}\\
&\propto P(s_t,o_t|o_{0:t-1})\\
&=\dfrac{P(s_t,o_{0:t})}{P(o_{0:t-1})}\\
&=\dfrac{P(s_t,o_{0:t})}{P(s_t,o_{0:t-1})}\dfrac{P(s_t,o_{0:t-1})}{P(o_{0:t-1})}\\
&=P(o_t|s_t,o_{t-1})P(s_t|o_{0:t-1})\\
&=P(o_t|s_t)P(s_t|o_{0:t-1})\to 条件独立性假设\\
&=P(ot|s_t)\sum_{s_{t-1}}P(s_t,s_{t-1}|o_{0:t-1})\to 全概率公式\\
&=P(ot|s_t)\sum_{s_{t-1}}P(s_t|s_{t-1},o_{0:t-1})P(s_{t-1}|o_{0:t-1})\to 条件概率\\
&=P(o_t|s_t)\sum_{s_{t-1}}P(s_t|s_{t-1})P(s_{t-1}|o_{0:t-1})
\end{aligned}
$$

其中$P(o_t|s_t)$和$P(s_t|s_{t-1}$可以直接由模型得到.

> 这里其实是一个递归式.

### 预测

单步预测就是滤波；没有增加新观察的条件下的滤波：

$$
P(s_{t+k+1}|o_{0:t})=\sum_{s_{t+k}}P(s_{t+k+1}|s_{t+k})P(s_{t+k}|o_{0:t})
$$

同样也是递归.

### 平滑

$$
\begin{aligned}
P(s_{k}|o_{0:t})&=P(s_k|o_{0:k},o_{k+1:t})\\
&\propto P(s_k|o_{0:k})P(o_{k+1:t}|s_k,o_{0:k})\\
&=P(s_k|o_{0:k})P(o_{k+1:t}|s_k)
\end{aligned}
$$

分别用前向算法和后向算法解决.

后向算法：

$$
\begin{aligned}
P(o_{k+1:t}|s_k)
&=\sum_{s_{k+1}}P(o_{k+1:t}|s_k,s_{k+1})P(s_{k+1}|s_k)\\
&=\sum_{s_{k+1}}P(o_{k+1:t}|s_{k+1})P(s_{k+1}|s_k)\\
&=\sum_{s_{k+1}}P(o_{k+1},o_{k+2:t}|s_{k+1})P(s_{k+1}|s_k)\\
&=\sum_{s_{k+1}}P(o_{k+1}|s_{k+1})P(o_{k+2:t}|s_{k+1})P(s_{k+1}|s_k)\\
\end{aligned}
$$

