import pymysql
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

class Getdata():
    # 打开数据库连接
    def data(self,name):
        db = pymysql.connect("localhost", "root", "root", "shengshuju")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM shengzongshuju WHERE  学校名称='"+name+"' "
        data = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                data.append(row[1:74])
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()
        return data,name

class Jisuandata():
    '''计算出各个维度值'''


    def __init__(self):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []
        data = Getdata().data("河北大学")
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

            for i in range(32,72):
                numz = numz + float(dataitem[i][0])
            self.z.append(numz/geshuz)


        return self.x,self.y,self.z


if __name__=="__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    data = Jisuandata()
    name = data.getname()
    x = data.getlist()[0]
    y = data.getlist()[1]
    z = data.getlist()[2]
    print(name)
    print(x)
    print(y)
    print(z)
    m = [(x[i]+y[i]+z[i])/3 for i in range(len(y))]
    color = [str(item / 5.) for item in m]
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter( x,y,z, c=color, s=5, marker='.',cmap='rainbow')
    ax.set_xlabel("学习动机",fontproperties=zhfont1)
    ax.set_ylabel("学习型投入",fontproperties=zhfont1)
    ax.set_zlabel("学习满意度",fontproperties=zhfont1)
    # 显示图像
    plt.show()