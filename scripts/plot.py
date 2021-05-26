#!/usr/bin/python3
'''
我们尝试编写一个自动画图脚本：
1. 通过输入获取函数，格式：y = f(x)
2. 再获取函数值域信息
3. 画图
4. 保存图片到img文件夹
5. 自动插入到制定文章最末端
'''
import numpy as np
import matplotlib.pyplot as plt
from os import listdir


def input_handle(input: str) -> str:
    formula = input[2:]
    return formula.replace("^", "**")  # 转换幂运算符号
    


def plot(formula: str, a: float, b: float, name: str):
    length = b - a
    x = np.linspace(a, b, 50 * int(length))
    y = x
    exec("y = %s" % formula)
    plt.plot(x, y)
    plt.savefig("img/matplotlib/%s.jpg" % name)


def insert_md(complete_filename: str, picture_name: str):
    with open("_posts/" + complete_filename, "a+") as passage:
        passage.write("\n![%s](/img/matplotlib/%s.jpg)\n" %
                      (picture_name, picture_name))


def find_post(broken_filename: str):
    complete_list = listdir("_posts")
    file_list = [file_string[11:-3] for file_string in complete_list]
    for i in range(len(file_list)):
        if file_list[i] == broken_filename:
            index = i
            break
    if index == -1:
        print("file not found")
        complete_filename = None
    else:
        complete_filename = complete_list[index]
    return complete_filename


if __name__ == "__main__":
    pict_name = input("输入图片文件名：")
    plot(
        input_handle(input("输入公式：")),
        float(input("输入下界：")),
        float(input("输入上界：")),
        pict_name,
    )
    insert_md(
        find_post(input("输入要嵌入的文件名（日期后面的内容）：")),
        pict_name,
    )
    print("script works successfully")