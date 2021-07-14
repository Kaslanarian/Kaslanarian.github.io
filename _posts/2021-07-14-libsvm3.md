---
layout:     post
title:      ligSVM源码解读（3）
subtitle:   数据存储相关
date:       2021-07-14
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 编程技巧
---

## <center>引言

SVM问题中，空间开销最大的两种数据，一个是训练数据，另一个则是核函数矩阵。由于两者都属于Tabular（表格）数据，因此我们没有必要将两者的实现分离。libSVM中用一个虚基类`QMatrix`表示数据矩阵，而其派生类`Kernel`则用来存储核函数，再往上是对应问题的特殊核函数存储。我们这里对它们进行讲解。

## <center>QMatrix类

我们直接看`QMatrix`类的源码：

```cpp
class QMatrix {
   public:
    virtual Qfloat *get_Q(int column, int len) const = 0;
    virtual double *get_QD() const = 0;
    virtual void swap_index(int i, int j) const = 0;
    virtual ~QMatrix() {}
};
```

里面的函数都是虚函数，因此`QMatrix`是一个虚基类，无法单独使用。我们来看看成员函数的作用：

- `get_Q`：顺序获取SVM问题的$Q$指定**列**的指定个元素；

- `get_QD`：看到后面的代码有这样一句：

  ```cpp
  double quad_coef = QD[i] + QD[j] + 2 * Q_i[j];
  ```

  对应求$K_{ii}-2K_{ij}+K_{jj}$，就明白`QD`的意思是QMatrix Diagonal，为了减少存取的时间消耗，特地用一个浮点数组存储$Q$的对角线元素；

- `swap_index`：交换指定的数据列。

## <center>Kernel类

Kernel类是QMatrix类的继承，用来存储和处理核函数矩阵：

```cpp
class Kernel : public QMatrix {
   public:
    Kernel(int l, svm_node *const *x, const svm_parameter &param);
    virtual ~Kernel();

    static double k_function(const svm_node *x, const svm_node *y,
                             const svm_parameter &param);
    virtual Qfloat *get_Q(int column, int len) const = 0;
    virtual double *get_QD() const = 0;
    virtual void swap_index(int i, int j) const  // no so const...
    {
        swap(x[i], x[j]);
        if (x_square) swap(x_square[i], x_square[j]);
    }

   protected:
    double (Kernel::*kernel_function)(int i, int j) const;

   private:
    const svm_node **x;
    double *x_square;

    // svm_parameter
    const int kernel_type;
    const int degree;
    const double gamma;
    const double coef0;

    static double dot(const svm_node *px, const svm_node *py);
    double kernel_linear(int i, int j) const { return dot(x[i], x[j]); }
    double kernel_poly(int i, int j) const {
        return powi(gamma * dot(x[i], x[j]) + coef0, degree);
    }
    double kernel_rbf(int i, int j) const {
        return exp(-gamma * (x_square[i] + x_square[j] - 2 * dot(x[i], x[j])));
    }
    double kernel_sigmoid(int i, int j) const {
        return tanh(gamma * dot(x[i], x[j]) + coef0);
    }
    double kernel_precomputed(int i, int j) const {
        return x[i][(int)(x[j][0].value)].value;
    }
};
```

先从成员变量开始：

- `x`：指向样本数据的指针；
- `x_square`：只在使用RBF核时用到；
- `kernel_type`：在`svm.h`中提过，略；
- `degree`：同上；
- `gamma`：同上；
- `coef0`：同上.
- `kernel_function`：函数指针，指向核函数.

成员函数：

- 构造函数`Kernel`：

  ```cpp
  Kernel::Kernel(int l, svm_node *const *x_, const svm_parameter &param)
      : kernel_type(param.kernel_type),
        degree(param.degree),
        gamma(param.gamma),
        coef0(param.coef0) {
      switch (kernel_type) {
          case LINEAR:
              kernel_function = &Kernel::kernel_linear;
              break;
          case POLY:
              kernel_function = &Kernel::kernel_poly;
              break;
          case RBF:
              kernel_function = &Kernel::kernel_rbf;
              break;
          case SIGMOID:
              kernel_function = &Kernel::kernel_sigmoid;
              break;
          case PRECOMPUTED:
              kernel_function = &Kernel::kernel_precomputed;
              break;
      }
  
      clone(x, x_, l);
  
      if (kernel_type == RBF) {
          x_square = new double[l];
          for (int i = 0; i < l; i++) 
              x_square[i] = dot(x[i], x[i]);
      } else
          x_square = 0;
  }
  ```

  构造函数做了下面几件事：

  1. 对成员变量中的SVM参数赋值；
  2. 确定核函数；
  3. 复制训练集；
  4. 如果选择RBF核，则令`x_square[i]`为$\pmb x_i^\top\pmb x_i$。

- 析构函数`~Kernel`：释放空间；

- `dot`：实现两个向量的点积；注意到`svm_node`的设计在节约空间的同时优化了计算；

- `k_function`：用来计算$Q$，给定两个向量$\pmb x$和$\pmb y$和核函数$K$，计算$K(\pmb x,\pmb y)$；

- `kernel_linear`，`kernel_poly`，`kernel_rbf`，`kernel_sigmoid`：也是计算对应的核函数，“用于预测步骤”，和`k_function`不同的是参数：`k_function`接受的向量格式是`svm_node*`，`kernel_*`这些函数接受的是给定数据集的序列数：`int i`和`int j`。

## <center>SVC_Q类等

Kernel类只是抽象的核函数存储类，实际上不同的问题有不同的核函数矩阵，比如分类问题下

