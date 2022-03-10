# -*- coding:UTF-8 -*-
import random
data = random.choice([1,2,3,4,5,6]) #隨機選取1個資料
print(data)
data = random.sample([1,2,3,4,5,6,7],3) #隨機選取2個資料
print(data)

data = [1,2,3,4,5,6,7,8]
random.shuffle(data) #隨機調換 
print(data)

data = random.random()
print(data) #0-1之間隨機亂數
data = random.uniform(0.0,10.0)
print(data) #n之間隨機亂數

data = random.normalvariate(100,10) # 100 = mean, 10 = std 常態分佈亂數
print(data)
import statistics as stat
#載入統計模組 mean, median, stdev(標準差), 
data = stat.mean([1,5,8,9])
print(data)
data = stat.median([1,5,8,9])
print(data)
data = stat.stdev([1,5,8,9])
print(data)