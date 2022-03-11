# -*- coding:UTF-8 -*-
from ast import keyword
import pandas as pd
data= pd.read_csv("googleplaystore.csv") #讀取成DataFrame
# print("資料數量: ",data.shape) 
# print("資料欄位: ", data.columns) #裡面的13個欄位
# print("=====================")

# #分析資料 篩選
# condition = data["Rating"] <= 5 #排除錯誤
# data = data[condition] #排除錯誤

# print("avg: ", data["Rating"].mean())
# print("mid: ", data["Rating"].median())
# print("top 1000 avg: ",data["Rating"].nlargest(1000).mean())
# print("low 1000 avg: ",data["Rating"].nsmallest(1000).mean())

# print(data["Installs"]) #是字串 不是數字
# print(data["Installs"][10472])
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free","")) #轉換成數字
# print("AVG: ",data["Installs"].mean())
# condition_Installs = data["Installs"] > 100000
# print("安裝數量大於十萬: ",data[condition_Installs].shape[0])

#關鍵字收尋程式名稱
keyword1 = input("輸入關鍵字: ")
condition = data["App"].str.contains(keyword1,case = False) #包含"game"名稱的標題 #case = False 忽略大小寫
print(data[condition]["App"])
print("包含關鍵字得數量: ",data[condition].shape[0])