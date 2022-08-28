# -*- coding: cp1251 -*-
import os
import numpy

text = open('Модули.txt','r+')

url_to_directory = input("Путь к каталогу с программой: ")
os.chdir(url_to_directory)
i = 1
for root, dirs, files in os.walk("Models", topdown = False):
   for name in files:
    if(".exe" in name and "UnityCrashHandler64" not in name):
        print(os.path.join(root, name))
        text.write(str(i)  + "\n")
        text.write(os.path.join(root, name) + "\n")
        text.write("1 \n" )
        i = i + 1

print("\nУспешно!\n")
print("Нажмите 'enter' для выхода")
input()

