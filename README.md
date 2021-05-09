# 关于博客脚本

在编写博客时为了便于批处理，新建了`scripts`文件夹并在其中加入脚本:

- img_handle.py : 在Ubuntu系统中进行截图后，脚本会自动将图片资源移入img文件夹；

```shell
# 在主文件夹中运行：
> ./scripts/img_handle.py
图片新名称：test
> # 此时会在img文件夹中生成一个test.X图片
```

- post_gen.py : 自动生成指定文件名的新md文件，用于撰写博客：

```shell
# 在主文件夹中运行：
> ./scripts/post_gen.py
输入文章名：test
> # 此时会在_posts文件夹中生成一个20XX-XX-XX-test.md文件，其中"XX"都是当前日期
```

- typora_ver.py : 将博客md文件转换为typora格式的markdown，以便PDF转换.

```shell
> ./scripts/typora_ver.py
输入文件名（日期后面的内容）：test # 忽略日期
输入生成文本的文件名：test
转换完成
> # 此时_posts文件夹中会出现test.md文件，尝试用typora打开它看看效果吧
```
