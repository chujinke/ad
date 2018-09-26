import pymysql
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
import pandas as pd
from sklearn import linear_model

class Getdata():

    # 打开数据库连接
    def data(self,name):
        db = pymysql.connect("localhost", "root", "root", "shengshuju")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM shengzongshuju WHERE  学校名称='"+name+"' "
        sql2 = "select distinct 学校名称 from shengzongshuju"
        data = []
        name_set = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                data.append(row[1:76])
        except:
            print("Error: unable to fetch data")

        try:
            # 执行SQL语句
            cursor.execute(sql2)
            # 获取所有记录列表
            results = cursor.fetchall()
            name_set = results
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()
        return data,name,name_set

class Jisuandata():
    '''计算出各个维度值'''


    def __init__(self):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []
        data = Getdata().data("中国地质大学长城学院")
        self.data = data[0]
        self.name = data[1]
    def getname(self):
        return self.name
    def getlist(self,targ,yarg,zsarg):

        for dataitem in self.data:

            max = 0
            numy = 0
            zqvalue = ""
            numz = 0
            time = 0
            if dataitem[0]<1500:
                time = dataitem[0]
            else:
                time = 1500
            self.x.append(time)

            for i in range(1,72):
                if zqvalue == dataitem[i][0]:
                    numy = numy + 1
                else:
                    if max<numy:
                        max = numy
                    zqvalue = dataitem[i][0]
                    numy = 0

            max = (max+yarg)
            self.y.append(max)
            if dataitem[73] not in "无(空)":
                if dataitem[74] not in "无(空)":
                    numz = len(dataitem[73])+len(dataitem[74])
                else:
                    numz = (len(dataitem[73]))
            else:
                if dataitem[74] not in "无(空)":
                    numz = len(dataitem[74])
            self.z.append(numz)








        return self.x,self.y,self.z


if __name__=="__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    jisuandata = Jisuandata()
    name = jisuandata.getname()
    data = jisuandata.getlist(0,0,0)
    x = data[0]
    y = data[1]
    z = data[2]

    m = [(x[i]+y[i]+z[i])/3 for i in range(len(y))]
    color = [str(item / 5.) for item in m]
    ax = plt.figure().add_subplot(111, projection='3d')

    # # 绘制最佳拟合线：标签用的是训练数据的预测值y_train_pred
    # ax.scatter(x,y, z_train_pred,color='black', linewidth=1, label="best line")
    ax.scatter( x,y,z, c=color, s=5, marker='.',cmap='rainbow')
    ax.set_xlabel(name+"时间",fontproperties=zhfont1)
    ax.set_ylabel("连续答题数",fontproperties=zhfont1)
    ax.set_zlabel("字数",fontproperties=zhfont1)
    # 显示图像
    plt.show()