$$
Q_{ij}\equiv y_iy_jK(\pmb x_i,\pmb x_j)
$$

而在One-class SVM中则是

$$
Q_{ij}\equiv K(\pmb x_i,\pmb x_j)
$$

因此，根据不同问题，libSVM以Kernel为基类又派生出三个类：SVC_Q, ONE_CLASS_Q和SVR_Q，分别对应分类、区间估计和回归问题。

### SVC_Q类

```cpp
class SVC_Q : public Kernel {
   public:
    SVC_Q(const svm_problem &prob, const svm_parameter &param, const schar *y_)
        : Kernel(prob.l, prob.x, param) {
        clone(y, y_, prob.l);
        cache = new Cache(prob.l, (long int)(param.cache_size * (1 << 20)));
        QD = new double[prob.l];
        for (int i = 0; i < prob.l; i++) 
            QD[i] = (this->*kernel_function)(i, i);
    }

    Qfloat *get_Q(int i, int len) const {
        Qfloat *data;
        int start, j;
        if ((start = cache->get_data(i, &data, len)) < len) {
            for (j = start; j < len; j++)
                data[j] =
                    (Qfloat)(y[i] * y[j] * (this->*kernel_function)(i, j));
        }
        return data;
    }

    double *get_QD() const { return QD; }

    void swap_index(int i, int j) const {
        cache->swap_index(i, j);
        Kernel::swap_index(i, j);
        swap(y[i], y[j]);
        swap(QD[i], QD[j]);
    }

    ~SVC_Q() {
        delete[] y;
        delete cache;
        delete[] QD;
    }

   private:
    schar *y;
    Cache *cache;
    double *QD;
};
```

由于每个函数实现语句不多，因此把实现放进类中。我们先看成员变量：

- `y`：是一个`signed char`指针，因为是分类问题，$y_i\in\{-1,+1\}$，因此选择最小的带符号类型`signed char`；
- `cache`：在[libSVM的Caching - 邢存远的博客 | Welt Xing's Blog (welts.xyz)](https://welts.xyz/2021/07/12/cache/)中已经详细解释过；
- `QD`：前面也解释过，$Q$矩阵的对角线元素；

成员函数大部分是对基类虚函数的改写：

- 构造函数：主要任务有

  1. 参数赋值；
  2. 数据集（包括特征向量和标签）的复制；
  3. 初始化缓存和`QD`数组；

- 析构函数：释放占用的空间；

- `get_Q`：获取$Q$矩阵指定行（考虑到对称性，列也可以）的多个元素，注意到分类问题中

  ```cpp
  Q[i][j] == (Qfloat)(y[i] * y[j] * (this->*kernel_function)(i, j));
  ```

  这里的`for`循环其实是由于Cache的未命中而做出的弥补；

- `get_QD`：获取对角线元素数组；

- `swap_index`：将第$i$个数据和第$j$个数据进行调换，对很多变量都要做出调整；

### ONE_CLASS_Q类

和SVC_Q类大同小异，由于没有标签，在`swap_index`也就不需要对$y$进行调换，此外这里的$Q_{ij}$：

```cpp
Q[i][j] = (Qfloat)(this->*kernel_function)(i, j);
```

### SVR_Q类

```cpp
class SVR_Q : public Kernel {
   public:
    SVR_Q(const svm_problem &prob, const svm_parameter &param)
        : Kernel(prob.l, prob.x, param) {
        l = prob.l;
        cache = new Cache(l, (long int)(param.cache_size * (1 << 20)));
        QD = new double[2 * l];
        sign = new schar[2 * l];
        index = new int[2 * l];
        for (int k = 0; k < l; k++) {
            sign[k] = 1;
            sign[k + l] = -1;
            index[k] = k;
            index[k + l] = k;
            QD[k] = (this->*kernel_function)(k, k);
            QD[k + l] = QD[k];
        }
        buffer[0] = new Qfloat[2 * l];
        buffer[1] = new Qfloat[2 * l];
        next_buffer = 0;
    }

    void swap_index(int i, int j) const {
        swap(sign[i], sign[j]);
        swap(index[i], index[j]);
        swap(QD[i], QD[j]);
    }

    Qfloat *get_Q(int i, int len) const {
        Qfloat *data;
        int j, real_i = index[i];
        if (cache->get_data(real_i, &data, l) < l) {
            for (j = 0; j < l; j++)
                data[j] = (Qfloat)(this->*kernel_function)(real_i, j);
        }

        // reorder and copy
        Qfloat *buf = buffer[next_buffer];
        next_buffer = 1 - next_buffer;
        schar si = sign[i];
        for (j = 0; j < len; j++)
            buf[j] = (Qfloat)si * (Qfloat)sign[j] * data[index[j]];
        return buf;
    }

    double *get_QD() const { return QD; }

    ~SVR_Q() {
        delete cache;
        delete[] sign;
        delete[] index;
        delete[] buffer[0];
        delete[] buffer[1];
        delete[] QD;
    }

   private:
    int l;
    Cache *cache;
    schar *sign;
    int *index;
    mutable int next_buffer;
    Qfloat *buffer[2];
    double *QD;
};
```

和分类问题不同，SVR问题中每个样本向量对应的是两个参数$\alpha_i$和$\alpha^*$，从而我们可以在其构造函数中看到它申请了不少长度为两倍样本数的数组。同时它申请了缓冲区，我暂时不明白这些数组的用处，只能从注释中知道它们是为了所谓“重排和复制”。注意到回归问题中的$Q_{ij}$和ONE_CLASS_SVM中相同。

至此我们大致分析完libSVM中的数据存储相关部分，接下来就是问题求解的算法代码了。
