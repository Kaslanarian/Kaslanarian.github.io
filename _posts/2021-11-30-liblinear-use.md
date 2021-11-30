---
layout:     post
title:      初识LIBLINEAR
subtitle:   命令行模式和问题形式化
date:       2021-11-30
author:     Welt Xing
header-img: img/background.jpg
catalog:    true
tags:
    - LIBLINEAR
---

源码地址：<https://github.com/cjlin1/liblinear>. 本文着重介绍LIBLINEAR软件包的使用方法，同时有一些C++代码的少许解读，内容基于软件包中的README文件。

本文的所有命令行相关内容都是基于Linux平台上运行。

## Quick start

通过命令

```bash
git clone https://github.com/cjlin1/liblinear
```

来获取LIBLINEAR源码，然后在代码文件夹中输入

```bash
make
```

编译链接生成了可执行文件`train`和`predict`，分别用于训练和预测。

观察到文件夹中自带了一个数据集文件：`heart_scale`，观察第一行内容：

```text
+1 1:0.708333 2:1 3:1 4:-0.320755 5:-0.105023 6:-1 7:1 8:-0.419847 9:-1 10:-0.225806 12:1 13:-1
```

"+1"是标签，代表正类；后面都是整数-实数对，比如"9:-1"表示数据的第九个特征的值为-1，可以发现这里没有声明第11特征的值，**表明该值为0**。

命令行输入

```bash
./train heart_scale
```

LIBLINEAR会开始训练，并生成一个`heart_scale.model`文件，也就是训练出来的分类器模型：

```text
solver_type L2R_L2LOSS_SVC_DUAL
nr_class 2
label 1 -1
nr_feature 13
bias -1
w
0.097676078338076164 
0.23109212170976423 
0.42388465345789894 
0.26935952028128246 
-0.0039347576271112567 
-0.16445570938453191 
0.12391045718196422 
-0.27439908304665195 
0.12612333772083062 
0.049934679120800664 
0.16887189609150505 
0.44422682651532758 
0.26100864387282813 
```

从上往下分别记录了：模型类型、分类问题的类别数、标签、特征数、判别函数$f(\pmb x)=\pmb w^T\pmb x+b$的两参数$b$和$\pmb w$。

在模型完成后，我们就可以使用它对数据进行预测，我们可以用它来对原训练集进行测试：

```bash
./predict heart_scale heart_scale.model output
```

该命令是用模型`heart_scale.model`对数据集`heart_scale`进行预测，将结果输入到文件`output`中。命令行输出准确率：

```text
Accuracy = 84.4444% (228/270)
```

文件中是预测结果：

```text
1
-1
-1
1
-1
...
```

## 自定义训练

在前面的训练步骤中，我们并没有指定`./train`的参数。事实上，通过指定不同的参数，我们可以调用不同的模型对数据进行学习，获得不同的效果。训练命令的完整形式应该是

```bash
./train [options] train_set_file [model_file]
```

其中"[]"表示参数非必须。如果不指定`model_file`，默认将模型输出到`数据集名.model`文件中。现在来看options：

- -s type，类别参数，选择求解器(Solver)的类型，默认是1。对于多分类问题，可选的参数有（SVC：支持向量分类；LR：逻辑回归）

  - 0——L2正则化的逻辑回归（求解原问题）；
  - 1——L2正则化的L2-SVC（求解对偶问题）；
  - 2——L2正则化的L2-SVC（求解原问题）；
  - 3——L2正则化的L1-SVC（求解对偶问题）；
  - 4——Crammer和Singer提出的SVC；
  - 5——L1正则化的L2-SVC；
  - 6——L1正则化的LR；
  - 7——L2正则化的LR（求解对偶问题）.

  对于分类问题，可选的参数有（SVR：支持向量回归）

  - 11——L2正则化的L2-SVR（求解原问题）；
  - 12——L2正则化的L2-SVR（求解对偶问题）；
  - 12——L2正则化的L1-SVR（求解对偶问题）.

  对于边缘检测问题，可选的参数有

  - 21——单分类SVM（求解对偶问题）.

- -c cost，代价参数，也就是SVM中的惩罚参数$C$，默认为1；

- -p epsilon，$\epsilon$-SVR问题中的参数$\epsilon$，默认为0.1；

- -n nu，对应One-class SVM中的参数$\nu$，默认0.5；

- -e epsilon，优化过程中的迭代终止阈值$\epsilon$，目标值的变化量小于该值时便认为其收敛，停止迭代；

- -B bias，偏置参数，用于对数据集进行增广：$x\gets[x;bias]$，如果该参数为负数，则不会增加偏置，默认是-1；

- -R，不对上面的bias项进行正则化（后面会提及），其起作用必须搭配-B参数为1；

- -wi weight，类别权重，用于调整不同类别数据对应的惩罚参数$C$；

- -v n，进行$n$次交叉验证；

- -C，开启寻找最优模型超参数模式（调参）；

- -q，静默模式，不输出任何内容.

### LIBLINEAR可求解的优化问题

通过-s参数，我们可以指定不同的优化器对当前数据集进行学习，我们接下来研究这些优化问题的形式化。

先是分类问题：

- L2正则化的逻辑回归（求解原问题）：

  $$
  \min_{\pmb w}\quad\frac12\pmb w^T\pmb w+C\sum_{i=1}^m\log(1+\exp(-y_i\pmb w^T\pmb x_i))
  $$

