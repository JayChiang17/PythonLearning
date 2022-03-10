# -*- coding:UTF-8 -*-
#自行建立的模組
#定義平面幾何運算的函示

def distance(x1,y1,x2,y2):
    x = ((x2-x1**2+(y2-y1)**2))**0.5 #兩點間距離
    return x

def slope(x1,y1,x2,y2):
    n = (y2-y1)/(x2-x1) #斜率
    return n