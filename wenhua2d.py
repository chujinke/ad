from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import matplotlib
import random
import  pandas as pd


def getyuandata(chengshi,z):
    list1 = []
    shouru = []
    xiaofei = []
    zhichuzengfu= []
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    for i in range(6):
        sheet2 = workbook.sheet_by_name(sheet_names[i])
        hang = sheet2.nrows
        print(hang)
        for i in range(2,hang):
            if sheet2.row_values(i)[8] ==chengshi:
                shouru.append(sheet2.row_values(i)[5])
                xiaofei.append(sheet2.row_values(i)[12])
                zhichuzengfu.append(z)

    return shouru,xiaofei,zhichuzengfu
class Getdata():
    '''计算出各个维度值'''

    def __init__(self):
        '''初始化数据'''
        self.x1 = []
        self.y1 = []

        self.x2 = []
        self.y2 = []

        self.x3 = []
        self.y3 = []

        self.x4 = []
        self.y4 = []

        data = getyuandata("A",0.057)
        self.shouru1 = data[0]
        self.xiaofei1 = data[1]
        self.z1 = data[2]
        data = getyuandata("B",0.066)
        self.shouru2 = data[0]
        self.xiaofei2 = data[1]
        self.z2 = data[2]
        data = getyuandata("C",0.083)
        self.shouru3 = data[0]
        self.xiaofei3 = data[1]
        self.z3 = data[2]
        data = getyuandata("D",0.083)
        self.shouru4 = data[0]
        self.xiaofei4 = data[1]
        self.z4 = data[2]


    # def jisuan(self):
    #     dic1 = {"A":1000,"B":3000,"C":4000,"D":7000,"E":10000,"F":15000}
    #     dic2 = {"A": 100, "B": 300, "C": 800, "D": 1500, "E": 2000}
    #     dic3 = {"A": 1, "B": 2, "C": 3, "D": 4}
    #     for i in range(len(self.shouru)):
    #         try:
    #             self.x.append(dic1[self.shouru[i]])
    #             self.y.append(dic2[self.xiaofei[i]])
    #             self.z.append(dic3[self.diqu[i]])
    #         except:
    #             print(i)
    #     return self.x,self.y,self.z
    def jisuan(self):

        for i in range(len(self.shouru1)):
            dic1 = {"A": random.randrange(0, 1000), "B": random.randrange(1000, 3000),
                    "C": random.randrange(3000, 4000), "D": random.randrange(4000, 7000),
                    "E": random.randrange(7000, 10000), "F": random.randrange(10000, 15000)}
            dic2 = {"A": random.randrange(0, 100), "B": random.randrange(100, 300), "C": random.randrange(300, 800),
                    "D": random.randrange(800, 1500), "E": random.randrange(1500, 2000)}
            try:
                self.x1.append(dic1[self.shouru1[i]])
                self.y1.append(dic2[self.xiaofei1[i]])
            except:
                print(i)

        for i in range(len(self.shouru2)):
            dic1 = {"A": random.randrange(0, 1000), "B": random.randrange(1000, 3000),
                    "C": random.randrange(3000, 4000), "D": random.randrange(4000, 7000),
                    "E": random.randrange(7000, 10000), "F": random.randrange(10000, 15000)}
            dic2 = {"A": random.randrange(0, 100), "B": random.randrange(100, 300), "C": random.randrange(300, 800),
                    "D": random.randrange(800, 1500), "E": random.randrange(1500, 2000)}
            try:
                self.x2.append(dic1[self.shouru2[i]])
                self.y2.append(dic2[self.xiaofei2[i]])
            except:
                print(i)

        for i in range(len(self.shouru3)):
            dic1 = {"A": random.randrange(0, 1000), "B": random.randrange(1000, 3000),
                    "C": random.randrange(3000, 4000), "D": random.randrange(4000, 7000),
                    "E": random.randrange(7000, 10000), "F": random.randrange(10000, 15000)}
            dic2 = {"A": random.randrange(0, 100), "B": random.randrange(100, 300), "C": random.randrange(300, 800),
                    "D": random.randrange(800, 1500), "E": random.randrange(1500, 2000)}
            try:
                self.x3.append(dic1[self.shouru3[i]])
                self.y3.append(dic2[self.xiaofei3[i]])
            except:
                print(i)

        for i in range(len(self.shouru4)):
            dic1 = {"A": random.randrange(0, 1000), "B": random.randrange(1000, 3000),
                    "C": random.randrange(3000, 4000), "D": random.randrange(4000, 7000),
                    "E": random.randrange(7000, 10000), "F": random.randrange(10000, 15000)}
            dic2 = {"A": random.randrange(0, 100), "B": random.randrange(100, 300), "C": random.randrange(300, 800),
                    "D": random.randrange(800, 1500), "E": random.randrange(1500, 2000)}
            try:
                self.x4.append(dic1[self.shouru4[i]])
                self.y4.append(dic2[self.xiaofei4[i]])
            except:
                print(i)
        return self.x1,self.y1,self.x2,self.y2,self.x3,self.y3,self.x4,self.y4,self.z1,self.z2,self.z3,self.z4

if __name__ == "__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    color  = ["red","green"]
    ax = plt.figure().add_subplot(111, projection='3d')
    data = Getdata().jisuan()
    ax.scatter( data[0],data[1],data[8], c="red",s=5, marker='o',cmap='rainbow')
    ax.scatter(data[2], data[3], data[9],c="green", s=5, marker='o', cmap='rainbow')
    ax.scatter(data[4], data[5], data[10],c="blue", s=5, marker='o', cmap='rainbow')
    ax.scatter(data[6], data[7], data[11],c="blue", s=5, marker='o', cmap='rainbow')
    ax.set_xlabel("收入",fontproperties=zhfont1)
    ax.set_ylabel("文化消费",fontproperties=zhfont1)
    ax.set_zlabel("人均消费支出增幅", fontproperties=zhfont1)
    ax.legend(["北京", "天津", "河北"], prop=zhfont1, markerfirst=True)
    # 显示图像
    plt.show()