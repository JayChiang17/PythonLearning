# -*- coding:UTF-8 -*-
#網路連線
import urllib.request as request
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
# #如果您不是在尋找經過驗證的 SSL，那麼只需使用未經驗證的 SSL
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8") #中文解碼
# print(data)
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  #use json

# print(data)
#取得公司名稱列表

clist = data["result"]["results"]
with open("TPEdata.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
        


