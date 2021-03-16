---
layout:     post
title:      C的多线程编程
subtitle:   以及操作系统相关知识的学习
date:       2021-03-16
author:     Welt Xing
header-img: img/SB8NYc8sC.jpg
catalog:    true
tags:
    - 操作系统
    - C/C++
---

## 引言

目前正在学习《操作系统（2021年春）》的课程，当然躲不了关于线程和进程的问题。想起当年学习程序设计语言时，遇到线程编程就跳过的情况，所以准备学习这方面的内容，顺便学习操作系统的知识并记录下来.

## 概念

我们常常会将“程序”与“进程”进行比较：“程序”只是一组指令序列，指导计算机行为；而一个“进程”是一个**正在执行的程序**，有了动态特性，它也是操作系统进行资源分配和保护的基本单位。

除了“静”与“动”的关系，两者还是“一”对“多”的关系：在并发概念出现后，多个程序能够同时执行，此时引入了进程的新概念。

引入进程的主要目的，一个是刻画程序的并发性，如上面所说，多道程序系统出现后，执行的程序不再是封闭的，而是互相存在这联系，这一点是程序这一静态概念无法刻画的；二是解决资源的共享性，假设有一个先读磁盘再计算的程序$A$，和一个先计算再写磁盘的程序$B$，一个最简单的设计方法就是让$A$和$B$依次运行，但实际上我们完全可以先让$A$占用磁盘，让$B$占用CPU，当两进程都完成了各自的第一项任务后，再将两者占有的设备互换，这样显然会提高计算机的运行效率。

如果说操作系统中引入进程的目的是为了使多个程序并发执行，以便改善资源利用率和提高系统效率，那么，在进程之后再引入线程是为了减少程序并发执行时间所付出的系统开销，使得**并发粒度更细，并发性更好**。

## 创建线程

我们可以用下面的程序创建一个POSIX线程：

```cpp
#include <pthread.h>
pthread_create(thread, attr, start_routine, arg);
```

在这里，`pthread_create`创建一个新的线程并让它可执行，下面是关于参数的说明：

|      参数       |                             描述                             |
| :-------------: | :----------------------------------------------------------: |
|    `thread`     |                     指向线程描述符的指针                     |
|     `attr`      |  一个不透明的属性对象，可以用来设置线程属性，可以默认为NULL  |
| `start_routine` |          线程运行函数起始地址，一旦线程创建就会执行          |
|      `arg`      | 运行函数的参数，它必须通过把引用作为指针强制转换为 void 类型进行传递。如果没有传递参数，则使用 NULL。 |

## 终止线程

我们可以用下面的程序来终止一个线程：

```cpp
#include <pthread.h>
pthread_exit(status);
```

在这里，pthread_exit 用于显式地退出一个线程。通常情况下，`pthread_exit()`函数是在线程完成工作后无需继续存在时被调用。

如果`main()`是在它所创建的线程之前结束，并通过`pthread_exit()`退出，那么其他线程将继续执行。否则，它们将在`main()`结束时自动被终止。

## 简单实例

我们用下面的程序创建五个线程输出$\text{Hello world!}$

```cpp
#include <pthread.h>
#include <stdio.h>
#define NUMS_THREAD 5

void* say_hello(void* args) {
    printf("Hello world!\n");
    return 0;
}

int main(int argc, char const* argv[]) {
    // 定义线程数组
    pthread_t tids[NUMS_THREAD];
    for (int i = 0; i < NUMS_THREAD; i++) {
        // 创造线程
        int ret = pthread_create(&tids[i], NULL, say_hello, NULL);
        if (ret != 0) {
            printf("pthread_create error: error_code=%d\n", ret);
        }
    }
    //等各个线程退出后，进程才结束，否则进程强制结束了，线程可能还没反应过来
    pthread_exit(NULL);
}
```

我们在命令行里输入

```bash
$gcc test.c -lpthread -o test # 这里使用了-lpthread库去编译程序
$./test
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
```

## 带参数的线程创建

我们对上面的程序稍作处理，就可以实现参数的存取：

```cpp
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define NUMS_THREAD 5

void* say_hello(void* args) {
    int arg = *((int*)args);
    printf("Hello world! arg is %d\n", arg);
    return 0;
}

int main(int argc, char const* argv[]) {
    pthread_t threads[NUMS_THREAD];
    int indexes[NUMS_THREAD];
    int rc, i;

    for (i = 0; i < NUMS_THREAD; i++) {
        indexes[i] = i;
        rc = pthread_create(&threads[i], NULL, say_hello, (void*)(indexes + i));
        if (rc != 0) {
            printf("pthread_create error: error_code=%d\n", rc);
            exit(-1);
        }
    }
    pthread_exit(NULL);
}
```