- L2正则化的逻辑回归（求解对偶问题）：

  $$
  \begin{aligned}
  \min&\quad\frac12\pmb\alpha^T(Q+\frac{1}{C}I)\pmb\alpha-e^T\alpha\\
  \text{s.t.}&\quad\alpha_i\geq 0
  \end{aligned}
  $$

- L2正则化的L2-SVC（求解原问题）:

  $$
  \min\quad\frac12\pmb{w}^T\pmb w+C\sum_{i=1}^m\max(0,1-y_i\pmb w^T\pmb x_i)^2
  $$

- L2正则化的L1-SVC（求解对偶问题）:

  $$
  \begin{aligned}
  \min_{\pmb\alpha}&\quad\frac12\pmb{\alpha}^TQ\pmb\alpha-e^T\alpha\\
  \text{s.t.}&\quad0\leq\alpha_i\leq C
  \end{aligned}
  $$

- L1正则化的L2-SVC：

  $$
  \min_{\pmb w}\quad\sum|\pmb w_j|+C\sum_{i=1}^m\max(0, 1-y_i \pmb w^T\pmb x_i)^2
  $$

- L1正则化的LR：

  $$
  \min_{\pmb w}\quad \sum|\pmb w_j|+C\sum_{i=1}^m\log(1+\exp(-y_i\pmb w^T\pmb x_i))
  $$

- L2正则化的LR（解对偶问题）：

  $$
  \begin{aligned}
  \min_\alpha&\quad\frac12\alpha^T Q\alpha + \sum_{i=1}^m\alpha_i\log(\alpha_i) + \sum_{i=1}^m (C-\alpha_i)\log(C-\alpha_i)\\
  s.t.&\quad0\leq\alpha_i\leq C
  \end{aligned}
  $$

以上提到的$Q$矩阵：$Q_{ij}=y_iy_jx_i^Tx_j$.

回归问题：

- L2正则化的L2-SVR（求解原问题）：

  $$
  \min_{\pmb w}\quad\frac12\pmb w^T\pmb w + C\sum_{i=1}^m\max(0, |y_i-\pmb w^T\pmb x_i|-\epsilon)^2
  $$

- L2正则化的L2-SVR（求解对偶问题）：

  $$
  \min_{\pmb\beta}\quad \frac12\pmb\beta^T(Q+\frac{1}{C}I)\pmb\beta - y^T\pmb\beta + \sum|\pmb\beta_i|
  $$

- L2正则化的L1-SVR（求解对偶问题）：

  $$
  \min_{\pmb\beta}\quad\frac12\pmb\beta^TQ\pmb\beta-y^T\pmb\beta+\sum|\pmb\beta_i|\\
  \text{s.t.}\quad-C\leq\beta_i\leq C
  $$

上述回归问题中的$Q$矩阵满足$Q_{ij}=\pmb x_i^T\pmb x_j$.

单分类SVM的对偶问题：

$$
\min_{\pmb\alpha}\quad\pmb\alpha^TQ\pmb\alpha\\
\text{s.t.}\quad0\leq\alpha_i\leq 1,\sum\alpha_i=\nu l
$$

我们在前面提到参数-B，表示对数据进行增广，随之而来的是参数维度的增加，以及优化问题的变化，比如L2正则化的LR问题变成了：

$$
\min_{\pmb w}\quad\frac12\pmb w^T\pmb w+\frac12(\pmb w_{n+1})^2+C\sum_{i=1}^m\log(1+\exp(-y_i [\pmb w; \pmb w_{n+1}]^T[\pmb x_i; bias]))
$$

但存在一种观点是不要加上面的$\frac12(\pmb w_{n+1})^2$项，也就是偏置项未被正则化，因此我们提供了一个-R参数，如果用户使用该参数，我们就会移除这一项，不对其进行正则化。

### LIBLINEAR的多分类

LIBLINEAR采用的是“一对多”的策略进行多分类。此外，LIBLINEAR还实现了一个笔者未见过的多分类SVM：multi-class SVM by Crammer and Singer，先给出优化问题形式：

$$
\begin{aligned}
\min_{w_m, \xi_i}&\quad\frac12\sum_m ||w_m||^2 + C \sum_i \xi_i\\
\text{s.t.}&\quad w^T_{y_i} x_i - w^T_m x_i\geq e^m_i - \xi_i ,\forall m,i
\end{aligned}
$$

其中$e^m_i = 0\text{ if }y_i  = m,e^m_i = 1\text{ if }y_i\neq m$；其对偶形式：

$$
\begin{aligned}
\min_{\alpha}&\quad\frac12\sum_m ||w_m(\alpha)||^2 + \sum_i \sum_m e^m_i\alpha^m_i\\
\text{s.t.}&\quad \alpha^m_i\leq C^m_i,\forall m,i \\&\quad\sum_m \alpha^m_i=0,\forall i
\end{aligned}
$$

其中$w_m(\alpha) = \sum_i \alpha^m_i x_i$, $C^m_i = C\text{ if }m  = y_i$, $C^m_i = 0\text{ if }m\neq y_i$.

## 自定义预测

类似的，我们也可以指定参数，从而自定义模型预测，命令的完整形式：

```bash
predict [options] test_file model_file output_file
```

对于options参数：

- -b probability_estimates: 选择是否输出预测概率, 0或1 (默认0)，现在只适用于逻辑回归（SVM不存在概率语义）；
- -q : 静默模式，不输出任何内容.
