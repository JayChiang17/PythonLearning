# -*- coding:UTF-8 -*-
#動態產生可迭代得資料，搭配for迴圈使用
# yield 語法：呼叫時回傳generator

#建立生成器函式：
def test():
    print("test1")
    yield 5
    print("test2")
    yield 10 

gen = test()

for d in gen:
    print(d)

def generatorEven(maxNum = 300):
    num = 0
    while num <= maxNum:
        yield num
        num += 2

evenGenerator = generatorEven()
for x in evenGenerator:
    if x < 100:
        print(x)
    else: 
        break