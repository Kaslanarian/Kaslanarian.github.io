---
layout:     post
title:      决策树算法
subtitle:   《机器学习》摘要
date:       2021-04-11
author:     Welt Xing
header-img: img/decision_tree.jpg
catalog:    true
tags:
    - 机器学习
---

## 引言

决策树算法，可能并没有一些算法，比如$\text{SVM}$，神经网络出名，正因为如此，当我在通览《机器学习》时，看到决策树这一章的标题时，大脑一片空白，没有一点的知识储备，因此作此文作为读书笔记吧.

## 决策树初探

顾名思义，决策树时基于树结构来进行决策的，网上常常用相亲的例子来作为介绍决策树算法的开场白，这里就地引用：

![example](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9jQW9DbGd4NTNWdjlwMDRZNERMSHoxaDhHVHdEdXd6UzZrUU00aWJ0OXJ0Y2ljTGcxRG9XM0RnRTFTOWJ0WUZObHFld1o0aWNNM09JMnhOelNuRUxLRDNZZy82NDA?x-oss-process=image/format,png)

可以发现，我们在做决定（make decision）时，思维常常像上面这样：经过思考，大脑里已经有了这样一棵决策树，一个输入必定会有一个输出作为决策结果。

对应到我们的机器学习任务中，决策树的叶子节点对应的就是决策结果（比如分类任务的话就是类别），内部节点包括根节点对应的是属性测试。决策树学习的目的是产生一棵泛化能力强（对未见过的样本也有很强的处理能力）的决策树。

## 决策树算法

决策树算法的特点是使用起来方便，不用像对数几率回归那样涉及到数学运算。那么决策树创建起来是不是也很简单呢？我们接下来看看**决策树学习**的基本算法：

![algo](/img/decision_tree_algo.png)

伪代码告诉我们有三种情况会导致递归返回：

1. 样本类别相同，无法分类；（无需划分）
2. 当前属性集为空，或者虽然类别不同但是样本特征相同；（无法划分）
3. 节点包含的样本集合为空，此时只能依赖父节点的样本分布，将其作为先验分布.（无法划分）

## 划分选择

伪代码中最重要的一环就是$\text{BEST-DIVISION-ATTRIBUTE}(D,A)$例程，即选择**最优划分属性**，我们希望每次划分后每一个节点包含的样本尽可能属于同一类别.

### 信息增益

“信息熵”是度量样本集合纯度最常用的一种指标. 假设档期那样本集合$D$中第$k$类样本所占的比例为$p_k(k=1,2,\cdots,K)$，则$D$的信息熵定义为

$$
\text{Ent}(D)=-\sum_{k=1}^{K}p_k\log_2p_k\\
$$

$\text{Ent}(D)$的值越小，说明$D$的纯度越高.

假定离散属性$a$有$V$个不同取值$\{a^1,a^2,\cdots,a^V\}$，我们根据$a$来对样本集$D$进行划分，产生$V$个分支节点，节点$v$中包含的是$D$中$a$特征为$a^v$的数据. 由此可算出每个子节点的信息熵. 考虑到每个子节点样本数不同，我们给他们赋予权重$\vert D^v\vert/\vert D\vert$，从而计算出根据属性$a$对数据集$D$进行划分时获得的**信息增益**：

$$
\text{Gain}(D,a)=\text{Ent}(D)-\sum_{v=1}^V\dfrac{\vert D^v\vert}{\vert D\vert}\text{Ent}(D^v)
$$

信息增益越大，“纯度提升”越大，所以我们的$\text{BEST-DIVISION-ATTIBUTE}$也就是

$$
\mathop{\arg\max}\limits_{a\in A}\text{Gain}(D,a)
$$

### 增益率

我们考虑这样一棵决策树，每一个叶子节点只包含一个样本。显然，这样的决策树的泛化能力很差，因为它已经**过拟合**。遗憾的是，信息增益准则在遇到可取值数目较多的情况下，就更偏向这种过拟合局面发展。为了减少这种偏好及其带啦的不良影响，著名的$\text{C4.5}$决策树算法使用**增益率**替代信息增益来选择最优划分属性：

$$
\text{Gain_ratio}(D,a)=\dfrac{\text{Gain}(D,a)}{\text{IV}(a)}
$$

其中

$$
\text{IV}(a)=-\sum_{i=1}^V\dfrac{|D^v|}{|D|}\log_2\dfrac{|D^v|}{|D|}
$$
称为属性$a$的**固有值**，可能取值越多，那么固有值就越大. 需要注意的是，增益率准则对取值可能少的属性有所偏好，我们也不能直接选择增益率最大的属性进行划分，而是先从候选划分属性中找出信息增益高于平均水平的属性，再从中选择增益率最高的.

### 基尼系数

$\text{CART}$决策树使用**基尼系数**来选择划分属性，这里用**基尼值**来度量数据集的纯度：

$$
\begin{aligned}
\text{Gini}(D)
&=\sum_{k=1}^K\sum_{k'\neq k}p_kp_k'\\
&=1-\sum_{k=1}^Kp_k^2
\end{aligned}
$$
从而有基尼系数：

$$
\text{Gini_index}(D,a)=\sum_{v=1}^V\dfrac{|D^v|}{|D|}\text{Gini}(D^v)
$$