输出：

```bash
$gcc test.c -lpthread -o test && ./test
Hello world! arg is 0
Hello world! arg is 1
Hello world! arg is 3
Hello world! arg is 4
Hello world! arg is 2
```

注意：在传递参数的时候，参数是以`void*`形式传递的，我们需要在传入时将`int*`强制类型转换为`void*`，并在读取时将`void*`转换为`int*`；此外，我们从输出中可以发现，线程执行时是独立的，由于微小的时间差导致输出顺序的改变.

## 向线程传递多个参数

只要知道我们向线程传递参数是以指针形式传递，那么我们很容易就可以实现多个参数的传递：

```cpp
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define NUMS_THREAD 5

typedef struct Args {
    int id;
    char* message;
} Args;

void* say_hello(void* args) {
    Args* arg = (Args*)args;
    printf("thread %d output : %s\n", arg->id, arg->message);
    return 0;
}

int main(int argc, char const* argv[]) {
    pthread_t threads[NUMS_THREAD];
    int indexes[NUMS_THREAD];
    int rc, i;
    Args args[] = {
        {0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
    };

    for (i = 0; i < NUMS_THREAD; i++) {
        indexes[i] = i;
        rc = pthread_create(&threads[i], NULL, say_hello, args + i);
        if (rc != 0) {
            printf("pthread_create error: error_code=%d\n", rc);
            exit(-1);
        }
    }
    pthread_exit(NULL);
}
```

我们定义了一个结构体来存储两个参数，然后按照类似的方式输出信息：

```bash
thread 0 output : zero
thread 2 output : two
thread 4 output : four
thread 3 output : three
thread 1 output : one
```

## 链接和分离线程

我们可以使用以下两个函数来连接或分离线程：

```cpp
pthread_join(thread_id, status);
pthread_detach(thread_id);
```

`pthread_join()`子程序阻碍调用程序，直到指定的`threadid`线程终止为止。当创建一个线程时，它的某个属性会定义它是否是可连接的（joinable）或可分离的（detached）。只有创建时定义为可连接的线程才可以被连接。如果线程创建时被定义为可分离的，则它永远也不能被连接。

这个实例演示了如何使用`pthread_join()`函数来等待线程的完成：

```cpp
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_THREADS 3

void *wait(void *t) {
    int i;
    long tid;

    tid = (long)t;

    sleep(1);
    printf("Sleeping in thread");
    printf("Thread with id : %ld ...exiting\n", tid);
    pthread_exit(NULL);
}

int main(int argc, char const *argv[]) {
    int rc;
    int i;
    pthread_t threads[NUM_THREADS];
    pthread_attr_t attr;
    void *status;

    // 初始化并设置线程为可连接的（joinable）
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for (int i = 0; i < NUM_THREADS; i++) {
        printf("main() : creating thread %d\n", i);
        rc = pthread_create(&threads[i], NULL, wait, (void *)&i);
        if (rc != 0) {
            printf("error:unable to create thread, %d\n", rc);
            exit(-1);
        }
    }

    // 删除属性并等待其他线程
    pthread_attr_destroy(&attr);
    for (int i = 0; i < NUM_THREADS; i++) {
        rc = pthread_join(threads[i], &status);
        if (rc) {
            printf("error:unable to join, %d\n", rc);
            exit(-1);
        }
        printf("Main: completed thread id :%d", i);
        printf("  exiting with status :%p\n", status);
    }
    printf("Main: program exiting\n");
    pthread_exit(NULL);
}
```

运行后输出整齐：

```bash
main() : creating thread 0
main() : creating thread 1
main() : creating thread 2
Sleeping in threadThread with id : 140723229965192 ...exiting
Sleeping in threadThread with id : 140723229965192 ...exiting
Sleeping in threadThread with id : 140723229965192 ...exiting
Main: completed thread id :0  exiting with status :(nil)
Main: completed thread id :1  exiting with status :(nil)
Main: completed thread id :2  exiting with status :(nil)
Main: program exiting
```

在前面的例子中，函数执行和创建是并行的，但这里显然存在进程阻碍.
