# -*- coding:UTF-8 -*-
import pandas as pd
#資料索引
# data = pd.Series([3,56,-29,3,13], index=["a","b","c","d","e"])
Data = pd.Series(["你好","pandas","PYTHON"])
# print(Data.str.lower())
# print(Data.str.len())
# print(Data.str.cat(sep="--")) #字串串接符號
# print(Data.str.contains("P")) #判斷字串中是否有“p" bool
print(Data.str.replace("你好", "hello"))
#---------------------------------- INT
# print(data)
# print("Data-type: ", data.dtype)
# print("data-count: ", data.size)
# print("data-index: ",data.index)
# print(data[2],data[3]) 
# print(data["b"])
# print("max: ",data.max())
# print("sum: ",data.sum())
# print("std: ", data.std())
# print("mid: ", data.median())
# print("biggest n number: ", data.nlargest(3))
# print("small n number: ", data.nsmallest(3))