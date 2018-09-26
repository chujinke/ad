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
        #sql = "SELECT * FROM shengzongshuju  "
        sql2 = "select distinct 学校名称 from shengzongshuju"
        data = []
        name_set = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                data.append(row[1:73])
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


    def __init__(self,sehoolname):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []
        data = Getdata().data(sehoolname)
        self.data = data[0]
        self.name = data[1]
    def getname(self):
        return self.name
    def getlist(self):
        geshuy = len(range(15, 32))
        geshuz = len(range(32, 72))
        for dataitem in self.data:
            numx = 0
            numy = 0
            numz = 0
            for i in range(1,15):
                numx = numx + float(dataitem[i][0])
            self.x.append(numx/14)

            for i in range(15,32):
                numy = numy + float(dataitem[i][0])
            self.y.append(numy/geshuy)

            for i in range(32,71):
                try:
                    numz = numz + float(dataitem[i][0])
                except:
                    print(i,dataitem[i])
            self.z.append(numz/geshuz)


        return self.x,self.y,self.z


if __name__=="__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    data = Jisuandata("中国地质大学长城学院")
    name = data.getname()
    x = data.getlist()[0]
    y = data.getlist()[1]
    z = data.getlist()[2]

    data = Jisuandata("石家庄铁道大学")
    name1 = data.getname()
    x1 = data.getlist()[0]
    y1 = data.getlist()[1]
    z1 = data.getlist()[2]

    data = Jisuandata("河北大学")
    name2 = data.getname()
    x2 = data.getlist()[0]
    y2 = data.getlist()[1]
    z2 = data.getlist()[2]

    # df = pd.DataFrame({'X': x,
    #                    'Y': y,
    #                    'Z': z})
    # xishu = df.corr()
    # print(xishu)
    # # 线性回归训练
    # model = linear_model.LinearRegression()
    # xy = []
    # for i in range(len(x)):
    #     xy1 = []
    #     xy1.append(y[i])
    #     xy1.append(x[i])
    #     xy.append(xy1)
    # model.fit(xy,z)
    # a = model.intercept_  # 截距
    # b = model.coef_  # 回归系数
    # # 训练数据的预测值
    # z_train_pred = model.predict(xy)

    m = [(x[i]+y[i]+z[i])/3 for i in range(len(y))]
    color = [str(item / 5.) for item in m]
    ax = plt.figure().add_subplot(111, projection='3d')

    # # 绘制最佳拟合线：标签用的是训练数据的预测值y_train_pred
    # ax.scatter(x,y, z_train_pred,color='black', linewidth=1, label="best line")
    ax.scatter( x,y,z, c="blue", s=5, marker='o',cmap='rainbow')
    ax.scatter(x1, y1, z1, c="red", s=5, marker='.', cmap='rainbow')
    ax.scatter(x2, y2, z2, c="green", s=5, marker='.', cmap='rainbow')
    ax.set_xlabel("学习动机",fontproperties=zhfont1)
    ax.set_ylabel("学习型投入",fontproperties=zhfont1)
    ax.set_zlabel("学习满意度",fontproperties=zhfont1)
    ax.legend(["中国地质大学长城学院","石家庄铁道大学","河北大学"],prop =zhfont1,markerfirst=True)
    # 显示图像
    plt.show()