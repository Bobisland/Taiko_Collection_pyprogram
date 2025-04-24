import tkinter as tk
import ctypes
from PIL import Image,ImageTk
from modules.module_input_path import input_path_module


# 设置 DPI 意识
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 设置 DPI 意识为开启
except:
    pass  # 如果设置不了就跳过


# 定义UI
class tkcreate:
    def __init__(self,root_temp):
        self.root_temp = root_temp
    
    # 添加文本
    def tkc_text(self,text_temp,x_temp,y_temp):
        root_text = tk.Label(self.root_temp,text=text_temp)
        root_text.place(x=x_temp,y=y_temp)
        return root_text
    
    # 添加输入框
    def tkc_entry(self,x_temp,y_temp,width_temp):
        root_entry = tk.Entry(self.root_temp,width=width_temp)
        root_entry.place(x=x_temp,y=y_temp)
        return root_entry
    
    # 添加按钮
    def tkc_button(self,text_temp,x_temp,y_temp,width_temp,height_temp,bg_color,command_temp):
        root_canvas = tk.Canvas(self.root_temp,width=width_temp,height=height_temp,bg="white")
        
        
        root_button = tk.Button(self.root_temp,text=text_temp,width=width_temp,height=height_temp,bg=bg_color,command=command_temp,fg="black",borderwidth=2,highlightbackground="black",highlightcolor="black")
        root_button.place(x=x_temp,y=y_temp)
        return root_button

    # 添加图片
    def tkc_image(self,image_temp,x_temp,y_temp,width_temp,height_temp):
        root_image = Image.open(image_temp)
        root_photo = ImageTk.PhotoImage(root_image)

        root_put_image = tk.Label(self.root_temp,image=root_photo,width=width_temp,height=height_temp)
        root_put_image.place(x=x_temp,y=y_temp)
        return root_put_image
    
    def tkc_entry_refresh(self):
        global path
        path = input_path_module()


