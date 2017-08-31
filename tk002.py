#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 21:15
# @Author  : 李振华

import tkinter


# Window Manager 窗口管理器
# 设置界面的图标，标题大小和偏移量
def application():
    # 创建一个窗口对象
    top = tkinter.Tk()
    # 设置窗口的大小和对于屏幕的偏移量，其中'x'是英文字母，前面两个数值为长宽，后面两个数值为相对于屏幕最左和最上边的距离
    top.wm_geometry("500x300+200+100")
    # 设置窗口标题
    top.wm_title('python tkinter 学习')
    # 设置窗口图标
    # 生成icon图标的链接：https://www.ico.la
    top.wm_iconbitmap("resource/icon.ico")

    # 设置主循环
    top.mainloop()


if __name__ == "__main__":
    # 调用函数
    application()
