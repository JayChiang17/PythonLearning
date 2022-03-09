# -*- coding:UTF-8 -*-
#抓取ptt網頁原始碼 HTML
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
def getData(url):
    #建立一個Requset物件, 附加Request Headers的資訓
    request = req.Request(url,headers={
        "cookie":"over18=1",
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
    print(root.title.text)
    for title in Title:
        if title.a != None:
            print(title.a.text)

    #抓取上ㄧ頁網址
    nextLink = root.find("a",string = "‹ 上頁") #找到內文是 ‹ 上頁 的a標籤
    return nextLink["href"]
#主程序
#抓取一個介面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    pageURL = "https://www.ptt.cc/"+getData(pageURL)
    count+=1
    print(pageURL)