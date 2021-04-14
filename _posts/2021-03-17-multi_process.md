---
layout:     post
title:      C的进程编程
subtitle:   以及操作系统相关知识的学习
date:       2021-03-17
author:     Welt Xing
header-img: img/process_header.jpg
catalog:    true
tags:
    - 操作系统
    - 编程技术
---

## 引入

在$\text{Linux}$中，一个进程可以创建新的进程，这两个进程分别称作父进程和子进程，如此下去，就会形成一个进程树，如图是一个典型$\text{Linux}$系统的一个进程树：

![进程树](http://c.biancheng.net/uploads/allimg/181102/2-1Q1021100135W.gif)

图中的$\text{pid}$叫做进程标识符，通常是个整数，它可以用作索引，以便访问内核中的进程的各种属性。

> 进程`init`的pid总是1，是所有用户进程的父进程.

## 进程创建

```cpp
#include <stdio.h>
#include <sys/types.h>
int main() {
    fork();
    printf("Hello world!");
    return 0;
}
```

编译运行程序，我们会看到两个$\text{Hello world!}$的输出，所以这里其实是**运行了两次程序**，这是我们就可以发现`fork`系统调用的用途：创建进程.

我们试着对上面的程序做一些修改：

```cpp
#include <stdio.h>
#include <unistd.h>
int main() {
    fork();
    fork();
    fork();
    printf("Hello world!");
    return 0;
}
```

猜猜会输出几个Hello world？实际上是8个！我们来分析一下：

假设我们的程序是这样的：

```cpp
int main() {
    ... // n的赋值
    for(int i = 0; i < n; i++) {
        fork();
    }
    printf("Hello world!");
}
```

第一行的`fork`，创建了一个子进程，该子进程和父进程一样都要运行$n-1$次`fork()`和输出一次$\text{Hello world!}$. 我们设$f(n)$为需要执行$n$个`fork()`语句的进程会输出的$\text{Hello world!}$的句数，那么我们就有：

$$
\begin{cases}
f(n)=2f(n-1),n\ge1\\
f(1)=1,n=0
\end{cases}
$$

所以当有$n$句连续的`fork()`语句时会输出$2^{n}$次$\text{Hello world!}$.

## 进程的独立性

试着运行下面的程序：

```cpp
int main() {
    int x = 1;
    if (0 == fork()) {
        printf("child process %d\n", --x);
    } else {
        printf("parent process %d\n", ++x);
    }
    return 0;
}
```

编译运行后输出如下：

```bash
parent process 2
child process 0
```

显然，两个进程只是运行了相同的程序，彼此不会影响，这里体现出进程的“独立性”.

## fork()和exec()

fork()虽然创建了进程，但仍是原来程序的复制，而`exec()`系统调用则是用一个新的程序去替换原程序，使得进程更加自由.

我们直接看程序，之后解释程序的含义：

```cpp
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
    pid_t pid;
    pid = fork(); /* fork a child process */
    if (pid < 0) {  /* error occurred */
        fprintf(stderr, "Fork Failed\n");
        return 1;
    } else if (pid == 0) { /* child process */
        execlp("/bin/ls", "ls", NULL);
    } else { /* parent process */
        /* parent will wait for the child to complete */
        wait(NULL); 
        printf("Child completed\n");
    }
    return 0;
}
```

我们在命令行输入：

```bash
$gcc test.c -o test
$./test
test  test.c
Child completed
```

我们调用Linux系统调用`fork()`，系统便创建一个子进程，父进程的$\text{pid}$大于0，而子进程的$\text{pid}$为0，父进程会等待直到子进程结束，子进程则是调用`exec`系统调用，执行`ls`指令，具体流程如下图所示：

![程序流程图](http://c.biancheng.net/uploads/allimg/181102/2-1Q102110425511.gif)

## exec函数族

事实上，C中并不存在`exec`函数，而是由execl, execlp, execle, execv, execvp, execve等函数组成的函数族（$\text{exec family}$），这些函数参数不同，但功能相同，都是用一个新的程序去替换原程序（replaces the current process image with a new process image）。下面是

```cpp
/* Execute PATH with arguments ARGV and environment from `environ'.  */
extern int execv (const char *__path, char *const __argv[])
     __THROW __nonnull ((1, 2));

/* Execute PATH with all arguments after PATH until a NULL pointer,
   and the argument after that for environment.  */
extern int execle (const char *__path, const char *__arg, ...)
     __THROW __nonnull ((1, 2));

/* Execute PATH with all arguments after PATH until
   a NULL pointer and environment from `environ'.  */
extern int execl (const char *__path, const char *__arg, ...)
     __THROW __nonnull ((1, 2));

/* Execute FILE, searching in the `PATH' environment variable if it contains
   no slashes, with arguments ARGV and environment from `environ'.  */
extern int execvp (const char *__file, char *const __argv[])
     __THROW __nonnull ((1, 2));

/* Execute FILE, searching in the `PATH' environment variable if
   it contains no slashes, with all arguments after FILE until a
   NULL pointer and environment from `environ'.  */
extern int execlp (const char *__file, const char *__arg, ...)
     __THROW __nonnull ((1, 2));

...

/* Replace the current process, executing PATH with arguments ARGV and
   environment ENVP.  ARGV and ENVP are terminated by NULL pointers.  */
extern int execve (const char *__path, char *const __argv[],
           char *const __envp[]) __THROW __nonnull ((1, 2));
```

## 进程终止

当进程完成执行最后语句并且通过系统调用`exit()`请求操作系统删除自身时，进程终止。这时，进程可以返回状态值（通常为整数）到父进程（通过系统调用`wait()`）。所有进程资源，如物理和虚拟内存、打开文件和 I/O 缓冲区等，会由操作系统释放.

父进程终止子进程的原因有很多，如：

1. 子进程使用了超过它所分配的资源。（为判定是否发生这种情况，父进程应有一个机制，以检查子进程的状态）。
2. 分配给子进程的任务，不再需要。
3. 父进程正在退出，而且操作系统不允许无父进程的子进程继续执行。

事实上，在正常终止时，`exit()`可以直接调用，也可以间接调用（通过`main()`的返回语句）。
