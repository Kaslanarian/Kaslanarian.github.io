#!/usr/bin/python3
'''
由于WSL下markdown插件存在回车和退格键
延迟时间长的原因，我更愿意在Windows本地
的typora写作，因此这个脚本是来将typora
版本的markdown转成博文形式的自动化方法
'''

import os
import time
import re
from sys import argv

# 时间准备
localtime = time.localtime(time.time())

year = str(localtime.tm_year)
month = "%02d" % localtime.tm_mon
day = "%02d" % localtime.tm_mday
date = "-".join([year, month, day])

# typora版本md路径准备
typora_path = argv[1]  # 第一个参数

# 组合成新文件名
filename = "_posts/" + "-".join(
    [date, typora_path[typora_path.rfind('/') + 1:]])

# 查重
for fname in os.listdir("_posts"):
    assert fname != filename, "文章名 %s 重复，文章创建失败" % filename

# 默认背景
picture_path = "img/genshin.jpg"

# 默认作者
author_name = "Welt Xing"

# 要插入的yaml头
yaml_head = '''---
layout:     post
title:      %s
subtitle:   %s
date:       %s
author:     %s
header-img: %s
catalog:    true
tags:
---
''' % (
    "Title",
    "Subtitle",
    date,
    author_name,
    picture_path,
)

# 读文件
with open(typora_path, "r") as f:
    typora_text = "".join(f.readlines())

# 加入yaml头
blog_text = yaml_head + typora_text

# 处理图片等资源的迁移问题
rex = r'\!\[.*?\]\(.*?\)'
link_list = re.findall(rex, blog_text)
target_path = "./img/"

for link in link_list:
    # e.g. ![image-20210520235006246](C:\Users\17530\AppData\Roaming\Typora\typora-user-images\image-20210520235006246.png)
    start = link.find('(')
    src_path = link[start + 1:-1]
    os.system(
        "cp %s %s" %
        (src_path.replace('\\', '/').replace('C:', '/mnt/c'), target_path))
    # 修改blog_text中的文件名
    blog_text = blog_text.replace(
        src_path,
        target_path[1:] +
        src_path[max(src_path.rfind('\\'), src_path.rfind('/')) + 1:],
    )

# 处理公式现实问题：要在前一个"$$"前换行，在后一个"$$"后换行

# rex = r'\$\$\n.*?\n\$\$'
# formula_list = re.findall(rex, blog_text)

# for formula in formula_list:
    # blog_text = blog_text.replace(formula, '\n' + formula + '\n')

# 写新文件
print(filename)
with open(filename, "w") as f:
    f.write(blog_text)

print("convert over")