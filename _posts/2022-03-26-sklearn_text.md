---
layout:     post
title:      sklearn中的文本特征提取
subtitle:   实现针对中文特征提取的sklearn接口
date:       2022-03-26
author:     Welt Xing
header-img: img/genshin.jpg
catalog:    true
tags:
    - 自然语言处理
---

## 引言

最近在学习《自然语言处理》课程，第一次作业是使用非深度方法进行中文文本分类。笔者手动实现了数据的简单预处理，包括

- 文本分词；
- 停用词删除；
- 基于词袋模型构建词向量和文档向量。

最后笔者得到的数据集$X$是一个数量级为$10^6\times10^6$的非负整数矩阵。但当使用`sklearn`中的模型，比如`LinearSVC`进行分类时，会将$X$中元素转化成`float64`类型。这将使得矩阵空间超出内存。显然我们应将$X$转换成稀疏矩阵。笔者这里转换思路，准备调查现在的软件包，比如NLTK，`sklearn`中是否有实现特征提取的API。

在`sklearn.feature_extraction.text`中，有能够将文本特征向量化的接口，本篇是对这些接口的解释和使用。

## sklearn支持的向量化

`sklearn`支持三种对文档的向量化：

1. `CountVectorizer`：朴素的词袋模型，文档向量为词汇表中的单词词频；
2. `TfidfVectorizer`：文档向量为词频-逆文档频率；
3. `HashingVectorizer`：用于一致地散列单词，然后根据需要标记和编码文件。

我们这里只介绍前两个API，因为后一个很少使用。先用下面的语料库作为例子：

```python
corpus = [
    "I have a dog.",
    "You have a dog and a cat.",
    "He books a book.",
    "No cost too great.",
]
```

先看`CountVectorizer`，用法和一般的sklearn非训练类模型类似：

```python
from sklearn.feature_extraction.text import CountVectorizer

counter = CounterVectorizer() # 先使用默认参数
counter.fit(corpus)
X = counter.transform(corpus)
```

我们可以得到所输入语料库的词汇表：

```python
print(counter.vocabulary_)
```

输出字典，其键为单词，对应的值是单词在词汇表中的位置。

```python
{'have': 7, 'dog': 5, 'you': 11, 'and': 0, 'cat': 3, 'he': 8, 'books': 2, 'book': 1, 'no': 9, 'cost': 4, 'too': 10, 'great': 6}
```

可以发现一些单词，比如"I"，并没有出现在词汇表中，这里的原因我们后面会提到。

现在看语料库的向量化表示

```python
print(X.todence()) # X是一个稀疏矩阵，输出稠密化表示
```

就是

$$
\begin{bmatrix}
0&0&0&0&0&1&0&1&0&0&0&0\\
1&0&0&1&0&1&0&1&0&0&0&1\\
0&1&1&0&0&0&0&0&1&0&0&0\\
0&0&0&0&1&0&1&0&0&1&1&0\\
\end{bmatrix}
$$

比如第一行就是第一个文档，可以发现"have"和"dog"对应的位置上的值为1，表示出现了一次。

一些词语在某一文档中出现次数多，不一定代表它是特定类别的关键词。比如"the"，如果不考虑它是停用词，那么它在各个文档中出现的次数都很多。一个重要的关键词，不仅要它在该类文本中出现次数多，还要在其它文本中出现次数足够小。TF-IDF（Term frequency-Inverse document frequency）就是这样的度量指标。而`TfidfVectorizer`计算的就是以TF-IDF作为元素的文本表示向量：

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer() # 先使用默认参数
counter.fit(corpus)
X = counter.transform(corpus)
```

用同样的方式输出`X`，得到矩阵

```python
[[0.         0.         0.         0.         0.         0.70710678
  0.         0.70710678 0.         0.         0.         0.        ]
 [0.48546061 0.         0.         0.48546061 0.         0.38274272
  0.         0.38274272 0.         0.         0.         0.48546061]
 [0.         0.57735027 0.57735027 0.         0.         0.
  0.         0.         0.57735027 0.         0.         0.        ]
 [0.         0.         0.         0.         0.5        0.
  0.5        0.         0.         0.5        0.5        0.        ]]
