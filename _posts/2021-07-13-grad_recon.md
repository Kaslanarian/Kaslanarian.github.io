---
layout:     post
title:      梯度重构
subtitle:   在SVM中的应用
date:       2021-07-13
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 机器学习
---

## <center>引言

Joachims在《Making Large Scale SVM Learning Practical》中提出了三个解决SVM训练时间长问题的解决思路：

- 采用更有效的方法去选择工作集（Working set selection）;
- 采用收缩法（Shrinking）去减小数据规模；
- 采用计算上的技巧来提升效率，比如缓存（Caching）和梯度的增量式更新（Incremental updates of the gradient）.

我们这里来讨论梯度增量式更新及其在libSVM中的使用。

## <center>一个例子

在线性回归中，我们要解决的是下面的优化问题：

$$
\min_{\pmb w}\quad f(\pmb w)=\dfrac{1}{2}\|\pmb X\pmb w-\pmb y\|^2
$$

该问题固然是有解析解的，但倘若我们用梯度下降法，给定步长$\eta$，在每轮迭代中都有下面的操作：

$$
\begin{aligned}
\pmb w\gets\pmb w-\eta\dfrac{\partial f}{\partial\pmb w}
\end{aligned}
$$

也就是

$$
\pmb w\gets\pmb w-\eta\pmb X^\top(\pmb X\pmb w-\pmb y)
$$

如果不采用任何优化方法的话，我们每次都要计算一次$\pmb X^\top(\pmb X\pmb w-\pmb y)$；而实际上相邻两次更新之间梯度变化量是一个很简单的值：

$$
\begin{aligned}
\Delta\nabla f(\pmb w)&=\nabla f(\pmb w+\Delta\pmb w)-\nabla f(\pmb w)\\
&=\pmb X^\top\big(\pmb X(\pmb w+\Delta\pmb w)-\pmb y \big)-\pmb X^\top\big(\pmb X\pmb w-\pmb y \big)\\
&=\pmb X^\top\pmb X\Delta\pmb w
\end{aligned}
$$

如果我们能将$\pmb X^\top\pmb X$存储，那么花费在梯度计算上的时间会更少。这就是梯度的增量式更新带来计算负担减少的一个例子。

## <center>在SVM中的应用

虽然SVM主流的解法并不使用梯度下降，但其梯度仍会被使用，比如用在工作集选择上，每轮迭代都需要更新。对于其对偶优化问题的目标函数对应的梯度分量：

$$
\nabla f(\pmb\alpha)_i=\sum_{j=1}^l\pmb\alpha_jy_iy_jK_{ij}-1
$$

类似的，如果每次都对上式重新计算，对应的计算量是巨大的，因为$l$对应的是训练集样本数。因此Joachims引入变量$s$：

$$
s_i^{(t)}=\sum_{j=1}^l\pmb\alpha_j y_jK_{ij}
$$

从而其迭代式：

$$
s_i^{(t)}=s_i^{(t-1)}+\sum_{j\in B}(\alpha_j^{(t)}-\alpha_j^{(t-1)})y_jK_{ij}
$$

我们只需要稍加操作就能得到对应梯度：

$$
\nabla f(\pmb\alpha)_i^{(t)}=y_is_{i}^{(t)}-1
$$

注意到我们只需要对工作集中的$i$进行操作，因为工作集外都是固定量。

## <center>libSVM中的梯度重构

libSVM继承了Joachims在SVM-Light中使用的增量更新思想，分别对工作集和非工作集的梯度进行更新。对工作集中变量对应的梯度的更新：

```cpp
double delta_alpha_i = alpha[i] - old_alpha_i;
double delta_alpha_j = alpha[j] - old_alpha_j;

for (int k = 0; k < active_size; k++) {
    G[k] += Q_i[k] * delta_alpha_i + Q_j[k] * delta_alpha_j;
}
```

这里我们刚完成对$\alpha_i$和$\alpha_j$的更新，`delta_alpha_j`和`delta_alpha_j`是对应的变化量；这里的`active_size`指的是处在$(0,C)$，也就是没到边界的$\alpha_i$的数量。因为对于到达了边界（$0$或$C$）的参数，其值就不再发生变化，我们称这种变量是“inactive”的；`active_size`也需要每次迭代时实时更新。

这里的`G[k]`对应的就是$\nabla f(\pmb x)_k$，`Q_i[k]`就是$y_iy_kQ_{ik}$，可以发现符合数学语义。

但我们仍然需要这些inactive的参数对应的梯度，也就是全部的$\nabla f(\pmb x)$，为了减少梯度重构的开销，libSVM选择在迭代中维护一个向量$\bar{G}\in\mathbb{R}^l$：

$$
\bar{G}_i=C\sum_{j:\alpha_j=C}Q_{ij},i=1,\cdots,l
$$

从而对于不属于active集合的变量$\alpha_i$，我们有

$$
\begin{aligned}
\nabla f(\pmb\alpha)_i&=\sum_{j=1}^lQ_{ij}\alpha_j-1\\
&=\sum_{\alpha_j=0}Q_{ij}\cdot0+\sum_{\alpha_j=C}CQ_{ij}+\sum_{0<\alpha_j<C}Q_{ij}\alpha_j-1\\
&=C\sum_{\alpha_j=C}Q_{ij}+\sum_{0<\alpha_j<C}Q_{ij}\alpha_j-1\\
&=\bar{G}_i+\sum_{0<\alpha_j<C}Q_{ij}\alpha_j-1\\
\end{aligned}
$$

实现通过提前计算$\bar{G}$加快计算梯度：

```cpp
{
    bool ui = is_upper_bound(i);
    bool uj = is_upper_bound(j);
    update_alpha_status(i);
    update_alpha_status(j);
    int k;
    if (ui != is_upper_bound(i)) {
        Q_i = Q.get_Q(i, l);
        if (ui)
            for (k = 0; k < l; k++) 
                G_bar[k] -= C_i * Q_i[k];
        else
            for (k = 0; k < l; k++) 
                G_bar[k] += C_i * Q_i[k];
    }

    if (uj != is_upper_bound(j)) {
        Q_j = Q.get_Q(j, l);
        if (uj)
            for (k = 0; k < l; k++) G_bar[k] -= C_j * Q_j[k];
        else
            for (k = 0; k < l; k++) G_bar[k] += C_j * Q_j[k];
    }
}
```

这里对更新进行限制：只有状态发生变换的变量，才能参与$\bar{G}$的更新，这是为了减少循环次数。如果`ui`是false，也就是$\alpha_i$从active变成inactive，对应的就是将对应的增量加入$\bar{G}$，反之就是从$\bar{G}$中对应$\alpha_i$的增量删除。
