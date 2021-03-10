#!/usr/bin/python3
import os

picture_path = "/home/welt/Pictures"

time_picutre_pair = dict([[
    os.path.getmtime(picture_path + "/" + name),
    name,
] for name in os.listdir(picture_path)])

picture_got = time_picutre_pair[sorted(time_picutre_pair)[-1]]
new_name = input("图片新名称：")
os.system("mv %s/%s ./img/%s.%s" % (
    picture_path,
    picture_got,
    new_name,
    picture_got[picture_got.rfind(".") + 1:],
))
