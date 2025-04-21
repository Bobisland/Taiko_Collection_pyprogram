import configparser
import os
from modules.module_input_path import input_path_module
from modules.module_count import counts

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
"""!这里不用动!"""




'''准备进入总文件夹songs,如果文件路径不对就重新设置然后进入'''
config = configparser.ConfigParser()
config.read(file_path_ini_name)    #读取ini里面的配置
path_Taiko_songs = config.get("Paths","dir_path")    #把songs里面的值赋值到p_t_s

print("path_songs =",path_Taiko_songs)

for i in range(3):
    judge_input_user = input("如果路径正确,请按下y并回车,不正确请按下n并回车:").strip().lower()
    
    if judge_input_user == "y":
        print("进入下一步!")
        break
    elif judge_input_user == "n":
        path_Taiko_songs = input_path_module(path_Taiko_songs)
        if path_Taiko_songs != config.get("Paths","dir_path"):   
            config = configparser.ConfigParser()
            config.read(file_path_ini_name)
            config.set("Paths","dir_path",path_Taiko_songs)
            with open(file_path_ini_name,"w") as config_file:
                config.write(config_file)
            break
        else:
            print("没有选择!")
            break
    else:
        print("无效输入，请重试!(无效三次将退出)")
        print("第" + counts(i) + "次!")

if i == 2:
    print("已退出!")
