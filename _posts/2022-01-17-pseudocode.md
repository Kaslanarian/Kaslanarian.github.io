---
layout:     post
title:      基于LaTeX的伪代码书写
subtitle:   
date:       2022-01-17
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - LaTeX
---

笔者最开始是用`markdown`的代码块写算法伪代码:

```pseudocode
function CalculatePositiveSum(arr[1...n]):
    /* 计算数组非负数元素的和 */
    s <- 0
    foreach a in arr:
        if a >= 0:
            s <- s + a
    return s
```

但在后来，算法混入了很多的数学运算，此时继续使用`markdown`写为伪代码显然不利于观看，比如线性回归的解析解是

$$
\pmb w=(X^TX)^{-1}X^T\pmb y
$$

上面的公式无法用简单的文本表现出来。笔者后来考虑了用多行数学公式的方式写伪代码:

$$
\begin{aligned}
&\textbf{function }\text{LinearRegression}(X, \pmb y):\\
&\qquad\pmb w\gets(X^TX)^{-1}X^T\pmb y\\
&\qquad\textbf{return}\;\pmb w
\end{aligned}
$$

这样我们可以在非正式场合用这样的方法书写伪代码。但它还存在问题，比如居中格式看起来很不舒服。最后我们还是考虑使用LaTeX编写在论文中常见的算法伪代码格式，就像下图这样(选自《Coordinate Descent Method for Large-scale L2-loss Linear Support Vector Machines》):

<img src="/img/pseudo/image-20220116172910545.png" alt="image-20220116172910545" style="zoom:67%;" />

## 简单的LaTeX伪代码

在.tex文件中，先引入宏包

```latex
\usepackage{algorithm}
\usepackage{algorithmic}
```

然后写入

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
\end{algorithm}
```

就可以创建一个伪代码环境，如下图所示:

<img src="/img/pseudo/image-20220116174723271.png" alt="image-20220116174723271" style="zoom:67%;" />

此时伪代码是空的，我们在`algorithm`块中嵌入一个`algorithmic`块，可以发现我们是在代码块中内嵌数学公式:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
    \end{algorithmic}
\end{algorithm}
```

也就是说，伪代码是一个赋值语句，一行普通语句以"\STATE"开头:

<img src="/img/pseudo/image-20220116175034266.png" alt="image-20220116175034266" style="zoom:67%;" />

于是我们可以写出简单的伪代码了，比如对$x$进行各种操作:

```latex
\usepackage{amsmath}

\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
        \STATE $y\gets\sqrt{x}+1$
        \STATE $z\gets\dfrac{x}{y}$
    \end{algorithmic}
\end{algorithm}
```

生成多行伪代码:

<img src="/img/pseudo/image-20220116175429054.png" alt="image-20220116175429054" style="zoom:67%;" />

## 判断结构

上面的伪代码显然不能满足日常的需要，判断结构(if-else)和循环结构(for, while)是最常用的算法逻辑。我们用下面的LaTeX代码就可以实现一个简单判断结构:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
        \IF {$x\leq 0$}
        \STATE $x\gets x+1$
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

生成伪代码如下:

<img src="/img/pseudo/image-20220116183439834.png" alt="image-20220116183439834" style="zoom:67%;" />

注意到我们不需要手动缩进，只需要用"\IF"和"\ENDIF"限制范围即可。此外，IF后面的条件外面需要加上"{}"。类似的，加上\ELSE就可以实现一个完整的if-else子句:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
        \IF {$x\leq 0$}
        \STATE $x\gets x+1$
        \ELSE
        \STATE $x\gets x-1$
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

<img src="/img/pseudo/image-20220116183857474.png" alt="image-20220116183857474" style="zoom:67%;" />

伪代码中的else if对应\ELSIF:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
        \IF {$x\leq 0$}
        \STATE $x\gets x+1$
        \ELSIF{$x\geq1$}
        \STATE $x\gets x-1$
        \ELSE 
        \STATE $x\gets 2x$
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

<img src="/img/pseudo/image-20220116184429228.png" alt="image-20220116184429228" style="zoom:67%;" />

## 循环结构

类似if，我们可以用\WHILE来书写while循环:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$
        \WHILE {$x\leq10$}
        \STATE $x\gets x+1$
        \ENDWHILE
    \end{algorithmic}
\end{algorithm}
```

生成:

<img src="/img/pseudo/image-20220116210900667.png" alt="image-20220116210900667" style="zoom:67%;" />

除了While，还有algorithmic宏包还支持四种循环语法:

```latex
% for循环
\begin{algorithmic}
    \FOR {<condition>}
    \STATE <text>
    \ENDFOR
