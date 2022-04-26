---
layout:     post
title:      NumPy的广播机制
subtitle:   解析与实现
date:       2022-04-26
author:     Welt Xing
header-img: img/numpy.jpg
catalog:    true
tags:
    - Python
---

前篇：<https://welts.xyz/2021/04/26/numpy_dim/>.

我们在前面研究了NumPy在0,1,2维下的广播。但广播算法在NumPy的[文档](https://numpy.org/doc/stable/user/basics.broadcasting.html)中已经进行了充分的说明，我们在这里进行汉化和解读，以及测试。

先对NumPy数组的属性做一些规定，首先是`ndarray.shape`，我们称其为“形状”；`ndarray.ndim`被称为数组的“维数”，其实就是`len(ndarray.shape)`；数组的维数通常是反着数，比如一个`shape`为`(2, 3, 4)`的数组，其第一维有4块数组，第二维有3块数组，第三维有2块数组。

## 一般广播的shape

这里的一般广播，也就是针对加减乘除的广播，我们会在后面介绍面向矩阵乘法（`matmul`）的广播。针对两个ndarray，NumPy广播的可行的条件是两数组相同维数下的数组块数必须满足

1. 相同；
2. 其中一个为1

中的一个。比如，对于下面的数组

```python
import numpy as np

a = np.random.randn(2, 3, 4) # a.shape is (2, 3, 4)
b = np.random.randn(1, 4)    # b.shape is (1, 4)
c = a + b
```

我们对维度进行右对齐：

```python
(2, 3, 4)
(   1, 4)
```

从右边起，由于两个数组的第一维都是4，满足条件1；再往左看，两个数组的第二维中有一个是1，满足条件2。由于此时数组`b`维数只有2，所以判定程序结束，两个数组可以进行广播，`c.shape`为$(2, 3, 4)$。由此，我们可以写出广播机制的大致流程：

```python
import numpy as np

def judge_broadcast_shape(a: np.ndarray, b: np.ndarray) -> tuple:
    a = np.array(a)
    b = np.array(b)
    shape_a = list(a.shape)
    shape_b = list(b.shape)
    new_shape = []
    for i in range(1, min(a.ndim, b.ndim) + 1):
        if shape_a[-i] != shape_b[-i] and shape_a[-i] != 1 and shape_b[-i] != 1:
            return False
        else:
            new_shape.insert(0, max(shape_a[-i], shape_b[-i]))
    if a.ndim > b.ndim:
        longer_shape = shape_a
    elif a.ndim < b.ndim:
        longer_shape = shape_b
    else:
        return tuple(new_shape)

    return tuple(longer_shape[:len(longer_shape) - len(new_shape)] + new_shape)
```

我们进行一些测试（取自官方文档）：

```python
def test_broadcast_shape(a: np.ndarray, b: np.ndarray):
    # 左边是NumPy广播机制的结果，右边是我们的判别结果
    print("True shape : {:}, Our shape : {:}".format(
        (a + b).shape,
        judge_broadcast(a, b),
    ))

from numpy.random import randn

test_list = [
    (randn(256, 256, 3), randn(3)),
    (randn(8, 1, 6, 1), randn(7, 1, 5)),
    (randn(5, 4), randn(1)),
    (randn(5, 4), randn(4)),
    (randn(15, 3, 5), randn(15, 1, 5)),
    (randn(15, 3, 5), randn(3, 5)),
    (randn(15, 3, 5), randn(3, 1)),
]

for test_arrays in test_list:
    test_broadcast_shape(*test_arrays)
```

输出：

```python
Right shape : (256, 256, 3), Our shape : (256, 256, 3)
Right shape : (8, 7, 6, 5), Our shape : (8, 7, 6, 5)
Right shape : (5, 4), Our shape : (5, 4)
Right shape : (5, 4), Our shape : (5, 4)
Right shape : (15, 3, 5), Our shape : (15, 3, 5)
Right shape : (15, 3, 5), Our shape : (15, 3, 5)
Right shape : (15, 3, 5), Our shape : (15, 3, 5)
```

发现我们的判定算法是正确的。

## 矩阵乘法广播的shape

矩阵乘法，也就是`matmul`，也存在广播机制。简单的NumPy矩阵乘法就像下面这样：

```python
from numpy.random import randn
from numpy import matmul

a = randn(3, 4)
b = randn(4, 5)
c = matmul(a, b) # 或者写成 a @ b
```

对于两个二维的`ndarray`，`matmul`遵从数学上矩阵的乘法规则。而对于两个更高维（超过两维）的数组，那么NumPy会取两个数组的前两个维度，判定是否符合矩阵乘法的规定，然后更高的维度按照上面一般广播运算处理。比如数组：

```python
a = randn(3, 4)
b = randn(3, 4, 5)
c = matmul(a, b) # c.shape为(3, 3, 5)
```

注意操作数组中存在一维数组的情形，比如

```python
a = randn(3, 4)
b = randn(4)
c = matmul(a, b) # c.shape为(3,)

d = randn(3)
e = randn(3, 4)
f = matmul(d, e) # f.shape为(4,)

g = randn(3)
h = randn(3)
i = matmul(g, h) # i.shape为(,)
```

可以看出`matmul(a, b)`在操作数为一维数组时的处理方法：

1. `a`为一维数组时，将其视作行向量，或者说，将其进行升维成`(1, m)`这样形状的数组去执行矩阵乘法，结果的形状理应是`(..., 1, n)`，其中`n`是`b`最后一个维度，但真正的结果会将那个"1维"删掉；
2. `b`为一维数组时，将其视作列向量，或者说，将其进行升维成`(m, 1)`这样形状的数组去执行矩阵乘法，结果的形状理应是`(..., n, 1)`，其中`n`是`a`第一个维度，但真正的结果会将那个"1维"删掉。

举例：

```python
a = randn(3, 4, 5)
b = randn(5)
c = matmul(a, b) # c.shape should be (3, 4)
```

类似的，我们也可以将上面的逻辑写出来：

```python
def judge_matmul_broadcast_shape(a: np.ndarray, b: np.ndarray):
    shape_a = list(a.shape)
    shape_b = list(b.shape)
    if a.ndim == 0 and b.ndim == 0:
        # matmul不允许零位数组
        return False
    elif a.ndim == 1 and b.ndim == 1:
        if shape_a[0] != shape_b[0]:
            return False
        return ()
    elif a.ndim >= 2 and b.ndim >= 2:
        # 判断矩阵乘法合法性
        mat_dim_a = shape_a[-2:]
        mat_dim_b = shape_b[-2:]
        if mat_dim_a[1] != mat_dim_b[0]:
            return False
        mat_dim = [mat_dim_a[0], mat_dim_b[1]]
        broadcast_shape = judge_broadcast(a[..., 0, 0], b[..., 0, 0])
        if broadcast_shape == False:
            return False
        return tuple(list(broadcast_shape) + mat_dim)
    elif a.ndim == 1:
        if shape_a[0] != shape_b[-2]:
            return False
        return tuple(shape_b[:-2] + shape_b[-1:])
    else:
        if shape_a[-1] != shape_b[0]:
            return False
        return tuple(shape_a[:-1])
```

类似的，做一些`matmul`测试：

```python
matmul_test_list = [
    (randn(3, 4), randn(4, 5)),  # 一般矩阵
    (randn(5, 4, 5, 4), randn(4, 4, 1)),  # 高维张量
    (randn(3, 4, 5), randn(5)),  # 其中一个操作数维数为1
    (randn(4), randn(3, 4, 5)),  # 其中一个操作数维数为1
    (randn(3), randn(3)),  # 2个操作数维数为1
]

def test_matmul_broadcast_shape(a: np.ndarray, b: np.ndarray):
    # 左边是NumPy广播机制的结果，右边是我们的判别结果
    print("Right shape : {:}, Our shape : {:}".format(
        (a @ b).shape,
        judge_matmul_broadcast(a, b),
    ))


for a, b in matmul_test_list:
    test_matmul_broadcast(a, b)
```

测试结果：

```python
Right shape : (3, 5), Our shape : (3, 5)
Right shape : (5, 4, 5, 1), Our shape : (5, 4, 5, 1)
Right shape : (3, 4), Our shape : (3, 4)
Right shape : (3, 5), Our shape : (3, 5)
Right shape : (), Our shape : ()
```

说明我们自设计的广播规则是正确的。

## 一般广播求值

在求得一般广播的shape变化规则后，我们考虑手动实现NumPy的广播机制，即求出广播之后的数组值。比如两个数组

```python
import numpy as np

x = np.array([[1, 2, 3]])
y = np.array([[1], [2], [3], [4]])
z = x + y
```

两数组的形状：

```python
(1, 3)
(4, 1)
```

所以可以广播，`z`的形状是`(4, 3)`。广播的重点在于“复制”，`y`的第一维只有一块数组，而`x`的第一维有3块数组，所以需要沿着`y`的第一维进行复制，即从`(4, 1)`复制成`(4, 3)`：

```python
[
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4],
]
```

这就是我们进行的”广播“。现在看第二维，类似的，我们需要将`x`沿着行方向进行广播：

```python
[
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]
```

两个数组的形状被补全，此时进行加减乘除，不再需要广播运算：

```python
[
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4],
] + [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
] = [
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
]
```

我们再考虑操作数数组的维数不等长的情形，比如本文一开始的例子：

```python
import numpy as np

a = np.random.randn(2, 3, 4)
b = np.random.randn(1, 4)
c = a + b
```

从右往左看，第一维都是4，不需要广播；`b`的第二维只有一块数组，所以`b`需要广播成`(3, 4)`的数组，再往左看，`a`比`b`多出一个维度，那么此时`b`应当将其维数拓展成`(1, 3, 4)`，然后再广播成`(2, 3, 4)`，此时两数组的形状相同，故可直接进行加法。

据此，我们也可写出手动广播的函数：

```python
def broadcast(a: np.ndarray, b: np.ndarray):
    if a.ndim < b.ndim:
        b, a =  broadcast(b, a)
        return a, b
    # a.ndim >= b.ndim，对b升维
    for _ in range(a.ndim - b.ndim):
        b = b[np.newaxis, :]
    shape_a = a.shape
    shape_b = b.shape
    for i in range(1, b.ndim + 1):
        if shape_a[-i] != shape_b[-i] and shape_a[-i] != 1 and shape_b[-i] != 1:
            return None
        elif shape_a[-i] == 1:
            a = np.repeat(a, shape_b[-i], -i)
        elif shape_b[-i] == 1:
            b = np.repeat(b, shape_a[-i], -i)

    assert a.shape == b.shape
    return a, b
```

我们进行用上面的例子进行测试：

```python
def test_broadcast(a: np.ndarray, b: np.ndarray) -> bool:
    # 判断是否相等
    bc_a, bc_b = broadcast(a, b)
    return (a + b == bc_a + bc_b).all()

for a, b in test_list:
    print(test_broadcast(a, b))
```

输出

```python
True
True
True
True
True
True
True
```

说明我们成功实现了广播算法。

## 矩阵乘法广播求值

类似的，我们也可以实现矩阵乘法广播求值（分四种情况）：

```python
def matmul_broadcast(a: np.ndarray, b: np.ndarray):
    assert a.ndim != 0 and b.ndim != 0

    def broadcast(a: np.ndarray, b: np.ndarray):
        if a.ndim < b.ndim:
            b, a = broadcast(b, a)
            return a, b
        for _ in range(a.ndim - b.ndim):
            b = b[np.newaxis, :]
        shape_a = a.shape
        shape_b = b.shape
        for i in range(3, b.ndim + 1): # 这里是对2维以后的维数进行广播
            if shape_a[-i] != shape_b[-i] and shape_a[-i] != 1 and shape_b[
                    -i] != 1:
                return None
            elif shape_a[-i] == 1:
                a = np.repeat(a, shape_b[-i], -i)
            elif shape_b[-i] == 1:
                b = np.repeat(b, shape_a[-i], -i)
        assert a.shape[:-2] == b.shape[:-2]
        return a, b

    if a.ndim == 1 and b.ndim == 1:
        return a @ b
    elif a.ndim == 1:
        a = a[np.newaxis, :]
        a, b = broadcast(a, b)
        c = a @ b
        return c.reshape(c.shape[:-2] + c.shape[-1:])
    elif b.ndim == 1:
        b = b[:, np.newaxis]
        a, b = broadcast(a, b)
        c = a @ b
        return c.reshape(c.shape[:-1])
    else:
        a, b = broadcast(a, b)
        return a @ b
```

使用`matmul_test_list`进行测试：

```python
for a, b in matmul_test_list:
    print((a @ b == matmul_broadcast(a, b)).all())
```

输出

```python
True
True
True
True
True
```

说明我们设计的矩阵广播也是没有问题的。
