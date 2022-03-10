# -*- coding:UTF-8 -*-
import sys as s #內建模組
s.path.append("modules")
import geometry
# print(s.platform)
# print(s.maxsize)
# print(s.path)

result = geometry.distance(10,2,5,23)
print(result) 
result = geometry.slope(1,6,5,20)
print(result)

#調整搜尋模組的路徑
# print(s.path)