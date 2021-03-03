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

我们将不再依赖一键编译运行工具，例如`code-runner`，一些IDE等去运行一个`Hello World`，而是通过自己的理解去用命令行写出来：

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
>> javac Main.java # Main.class文件
>> java Main
Hello world
```

运行成功！

## 简单语法复习

该部分着重强调的是`Java`语法与`C/C++`，`Python`语法的区别和联系，便于笔者记忆和学习，建议有一定`C/C++`语言基础的读者观看。

