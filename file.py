# -*- coding:UTF-8 -*-
# file = open("data.txt", mode="w") #open a file with withe
# # encoding="utf-8" --> 寫入中文文件
# file.write("""test write\nsecond line
# 123
# 321
# 1234567
# 帥哥
# 美女""") #operation
# file.close() #close

# with open("data.txt", mode="w") as file:
#     file.write("1\n2\n3")

#檔案讀取

#一行一行讀取出並加總
# sum = 0
# with open("data.txt", mode="r") as file:
#     for i in file: #一行一行讀取
#         sum += int(i)
# print(sum)

#使用JSON格式讀取複寫
import json
with open("config.json",mode = "r") as file:
    data = json.load(file)
print(data)
# print("name: ",data["name"]) #('name: ', u'My name')
# print("version: ",data["version"]) #('version: ', u'1.2.5')
data["name"]="New name" #修改變數中的資料
#把最新的資料更新回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)
print(data)