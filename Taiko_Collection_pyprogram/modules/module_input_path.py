from tkinter import filedialog
import ctypes

# 设置 DPI 意识（适用于 Windows）
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass  # 如果不是 Windows 或发生错误，忽略


def input_path_module(initial_dir=None):
    
    # 弹出选择文件夹的对话框
    folder_path = filedialog.askdirectory(title="选择Songs文件夹",initialdir=initial_dir)  # 默认打开的文件夹路径
    # 如果选择了文件夹，返回路径，否则返回 None
    return folder_path if folder_path else None