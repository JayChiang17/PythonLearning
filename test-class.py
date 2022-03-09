# -*- coding:UTF-8 -*-
#定義類別 IO
class IO:
    supportedSrcs = ["console", "file"] #創建列表

    def read(src):
        if src not in IO.supportedSrcs: #讀取class中的supportedSrcs
            print("not supppeted")
        else:
            print("read from", src)

#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")
