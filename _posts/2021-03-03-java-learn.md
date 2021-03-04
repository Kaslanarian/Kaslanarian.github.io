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

### 基本数据类型

#### 整数类型

- 八进制表示：以0开头，`0123`就是十进制的`83`；

- 多出一个`byte`类型表示`int8`；

#### 浮点类型

- 小数默认被看做`double`，如果想要是`float`就要在后面加上`f`或者`F`
    
    ```java
    float f1 = 13.23f;
    double d1 = 4562.12d;
    double d2 = 45678.1564;
    ```

#### 字符类型

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

#### 布尔类型

- 此处的布尔类型为`boolean`，而不是`C++`中的`bool`，但两个字面量`true`和`false`是相同的。

### 变量和常量

#### 常量的声明

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

### 运算符

- Java中自增自减运算符存在，用法与`C/C++`相同；

- Java中移位操作多出一个`>>>`，意思是无符号右移。

### 流程控制

- Java也有switch-case，语法与C相同，但多出对**字符串**类型的支持；

- Java有和C++类似的基于范围for循环：

    ```java
    int arr[] = {7, 10, 1};
    for (int x : arr) {
        System.out.println(x);
    }
    ```

### 字符串

#### 构造方法

常用的字符串构造方法：(字符串使用前必须经过初始化，否则报错)

- 用字符数组初始化

    ```java
    char a[] = {'w', 'e', 'l', 't'};
    String s = new String(a);
    ```

- 提取字符数组初始化

    ```java
    char a[] = {'w', 'e', 'l', 't'};
    String s = new String(a, 1, 2); // 偏移1，取2个，也就是"el"
    ```

- 字符串常量的引用赋值

    ```java
    String s1, s2;
    s1 = "welt";
    s2 = "welt";
    ```

    这里是`s1`和`s2`**指向同一段内存空间**，该内存空间存储的是字符串"welt"。

#### 常用用法

- `String`之间可以相互连接，用'+'即可；此外，还可以连接其他数据类型，过程是调用`toString()`方法，然后再连接；

- 字符串查找：`indexOf(String s)`找子串首次出现的索引位置，没找到就返回-1，`lastIndexOf`类似，但找的是最后一次出现的子串；

- 获取`String`指定索引位置的字符不能像`C++`那样直接用索引，而是`str.charAt(int index)`；

- 
    1. 用于获取子串的`subString(int begin_index), subString(int begin_index, end_index)`；
    2. 用于去除空格的`trim()`；
    3. 用于字符串替换的`replace(char old, char new)`；
    4. 用于判断字符串开头和结尾的`startWith(String prefix)`和`endWith(String suffix)`；
    5. 判断字符串相等不能用"=="，和C中原因几乎相同，`equals(Stirng)`方法返回`boolean`，`compareTo(String)`方法返回`int`，相当于`C`中的`strcmp(char*)`;
    6. 用于分割字符串的`split`，`split(String sign)`，sign为分割字符串的分割符，也可以用正则表达式；`split(String sign, int limit)`则限定了拆分次数，会分割`limit-1`次，也就是`limit`个字符串。

#### 字符串格式化

由于本人很少使用日期时间的原因，故关于日期和时间的格式化在这里跳过。

相比于`C\C++`，Java的常规类型格式化多出这些内容：

1. `"%b, %B"`，格式化为布尔类型；

2. `"%h, %H"`，格式化为散列码；

3. `"%a, %A"`，格式化为带有效位和指数的十六进制浮点数。

### 正则表达式

正则表达式，Java兼容了基本的正则表达式：

```java
public static void main(String[] args) {
   Scanner s = new Scanner(System.in);
   String str;
   String regex = "\\w+@\\w+(\\.\\w{2,3})*\\.\\w{2,3}";
   do {
       str = s.next();
       if (str.equals("exit")) {
           break;
       } else if (str.matches(regex)) {
           System.out.println(str + "是一个合法的邮箱地址格式");
       } else {
           System.out.println(str + "不是一个合法的邮箱地址格式");
       }
   } while (true);
   s.close();
   return;
}
```

该程序是一个邮箱地址格式判断的程序，其中的`regex`就是一个正则表达式。

### 字符串生成器

简单的说，就是`String`的内容无法改变，导致在进行连接的时候其实是多出一个`copy`，如果操作频繁，回导致效率很低，所以有一个新的类`StringBuilder`，一个可变的字符序列，它的几个常用方法：`append()`可以追加内容，参数可以是多个类型；`insert(int offset, String content)`将在offset处插入content字符串；`delete(int start, int end)`删除start和end之间的字符串。

### 数组

#### 一维数组的创建

你可以这样创建一个一维数组：

```java
ElemType ArrName[];
ElemType[] ArrName;
```

这样的数组是无法使用的，你还需要为其分配内存空间：

```java
ArrName = new ElemType[ElemNumber];
```

> 使用new分配数组内存时，整形数组中所有元素都是0。

当然，上面的操作可以合并进行：

```java
ElemType ArrName[] = new ElemType[ElemNumber];
ElemType[] ArrName = new ElemType[ElemNumber];
```

该写法是普遍采用的创建数组方法。

#### 一维数组的初始化

数组的初始化有以下两种基本形式：

```java
int arr1[] = new int[]{1, 2, 3};
int arr2[] = {4, 5, 6, 7};
```

#### 二维数组的创建

你可以这样先声明再分配一个二维数组：

```java
ElemType ArrName[][];
ElemType[][] ArrName;
```

分配空间的时候可以一起分配或者分别分配：

```java
a = new int[2][4]； // 一起分配

a = new int[2][];
a[0] = new int[3];
a[1] = new int[4];  // 分别分配
```

#### 二维数组的初始化

二维数组的初始化与一维数组类似，同样可以使用大括号完成：

```java
int arr[][] = { {1, 2}, {3, 4} };
```

> 使用new分配二维数组数组内存时，整形数组中所有元素都是0。

#### 数组遍历

最基础的遍历：

```java
for (int i = 0; i < arr.length(); i++) {
    for (int j = 0; j < arr[i].length(); j++) {
        TODO();
    }
    TODO();
}
```

利用`foreach`遍历：

```java
for (int x[] : arr) {
    for (int e : x) {
        TODO();
    }
    TODO();
}
```

#### 数组填充和替换

- `fill(ElemType[] a, ElemType value)`将数组`a`中所有元素填充为`value`；

- `fill(ElemType[] a, int formIndex, int toIndex, ElemType value)`是有范围的填充；

#### 对数组排序

```java
public static void main(String[] args) {
    int[] arr = { 1, 6, -1, 7 };
    Arrays.sort(arr);
    for (int e : arr) {
        System.out.print(e + " ");
    }
    System.out.println();
}
```

#### 数组复制

```java
int arr[] = {1, 2, 3, 4, 5};
int arr_copy[] = Arrays.copyOf(arr, 3);
```

`arr_copy`长度为3，是`arr`的前3个元素，如果`copyOf`的第二个参数，也就是长度参数大于复制目标的长度，那么就用0填充。

范围复制：

```java
int arr[] = {1, 2, 3, 4, 5};
int newarr[] = Arrays.copyOfRange(arr, 0, 3);
```