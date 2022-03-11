# -*- coding:UTF-8 -*-
# def myFactory(base):
#     def myDeco(callback):
#         def run():
#             ans = 10/base
#             callback(ans)
#         return run
#     return myDeco

# @myFactory(1000)
# def test(ans):
#     print(ans)

# test()



from email.mime import base

def calculateFactory(Max):
    def calculate(callback):
        def run():
            result = 0
            for i in range(Max+1):
                result += i
            callback(result)
        return run
    return calculate
@calculateFactory(100)
def show(ans):
    print("Anser is------>", ans)
@calculateFactory(20)
def show2(ans):
    print("答案是---->",ans)

show()
show2()








