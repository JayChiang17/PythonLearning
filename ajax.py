# -*- coding:UTF-8 -*-
#抓取Medium網頁原始碼 HTML
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
url = "https://medium.com/_/api/home-feed"
request = req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}) #看起來像是普通使用者, 用什麼系統等等
with req.urlopen(request) as response:
    data = response.read().decode("utf-8") #Json
#資料解析 取的文章標題
#解析JSON格式
import json
import pandas as pd
data = data.replace("])}while(1);</x>","")
data  = json.loads(data) #把原始的josn資料解析成字典/列表
df=pd.DataFrame(data)
df.to_csv("test_data.csv")
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])