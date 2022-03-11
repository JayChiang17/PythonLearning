# -*- coding:UTF-8 -*-
# 透過參數傳遞含式到另一個函式中

from multiprocessing.connection import answer_challenge
from unittest import result


def multiplication(x1,x2,muti):
    muti(x1*x2)

def callBack(ans):
    result = pow(ans,2)
    print(result)

multiplication(2,6,callBack)
# def test(arg):
#     arg(1000) #呼叫回呼函式帶入參數

# #定義一個call back函式
# def handle(data):
#     print(data)

# test(handle)
