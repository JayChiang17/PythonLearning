# -*- coding:UTF-8 -*-
# Itrrable data type
# string, List, set, dic
from traceback import print_tb
import xdrlib


for x in [3,5,7,]:
    print(x)

for x in "abc":
    print(x)

for x in {"a"," tnt", 4, 7}: #沒有順序性
    print(x)

dic = {"a":3, "b":4}
for key in dic:
    print(key) #取得a,b
    print(dic[key]) #取得3,4

#內建函式
# y = max([3,5,6,2,5,7,2])
# x = max("sdfz")
# s = max({"s",3,56,"sd"})
# c = max({"x":3,"e":5})

# Sorted("cds")
# Sorted([3,6,8.8,9,3,1])
# Sorted({8,9,-65,77})


