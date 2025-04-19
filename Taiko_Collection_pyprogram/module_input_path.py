import tkinter as tk
from tkinter import filedialog

def input_path_module(initial_dir=None):
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    # 设置窗口为最前端（如果需要）
    root.attributes('-topmost', True)
    
    # 弹出选择文件夹的对话框
    folder_path = filedialog.askdirectory(
        title="选择文件夹",
        initialdir=initial_dir  # 默认打开的文件夹路径
    )

    # 关闭主窗口
    root.destroy()

    # 如果选择了文件夹，返回路径，否则返回 None
    return folder_path if folder_path else None
