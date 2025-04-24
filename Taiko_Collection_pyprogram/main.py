import configparser
import os
import ctypes
import tkinter as tk
from modules.module_input_path import input_path_module
from modules.module_count import counts
from modules.module_UI_front_setting import tkcreate



# 设置 DPI 意识
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 设置 DPI 意识为开启
except:
    pass  # 如果设置不了就跳过


###变量定义###
i = 0  #temp
path_Taiko_songs = ""  # 总音乐文件夹的路径变量
path_Taiko_get_dir = ""  # 需要复制的音乐文件的文件夹路径变量
path_file_ini_name = r"\Taiko_Collection_pyprogram\config.ini"   # config.ini的文件变量
path_UI_photo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Taiko_Collection_pyprogram", "Photos", "Taiko_UI.jpg")
root_tkc_temp = ""


###打开总文件夹###
#尝试打开路径存储文件，如果没有就进行创立和前置配置
'''
if os.path.exists(path_file_ini_name):    #检测config.ini是否存在
    print("path配置存储文件已存在!")
else:
    print("path配置文件不存在,正在创建并配置!")
    config = configparser.ConfigParser()
    config.add_section("Paths")    #添加“paths”section
    config.set("Paths","dir_path",path_Taiko_songs)    #设置paths下面的参数
    with open(path_file_ini_name,"w") as config_file:    #打开文件并赋值到c_f,然后写入到ini
        config.write(config_file)
    print("path配置文件配置完成!")
'''
### 创建 start 界面 ###
## 实现
# 整个窗口，UI 图片，选择目录文字，输入框，选择目录按钮，退出按钮，开始按钮，版本文本

# 更新路径,实现目录功能
def dir_refresh():
    path = input_path_module()
    root_entry_temp.delete(0,tk.END)
    root_entry_temp.insert(0,path)


# 创建主窗口
root_start_screen = tk.Tk()
root_start_screen.title("Launch")
root_start_screen.geometry("825x520")
root_start_screen.resizable(False,False)

# 传递参数给 tkc
root_tkc_temp = tkcreate(root_start_screen)

# 添加图片
#root_tkc_temp.tkc_image(path_UI_photo,0,0,800,250)

# 添加文本“游戏目录”“version”
root_tkc_temp.tkc_text("游戏目录(songs)",20,300)
root_tkc_temp.tkc_text("v1.0.0",5,495)

# 添加输入框
root_entry_temp = root_tkc_temp.tkc_entry(150,304,50)

# 添加按钮“选择目录”“退出”“开始”

root_tkc_temp.tkc_button("选择目录",620,297,7,1,"white",dir_refresh)
#root_tkc_temp.tkc_button
#root_tkc_temp.tkc_button







root_start_screen.mainloop()