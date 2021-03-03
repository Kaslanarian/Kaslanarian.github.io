---
layout:     post
title:      关于pyecharts
subtitle:   学习记录
date:       2021-03-03
author:     Welt Xing
header-img: img/venti.png
catalog:    true
tags:
    - Python
---

# Pyecharts学习记录

## 引言

大一下修过《人工智能程序设计》，在那里初次接触了`pyecharts`，一个可视化效果非常好的图表绘画库，但当时前端知识为0，只能生成一个`html`文件之后截屏使用。最近随着博客的搭建，接触了一些`HTML`的知识，昨天又成功嵌入了一个`echarts`图表，随即兴趣大发，准备复习下原来学过的知识并将其制成个人手册，使得博客的多样性更加丰富。

## 参考

本文是对[官方教程](https://pyecharts.org/#/zh-cn/intro)的提炼，其中会删减不重要的内容，所以获得全部内容还请参考[这里](https://pyecharts.org/#/zh-cn/intro)

## Pyecharts获取相关

命令行输入

```bash
pip3 install pyecharts
```

就可以获取v1的`pyecharts`，顺带一提，当年学习的是v0.5的`pyecharts`，接口与现在是有区别的。

我们运行下面的$Python$脚本来测试安装是否成功：

```python
>> import pyecharts
>> print(pyecharts.__version__)
1.9.0
```

## 快速开始

我们用官网的例子作为快速开始程序：

```python
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.render()
```

调用`bar`的`render`函数可以将图表以`html`格式到处，默认是保存在脚本所在文件夹里，默认名是`render.html`，自然，你可以自定义保存路径和文件名。

### 链式调用

你也可以链式调用函数以生成图表：

```python
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
bar.render()
```

两脚本的执行结果相同：

![pyecharts1](/img/pyecharts1.png)

### 使用配置项

我们当然不能傻瓜一般地使用默认生成的图表，若我们想要修改大小，颜色，主题等配置时，就要用到`options`配置项，“在`pyecharts`中，一切皆Options”

```python
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render()
```

可以发现我们为图表加入了主标题和副标题：

![pyecharts2](/img/pyecharts2.png)

### 使用主题

主题的使用可以使你的可视化效果更好，更有美观性。

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT)).add_xaxis(
    ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋",
     "袜子"]).add_yaxis("商家A", [5, 20, 36, 10, 75, 90]).add_yaxis(
         "商家B", [15, 6, 45, 20, 35, 66]).set_global_opts(
             title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")))
bar.render()
```

下面是主题效果：

![pyecharts3](/img/pyecharts3.png)

### 图表嵌入

我们可以在个人博客中嵌入`pyecharts`生成的`HTML`文件，接下来可以看到它比图表更具有表现力。我们用上面的图表作为测试。

[这个](/file/pyecharts1.html)就是我们生成的HTML文件。我们按照网上的方法，修改HTML文件中图表的大小，再利用iframe标签进行插入：

```html
<iframe src="/file/pyecharts1.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400"
        frameborder="no">
</iframe>
```
我们在这里将`width`和`height`设置为700和400，那么在HTML文件中，就需要将HTML的配置项中的宽度和高度设为相同值：

```html
<div id="6329c2a1f2e0414b8bb6cc96d72d8f51" 
        class="chart-container" 
        style="width:700px; height:400px;">
</div>
```

效果如下，你可以将光标移动到色块上观察效果：

<iframe src="/file/pyecharts1.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

