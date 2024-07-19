#!/usr/bin/python3

"""
实例14: 第三方库自动安装脚本
"""

import os


def batch_install(libs):
    """
    批量安装第三方库
    :param libs: 第三方库名称集合
    :return:
    """
    try:
        for lib in libs:
            os.system("pip install " + lib)
            print(lib + " is installed successfully!")
        print("all libs are installed successfully!")
    except:
        print("Abort for failed somehow......")
    return


def batch_uninstall(libs):
    """
    批量安装第三方库
    :param libs: 第三方库名称集合
    :return:
    """
    try:
        for lib in libs:
            os.system("pip uninstall " + lib)
            print(lib + " is uninstalled successfully!")
        print(" all libs are uninstalled successfully!")
    except:
        print("Abort for failed somehow......")
    return


def main():
    libs = {"jieba", "wordcloud", "imageio"}
    batch_install(libs)


main()
