import tkinter as tk
import ctypes
from module_input_path import input_path_module
from module_UI_front_setting import  tkcreate


# 变量初始化
path = ""  # 路径存放


try: 
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def dir_refresh():
    global path
    path = input_path_module()


# 设置主屏幕
root = tk.Tk()  # 打开一个主屏幕
root.title("Taiko")  # 设置标题
root.geometry("900x500")  # 设置窗口大小
root.resizable(False,False)  # 不能被拖动窗口大小

# 将 root 传参给 tkc
tkc_root = tkcreate(root)

# 添加一个文本
tkc_root.tkc_text("nihao",10,10)

# 添加一个输入框
tkc_root.tkc_entry(10,50,50)

# 添加一个按钮
tkc_root.tkc_button("click",470,33,6,2,"yellow",dir_refresh)
print(path)

root.mainloop()