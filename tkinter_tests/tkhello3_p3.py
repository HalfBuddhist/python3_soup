#!/usr/bin/env python
# coding=utf-8
"""
例19.3 标签和按钮组件演示（tkhello3.py）'
"""

import tkinter

top = tkinter.Tk()
hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()