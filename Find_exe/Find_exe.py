# -*- coding: cp1251 -*-
import os
import numpy


dirname, filename = os.path.split(os.path.abspath(__file__))
print("Путь к каталогу с программой: " + dirname)

text = open('Materials.txt','w+')

#url_to_directory_programm = input("Путь к каталогу с программой: ")

url_to_directory_models = input("Путь к папке с модулями: ")
os.chdir(url_to_directory_models)
i = 0

for root, dirs, files in os.walk(url_to_directory_models, topdown = False):
   for name in files:
    if(".exe" in name and "UnityCrashHandler64" not in name and "UnityCrashHandler32" not in name):
        path = os.path.join(root, name)
        name_folder_model = path.replace(url_to_directory_models,"")
        url_to_models = "\\Models" + name_folder_model
        name_folder = name_folder_model.replace(name,"")
        name_folder = name_folder.replace("\\", "")
        #re_ind = string.rfind("\\")
        #re = string[re_ind+1:]
        text.write("1\n")
        print("1")
        text.write(name_folder + "\n")
        print(name_folder)
        text.write(url_to_models + "\n")
        print(url_to_models)
        text.write(str(i)  + "\n")
        print(str(i))
        i = i + 1

print("\nУспешно!\n")
print("Нажмите 'enter' для выхода")
text.close()
input()
