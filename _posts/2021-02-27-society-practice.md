---
layout:     post
title:      社会实践记录
subtitle:   数据处理
date:       2021-02-28
author:     Welt Xing
header-img: img/noelle.jpg
catalog:    true
tags:
    - 日常
---

## 数据源

数据：[关于疫情期间线下教学的调查](/file/society-practice/关于疫情期间线下教学的调查.xlsx)

数据是`excel`表格，选用最常用的`python`进行处理。你可以在[这里](/file/society-practice/关于疫情期间线下教学的调查.xlsx)获取初始数据

## 数据读取

```python
import pandas as pd
dataset = pd.read_excel(path)
```

## 数据预处理

### 数据区域截取

发现数据的包含了不少空行和空列。于是获取数据的语句改为：

```python
dataset = pd.read_excel("dataset.xlsx", index=false).iloc[:92, :11]
```

### 修改列名

表格中的列名过于冗杂，对程序设计带来不便，因此把列名转换为简短的英文是必要的，我作出的修改：

| 原列名                                                       | 现列名               |
| ------------------------------------------------------------ | -------------------- |
| 您现在就读于                                                 | diploma              |
| 您目前就读于何地                                             | location             |
| 目前，您的学校采取的是何种管理模式                           | measure              |
| 您的学校在疫情期间采取了何种措施                             | detailed measures    |
| 您个人认为您的学校在实行这些措施的时候实行力度如何           | intensity            |
| 那您对学校的监管方式及态度是否满意                           | evaluation           |
| 如果不太满意，那么是什么监管方式或态度导致您不太满意呢       | reason               |
| 针对目前的线下教育，您认为出现了哪些问题可能导致教育质量出现下滑 | quality_problem      |
| 针对这些问题，学校或老师采取了哪些措施                       | education_measures   |
| 你认为目前学校采取的这种教育措施是否有效                     | education_evaluation |
| 您对改良目前线下教育还有什么意见或建议                       | other_advice         |

### 处理空值

由于数据量不够，我准备将表中的空数据进行填充，发现空数据来源于问卷填写人的态度问题，空缺较多，所以将其删除。

### 指标数字化

由于表格中的内容大部分是中文，不利于结论分析，于是准备将指标数值化。

我们查看`diploma`列的内容：

```python
>> set(dataset.diploma)
{"小学", "高中", "大学"}
```

所以我们可以按照年龄大小进行数值化：

```python
d = {"小学": 1, "高中": 2, "大学": 3}
dataset.diploma = [d[x] for x in dataset.diploma]
```

我们接着对`measure`，`intensity`, `evaluation`和`education_evaluation`进行类似的操作，数值化规则如下：

| 指标\列名 | diploma | measure      | intensity | evaluation | education evaluation |
| --------- | ------- | ------------ | --------- | ---------- | -------------------- |
| 0         | 小学    | 不封闭式管理 | 非常松散  | 不满意     | 无效                 |
| 1         | 高中    | 半封闭式管理 | 较为松散  | 较不满意   | 较无效               |
| 2         | 大学    | 全封闭式管理 | 一般      | 较满意     | 较有效               |
| 3         |         |              | 较为严格  | 满意       | 有效                 |
| 4         |         |              | 非常严格  |            |                      |

你可以在[这里](/file/society-practice/indexize.xlsx)获取初步指标数字化的数据。

## 数据可视化

我们接下来会对数据处理后的数据进行一些可视化处理和分析，主要用到`matplotlib`和`seaborn`。

1. 先来看看我们调查对象的地域分布：

    ![distribution](/img/location_ratio.png)

    由于南京大学的地理位置和人际关系网络的辐射性，大部分调查对象的学校分布在我国东南部地区。

2. 防疫措施与采取措施学校数的关系:

    ![measure counter](/img/measure_count.png)

   我们可以发现“戴口罩”和“出入人员等级”几乎是学校防疫的标配，此外还可以发现，由于执行难度较大以及可能会影响教学质量，能减少或删除人数过多的集中授课的学校不是很多，组织错峰入校的学校更是少之又少。

3. 我们调查了学生们对学校防疫措施力度的评价：

    ![intensity counter](/img/intensity-count.png)(横轴的0~4分别表示非常松散，较为松散，一般，较为严格和非常严格，纵轴表示样本数)

    令人惊讶的是有不少同学觉得学校的防疫力度是较为松散的，说明全国各地确实零星存在学校管理不周到的问题。

4. 我们来看看学生是如何评价学校防疫政策的执行力度，纵轴表示评价的均值：

   ![intensity-evaluation](/img/evaluation_intensity.png)

   显然，学生们更喜欢松散一些的管理方案，因为严格的管控措施确实会给学习生活带来一些困扰。

5. 在疫情期间，学生由于会长时间“闭门造车”，有些会遇到学习上的问题，我们加以总结，统计结果如下：

    ![educational problems](/img/edu_problems.png)

    发现很多学生都在忏悔自己在家并没有认真学习（笔者也是），无人监管导致的学生自制力下降是一个普遍的问题，从另一角度说明了学校对学生发展的重要性。

6. 对此，学校也采取了一些措施来帮助学生克服这些困难：

    ![educational measres](/img/edu_measures.png)

    绝大多数学校增加了线上教育，再次基础上增加了授课时间，此外通过测验和提问加强了对学生的监管

7. 我们再来看看学生对学校措施的接纳程度：

    ![edu_eval](/img/education_eval.png)

    认为有效的同学只占$1.1\%$是因为学生普遍是较谦虚的，即使是觉得“有效”也会该填成“较有效”，我们还发现有近$1/4$的学生觉得措施无效，说明学生学习效果的两极分化现象存在。