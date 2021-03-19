#!/usr/bin/python3

import time, os

localtime = time.localtime(time.time())

year = str(localtime.tm_year)
month = "%02d" % localtime.tm_mon
day = "%02d" % localtime.tm_mday
name = input("输入文章名：") + ".md"
date = "-".join([year, month, day])
filename = "-".join([date, name])

for fname in os.listdir("_posts"):
    if fname == filename:
        print("File name \"%s\" has exists" % filename)
    else:
        with open("_posts/" + filename, "w") as file:
            file.write("---\n")
            file.write("layout:     post\n")
            file.write("title:\n")
            file.write("subtitle:\n")
            file.write("date:       %s\n" % date)
            file.write("author:     Welt Xing\n")
            file.write("header-img:\n")
            file.write("catalog:    true\n")
            file.write("tags:\n")
            file.write("---\n")