from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import matplotlib


workbook = xlrd.open_workbook(r'省级专业数据提取—教育学、学前教育（分类赋值）.xls')
sheet_names= workbook.sheet_names() # 获取样本数据


class Getdata():
    '''计算出各个维度值'''

    def __init__(self):
        '''初始化数据'''
        self.x = []
        self.y = []
        self.z = []

    def getname(self):
        sheet2 = workbook.sheet_by_name(sheet_names[0])
        lie = sheet2.col_values(0)
        return lie[2:19]
    def getlistx(self):
        for i in range(17):
            sheet2 = workbook.sheet_by_name(sheet_names[0])
            row = sheet2.row_values(2+i)
            rows = []
            for item in row:
                try:
                    rows.append(float(item))
                except :
                    rows.append(None)
            x = rows[4] + rows[7] + rows[10] + rows[13] + (rows[14]*0.4+rows[15]*0.6) + (rows[16]*0.7+rows[17]*0.3) + (rows[18]*0.4+rows[19]*0.6)
            self.x.append(x)
        return self.x

    def getlisty(self):
        for i in range(17):
            sheet2 = workbook.sheet_by_name(sheet_names[1])
            row = sheet2.row_values(3+i)
            rows = []
            for item in row:
                try:
                    rows.append(float(item))
                except :
                    rows.append(None)
            y = rows[1]*0.5 + (rows[2]*0.8+rows[3]*0.5+rows[4]*0.3) + (rows[6]*0.8+rows[7]*0.5+rows[8]*0.5) + rows[9] + rows[10] + (rows[11]*0.5+rows[12]*0.5)
            self.y.append(y)
        return self.y

    def getlistz(self):
        for i in range(17):
            sheet2 = workbook.sheet_by_name(sheet_names[2])
            row = sheet2.row_values(3+i)
            rows = []
            for item in row:
                try:
                    rows.append(float(item))
                except :
                    rows.append(None)
            z = rows[4] + rows[16] + (rows[23]*0.5+rows[24]*0.5)
            self.z.append(z)
        return self.z

if __name__ == "__main__":
    # 防止中文乱码
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
    data = Getdata()
    name = data.getname()
    x = data.getlistx()
    y = data.getlisty()
    z = data.getlistz()
    m = [(x[i]+y[i]+z[i])/3 for i in range(len(y))]
    color = [str(item / 5.) for item in m]
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter( x,y,z, c=color, s=50, marker='o',cmap='rainbow')
    ax.view_init(elev=0,azim=0)#改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
    for i in range(len(x)):
        ax.text(x[i], y[i], z[i], name[i],fontproperties=zhfont1)
    ax.set_xlabel("教师数量与结构",fontproperties=zhfont1)
    ax.set_ylabel("教师科研成果",fontproperties=zhfont1)
    ax.set_zlabel("教师教学投入",fontproperties=zhfont1)
    # 显示图像
    plt.show()