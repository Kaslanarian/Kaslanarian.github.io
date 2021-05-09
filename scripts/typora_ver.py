#!/usr/bin/python3
'''
由于使用Typora作为markdown→PDF转换，
博客的文章由于图片链接和存在标题头，使得转换成PDF效果不尽人意，
因此该脚本尝试将指定的markdown文章转换成Typora版本markdown，
然后进行PDF转换
'''

import os

filename = input("输入文件名（日期后面的内容）：")
file_list = [file_string[11 : -3] for file_string in os.listdir("_posts")]
index = -1
for i in range(len(file_list)):
    if file_list[i] == filename:
        index = i
if index == -1:
    print("file not found")
else:
    complete_filename = os.listdir("_posts")[index]
    with open("_posts/" + complete_filename, "r") as passage:
        file_str = "".join(passage.readlines())
    
    # 删除yaml头
    head_end = file_str.find("---", 3) + 3
    while file_str[head_end] == '\n':
        head_end += 1
    passage_without_head = file_str[head_end:]
    
    # 修改图片路径
    key_str = "/img"
    index = 0
    while True:
        index = passage_without_head.find(key_str, index)
        if index == -1:
            break
        before = passage_without_head[:index]
        after = passage_without_head[index:]
        passage_without_head = before + ".." + after
        index += 3
    typora_passage = passage_without_head
    typora_name = input("输入生成文本的文件名：")
    with open("_posts/%s.md" % typora_name, "w") as f:
        f.write(typora_passage)
        print("转换完成")