\end{algorithmic}

% forall循环
\begin{algorithmic}
    \FORALL {<condition>}
    \STATE <text>
    \ENDFOR
\end{algorithmic}

% repeat循环
\begin{algorithmic}
    \REPEAT <text>
    \UNTIL {<condition>}
\end{algorithmic}

% loop循环
\begin{algorithmic}
    \LOOP <text>
    \ENDLOOP
\end{algorithmic}
```

## 输入输出

在算法伪代码中，我们常常需要说明算法的输入和输出，帮助读者更好理解代码。而在`algorithmic`宏包中，输入对应\REQUIRE，输出对应\ENSURE:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \ENSURE{$x$}
        \REQUIRE{$y$}
        \STATE $x\gets0$
        \IF{$x\leq0$}
        \STATE{$y\gets-1$}
        \ELSE
        \STATE{$y\gets1$}
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

<img src="/img/pseudo/image-20220117134433863.png" alt="image-20220117134433863" style="zoom:67%;" />

如果更喜欢用INPUT表示输入，OUTPUT表示输出，可以对关键字重定义:

```latex
\renewcommand{\algorithmicrequire}{\textbf{Input:}}
\renewcommand{\algorithmicensure}{\textbf{Output:}}
```

这样上面的LaTeX代码生成的伪代码:

<img src="/img/pseudo/image-20220117134707967.png" alt="image-20220117134707967" style="zoom:67%;" />

## 杂项

#### 显示行号

在`\begin{algorithmic}`后面加上`[1]`，算法伪代码会显示行号:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}[1]
        \STATE $x\gets0$
        \IF {$x\leq1$}
        \STATE $x\gets x+1$
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

<img src="/img/pseudo/image-20220117141904227.png" alt="image-20220117141904227" style="zoom:67%;" />

[1]表示每行均显示行号，如果是[2]，意思是每2行显示一次行号。

#### 注释

\COMMENT命令会在算法伪代码中加上注释:

```latex
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \STATE $x\gets0$\COMMENT{This is a comment}
        \IF {$x\leq1$}
        \STATE $x\gets x+1$
        \ENDIF
    \end{algorithmic}
\end{algorithm}
```

<img src="/img/pseudo/image-20220117142302831.png" alt="image-20220117142302831" style="zoom:67%;" />

如果是IF、FOR这些语句，则需要这样写注释:

```latex
\IF[This is a comment] {<text>}
```

但这样效果不是很好，因为注释和代码距离太小。我们有更好的写注释方法:

```latex
\usepackage{algorithm}
\usepackage{algorithmicx}
\usepackage{algpseudocode}

\begin{document}
\begin{algorithm}
    \caption{Example Pseudocode}
    \begin{algorithmic}
        \State $x\gets0$
        \If {$x\leq1$}\Comment{Comment1}
        \State $x\gets x+1$\Comment{Comment2}
        \EndIf
    \end{algorithmic}
\end{algorithm}
\end{document}
```

`algorithmic`宏包和`algorithmicx`宏包用法几乎相同，只不过前者的命令全为大写，后者仅首字母大写。在引用`algpseudocode`后，注释变成了下面这样:

<img src="/img/pseudo/image-20220117144730568.png" alt="image-20220117144730568" style="zoom:67%;" />

这样注释的效果比之前要好不少。

#### `algorithmic`支持的宏

这里列举`algorithmic`支持的宏:

```latex
 \STATE <text>
 \IF{<condition>} \STATE {<text>} \ELSE \STATE{<text>} \ENDIF
 \IF{<condition>} \STATE {<text>} \ELSIF{<condition>} \STATE{<text>} \ENDIF
 \FOR{<condition>} \STATE {<text>} \ENDFOR
 \FOR{<condition> \TO <condition> } \STATE {<text>} \ENDFOR
 \FORALL{<condition>} \STATE{<text>} \ENDFOR
 \WHILE{<condition>} \STATE{<text>} \ENDWHILE
 \REPEAT \STATE{<text>} \UNTIL{<condition>}
 \LOOP \STATE{<text>} \ENDLOOP
 \REQUIRE <text>
 \ENSURE <text>
 \RETURN <text>
 \PRINT <text>
 \COMMENT{<text>}
 \AND, \OR, \XOR, \NOT, \TO, \TRUE, \FALSE
```

至此，我们可以用LaTeX写出简单的算法伪代码。
