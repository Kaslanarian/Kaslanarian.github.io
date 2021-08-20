---
layout:     post
title:      异常处理：总结
subtitle:   Exception in C++, Java and Python
date:       2021-03-07
author:     Welt Xing
header-img: img/post-bg-desk.jpg
catalog:    true
tags:
    - 编程技术
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

#### try/except

在`Pytohn`中，我们可以用`try/except`语句来捕获异常：

```python
try:
    doSomething
except:
    handleException
```

和C++中的`try/catch`语法相似：

```python
try:
    x = int(input("Input a number: "))
except ValueError:
    print("Not a number input!")
```

一个`except`子句是可以处理多个异常的：

```python
...
except (RuntimeError, TypeError, NameError):
    pass
```

为了应对人为忽略的情况，我们会在最后一个子句收纳所有的异常：

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    '''打印未预料到的异常，然后把异常揪出来'''
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

#### try/except...else

`try/except`还有一个可选的`else`子句，如果使用这个子句，那么必须放在所有的`except`语句之后，它将在`try`语句**未发生任何异常是执行**：

```python
try:
    doSomething
except Error1:
    HandleError1
except Error2:
    HandleError2
...
else:
    print("No exception")
    doMoreThings
```

> 使用`else`子句比把所有的语句都放在`try`子句里面要好，这样可以避免一些意想不到，而`except`又无法捕获的异常。

#### try-finally

这是最完整的异常处理语句：

```python
try:
    doSomething
except Error:
    HandleError
else:
    '''没有异常时会执行的代码'''
    doWithoutException
finally:
    '''不管有没有异常都要执行的代码'''
    doNoMatterException
```

#### 抛出异常

我们发现，`python`中，`try`和C++中的`try`等价，`except`和C++中的`catch`等价。实际上`python`中也有和C++中`throw`近似的关键字：`raise`。

我们用`raise`语句抛出一个指定异常：

```python
raise [Exception [, args [, traceback]]]
```

例如：

```python
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```

这时就会触发异常：

```bash
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
Exception: x 不能大于 5。x 的值为: 10
```

当我们已经捕获一个异常后，如果不想处理它，我们也可以在`except`语句下，仅用`raise`就可以抛出该异常：

```python
>>> try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise
   
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in ？
NameError: HiThere
```

#### 用户自定义异常

我们通过创建`Exception`类的子类，重写方法来拥有自己的异常：

```python
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

# 此时我们触发一个异常：

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)
```

执行后会输出：

```bash
My exception occurred, value: 4
```

> 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类。

#### try/finally：定义清理行为

我们甚至可以忽略`except`子句：

```python
try:
    doSomething
finally:
    cleanBehavior
```

如果一个异常在`try`子句里（或者在`except`和`else`子句里）被抛出，而又没有任何的`except`把它截住，那么这个异常会在`finally`子句执行**后**被抛出。

#### Python断言

`Python`断言的语法很简单：

```python
assert expression
```

等价于：

```python
if not expression:
    raise AssertionError
```

你可以像Java那样在断言中加入信息：

```python
assert 1==2, '1 不等于 2'
```

## Java异常处理

#### Exception类的层次

和`Python`类似，所有异常类都是从`java.lang.Exception`类继承的子类。相关类的继承关系如下：

