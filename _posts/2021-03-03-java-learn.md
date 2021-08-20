---
layout:     post
title:      Java手册
subtitle:   学习记录
date:       2021-03-03
author:     Welt Xing
header-img: img/java_header.jpg
catalog:    true
tags:
    - 编程技术
---

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

* 八进制表示：以0开头，`0123`就是十进制的`83`；

* 多出一个`byte`类型表示`int8`；

#### 浮点类型

* 小数默认被看做`double`，如果想要是`float`就要在后面加上`f`或者`F`
  
    ```java
    float f1 = 13.23f;
    double d1 = 4562.12d;
    double d2 = 45678.1564;
    ```

#### 字符类型

* Java里的`char`占两个字节，是`C/C++`的两倍，使得java的字符几乎可以处理所有国家的语言文字:

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

* 此处的布尔类型为`boolean`，而不是`C++`中的`bool`，但两个字面量`true`和`false`是相同的。

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

* 如果`member_final`(成员常量)只声明不赋值，那么会报错；

* 如果`local_final`(局部常量)只声明不赋值是可以的，但之后必须被赋值，也只能被赋值一次，否则报错；

### 运算符

* Java中自增自减运算符存在，用法与`C/C++`相同；

* Java中移位操作多出一个`>>>`，意思是无符号右移。

### 流程控制

* Java也有switch-case，语法与C相同，但多出对**字符串**类型的支持；

* Java有和C++类似的基于范围for循环：

    ```java
    int arr[] = {7, 10, 1};
    for (int x : arr) {
        System.out.println(x);
    }
    ```

### 字符串

#### 构造方法

常用的字符串构造方法：(字符串使用前必须经过初始化，否则报错)

* 用字符数组初始化

    ```java
    char a[] = {'w', 'e', 'l', 't'};
    String s = new String(a);
    ```

* 提取字符数组初始化

    ```java
    char a[] = {'w', 'e', 'l', 't'};
    String s = new String(a, 1, 2); // 偏移1，取2个，也就是"el"
    ```

* 字符串常量的引用赋值

    ```java
    String s1, s2;
    s1 = "welt";
    s2 = "welt";
    ```

    这里是`s1`和`s2`**指向同一段内存空间**，该内存空间存储的是字符串"welt"。

#### 常用用法

* `String`之间可以相互连接，用'+'即可；此外，还可以连接其他数据类型，过程是调用`toString()`方法，然后再连接；

* 字符串查找：`indexOf(String s)`找子串首次出现的索引位置，没找到就返回-1，`lastIndexOf`类似，但找的是最后一次出现的子串；

* 获取`String`指定索引位置的字符不能像`C++`那样直接用索引，而是`str.charAt(int index)`；

*
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

* `fill(ElemType[] a, ElemType value)`将数组`a`中所有元素填充为`value`；

* `fill(ElemType[] a, int formIndex, int toIndex, ElemType value)`是有范围的填充；

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

## 类与对象

### 权限修饰符

虽然C++和Java共用一套权限修饰符，但含义有些许差别。

|                    | private | protected | public |
| ------------------ | ------- | --------- | ------ |
| 本类               | 可见    | 可见      | 可见   |
| 同包的其他类或子类 | 不可见  | 可见      | 可见   |
| 其他包的类或子类   | 不可见  | 不可见    | 可见   |

包的概念将在后面介绍。

### 构造方法

特点，没有返回值（和`C++`相同），而且不需要`void`关键字修饰。

> 如果在类中定义的构造方法都不是无参的，那么编译器也不会为其设置一个默认构造函数，只有在类中没有定义任何构造方法时，系统才会自动创建默认构造函数。

`this`也可以调用构造方法：

```java
public Anything() {
    this("this 调用有参构造方法");
    System.out.println("无参构造方法");
}

public Anything(String name) {
    System.out.println("有参构造方法");
}
```

### 静态变量，常量和方法

由`static`关键字修饰的变量，常量和方法被称作静态变量、常量和方法。

作用是为了"共享"（和C中的`static`的作用“相反”）；我们直接使用`类名.静态成员/方法`就可以使用。

静态方法的规定：

1. 静态方法中不能使用`this`关键字；

2. 在静态方法中不能**直接**调用非静态方法。

> Java中不允许方法体内的局部变量为`static`。
> 如果在执行类的时候希望先执行类的一些初始化动作，可以使用`static`定义一个静态区域：
>
> ```java
> public class example {
>       static {
>           TODO();
>       }
> }
> ```

### 类的主方法

形式：

```java
public static void main(String[] args) {
    TODO();
}
```

可以看出：

1. 主方法是静态的，所以如果要在主方法中调用其他函数，**这些函数也必须是静态的**；

2. 和`C`不一样，这里的`main`是没有返回值的；