```

此时矩阵元素不再是正整数，而是正实数。

## sklearn向量化的缺陷

`sklearn`**是不支持中文的**，查看上面提到的API的源码，我们发现它们使用的是正则表达式对语句进行tokenize：

```python
'''
token_pattern : str, default=r"(?u)\\b\\w\\w+\\b"
        Regular expression denoting what constitutes a "token", only used
        if ``analyzer == 'word'``. The default regexp select tokens of 2
        or more alphanumeric characters (punctuation is completely ignored
        and always treated as a token separator).

        If there is a capturing group in token_pattern then the
        captured group content, not the entire match, becomes the token.
        At most one capturing group is permitted.
'''
```

上面的字符串节选自`CountVectorizer`的参数说明，用户实际上可以指定进行语义分割的正则表达式，默认的正则表达式是`(?u)\b\w\w+\b`。前面的`?u`表示打开`re.U`，也就是Unicode匹配，这是为了应对非英文的文字，比如法文，德文。但前提都是可按照空格划分的，看正则表达式后面的`\b\w\w+\b`，`\b`表示单词边界，这就注定了这些API不支持中文，`\w`匹配字母数字，可以发现这里限制了单词中字母数字的出现次数不小于2，这也是前面为什么一些单词被删掉了，比如"I"。

一个可行的解决方案是指定`tokenizer`参数，比如

```python
from sklearn.feature_extraction.text import CountVectorizer
from jieba import lcut

corpus = [
    "昨天我吃了一个坏苹果",
    "我肚子疼，他送我去医院",
    "医生让我不要再做这种事",
]
counter = CountVectorizer(tokenizer=lcut)
counter.fit(corpus)
print(counter.vocabulary_)
```

输出中文的词典

```python
{'昨天': 13, '我': 12, '吃': 10, '了': 2, '一个': 0, '坏': 11, '苹果': 15, '肚子疼': 14, '，': 19, '他': 4, '送': 18, '去': 9, '医院': 8, '医生': 7, '让': 16, '不要': 1, '再': 6, '做': 5, '这种': 17, '事': 3}
```

显然”了“等词属于停用词，应当删去，`sklearn.*Vectorizer`支持停用词筛选，但只支持英文词库和自定义词库，可以用列表作为词库：

```python
counter = CountVectorizer(
    tokenizer=lcut,
    stop_words=["了", "，"]
)
```

词典就缩减为

```python
{'昨天': 12, '我': 11, '吃': 9, '一个': 0, '坏': 10, '苹果': 14, '肚子疼': 13, '他': 3, '送': 17, '去': 8, '医院': 7, '医生': 6, '让': 15, '不要': 1, '再': 5, '做': 4, '这种': 16, '事': 2}
```

## 我们能做什么

原生的`sklearn`中文文本特征提取的缺陷：

- 需要额外指定中文分词器，如果要对分词器指定参数，需要用到`functools.partial`等额外工具；
- 不支持中文的停用词，需要自己收集；
- 如果指定最大`n_gram`大于1，会形成不规范的，用空格进行连接的词语。

面对这些问题，我们仿照`sklearn`的语法编写了一个基于`jieba`的[中文文本向量化API](https://github.com/Kaslanarian/SklearnFeatureExtraction4CN)。支持了停用词，多种分词方式。此外，我们实现了将我们的API嵌入到`sklearn`的脚本（目前只有Windows平台）。这样我们就可以在本地的任何路径，只要调用

```python
from sklearn.feature_extraction.cn_text import CNCountVectorizer, TfidfVectorizer
```

来进行特征提取。
