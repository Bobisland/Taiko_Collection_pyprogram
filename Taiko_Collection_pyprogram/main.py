import configparser
import os
from module_input_path import input_path_module
from module_count import counts

"""变量定义"""
i = 0                               #temp
path_Taiko_songs = ""               #总音乐文件夹的路径变量
path_Taiko_get_dir = ""             #需要复制的音乐文件的文件夹路径变量
file_path_ini_name = "config.ini"   #config.ini的文件变量




"""打开总文件夹"""

'''尝试打开路径存储文件，如果没有就进行创立和前置配置'''
if os.path.exists(file_path_ini_name):    #检测config.ini是否存在
    print("path配置存储文件已存在!")
else:
    print("path配置文件不存在,正在创建并配置!")
    config = configparser.ConfigParser()
    config.add_section("Paths")    #添加“paths”section
    config.set("Paths","dir_path",path_Taiko_songs)    #设置paths下面的参数
    with open(file_path_ini_name,"w") as config_file:    #打开文件并赋值到c_f，然后写入到ini
        config.write(config_file)
    print("path配置文件配置完成!")