![Exception的继承](https://www.runoob.com/wp-content/uploads/2013/12/12-130Q1234I6223.jpg)

如上图所示，异常类有两个主要的子类：`IOException`和`RuntimeException`类

#### 两种异常

Java提供了两类主要的异常: `runtime exception`和`checked exception`，也就是运行时异常和检查性异常：

- 对于运行期异常，我们可以不需要处理运行时异常，当出现这样的异常时，总是由JVM接管。比如：我们从来没有人去处理过NullPointerException异常，它就是运行时异常，并且这种异常还是最常见的异常之一。

- 检查性异常，也就是我们经常遇到的IO异常，以及SQL异常都是这种异常。对于这种异常，JAVA编译器强制要求我们必需对出现的这些异常进行catch。所以，面对这种异常不管我们是否愿意，只能自己去写一大堆catch块去处理可能的异常。

#### 捕获异常

使用`try`和`catch`可以捕获异常：

```java
try {
    // 程序代码
} catch (ExceptionName e1) {
    // Catch块
}
```

你会发现这个写法几乎和C++的异常处理一模一样，在此不做赘述。

实例：

```java
import java.io.*;
public class ExceptTest {
    public static void main(String[] args) {
        try {
            int a[] = new int[2];
            System.out.println("Access element three :" + a[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception thrown  :" + e);
        }
        System.out.println("Out of the block");
    }
}
```

上述代码编译运行输出如下：

```bash
Exception thrown  :java.lang.ArrayIndexOutOfBoundsException: 3
Out of the block
```

#### 多重捕获快

类似与C++，Java也支持多重捕获块：

```java
try {
   // 程序代码
} catch (异常类型1 异常的变量名1) {
  // 程序代码
} catch(异常类型2 异常的变量名2) {
  // 程序代码
} catch(异常类型3 异常的变量名3) {
  // 程序代码
}
```

实例：

```java
try {
    file = new FileInputStream(fileName);
    x = (byte) file.read();
} catch(FileNotFoundException f) { // Not valid!
    f.printStackTrace();
    return -1;
} catch(IOException i) {
    i.printStackTrace();
    return -1;
}
```

#### throws/throw关键字

如果一个方法没有捕获到一个检查性异常，那么该方法必须使用`throws`关键字来声明。`throws`关键字放在方法签名的尾部：

```java
public void function(double amount) throws RemoteException,
                                    InsufficientFundsExecption 
{
    // Method implementtation
    if (something) {
        throw new RemoteException();
    }
}
```

在这里`throws`后是函数中可能会出现的问题，标识以便于这样的处理：

```java
try {
    function();
} catch (RemoteException e1) {
    handle exception 1
} catch (InsufficientFundsExecption e2) {
    handle exception 2
}
```

也可以使用`throw`关键字抛出一个异常，无论它是新实例化的还是刚捕获到的，这里就和C++中用法一模一样，不做赘述。

#### finally关键字

和`Python`一样，我们会有一个`finally`语句来创建在`try`代码块后面执行的代码块（无论是否发生异常总会被执行）。在 finally 代码块中，可以运行清理类型等收尾善后性质的语句：

```java
try {
  // 程序代码
} catch(异常类型1 异常的变量名1) {
  // 程序代码
} catch(异常类型2 异常的变量名2) {
  // 程序代码
} finally {
  // 程序代码
}
```

#### 注意

- `catch`不能独立于`try`存在；

- 在`try/catch`后面添加`finally`块并非强制性要求的；

- `try`代码后不能既没`catch`块也没`finally`块；

- `try,`catch,`finally`块之间不能添加任何代码。

#### 声明自定义异常

Java也可以自定义异常，但有以下几点注意：

- 所有异常都必须是`Throwable`的子类；

- 如果希望写一个检查性异常类，则需要继承`Exception`类；

- 如果你想写一个运行时异常类，那么需要继承`RuntimeException`类。

一个常见的做法是自定义一个BaseException作为“根异常”，然后，派生出各种业务类型的异常。

BaseException需要从一个适合的Exception派生，通常建议从RuntimeException派生：

```java
public class BaseException extends RuntimeException {
}
```

其他业务类型的异常就可以从`BaseException`派生：

```java
public class UserNotFoundException extends BaseException {
}

public class LoginFailedException extends BaseException {
}
...
```

自定义的`BaseException`应该提供多个构造方法：

```java
public class BaseException extends RuntimeException {
    public BaseException() {
        super();
    }

    public BaseException(String message, Throwable cause) {
        super(message, cause);
    }

    public BaseException(String message) {
        super(message);
    }

    public BaseException(Throwable cause) {
        super(cause);
    }
}
```

上述构造方法实际上都是原样照抄`RuntimeException`。这样，抛出异常的时候，就可以选择合适的构造方法。通过IDE可以根据父类快速生成子类的构造方法。

#### Java断言

同样，你也可以用`assert`作为程序断言：

```java
assert 1==2;

assert 1==2 : "1不等于2";
```

## 参考

- <https://www.runoob.com/cplusplus/cpp-exceptions-handling.html>

- <http://www.cplusplus.com/reference/exception/exception/what/>

- <https://www.runoob.com/python/python-exceptions.html>

- <https://www.runoob.com/java/java-exceptions.html>
