from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import matplotlib
import random
import  pandas as pd


def getyuandata():
    list1 = []
    shouru = []
    xiaofei = []
    diqu = []
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    for i in range(6):
        sheet2 = workbook.sheet_by_name(sheet_names[i])
        hang = sheet2.row_values(1)
        shouru.append(sheet2.col_values(5)[2:])
        xiaofei.append(sheet2.col_values(12)[2:])
        diqu.append(sheet2.col_values(8)[2:])

    return shouru,xiaofei,diqu
class Getdata():
    '''计算出各个维度值'''

    def __init__(self):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []
        data = getyuandata()
        self.shouru = data[0]
        self.xiaofei = data[1]
        self.diqu = data[2]

    def jisuan(self):
        dic1 = {"A":1000,"B":3000,"C":4000,"D":7000,"E":10000,"F":15000}
        dic2 = {"A": 100, "B": 300, "C": 800, "D": 1500, "E": 2000}
        dic3 = {"A": 1, "B": 2, "C": 3, "D": 4}
        for i in range(len(self.shouru)):
            if dic3[self.diqu[i]
            try:
                self.x.append(dic1[self.shouru[i]])
                self.y.append(dic2[self.xiaofei[i]])
                self.z.append(dic3[self.diqu[i]])
            except:
                print(i)
        return self.x,self.y,self.z

if __name__ == "__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    ax = plt.figure().add_subplot(111, projection='3d')
    data = Getdata()
    for i in range(6):
        x = data.jisuan()[0][i]
        y = data.jisuan()[1][i]
        z = data.jisuan()[2][i]
        ax.scatter( x,y,z, c="red",s=5, marker='o',cmap='rainbow')
    ax.set_xlabel("收入",fontproperties=zhfont1)
    ax.set_ylabel("文化消费",fontproperties=zhfont1)
    # 显示图像
    plt.show()