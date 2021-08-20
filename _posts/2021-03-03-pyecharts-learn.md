---
layout:     post
title:      关于pyecharts
subtitle:   学习记录
date:       2021-03-03
author:     Welt Xing
header-img: img/pyecharts_header.jpg
catalog:    true
tags:
    - 编程技术
---

# Pyecharts学习记录

## 引言

大一下修过《人工智能程序设计》，在那里初次接触了`pyecharts`，一个可视化效果非常好的图表绘画库，但当时前端知识为0，只能生成一个`html`文件之后截屏使用。最近随着博客的搭建，接触了一些`HTML`的知识，昨天又成功嵌入了一个`echarts`图表，随即兴趣大发，准备复习下原来学过的知识并将其制成个人手册，使得博客的多样性更加丰富，同时为日后的数据可视化工作提供模板和带来便利。

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

#### 链式调用

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

#### 使用配置项

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

#### 使用主题

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

#### 图表嵌入

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

## 全局配置项

全局配置项可通过`set_global_opts`方法设置。

下面是各种配置项的位置情况：

![global opts](/img/global_opts.png)

我们在此记录较重要和常用的配置

#### 初始化配置项

我们在之前设置主题时用到了下面的语句：

```python
Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT)
```

这里就是初始化配置项填写的位置，具体参数说明：

|     参数名     |          数据类型          |       默认值        |                             说明                             |
| :------------: | :------------------------: | :-----------------: | :----------------------------------------------------------: |
|     width      |            str             |       "900px"       |                  图表画布宽度，css长度单位                   |
|     height     |            str             |       "500px"       |                  图表画布高度，css长度单位                   |
|    chart_id    |       Optional[str]        |        None         |          图表 ID，图表唯一标识，用于在多图表时区分           |
|    renderer    |            str             |      "canvas"       |                渲染风格，可选 "canvas"，"svg"                |
|   page_title   |            str             | "Awesome-pyecharts" |                           网页标题                           |
|     theme      |            str             |       "white"       |                           图表主题                           |
|    bg_color    |       Optional[str]        |        None         |                         图表背景颜色                         |
|    js_host     |            str             |         ""          | 远程 js host，如不设置默认为 https://assets.pyecharts.org/assets/" |
| animation_opts | Union[AnimationOpts, dict] |   AnimationOpts()   |   画图动画初始化配置，参考 `global_options.AnimationOpts`    |

#### 标题配置项

我们要这样修改标题配置项：

```python
bar.set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"}
```

更多配置如下表所示：

|     参数名      |         数据类型         | 默认值 |                             说明                             |
| :-------------: | :----------------------: | :----: | :----------------------------------------------------------: |
|      title      |      Optional[str]       |  None  |                主标题文本，支持使用 \n 换行。                |
|   title_link    |      Optional[str]       |  None  |                     主标题跳转 URL 链接                      |
|  title_target   |      Optional[str]       |  None  | 主标题跳转链接方式，默认值是: blank ，可选参数: 'self', 'blank' ，self' 当前窗口打开; 'blank' 新窗口打开 |
|    subtitle     |      Optional[str]       |  None  |                 副标题文本，支持使用 \n 换行                 |
|  subtitle_link  |      Optional[str]       |  None  |                     副标题跳转 URL 链接                      |
| subtitle_target |      Optional[str]       |  None  | 副标题跳转链接方式，默认值是: blank ，可选参数: 'self', 'blank' ，self' 当前窗口打开; 'blank' 新窗口打开 |
|    pos_left     |      Optional[str]       |  None  | title 组件离容器左侧的距离，left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，也可以是 'left', 'center', 'right' |
|     padding     | Union[Sequence, Numeric] |   5    | 标题内边距，单位px，默认各方向内边距为5，接受数组分别设定上右下左边距，分别设置四个方向的内边距：padding: [5， 10， 5， 10]，分别是上，右，下，左 |
|    item_gap     |         Numeric          |   10   |                      主副标题之间的间距                      |

其余的配置相对来说不是很重要，在此省略。

## 图表

接下来会介绍几类常用的图表的例子，并将其嵌入在网页中

#### 柱状图

```python
import pyecharts.options as opts
from pyecharts.charts import Bar, Line

x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

bar = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="蒸发量",
        y_axis=[
            2.0,
            4.9,
            7.0,
            23.2,
            25.6,
            76.7,
            135.6,
            162.2,
            32.6,
            20.0,
            6.4,
            3.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="降水量",
        y_axis=[
            2.6,
            5.9,
            9.0,
            26.4,
            28.7,
            70.7,
            175.6,
            182.2,
            48.7,
            18.8,
            6.0,
            2.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="温度",
            type_="value",
            min_=0,
            max_=25,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="水量",
            type_="value",
            min_=0,
            max_=250,
            interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="平均温度",
        yaxis_index=1,
        y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line).render("mixed_bar_and_line.html")
```
<iframe src="/file/mixed_bar_and_line.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>


