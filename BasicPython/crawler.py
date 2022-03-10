# -*- coding:UTF-8 -*-
#抓取ptt網頁原始碼 HTML
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
url = "https://www.104.com.tw/jobs/search/?keyword=%E6%9A%91%E6%9C%9F%E5%AF%A6%E7%BF%92%E7%94%9F"
#建立一個Requset物件, 附加Request Headers的資訓
request = req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}) #看起來像是普通使用者, 用什麼系統等等
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
#資料解析 取的文章標題
#安裝pip3 install beautifulsoup4
import bs4 
root = bs4.BeautifulSoup(data, "html.parser")#解析HTML文件
# find_all 找到所有指定的標籤, 如果沒有只會抓倒一個
Title = root.find_all("div", class_="title") #尋找class = "title" 的 div標籤
print(root.title.string)
# subTitle = root.find_all('a')
# subTitle3 = root.select('ul')
subTitle2 = root.find_all('articlev')
for li in subTitle2:
    print(li.text)

# for i in subTitle2: #.a 表示 HTML裡面的 <a
#     if i.h2 != None: #如果有包含a標籤 印出來
#         print(i.h2.string)



