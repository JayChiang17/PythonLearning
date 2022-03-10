# # -*- coding:UTF-8 -*-
#封裝在實體物件中的變數
#Point: 實體物件的設計: 平面做標上的點 ass Point:
class Point:
    def __init__(self, x, y):
         self.x = x
         self.y = y
p1 = Point(3,4)
print(p1.x,p1.y)
p2 = Point(5,6)
print(p2.x,p2.y)
# class Point2:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
# p2 = Point2(1,5)

#FullName 實體物件的設計: 紀錄名字
class FullName:
    def __init__(self, frist, last):
        self.frist = frist
        self.last = last
name1 = FullName("Jay","Chiang")
print(name1.frist, name1.last)
name2 = FullName("lily","Lin")
print(name2.frist, name2.last)

#-----------------------------------------
#實體方法
#封裝在實體物件中的函式

class Point3:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def distance(self, targetX,targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

p = Point3(9,12)
p.show()
result = p.distance(0,0)
print(result)

#----------------
#包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(self,name):
        self.name = name
        self.file = None #尚未開啟檔案
    #實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding = "utf-8")

    def read(self):
        return self.file.read()
#讀取第一個檔案    
q1 = File("data1.txt")
q1.open()
data = q1.read()
print(data)
#讀取第二個
q2 = File("data2.txt")
q2.open()
data = q2.read()
print(data)