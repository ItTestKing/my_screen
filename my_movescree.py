# coding:gbk
import os
import re

"""
����ű��������ǣ����ֻ���ͼ�ŵ�ָ��Ŀ¼������ɾ����ͼ��
����ʵ�ַ������£�
1.ȡ�����н�ͼ��
2.�жϱ����ļ����Ƿ��иý�ͼ��
3.�иý�ͼ��ɾ����ͼ��û�иý�ͼ������洢��ָ��Ŀ¼��
"""


class MyScreen(object):
    file_names = "Screenshot_20190905-153411.png"
    phone_paths = r" /sdcard/DCIM/Screenshots/"
    move_paths = r" C:\Users\user\Desktop\����������\ѧϰǿ����ʱͨѶ"
    all_screen = "adb shell ls -l /sdcard/DCIM/Screenshots/"
    result_list = None

    # ɾ���ֻ�ͼƬpath��Ҫ���Ĳ�����
    def screen_remove(self, path):
        # reslt = self.phone_path + self.move_paths
        # print(reslt)
        os.popen(r"adb shell rm" + self.phone_paths + path)
        print("ɾ���ļ�{}".format(path))

    # �ж��Ƿ��и��ļ�������з���Ture��û�з���false
    def is_screen_in(self, phone_file):
        new_phone_file = phone_file.replace(' ', '').replace('/', '\\')
        # print(new_phone_file)
        # print(os.path.exists(new_phone_file))
        return os.path.exists(new_phone_file)

    # �����ֻ�ָ��Ŀ¼�����ļ������ҷ���һ���ļ��б�
    def walk_file(self):
        list = os.popen(self.all_screen)
        list_all = list.read()
        self.result_list = re.findall(r"S(.+?)g", list_all)
        # print(self.result_list)
        return self.result_list

    # ����ִ�����
    def mian(self):
        # ����ָ��Ŀ¼
        list = self.walk_file()
        if not list:
            print("û�н���!!!")
        else:
            for screen in list:
                file = "S" + screen + 'g'
                file_path = self.phone_paths + "S" + screen + 'g'
                if self.is_screen_in(self.move_paths + '\\' + file):
                    self.screen_remove(file)
                else:
                    os.popen(r"adb pull" + file_path + self.move_paths)
                    print("{} �ɹ����浽��{}".format(file, self.move_paths))


if __name__ == "__main__":
    MyScreen().mian()
