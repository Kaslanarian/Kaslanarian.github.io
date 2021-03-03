---
layout:     post
title:      Java Notebook
subtitle:   学习记录
date:       2021-03-03
author:     Welt Xing
header-img: img/java_header.jpg
catalog:    true
tags:
    - Java
---

# Java Learning Note

## 导语

去年的人工智能导论中就已经接触过`Java`，在那之前还学习过一段时间，但随着时间推移内容已经忘了不少，只记得基础的语法，今年的$KR\&P$还是要用到`Java`，故在学期初期事情比较少的时候进行学习和整理。同时，作为一门流行至今的程序设计语言，会总比不会好。

## Java的运行过程

自从学习过《计算机系统基础》之后，对程序设计语言的了解不再满足于仅仅编写出`Hello World`，而是想知道程序的运行过程。

我们来看看Java的编译和运行过程：

![Java运行过程](/img/java_process.png)

Java程序既是编译型，又是解释型的：

1. 程序代码经过编译之后转换为称作Java字节码的中间语言；

2. Java虚拟机(JVM)对字节码进行解释(解释成机器码)和运行。

3. 编译一次但解释在每次运行程序时都会进行。

明白这一过程，我们就可以弄清`JDK`和`JRE`的区别了：

* JRE : Java runtime environment，它提供了Java的**运行**环境，也就是说，它只能运行编译好的字节码，而不能让程序被编译成字节码，有了JRE我们就可以运行Java程序，比如[Logisim](https://vlab.ustc.edu.cn/guide/doc_logisim.html);

* JDK : Java development kit，是程序员使用java语言编写java程序所需的开发工具包，是提供给程序员使用的。JDK包含了JRE，同时还包含了编译java源码的编译器javac，还包含了很多java程序调试和分析的工具：jconsole，jvisualvm等工具软件，还包含了java程序编写所需的文档和demo例子程序。——摘自[知乎问答](https://www.zhihu.com/question/20317448/answer/14737358)

## Hello World

这里，我们将不再依赖一键编译运行工具，例如`code-runner`，一些IDE等去运行一个`Hello World`，而是通过自己的理解去用命令行写出来：

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}
```

我们已经知道，`javac`就是前面所说的编译器，而`java`是解释器：

```bash
>> tldr java
 - Execute a java .class file that contains a main method by using just the class name:
   java {{classname}}
...

>> tldr javac
 - Compile a .java file:
   javac {{file.java}}
...
```

那么我们需要做什么？先编译后运行：

```bash
>> javac Main.java # 会生成Main.class文件
>> java Main       # 运行的是Main这个类
Hello world
```

运行成功！

## 简单语法复习

该部分着重强调的是`Java`语法与`C/C++`，`Python`语法的区别和联系，便于笔者记忆和学习，建议有一定`C/C++`语言基础的读者观看。

#### 基本数据类型

##### 整数类型

- 八进制表示：以0开头，`0123`就是十进制的`83`；

- 多出一个`byte`类型表示`int8`；

##### 浮点类型

- 小数默认被看做`double`，如果想要是`float`就要在后面加上`f`或者`F`
    
    ```java
    float f1 = 13.23f;
    double d1 = 4562.12d;
    double d2 = 45678.1564;
    ```

##### 字符类型

- Java里的`char`占两个字节，是`C/C++`的两倍，使得java的字符几乎可以处理所有国家的语言文字:

    我们若在`C`中运行下面的程序：

    ```c
    int main() {
        char c = '你';
        printf("%c\n", c);
        return 0;
    }
    ```

    程序会报错，因为此时字符‘你’不在ASCII表内，属于`overflow`；

    但在Java中：

    ```java
    public static void main(String[] args) {
        char c = '你';
        System.out.println(c);
    }
    ```

    程序会正确输出‘你’，这就是差异。

##### 布尔类型

- 此处的布尔类型为`boolean`，而不是`C++`中的`bool`，但两个字面量`true`和`false`是相同的。

#### 变量和常量

##### 常量的声明

Java中我们用`const`关键字声明一个常量，而且常量是否为成员变量会影响其用法：

```java
public class Main {
    static final int member_final = 1;
    public static void main(String[] args) {
        final int local_final;
        local_final = 2;
        System.out.println(local_final);
    }
}
```

- 如果`member_final`(成员常量)只声明不赋值，那么会报错；

- 如果`local_final`(局部常量)只声明不赋值是可以的，但之后必须被赋值，也只能被赋值一次，否则报错；