#### 饼图

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-Base"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("./file/pie_base.html")
)
```

<iframe src="/file/pie_base.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>


这里的数据来自`Pyecharts`提供的`dataset`，但我们可以知道数据格式必须是`list(dict)`。

#### 关系图

```python
from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "node 1", "symbolSize": 10},
    {"name": "node 2", "symbolSize": 20},
    {"name": "node 3", "symbolSize": 30},
    {"name": "node 4", "symbolSize": 40},
    {"name": "node 5", "symbolSize": 50},
    {"name": "node 6", "symbolSize": 40},
    {"name": "node 7", "symbolSize": 30},
    {"name": "node 8", "symbolSize": 20},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-Base"))
    .render("graph_base.html")
)
```

我们将每个节点之间都连上：

<iframe src="/file/graph_base.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

#### 雷达图

```python
import pyecharts.options as opts
from pyecharts.charts import Radar

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

(Radar(init_opts=opts.InitOpts(
    width="1280px", height="720px", bg_color="#CCCCCC")).add_schema(
        schema=[
            opts.RadarIndicatorItem(name="销售（sales）", max_=6500),
            opts.RadarIndicatorItem(name="管理（Administration）", max_=16000),
            opts.RadarIndicatorItem(name="信息技术（Information Technology）",
                                    max_=30000),
            opts.RadarIndicatorItem(name="客服（Customer Support）", max_=38000),
            opts.RadarIndicatorItem(name="研发（Development）", max_=52000),
            opts.RadarIndicatorItem(name="市场（Marketing）", max_=25000),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    ).add(
        series_name="预算分配（Allocated Budget）",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    ).add(
        series_name="实际开销（Actual Spending）",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
    ).set_series_opts(label_opts=opts.LabelOpts(
        is_show=False)).set_global_opts(
            title_opts=opts.TitleOpts(title="基础雷达图"),
            legend_opts=opts.LegendOpts()).
 render("/home/welt/Desktop/Kaslanarian.github.io/file/basic_radar_chart.html")
 )
```

<iframe src="/file/basic_radar_chart.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

#### 散点图

```python
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker

c = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
        visualmap_opts=opts.VisualMapOpts(max_=150),
    )
    .render("scatter_visualmap_color.html")
)
```

<iframe src="/file/scatter_visualmap_color.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

#### 3D曲面图

```python
import math
from typing import Union

import pyecharts.options as opts
from pyecharts.charts import Surface3D

def float_range(start: int,
                end: int,
                step: Union[int, float],
                round_number: int = 2):
    """
    浮点数 range
    :param start: 起始值
    :param end: 结束值
    :param step: 步长
    :param round_number: 精度
    :return: 返回一个 list
    """
    temp = []
    while True:
        if start < end:
            temp.append(round(start, round_number))
            start += step
        else:
            break
    return temp


def surface3d_data():
    for t0 in float_range(-3, 3, 0.05):
        y = t0
        for t1 in float_range(-3, 3, 0.05):
            x = t1
            z = math.sin(x**2 + y**2) * x / 3.14
            yield [x, y, z]


(Surface3D(init_opts=opts.InitOpts(width="1600px", height="800px")).add(
    series_name="",
    shading="color",
    data=list(surface3d_data()),
    xaxis3d_opts=opts.Axis3DOpts(type_="value"),
    yaxis3d_opts=opts.Axis3DOpts(type_="value"),
    grid3d_opts=opts.Grid3DOpts(width=100, height=40, depth=100),
).set_global_opts(visualmap_opts=opts.VisualMapOpts(
    dimension=2,
    max_=1,
    min_=-1,
    range_color=[
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#ffffbf",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ],
)).render("surface_wave.html"))
```

<iframe src="/file/surface_wave.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

#### 树图

```python
from pyecharts import options as opts
from pyecharts.charts import Tree


data = [
    {
        "children": [
            {"name": "B"},
            {
                "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
                "name": "C",
            },
            {
                "children": [
                    {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                    {"name": "H"},
                ],
                "name": "D",
            },
        ],
        "name": "A",
    }
]
c = (
    Tree()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    .render("/home/welt/Desktop/Kaslanarian.github.io/file/tree_base.html")
)
```

<iframe src="/file/tree_base.html" 
        scrolling="no" 
        allowfullscreen="true" 
        width="700" 
        height="400" 
        frameborder="no">
</iframe>

至此，我们总结出大部分常用的图表的基本形式，如果对自定义要求不高的话，完全可以做到开箱即用。