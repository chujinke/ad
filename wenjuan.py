from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import matplotlib

import  pandas as pd


def getyuandata():
    list1 = []
    workbook = xlrd.open_workbook(r'2017学习体验问卷.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    sheet2 = workbook.sheet_by_name(sheet_names[0])
    hang = sheet2.row_values(1)
    lienum = sheet2.nrows
    start = hang.index("Q01")
    stop = hang.index("Q71")
    name = hang.index("学校名称")
    for i in range(2,lienum):
        list1_1 = []
        list1_1.append(sheet2.col_values(name)[i])
        for item in sheet2.row_values(i,start,stop+1):
            list1_1.append(item)
        list1.append(list1_1)
    news_ids = []
    for id in sheet2.col_values(name)[2:]:
        if id not in news_ids:
            news_ids.append(id)
    return list1,news_ids
class Getdata():
    '''计算出各个维度值'''


    def __init__(self):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []
        data = getyuandata()
        self.data = data[0]
        print(self.data)
        self.name = data[1]
    def getname(self):
        return self.name
    def getlistx(self):
        geshu = len(range(1,15))
        for item in self.name:
            num = 0
            renshu = 0
            for dataitem in self.data:
                if item in dataitem:
                    renshu = renshu + 1
                    for i in range(1,15):
                        num = num + float(dataitem[i])
            self.x.append(num/(renshu*14))
        return self.x

    def getlisty(self):
        geshu = len(range(15,32))
        for item in self.name:
            num = 0
            renshu = 0
            for dataitem in self.data:
                if item in dataitem:
                    renshu = renshu + 1
                    for i in range(15,32):
                        num = num + float(dataitem[i])
            self.y.append(num/(renshu*geshu))
        return self.y

    def getlistz(self):
        geshu = len(range(32,72))
        for item in self.name:
            num = 0
            renshu = 0
            for dataitem in self.data:
                if item in dataitem:
                    renshu = renshu + 1
                    for i in range(32,72):
                        num = num + float(dataitem[i])
            self.z.append(num/(renshu*geshu))
        return self.z

if __name__ == "__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    data = Getdata()
    name = data.getname()
    x = data.getlistx()
    y = data.getlisty()
    z = data.getlistz()
    print(name)
    print(x)
    print(y)
    print(z)
    m = [(x[i]+y[i]+z[i])/3 for i in range(len(y))]
    color = [str(item / 5.) for item in m]
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter( x,y,z, c=color, s=50, marker='o',cmap='rainbow')
    for i in range(len(x)):
        ax.text(x[i], y[i], z[i], name[i],fontproperties=zhfont1)
    ax.set_xlabel("学习动机",fontproperties=zhfont1)
    ax.set_ylabel("学习型投入",fontproperties=zhfont1)
    ax.set_zlabel("学习满意度",fontproperties=zhfont1)
    # 显示图像
    plt.show()