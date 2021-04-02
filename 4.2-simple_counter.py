from tkinter import *
"""简单计算器
    1.界面
    2.按钮（数字、运算符、清除）
    3.显示输入内容
    4.显示输出结果
"""

# 测试


def counter(self, *args):
    # 触发-计算事件
    global i_entry, r_entry
    i = i_entry.get().strip().replace("\n", "").encode()    # 提取输入内容
    r_entry.delete(0, END)    # 清除结果文本框内容
    r_entry.insert(0, eval(i))   # 计算输入内容，并显示结果


def clear(self, *args):
    # 触发-清除事件
    global i_entry, r_entry
    i_entry.delete(0, END)    # 清除输入文本框内容
    r_entry.delete(0, END)    # 清除结果文本框内容


root = Tk()
root.title("简单计算器")
Label(root, text = "输入").grid(row = 0, sticky = W)    # 输入文本框
i_entry = Entry(root)
i_entry.grid(row = 0, column = 1, sticky = E)

Label(root, text = "结果").grid(row = 1, sticky = W)    # 结果文本框
r_entry = Entry(root)
r_entry.grid(row = 1, column = 1, sticky = E)

b1 = Button(root, text = "计算")      # 计算按钮
b1.grid(row = 2, column = 0, sticky = E)
b1.bind("<Button-1>", counter)      # 绑定鼠标左键
b1.bind_all("<Return>", counter)    # 绑定回车键

b2 = Button(root, text = "清除")      # 清除按钮
b2.grid(row = 2, column = 1, sticky = E)
b2.bind("<Button-1>", clear)      # 绑定鼠标左键
b2.bind_all("<Delete>", clear)    # 绑定Delete键

root.mainloop()

