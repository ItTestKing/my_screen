# coding:gbk
import os

"""
这个脚本的作用是，将手机截图放到指定目录。
具体实现方法如下：
1.导入os模块。
2.使用os.popen("执行语句")方法执行命令,执行语句中有中文需要加r。
3.使用os.path.exists(path)判断文件是否导入成功。

"""


class MyScreen():
    os.popen(r"adb pull /sdcard/DCIM/Screenshots/Screenshot_20190905-153411.png C:\Users\user\Desktop\软件分析检测\学习强国即时通讯")



