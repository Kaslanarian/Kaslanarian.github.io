---
layout:     post
title:      LIBLINEAR源码解读(1)
subtitle:   liblinear.h
date:       2021-12-01
author:     Welt Xing
header-img: img/background.jpg
catalog:    true
tags:
    - LIBLINEAR
---

在LIBLINEAR软件包中，头文件`liblinear.h`包含了多种重要的结构体和接口函数，可以供用户调用与使用。本文借助README的帮助，对`liblinear.h`中的内容进行简单的列举与分析。

## 结构体

`liblinear`中定义了4个结构体：`feature_node`、`problem`、`parameter`和`model`，分别表示数据、数据集、模型参数和模型。

先来看`feature_node`，它表示的就是数据集中的“一格”：

```cpp
struct feature_node {
    int index;
    double value;
};
```

对于一个已定义的`feature_node`，其含义就是数据的第`index`个特征的值为`value`。我们在前面提到LIBLINEAR中合法的数据形式：

```text
1:0.708333 2:1 3:1 4:-0.320755 5:-0.105023 6:-1 7:1 8:-0.419847 9:-1 10:-0.225806 12:1 13:-1
```

该条数据就是一个长度为12个`feature_node`数组。对于数组的第一个元素，其`index`为1，`value`是0.708333.

再来看`problem`结构的定义：

```cpp
struct problem {
    int l, n;
    double *y;
    struct feature_node **x;
    double bias; /* < 0 if no bias term */
};
```

一个问题，对应的就是一个数据集：

- `l`是训练数据量；
- `n`是特征数；
- `y`为指向一个数组的指针，该数组承载的是数据集的标签值；
- `x`是二级指针，指向一个数组，数组的每一个元素又是一个指针，指向由`feature_node`构成的数组，就像前面提到的那样；
- `bias`是偏置项，如果大于0，则会在后面对数据进行增广；否则没意义。

举例来说，如果我们有下面的训练数据集：

| LABEL | ATTR1 | ATTR2 | ATTR3 | ATTR4 | ATTR5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
|   1   |   0   |  0.1  |  0.2  |   0   |   0   |
|   2   |   0   |  0.1  |  0.3  | -1.2  |   0   |
|   1   |  0.4  |   0   |   0   |   0   |   0   |
|   2   |   0   |  0.1  |   0   |  1.4  |  0.5  |
|   3   | -0.1  | -0.2  |  0.1  |  1.1  |  0.1  |

且设置了增广项为1，那么`problem`的内容如下：

```cpp
l = 5
n = 6
y -> 1 2 1 2 3
x -> [ ] -> (2,0.1) (3,0.2) (6,1) (-1,?)
     [ ] -> (2,0.1) (3,0.3) (4,-1.2) (6,1) (-1,?)
     [ ] -> (1,0.4) (6,1) (-1,?)
     [ ] -> (2,0.1) (4,1.4) (5,0.5) (6,1) (-1,?)
     [ ] -> (1,-0.1) (2,-0.2) (3,0.1) (4,1.1) (5,0.1) (6,1) (-1,?)
```

最后一个结构体是`parameter`，用于刻画一个分类器/回归器：

```cpp
struct parameter {
    int solver_type;

    /* these are for training only */
    double eps; /* stopping tolerance */
    double C;   /* 惩罚参数 */
    int nr_weight; /* 数组weight_label和weight的长度*/
    int *weight_label; /* 加权类的类标签*/
    double *weight; /* 对应类标签的权重 */
    double p;
    double nu;  /* one-class SVM only */
    double *init_sol; /* 初始解w */
    int regularize_bias;
};
```

其中`solver_type`可以是下面枚举变量中的整数值：

```cpp
enum {
    L2R_LR,
    L2R_L2LOSS_SVC_DUAL,
    L2R_L2LOSS_SVC,
    L2R_L1LOSS_SVC_DUAL,
    MCSVM_CS,
    L1R_L2LOSS_SVC,
    L1R_LR,
    L2R_LR_DUAL,
    L2R_L2LOSS_SVR = 11,
    L2R_L2LOSS_SVR_DUAL,
    L2R_L1LOSS_SVR_DUAL,
    ONECLASS_SVM = 21
}; /* solver_type */
```

我们在前面介绍了这些优化器以及对应的形式，在此不过多介绍。

最后是用来表示模型的结构体`model`：

```cpp
struct model
{
  struct parameter param;
  int nr_class;           /* number of classes */
  int nr_feature;
  double *w;
  int *label;             /* label of each class */
  double bias;
  double rho;             /* one-class SVM only */
};
```

`nr_class`和`nr_feature`分别是问题的类别数和特征数，**如果是回归问题，类别数设置为2**，具体原因参考<https://welts.xyz/2021/09/16/svr/>。

对于多分类问题，`w`是一个`nr_feature`乘`nr_class`的矩阵，因为LIBLINEAR训练了`nr_class`个分类器，每个分类器都对应一个$\pmb w$，特别的，当`nr_class`为2时，只需要一个$\pmb w$。

## 函数

我们逐一介绍LIBLINEAR中的接口函数，它们被定义在`liblinear.h`中，用于模型训练、模型预测、以及模型信息获取等功能。

```cpp
struct model *train(const struct problem *prob, const struct parameter *param);
```

给定问题和模型，训练模型并返回该模型的指针。

```cpp
void cross_validation(const problem *prob, const parameter *param, int nr_fold, double *target);
```

n折交叉验证函数，将结果储存在`target`中。

```cpp
void find_parameters(const struct problem *prob, const struct parameter *param,
                     int nr_fold, double start_C, double start_p,
                     double *best_C, double *best_p, double *best_score);
```

该函数的功能类似于`sklearn`中的`GridSearch`，通过交叉验证寻找最优参数，如果模型没有参数`p`，指定了一个`start_C`作为初始参数$C$之后，模型会以$C,2C,4C,8C,\cdots$的顺序来交叉验证训练模型，获取最优的参数`best_C`；如果模型有`p`和`C`两个参数，那么函数会进行二重循环，外循环将参数$p$依次设置为$\frac{19}{20}p_{max},\cdots,\frac1{20}p_{max},0$，而内部的循环和上面一样，是对最优参数`C`的寻找。

最优参数和最优的模型表现都被赋值到参数指针中，以便于获取。

```cpp
double predict(const struct model *model_, const struct feature_node *x);
double predict_values(const struct model *model_, const struct feature_node *x,
                      double *dec_values);
double predict_probability(const struct model *model_,
                           const struct feature_node *x,
                           double *prob_estimates);
```

三个预测函数接口，第一个函数用于对单个数据进行预测，返回预测值；第二个函数也是对单个数据进行预测，同时将预测值赋到了参数指针上；第三个函数输出的是预测概率（仅适用于逻辑回归模型）。

剩下的函数功能比较明确：

- `get_*`函数，主要是获取模型的信息；
- `check_*`函数，对模型类别进行判断，也是为了防止用户错误指定模型参数；
- 模型的加载、保存、清理函数.

我们不再一一介绍这些函数，一是因为逻辑简单，二是因为和我们的研究方向（优化算法）没有太大关系。

至此，我们完成了`liblinear.h`的解读。
