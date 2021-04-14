---
layout:     post
title:      Java反射
subtitle:   —— 一种“自审”机制
date:       2021-03-13
author:     Welt Xing
header-img: img/Java/reflection.jpg
catalog:    true
tags:
    - 编程技术
---

我们使用`matrix-java`中的自定义类来进行学习，在`main.java`进行程序测试，代码获取：<https://github.com/Kaslanarian/matrix-java>

## 反射是什么？

反射的概念是由 Smith 在 1982 年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力。通俗地讲，一提到反射，我们就可以想到镜子。镜子可以明明白白地照出我是谁，还可以照出别人是谁。反映到程序中，反射就是用来让开发者知道这个类中有什么成员，以及别的类中有什么成员。

## 为什么要有反射？

反射看起来是和封装的思想相悖，因为封装就是不想让用户接触到一些私有成员和函数实现细节，反射似乎让类变得“不安全起来”，但实际上：

* 反射让开发人员可以通过外部类的全路径名创建对象，并使用这些类，实现一些扩展的功能。

* 反射让开发人员可以枚举出类的全部成员，包括构造函数、属性、方法。以帮助开发者写出正确的代码。

* 测试时可以利用反射 API 访问类的私有成员，以保证测试代码覆盖率。

所以说，反射其实是一个后门，为程序设计提供灵活性。

## 反射API

我们来看看反射的API：

![反射API](https://pic4.zhimg.com/v2-312b1b34ca2ebd1317bedf70ddfad38b_r.jpg)

## 获取Class对象

我们可以分别通过字符串、类、对象的方式获取class对象：

```java
Class matrixClass = Class.forName("xyz.welts.Matrix");
Class matrixClass2 = Matrix.class;
Class matrixClass3 = (new Matrix()).getClass();
```

我们可以通过程序验证这三个Class对象是同一个，也就是说一个类只会生成一个Class对象.

## 获取成员变量

我们通过`getDeclaredFields()`方法去访问所有的成员变量，用`getFields()`方法去访问`public`成员：

```java
public static void main(String[] args) {
    for (Field field : Matrix.class.getDeclaredFields()) {
        System.out.println(field);
    }
}
```

输出：

```java
private double[][] Matrix.data
private int Matrix.rowNumber
private int Matrix.columnNumber
final double Matrix.PRECISION
static final boolean Matrix.$assertionsDisabled
```

## 获取构造方法

与上面类似，我们通过`getDeclaredConstructors()`方法去访问所有的构造方法，用`getConstructors()`方法去访问公有构造方法：

```java
for (Constructor constructor : Matrix.class.getDeclaredConstructors()) {
    System.out.println(constructor);
}
```

输出：

```java
public Matrix(double[][])
public Matrix(Matrix)
public Matrix(int,int)
public Matrix()
```

## 获取非构造方法

同样，我们只需要将`Constructors`改成`Methods`就可以访问成员方法：

```java
for (Method method : Linearlib.class.getMethods()) {
    System.out.println(method);
    }
```

输出：

```java
public static Matrix Linearlib.inv(Matrix)
private static void Linearlib.lineMultiply(Matrix,int,double)
private static void Linearlib.lineSwap(Matrix,int,int)
private static void Linearlib.lineMultiplyAdd(Matrix,int,double,int)
public static double Linearlib.det(Matrix)
public static void Linearlib.upperStep(Matrix)
public static Matrix[] Linearlib.linearSolve(Matrix,Matrix)
public static Matrix Linearlib.linearSolve(Matrix)
```

> 这里如果输出的是`getMethods`的返回值，那么还会获取到了很多 Object 类中的公有方法（Object 是所有 Java 类的父类）。

## 示例

我们将用一个程序修改一个`matrix`的行数并输出：

```java
public static void main(String[] args) throws NoSuchFieldException, SecurityException, IllegalArgumentException,
            IllegalAccessException, NoSuchMethodException, InstantiationException, InvocationTargetException {
    // 定义matrix类的class变量
    Class matrixClass = Matrix.class;
    // 找到参数为(int, int)类型的构造函数
    Constructor intIntConstructor = matrixClass.getConstructor(int.class, int.class);
    // 利用该构造函数创建对象
    Object matrix = intIntConstructor.newInstance(3, 3);
    // 输出该3×3矩阵
    System.out.println("old ： " + matrix);
    // 获取私有成员变量rowNumber
    Field rowNumberField = matrixClass.getDeclaredField("rowNumber");
    // 修改私有变量的访问权限
    rowNumberField.setAccessible(true);
    // 修改该私有成员
    rowNumberField.set(matrix, 1);
    // 查看输出
    System.out.println("new : " + matrix);
}
```

输出结果：

```bash
old ： {
   0.00000,     0.00000,     0.00000,  

   0.00000,     0.00000,     0.00000,  

   0.00000,     0.00000,     0.00000,  
}
new : {
   0.00000,     0.00000,     0.00000,  
}
```

说明我们已经成功修改了一个对象的私有成员.

注意：

1. 由于反射相关操作出现的异常都是检查性异常，我们需要人为进行异常处理，详情参考[Java异常处理：两种异常](https://welts.xyz/2021/03/07/exception/#%E4%B8%A4%E7%A7%8D%E5%BC%82%E5%B8%B8).

2. 若想使用私有成员/方法，在获取了对应的`field`、`constructor`或`method`后，要调用`setAccessible`方法将访问权限修改为`true`.

3. 我们无法通过`getMethod`去找到非公有方法，`getConstructor`和`getField`类似.
