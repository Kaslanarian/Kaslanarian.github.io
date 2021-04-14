---
layout:     post
title:      Java数据结构
subtitle:   简述
date:       2021-03-05
author:     Welt Xing
header-img: img/java_header.jpg
catalog:    true
tags:
    - 编程技术
---

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

## Collection接口

`Collection`接口是层次结构中的根接口，不能够直接使用，但提供了添加/删除元素和管理数据的方法，这些方法也是其子类`Set`和`List`的通用方法：

|        方法        |           功能           |
| :----------------: | :----------------------: |
|     `add(E e)`     |         添加元素         |
| `remove(Object o)` |       移除指定对象       |
|    `isEmpty()`     |       判断是否为空       |
|    `iterator()`    | 返回一个迭代器，用于遍历 |
|      `size()`      |     返回集合元素个数     |

例程：

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Collection<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            String str = (String) it.next();
            System.out.println(str);
        }
    }
}
```

> `Iterator`的`next`方法返回的是`Object`，所以需要类型转换。

## List集合

`List`接口常用的实现类有`ArrayList`和`LinkedList`，分别实现的是动态数组和链表，你可以像下面这样实例化`List`集合：

```java
List<E> list = new ArrayList<>();
List<E> list2 = new LinkedList<>();
```

### ArrayList

#### 初始化

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

#### 添加元素

在前面其实已经介绍过添加元素的`add`方法，比较简单。

#### 访问元素

`ArrayList`并不支持索引，而是用`get`方法：

```java
ArrayList<String> l = new ArrayList<String>() {{
    add("a");
    add("b");
    add("c");
}};
System.out.println(l.get(0)); // 输出第一个元素
```

#### 修改元素

`ArrayList`提供`set()`方法修改元素：

```java
al.set(2, 'x'); // 形式：索引，值
```

#### 删除元素

`remove`方法可以实现`ArrayList`中元素的删除：

```java
al.remove(3); // 删除第4个元素
```

#### 获取元素数量

你可以用`size()`方法得到`ArrayList`中的元素数量。

#### 排序

Java中`Collections`类提供的`sort()`方法可对字符或数字列表进行排序：

```java
import java.util.ArrayList;
import java.util.Collections;

...
    Collections.sort(al);
...
```

## Set集合

`set`接口常用实现类有`HashSet`和`TreeSet`，分别使用哈希表和红黑树实现，而且`TreeSet`在遍历时时按照自然顺序递增排序，也可以按照指定比较器递增排序。在`TreeSet`中有新增的方法：

|                 方法                 |                           功能描述                           |
| :----------------------------------: | :----------------------------------------------------------: |
|              `first()`               |                        返回第一个元素                        |
|               `last()`               |                       返回最后一个元素                       |
|            `comparator()`            |       返回一个排序的比较器，如果是自然排序则返回`null`       |
|        `headSet(E toElement)`        | 返回一个新的`Set`集合，新集合是$[-\infty,toElement)$的所有对象 |
| `subSet(E fromElement, E toElement)` |      返回新的`Set`集合，值域为$[fromElement,ToElement)$      |
|       `tailSet(E fromElement)`       |          返回新集合，值域是$[fromElement,+\infty)$           |

存入`TreeSet`类实现的`Set`集合必须是实现`Comparable`接口：

```java
import java.util.Iterator;
import java.util.TreeSet;

public class MyClass implements Comparable<Object> {
    public int id;
    
    public MyClass(int id) {
        this.id = id;
    }
    
    public int compareTo(Object o) {
        MyClass instance = (MyClass) o;
        int result = id > indtance.id ? 1 (id == instance.id ? 0 : -1);
        return result;
    }
    
    public static void main(String[] args) {
        MyClass a = MyClass(1);
        MyClass b = MyClass(-1);
        MyClass c = MyClass(2);
        MyClass d = MyClass(0);
        TreeSet<MyClass> tree = new TreeSet<>();
        tree.add(a);
        tree.add(b);
        tree.add(c);
        tree.add(d);
        Iterator<MyClass> it = tree.iterator();
        while (it.hasNext()) {
            MyClass temp = (MyClass) it.next();
            System.out.println(temp.id);
        }
        return;
    }
}
```

## Map集合

与`Python`中的字典(`dict`)类似，`Map`接口中同样提供了集合的常用方法，此外还有以下的常用方法：

|             方法              |                  功能描述                  |
| :---------------------------: | :----------------------------------------: |
|     `put(K key, V value)`     |                 加入键值对                 |
|   `containsKey(Object key)`   |           判断键集合中是否有key            |
| `containsValue(Object value)` |          判断值集合中是否有value           |
|       `get(Object key)`       | 获取键key对应的value，没有的化则返回`null` |
|          `keySet()`           |                 获取键集合                 |
|          `values()`           |    获取所有值对象形成的`Collection`集合    |

```java
public static void main(String[] args) {
    Map<String, String> map = new HashMap<>();
    map.put("191300063", "习三卓");
    map.put("191300064", "邢存远");
    map.put("191300065", "徐茂");
    Set<String> set = map.keySet();
    Iterator<String> it = set.iterator();
    while (it.hasNext()) {
        System.out.println(it.next());
    }
    Collection<String> coll = map.values();
    it = coll.iterators();
    while (it.hasNext()) {
        System.out.println(it.next());
    }
}
```

> map集合允许值为`null`

## Map接口的实现类

和`Set`相同，Map接口常用的实现类有`HashMap`和`TreeMap`，由于前者执行操作效率高，因此推荐前者；此外，由于`TreeMap`的映射关系也是按顺序排列，故不允许键对象是`null`.

我们可以通过HashMap创建Map结合，再创建一个完成相同映射关系的TreeMap类实例：

```java
public class MapTest {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("191300064", "邢存远")；
        map.put("191300063", "习三卓");
        map.put("191300065", "徐茂");
        
        Set<String> set = map.keySet();
        Iterator<String> it = set.iterator();
        // HashMap下输出是无序的
        while (it.hasNext()) {
            System.out.println((String) it.next());
        }
        
        TreeMap<String, String> treemap = new TreeMap<>();
        treemap.putAll(map); // 将所有键值对加入
        
        it = treemap.keySet().iterator();
         // TreeMap下输出是升序的
        while (it.hasNext()) {
            System.out.println((String) it.next());
        }
    }
}
```

## 参考

[1] <https://www.runoob.com/java/java-collections.html>
