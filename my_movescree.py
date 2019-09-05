# coding:gbk
import os
import re

"""
这个脚本的作用是，将手机截图放到指定目录，并且删除截图。
具体实现方法如下：
1.取出所有截图。
2.判断本地文件夹是否有该截图。
3.有该截图，删除截图，没有该截图，将其存储到指定目录。
"""


class MyScreen(object):
    file_names = "Screenshot_20190905-153411.png"
    phone_paths = r" /sdcard/DCIM/Screenshots/"
    move_paths = r" C:\Users\user\Desktop\软件分析检测\学习强国即时通讯"
    all_screen = "adb shell ls -l /sdcard/DCIM/Screenshots/"
    result_list = None

    # 删除手机图片path是要传的参数。
    def screen_remove(self, path):
        # reslt = self.phone_path + self.move_paths
        # print(reslt)
        os.popen(r"adb shell rm" + self.phone_paths + path)
        print("删除文件{}".format(path))

    # 判断是否有该文件，如果有返回Ture，没有返回false
    def is_screen_in(self, phone_file):
        new_phone_file = phone_file.replace(' ', '').replace('/', '\\')
        # print(new_phone_file)
        # print(os.path.exists(new_phone_file))
        return os.path.exists(new_phone_file)

    # 遍历手机指定目录所有文件，并且返回一个文件列表。
    def walk_file(self):
        list = os.popen(self.all_screen)
        list_all = list.read()
        self.result_list = re.findall(r"S(.+?)g", list_all)
        # print(self.result_list)
        return self.result_list

    # 程序执行入口
    def mian(self):
        # 遍历指定目录
        list = self.walk_file()
        if not list:
            print("没有截屏!!!")
        else:
            for screen in list:
                file = "S" + screen + 'g'
                file_path = self.phone_paths + "S" + screen + 'g'
                if self.is_screen_in(self.move_paths + '\\' + file):
                    self.screen_remove(file)
                else:
                    os.popen(r"adb pull" + file_path + self.move_paths)
                    print("{} 成功保存到：{}".format(file, self.move_paths))


if __name__ == "__main__":
    MyScreen().mian()
