# -*- coding:utf-8 -*-
from math import log
import operator
import xlrd
import matplotlib

yinsu = "D"

def getyuanData(chengshi):
    ti1 = []
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    for i in range(6):
        sheets = workbook.sheet_by_name(sheet_names[i])
        hangshu = sheets.nrows
        for j in range(2,hangshu):
            for z in range(2):
                ti = []
                if (sheets.row_values(j)[8] == chengshi):
                    try:
                        ti1[z].append(sheets.row_values(j)[z+13])
                    except:
                        ti.append(sheets.row_values(j)[z+13])
                        ti1.append(ti)
    return ti1

ti1= getyuanData(yinsu)
print(len(ti1[0]))
import string
def jisuangeshu():
    xuanxiang1 = ["A","B","C","D","E","F"]
    xuanxiang1 = ["A", "B", "C", "D", "E", "F", "G", "H","I","J"]
    xuanxiangshu1 = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}
    xuanxiangshu1 = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G":0, "H":0,"I":0,"J":0}
    for item in xuanxiang1:
        for i in range(len(ti1[1])):
            if ti1[1][i].count(item)>0:
                xuanxiangshu1[item] = xuanxiangshu1[item]+1

    zongshu = 0
    for item1 in xuanxiangshu1:
        zongshu = xuanxiangshu1[item1] + zongshu

    print(zongshu)
    print(xuanxiangshu1)

    for item2 in xuanxiangshu1:
        print(item2,xuanxiangshu1[item2]/zongshu)

    list1 = []
    for item3 in xuanxiangshu1:
        list1.append(xuanxiangshu1[item3])

    return list1

print(jisuangeshu())


from matplotlib import pyplot as plt
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
#调节图形大小，宽，高
plt.figure(figsize=(6,9))
#定义饼状图的标签，标签是列表
# labels = [u"个人兴趣","媒体宣传","优惠折扣","亲朋好友的评价","进行消费的便利程度","惯性消费"]
labels = [u"电视","网络","报刊","文化消费场所阵地广告","亲朋好友","户外广告","移动媒体（地铁、公交广告）","手机","广播","其他"]
#每个标签占多大，会自动去算百分比
sizes = jisuangeshu()
colors = ['red','yellowgreen','lightskyblue','green','blue','yellow']
#将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0.05,0,0,0,0,0,0,0,0,0)

patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for font in l_text:
    font.set_fontproperties(zhfont1)

for font in p_text:
    font.set_fontproperties(zhfont1)
#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，百分比的text离圆心的距离
#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size=(30)
# for t in p_text:
#     t.set_size=(20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
# plt.legend()
plt.show()