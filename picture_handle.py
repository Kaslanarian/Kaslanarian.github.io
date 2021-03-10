#!/usr/bin/python3
import os, shutil

picture_path = "/home/welt/Pictures"

time_picutre_pair = dict([[
    os.path.getmtime(picture_path + "/" + name),
    name,
] for name in os.listdir(picture_path)])

picture_got = time_picutre_pair[sorted(time_picutre_pair)[-1]]
new_name = input("图片新名称：")

shutil.move("%s/%s" % (
    picture_path,
    picture_got,
), "./img")

shutil.move(
    "./img/%s" % (picture_got),
    "./img/%s" % new_name + picture_got[picture_got.rfind("."):],
)
