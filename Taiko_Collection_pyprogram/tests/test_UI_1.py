import tkinter as tk
from tkinter import filedialog

class FolderSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件夹选择工具")

        # 创建一个标签
        self.label = tk.Label(root, text="请选择文件夹:")
        self.label.pack(pady=10)

        # 创建一个输入框，用于显示选择的文件夹路径
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        # 创建一个按钮，用于打开文件夹选择对话框
        self.button = tk.Button(root, text="选择文件夹", command=self.select_folder)
        self.button.pack(pady=10)

    def select_folder(self):
        # 弹出选择文件夹的对话框
        folder_path = filedialog.askdirectory(title="选择文件夹")
        # 如果用户选择了文件夹，将路径显示在输入框中
        if folder_path:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, folder_path)
            print("选择的文件夹路径:", folder_path)
        else:
            print("没有选择文件夹")

# 创建主窗口
root = tk.Tk()
app = FolderSelectorApp(root)
root.mainloop()