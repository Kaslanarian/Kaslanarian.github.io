---
layout:     post
title:      编程作业记录
subtitle:   操作系统和文件读取
date:       2021-03-21
author:     Welt Xing
header-img: img/chomework.jpg
catalog:    true
tags:
    - 日常
---

今天在群里看到一个外校学生问的问题，是他们的操作系统作业，虽然和我们比起来相差甚远，但仍有学习的必要。

## 题面一览

—、实验目的:
1．熟悉Linux环境下c程序的编辑与运行;
2．测试Linux系统调用`exec()`、`fork()`、`exit()`等的使用。二、实验准备:
通过研习参考书《Linux程序设计>（第4版）（N.Matthew,R. Stones（译者:陈健，宋健建），人民邮电出版社，2010）第11章“进程和信号”的内容，熟悉进程创建、进程协同工作等相关函数如`fork()`、`system()`、`exec()`、`waitpid()`、`exit()`等的使用方法。二、实验题目:
1.编写一个程序 prog#1，要求:
（a）该程序带有一个参数,用以指定要操作的文本文件。
（b）把指定文本文件的内容显示在屏幕上。
（c）程序末尾显示总共显示了上述文件的文本行数。
2．编写一个主程序，该程序使用`fork()`来创建一个子进程，然后通过该子进程执行上
述程序prog#1:
（a）使用`system()`来执行;（b）使用`exec()`来执行。
观察并分析2种执行方式的差异，并写出产生这些差异的原因。

这里我们主要研究程序题.

## 任务一

任务一唯一的难点是文件的读写（因为我已经忘了），所以我们需要总结一下C语言文件的读写，和线程编程一样，当年学习C的时候并没有太重视.

[复习：C语言的文件读写](https://welts.xyz/2021/03/21/cfile/)

在知道文件读写过程后，我们就不难写出程序：

```cpp
/* prog#1.c */
#include <stdio.h>

int main(int argc, char const *argv[]) {
    if (argc == 1) {
        printf("no file input\n");
    } else {
        char const *filename = argv[1];
        FILE *fp = fopen(filename, "r");
        if (fp == NULL) {
            printf("file open failed");
        } else {
            int lines = 1;
            char ch = fgetc(fp);
            while (ch != EOF) {
                if (ch == '\n') {
                    lines++;
                }
                putchar(ch);
                ch = fgetc(fp);
            }
            printf("\n%d\n", lines);
        }
    }
    return 0;
}
```

如果`argc`为1，说明命令行里没有输入文件；如果文件指针`fp`为空，那么文件打开失败；否则就用`fgetc`函数获文件信息并输出，并对`\n`字符计数以计算行数.

效果：

```text
> gcc prog#1.c -o prog#1 && ./prog prog#1.c
#include <stdio.h>

int main(int argc, char const *argv[]) {
    if (argc == 1) {
        printf("no file input\n");
    } else {
        char const *filename = argv[1];
        FILE *fp = fopen(filename, "r");
        if (fp == NULL) {
            printf("file open failed");
        } else {
            int lines = 1;
            char ch = fgetc(fp);
            while (ch != EOF) {
                if (ch == '\n') {
                    lines++;
                }
                putchar(ch);
                ch = fgetc(fp);
            }
            printf("\n%d\n", lines);
        }
    }
    return 0;
}
25
```

## 任务二

该部分与之前学习的[C的进程编程](https://welts.xyz/2021/03/17/multi_process/)联系上了，这里我们打算用简单的宏定义去将两种执行方式融合在一个程序里。

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define USE_EXEC

int main(int argc, char const* argv[]) {
    if (argc == 1) {
        perror("no file input\n");
        exit(-1);
    }
    pid_t pid = fork();
    if (pid < 0) {
        perror("process created failed\n");
        exit(-1);
    } else if (pid == 0) {
        const char* filename = argv[1];
#ifdef USE_EXEC
        execl("prog#1", "./prog#1", filename, NULL);
        // 可执行文件路径，命令，参数，NULL
#else
        char* command = (char*)malloc(sizeof(char*));
        sprintf(command, "./prog#1 %s", filename);
        system(command);
#endif
    } else {
        printf("parent process\n");
    }
    return 0;
}
```

子进程默认会用`execl`函数去执行`prog#1`，如果将`#define USE_EXEC`注释掉就会用`system`函数去执行，我们在命令行里输入：

```bash
gcc prog\#1.c -o prog\#1
gcc prog\#2.c -o prog\#2
./prog\#2 prog\#2.c
```

就可以输出源文件`prog#2.c`的内容。

> 命令行里`#`是注释的意思，如果想要表示真正的`#`字符就要写成`\#`.

从源文件就可以看出，`exec`函数族和`system`函数执行命令时的输入参数存在差异：`system`函数，或者命令行输入时，一个命令已经和对应可执行程序的路径绑定（比如`echo`和`/usr/bin/echo`绑定），但在`exec`函数族中，第一个参数是可执行文件路径，第二个参数才是命令，两者分离.

> exec函数族中最后一个参数结尾必须是`NULL`.
