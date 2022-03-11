# -*- coding:UTF-8 -*-
# 特殊設計的函式，用來「輔助」其他的函式
#
# def 裝飾器名稱（回呼函式名稱):
#     內部函式的名稱():
#         回呼函式名稱():
#     return 內部函式名稱

# ＠裝飾器名稱
# def 函式名稱():
#     #程式碼
# 函式名稱()

# #def 裝飾器
# def myDeco(callback):
#     def run():
#         print("裝飾器中程式碼")
#         callback(1000) #函式 test()
#     return run
# #use 裝飾器

# @myDeco
# def test(n):
#     print("普通函式程式碼", n)

# test()

#1+2+3+4+5+6....+50 sum
from unittest import result


def calculate(callback):
    def run():
        result = 0
        for i in range(51):
            result += i
        callback(result)
    return run

@calculate #呼叫裝飾器
def show(ans):
    print("Anser is------>", ans)

@calculate #呼叫裝飾器
def show2(ans):
    print("答案是---->",ans)

show()
show2()