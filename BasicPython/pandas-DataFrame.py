# -*- coding:UTF-8 -*-
import pandas as pd
data = pd.DataFrame({
    "name":["Amy", "jay", "nic"],
    "salary":[10000,30000,20000],
    "work hours": ["24","55","12"]

},index = ["a","b","c",]
)
print(data)
print("------------------------")
#觀察
# print("number: ",data.size)
# print("shape: ",data.shape) #資料型態(列, 行)
# print('index: ',data.index) 

# print("取的第一列:", data.iloc[0], sep="\n")
# print("----------------")
# print("取得第c列: ",data.loc["c"],sep="\n")

# print("取得name欄位: ",data['name'],sep="\n")

# names = data["name"] #取得單維度的 series 資料
# print("cover to uppper char: ",names.str.upper(), sep="\n")

# salaryMean = data["salary"]
# print("Mean of the salary: ",salaryMean.mean(), sep="\n")

#建立新的colume
data["revenun"] = [500000,600000,300000] 
#以下功能與以上相同: 創立新的colume
data["rank"] = pd.Series([3,2,1], index=["a","c","b"])

data["cp"] = data["revenun"]/data["salary"] #直接用DataFrame裡面的去除
print(data)

# name  salary work hours  revenun  rank    cp
# a  Amy   10000         24   500000     3  50.0
# b  jay   30000         55   600000     1  20.0
# c  nic   20000         12   300000     2  15.0