3. 主方法的形参就是参数，我们可以用程序测试一下：

    ```java
    public static void main(String[] args) {
        for (String arg : args) {
            System.out.println(arg);
        }
    }
    ```

    在命令行输入：

    ```bash
    >> javac Main.java # 此处不是输入参数的地方，因为不执行
    >> java Main 1 2 3
    ```

    然后就可以看到输出：

    ```text
    1
    2
    3
    ```

### 对象

#### 对象的创建

在之前的数组和字符串部分，我们已经在创建对象了：

```java
String str = new String("abc");
```

在此强调这里的语法和`C++`的差别：

```cpp
A* a = new A(...);
```

`C++`的`new`语法创建的是一个指针，但`Java`创建的就是一个对象的引用。

> JVM的内存处理机制：每个对象都有生命周期，生命周期结束后就会被回收，无法再被使用。

#### 对象的引用

事实上，在

```java
String str = new String();
```

中，标识符`str`称作“引用对象”，如一个`Book`类的引用可以使用以下代码：

```java
Book book;
```

一个引用对象不一定需要有一个对象相关联（比如上面），**引用与对象相关联**的语法如下：

```java
Book book = new Book();
```

引用只是存放对象的内存地址，并非存放一个对象。严格地说，引用和对象不同。

> 前桥和弥在《[征服C指针](https://book.douban.com/subject/21317828/)》中提到过一个趣闻：JAVA在推出时宣传自己是没有指针的，目的就是为了吸引当时被C指针折磨已久的程序员们。但实际上前桥认为Java的引用可以说就是C的指针，所以这算是一个“虚假营销”。至此我们可以发现他的观点确实有合理之处。

#### 对象的比较

Java中有两种比较对象的方式：分别为“=="运算符和`equals()`方法：

```java
object1 == object2;     // 比较的是两个对象引用的地址是否相同；
object1.equals(object2) // 比较的是两个对象引用所指的内容是否相同.
```

区别可以理解为`C`中两个`char*`，`ptr1`和`ptr2`，`==`比较的就是地址是否相同，但`strcmp(ptr1, ptr2)`比较的是内容。

#### 对象的销毁

对象的销毁和我们之前提到的JVM垃圾回收机制相关，我们先来看下什么样的对象会被JVM识别为垃圾：

* 对象引用超过了作用域：

    ```java
    {
        A a = new A();
    }
    // 到了这里A就应该消亡了
    ```

* 将对象赋值为`null`：

    ```java
    A a = new A();
    a = null;
    ```

JVM只能回收由`new`操作符创建的对象，否则无法被其识别，此时你可以自定义`Object`的`finalize`方法，类似与`C++`中的重载`delete`.

## 异常处理

参见[Java异常处理](https://welts.xyz/2021/03/07/exception/#java%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)

## I/O（输入输出）

### 关于流

#### 输入流

Java中所有输入流都是抽象类`InputStream`（字节输入流）或者抽象类`Reader`（字符输入流）的子类。

Java中的字符是Unicode编码，是双字节的。`InputStream`是用来处理字节的，并不适合处理字节文本（如英文文档）。Java为字符文本的输入专门提供了一套单独的类`Reader`，但`Reader`类并不是`InputStream`类的替换者，只是在处理字符串时简化了编程。`Reader`类是字符输入流的抽象类。

#### 输出流

Java中所有输出流都是抽象类`OutputStream`（字节输出流）或者抽象类`Writer`（字符输出流）的子类。同样，`Writer`类也是为了处理字符而单独提供的抽象类。

### FIle类

#### 文件创建与删除

直接用程序说明：

```java
File file1 = new File(filename);
File file2 = new File("dirname", "filename") // 比如dirname为"/home"，filename为"test.txt"
```

你可以像下面这样进行更完备的文件创建：

```java
File file = new File("word.txt");
if (file.exists()) {
    file.delete(); // 文件已存在则将文件删除
} else {
    try {          // 文件不存在则创建新文件
        file.createNewFile();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

#### 获取文件信息

以下是`File`类的方法，供查阅使用：

| 序号 | 方法描述                                                     |
| :--- | :----------------------------------------------------------- |
| 1    | **public String getName()** 返回由此抽象路径名表示的文件或目录的名称。 |
| 2    | **public String getParent()**  返回此抽象路径名的父路径名的路径名字符串，如果此路径名没有指定父目录，则返回 `null`。 |
| 3    | **public File getParentFile()** 返回此抽象路径名的父路径名的抽象路径名，如果此路径名没有指定父目录，则返回 `null`。 |
| 4    | **public String getPath()** 将此抽象路径名转换为一个路径名字符串。 |
| 5    | **public boolean isAbsolute()** 测试此抽象路径名是否为绝对路径名。 |
| 6    | **public String getAbsolutePath()** 返回抽象路径名的绝对路径名字符串。 |
| 7    | **public boolean canRead()** 测试应用程序是否可以读取此抽象路径名表示的文件。 |
| 8    | **public boolean canWrite()** 测试应用程序是否可以修改此抽象路径名表示的文件。 |
| 9    | **public boolean exists()** 测试此抽象路径名表示的文件或目录是否存在。 |
| 10   | **public boolean isDirectory()** 测试此抽象路径名表示的文件是否是一个目录。 |
| 11   | **public boolean isFile()** 测试此抽象路径名表示的文件是否是一个标准文件。 |
| 12   | **public long lastModified()** 返回此抽象路径名表示的文件最后一次被修改的时间。 |
| 13   | **public long length()** 返回由此抽象路径名表示的文件的长度。 |
| 14   | **public boolean createNewFile() throws IOException** 当且仅当不存在具有此抽象路径名指定的名称的文件时，原子地创建由此抽象路径名指定的一个新的空文件。 |
| 15   | **public boolean delete()**  删除此抽象路径名表示的文件或目录。 |
| 16   | **public void deleteOnExit()** 在虚拟机终止时，请求删除此抽象路径名表示的文件或目录。 |
| 17   | **public String[] list()** 返回由此抽象路径名所表示的目录中的文件和目录的名称所组成字符串数组。 |
| 18   | **public String[] list(FilenameFilter filter)** 返回由包含在目录中的文件和目录的名称所组成的字符串数组，这一目录是通过满足指定过滤器的抽象路径名来表示的。 |
| 19   | **public File[] listFiles()**  返回一个抽象路径名数组，这些路径名表示此抽象路径名所表示目录中的文件。 |
| 20   | **public File[] listFiles(FileFilter filter)** 返回表示此抽象路径名所表示目录中的文件和目录的抽象路径名数组，这些路径名满足特定过滤器。 |
| 21   | **public boolean mkdir()** 创建此抽象路径名指定的目录。      |
| 22   | **public boolean mkdirs()** 创建此抽象路径名指定的目录，包括创建必需但不存在的父目录。 |
| 23   | **public boolean renameTo(File dest)**  重新命名此抽象路径名表示的文件。 |
| 24   | **public boolean setLastModified(long time)** 设置由此抽象路径名所指定的文件或目录的最后一次修改时间。 |
| 25   | **public boolean setReadOnly()** 标记此抽象路径名指定的文件或目录，以便只可对其进行读操作。 |
| 26   | **public static File createTempFile(String prefix, String suffix, File directory) throws IOException** 在指定目录中创建一个新的空文件，使用给定的前缀和后缀字符串生成其名称。 |
| 27   | **public static File createTempFile(String prefix, String suffix) throws IOException** 在默认临时文件目录中创建一个空文件，使用给定前缀和后缀生成其名称。 |
| 28   | **public int compareTo(File pathname)** 按字母顺序比较两个抽象路径名。 |
| 29   | **public int compareTo(Object o)** 按字母顺序比较抽象路径名与给定对象。 |
| 30   | **public boolean equals(Object obj)** 测试此抽象路径名与给定对象是否相等。 |
| 31   | **public String toString()**  返回此抽象路径名的路径名字符串。 |

### 文件输入输出流

目的是将`In/OutputStream`和`File`进行连接：

#### FileIn/OutputStream

`FileInputStream`常用的构造方法如下：

```java
FileInputStream(String filename);
FileInputStream(File file);
```

`FileOutputStream`类有与上面类似的构造方法，创建一个`FileOutputStream`对象时，可以指定不存在的文件名，但该文件不能被其他程序打开。

我们来看一个测试程序：

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        String content = "我虽无意逐鹿，却知苍生苦楚\n";
        FileOutputStream out = new FileOutputStream("test.txt");
        out.write(content.getBytes());
        out.close();

        FileInputStream in = new FileInputStream("test.txt");
        System.out.print(new String(in.readAllBytes()));
        in.close();
    }
}
```

这里我们实现了将一句话写入文件，然后读取文件并输出到控制台的程序。

> 这里的in/out是针对Java程序而言：将外部文件的内容引入源文件为“in”，反之为“out”.

#### FileReader/Writer类

背景：由于汉字在文件中只占用两个字节，如果使用字节流，读取不好会出现乱码现象，此时采用字符流`Reader/Writer`类即可避免这种情况。

`FileReader`顺序读取文件，只要不关闭流，每次调用`read()`方法就顺序地读取源中其余的内容，直到源的末尾或者流关闭。

我们再次用类似的程序做测试：

```java
public class Main {
    public static void main(String[] args) throws IOException {
        String content = "我虽无意逐鹿，却知苍生苦楚\n";
        FileWriter fw = new FileWriter("test.txt");
        fw.write(content);
        fw.close();

        FileReader fr = new FileReader("test.txt");
        char[] ret = new char[1024];
        fr.read(ret);
        System.out.print(new String(ret));
        fr.close();
    }
}

```

可以发现我们这里写入可以是直接的字符串，而读取也可以用字符流读取。