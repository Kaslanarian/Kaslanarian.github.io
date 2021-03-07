---
layout:     post
title:      异常处理：总结
subtitle:   Exception in C++, Java and Python
date:       2021-03-07
author:     Welt Xing
header-img: img/post-bg-desk.jpg
catalog:    true
tags:
    - Java
    - C/C++
    - Python
---

## 引言

很早之前就学习过`C++`和`Python`的异常处理，最近在`Java`学习中遇到了异常处理的知识点，所以将三门较为通用的语言的异常处理机制作出总结和比较。

## 术语回顾

蒋炎岩老师在讲解调试理论时介绍过三个计算机术语的含义与差异，在此进行回顾：

1. 错误（Error）：一般是在意料中可能出现问题的地方出现了问题，导致实际情况偏离了期望。比如`Linux`中常见的`Error : No such file or directory`；

2. 故障（Fault）：程序中出现非故意的、不可预料的行为。fault通常是由error导致的。比如`Segmentation Fault`（段错误）；

3. 失败（Failure）：一个系统或者组件不能完成它被要求的功能。failure通常是由fault导致的。比如Java中的`Build failed`。

一言以蔽之就是，人为的`error`导致程序出现不可预料的`fault`，最终使得整个程序系统`failed`。而异常处理的目的，是在出现人为`error`后防止`fault`的发生，进而避免`failure`。

## C的异常处理？

我在学习`C`的时候就发现它并没有类似`C++`的异常处理机制，但并不代表无法进行错误处理，在C标准库[`error.h`](https://zh.wikipedia.org/wiki/Errno.h)中就定义了很多错误码（$error\;\;code$）来辅助错误处理。当然我们也可以自己设置，我的`matrix-C`中的客户程序就采用了这种方式：

```cpp
enum error_type {
    EVENT_BAD_EXPR,             // 输入表达式不规范
    EVENT_DEVIDE_ZERO,          // 计算式除以0
    EVENT_NO_EXPR,              // 无输入
    EVENT_MATCH_FAIL,           // 正则表达式匹配错误
    EVENT_OPERATOR_NOT_FOUND,   // 输入无法识别的运算符
    EVENT_NOT_ASSIGN_SYNTAX,    // 无法识别的命令
    EVENT_UNDEFIND,             // 变量未定义
    EVENT_SHAPE_DIFF,           // 矩阵加减时形状不同
    EVENT_MUL_SHAPE_DIFF,       // 矩阵乘法中矩阵尺寸不合规范
    EVENT_INV_SHAPE_DIFF,       // 矩阵除法时矩阵尺寸不和规范
    EVENT_INV_DET_ZERO,         // 对一个行列式为0的矩阵求逆
    EVENT_POW_PARAM_FALSE,      // 矩阵幂的第二个操作符类型错误
};
```

大致流程如下，我们会在执行指令的时候遇到错误，此时就会修改`error_code`，注册异常

```pseudocode
error_code = -1 // no error
while true {
    enter command
    excute command while assigning error_code
    handle error code
}
```

缺点？在C语言里，使用返回值等方式来处理错误，实际上很容易变成Bug的温床，因为没有强制性的检查，很容易被开发者疏忽。另外，可读性非常差，处理错误的代码和正常代码交织在一起，陷入「错误地狱」。

## C++中的异常处理

C++异常处理涉及三个关键字：`try`、`catch`和`throw`：

- `throw`：意思是“抛出”异常；

- `catch`：在可能会出现`error`的地方，用于“捕获”异常；

- `try`：try块中的代码标识将被激活的特定异常，它后面通常跟着一个或多个`catch`块。

#### 抛出异常

程序实例，下面是一个实现整型除法的函数：

```cpp
int division(int a, int b) {
    if (b == 0) {
        // 这里可以是任意的表达式
        // 表达式的结果的类型决定了抛出的异常的类型
        throw "Division by zero exception";
    }
    return a / b;
}

int main() {
    division(1, 0);
}
```

`Linux`下会输出：

```bash
terminate called after throwing an instance of 'char const*'
[1]    52704 abort (core dumped)  ./test
```

我们`throw`了一个字符串字面量，所以是`char const*`的实例，我们当然可以改为其他类型，此时终端输出也会有差异。

#### 捕获异常

`catch`常常和`try`一起使用，用于捕获异常。我们可以指定要捕捉的异常类型：

```cpp
try {
    TODO();
} catch (ExceptionName1 e1) {
    HandleException1
} catch (ExceptionName1 e2) {
    HandleException2
} ...
```

在上面的代码中，如果出现了类型为`ExceptionName1`的异常，就会跳到第一个`catch`块中进行处理，以此类推。如果想让`catch`块能够处理`try`块抛出的任何类型的异常，则必须在异常声明的括号内使用省略号...：

```cpp
try {
    TODO();
} catch (...) {
    HandleAllException
}
```

我们试着将三个关键字综合起来使用：

```cpp
#include <iostream>
using namespace std;

double division(double a, double b) {
    if (b == 0) {
        throw "Division by zero exception";
    }
    return a / b;
}

int main() {
    double a, b, c;
    while (cin >> a >> b) {
        try {
            c = division(a, b);
            cout << c << endl;
        } catch (const char* msg) {
            cerr << msg << endl;
        }
    }
}
```

输入一对`a`和`b`，输出其相除结果，如果除数为0则输出异常信息。由于我们抛出了一个类型为`const char*`的异常，因此，当捕获该异常时，我们必须在`catch`块中使用`const char*`。

#### C++标准异常

C++提供了一系列标准的异常，定义在`<exception>`中，我们可以在程序中使用这些标准的异常。它们是以父子类层次结构组织起来的，如下所示：

![标准异常](https://www.runoob.com/wp-content/uploads/2015/05/exceptions_in_cpp.png)

在上面的程序中，我们实现了一个简单的异常处理，但这种字符串型的异常并不标准，我们可以看看`vscode`所提供的异常处理代码补全：

```cpp
try {
    /* code */
} catch (const std::exception& e) {
    std::cerr << e.what() << '\n';
}
```

`e.what()`方法返回对应标准异常的提示信息。

#### 自定义异常

我们可以通过继承和重载`exception`类来定义新的异常：

```cpp
#include <exception>
#include <iostream>

struct ooops : std::exception {
    const char* what() const noexcept { return "Ooops!"; }
};

int main() {
    try {
        throw ooops();
    } catch (const std::exception& ex) {
        std::cerr << ex.what() << '\n';
    }
    return 0;
}
```

我们将`ooops`作为`exception`类的子类，然后对`what`的方法进行重写，以输出自定义信息，也就是异常发生原因。

> 无抛出保证：你也许注意到了`noexcept`关键字，它被用来规定成员函数永远不会抛出异常，这也这也适用于C ++标准库中的所有派生类，在C++98中，写法是：`cosnt char* what() const throw();`。

#### 关于断言

除此之外，断言是更简单更粗暴的一种异常处理，你可以在[这里](https://welts.xyz/matrix-c/2021/02/20/matrix1/#%E5%8A%9F%E8%83%BD%E6%80%A7%E7%9A%84%E5%AE%8F)的`Assert`获取加强版的断言。

## Python异常处理

## 参考

- <https://www.runoob.com/cplusplus/cpp-exceptions-handling.html>

- <http://www.cplusplus.com/reference/exception/exception/what/>

- <https://www.runoob.com/python/python-exceptions.html>
