---
layout:     post
title:      libSVM源码解读（2）
subtitle:   编程技巧
date:       2021-07-14
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 编程技巧
---
## <center>引言

libSVM中有很多程序设计手法值得我们去学习，会为我们后面的程序设计工作带来帮助，在此进行收集和总结。

## <center>模板

libSVM使用了模板（template）去编写基础的函数，先是求极大极小的函数：

```cpp
#ifndef min
template <class T>
static inline T min(T x, T y) {
    return (x < y) ? x : y;
}
#endif

#ifndef max
template <class T>
static inline T max(T x, T y) {
    return (x > y) ? x : y;
}
#endif
```

注意到这里的预编译语句：只有标准库没有`min`和`max`函数的情况下才会调用模板，因为不是所有编译器都十分支持泛型编程（比如Microsoft VC++）。还注意到函数用`static inline`装饰，有效减少调用函数时的开销。

包括下面的`swap`函数：

```cpp
template <class T>
static inline void swap(T &x, T &y) {
    T t = x;
    x = y;
    y = t;
}
```

事实上C++的标准库中已经支持泛型的`swap`函数，编写者将这些基本函数自己重编写，估计是为了减少对库函数的依赖，从而支持多平台。

最后一个模板函数是`clone`：

```cpp
template <class S, class T>
static inline void clone(T *&dst, S *src, int n) {
    dst = new T[n];
    memcpy((void *)dst, (void *)src, sizeof(T) * n);
}
```

属于深拷贝，`dst`和`src`只是内容相同，此外没有任何联系。

## <center>宏定义

```cpp
#define Malloc(type, n) (type *)malloc((n) * sizeof(type))
```

我们知道在C++中申请空间标准是用`new`，C中才是用`malloc`函数族。作者把`malloc`封装起来，我认为是让C++程序更加规范。

## <center>数学函数

libSVM中幂次函数的设计颇为巧妙：

```cpp
static inline double powi(double base, int times) {
    double tmp = base, ret = 1.0;

    for (int t = times; t > 0; t /= 2) {
        if (t % 2 == 1) ret *= tmp;
        tmp = tmp * tmp;
    }
    return ret;
}
```

我们以求解$a^5$为例：

| `ret` | `tmp` | `t`  |
| :---: | :---: | :--: |
|  $1$  |  $a$  | $5$  |
|  $a$  | $a^2$ | $2$  |
|  $a$  | $a^4$ | $1$  |
| $a^5$ | $a^4$ | $0$  |

从上往下为循环过程。实际上就是分治算法：

$$
\begin{aligned}
a^{2k+1}&=a\cdot(a^2)^k\\
a^{2k}&=(a^2)^k
\end{aligned}
$$

直接相乘的复杂度为$O(n)$，$n$为幂次，该算法则是$O(\log n)$。

## <center>虚函数

虚函数是C++面向对象中多态的一个著名特性。C++基类定义的虚函数，在其派生类中如果进行了改写，但基类指针指向派生类对象，或基类引用绑定了派生类对象时，调用的虚函数是派生类中改写的函数：

```cpp
class Base {
  public:  
    virtual void virfunc() {}
};

class Derived : public Base {
  public:
	virtual void virfunc() {
        printf("Hello world");
    } 
};

Base* a = new Derived();
a->virfunc(); // 输出Hello world
```

而如果无法对基类中的虚函数进行定义，我们将其进行抽象成“纯虚函数”：

```cpp
class Base {
  public:  
    virtual void virfunc() = 0;
};
```

类似于Java中的接口（Interface），无法独自调用该函数，除非被派生类改写。

这一部分还有可以深挖的地方，比如虚函数表和虚函数指针是C++面试中的常见问题。
