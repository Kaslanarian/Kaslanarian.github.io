---
layout:     post
title:      Java数据结构
subtitle:   简述
date:       2021-03-05
author:     Welt Xing
header-img: img/java_header.jpg
catalog:    true
tags:
    - Java
---

# Java数据结构

> 本文将介绍一些数据结构及其使用方法，当作是构建`matrix-java`的准备工作。

## 特设类和集合框架

早在 Java 2 中之前，Java 就提供了特设类。比如：`Dictionary`, `Vector`, `Stack`, 和 `Properties` 这些类用来存储和操作对象组。虽然这些类都非常有用，但是它们缺少一个核心的，统一的主题。由于这个原因，使用 `Vector` 类的方式和使用 `Properties` 类的方式有着很大不同。

集合框架被设计成要满足以下几个目标：

1. 该框架必须是高性能的。基本集合（动态数组，链表，树，哈希表）的实现也必须是高效的；

2. 该框架允许不同类型的集合，以类似的方式工作，具有高度的互操作性；

3. 对一个集合的扩展和适应必须是简单的。

为此，整个集合框架就围绕一组标准接口而设计。你可以直接使用这些接口的标准实现，诸如： `LinkedList`, `HashSet`, 和 `TreeSet` 等,除此之外你也可以通过这些接口实现自己的集合：

![集合框架](/img/collections.jpg)

该图的最上面是两个核心容器：集合(`Collection`)和映射(`map`)，从上到下逐渐具象，最下面就是具体实现类，常用的有`ArrayList`、`LinkedList`、`HashSet`、`LinkedHashSet`，`HashMap`，`LinkedHashMap`等。

我们接下来仔细看看上述常用的类。

## ArrayList

### 初始化

```java
import java.util.ArrayList; // 引入 ArrayList 类

// 最基本的初始化
ArrayList<E> objectName1 = new ArrayList<>();

// 用Arrays.asList初始化
ArrayList<E> objectName2 = new ArrayList<>(Arrays.asList(object1, object2, ...));

// 生成匿名内部内进行初始化
ArrayList<E> objectName3 = new ArrayList<>() {{
    add(object1);
    add(object2);
    ...
}};
```

> 上面的`E`必须是引用数据类型，也就是说，不能像C++那样使用基本类型：`vector<int>`，而是`ArrayList<Integer>`。

### 添加元素

在前面其实已经介绍过添加元素的`add`方法，比较简单。

### 访问元素

`ArrayList`并不支持索引，而是用`get`方法：

```java
ArrayList<String> l = new ArrayList<String>() {{
    add("a");
    add("b");
    add("c");
}};
System.out.println(l.get(0)); // 输出第一个元素
```

### 修改元素

`ArrayList`提供`set()`方法修改元素：

```java
al.set(2, 'x'); // 形式：索引，值
```

### 删除元素

`remove`方法可以实现`ArrayList`中元素的删除：

```java
al.remove(3); // 删除第4个元素
```

### 获取元素数量

你可以用`size()`方法得到`ArrayList`中的元素数量。

### 排序

Java中`Collections`类提供的`sort()`方法可对字符或数字列表进行排序：

```java
import java.util.ArrayList;
import java.util.Collections;

...
    Collections.sort(al);
...
```

## 参考

[1] <https://www.runoob.com/java/java-collections.html>