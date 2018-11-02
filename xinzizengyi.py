# -*- coding:utf-8 -*-

from math import log
import operator
import xlrd
import matplotlib

chengshi1 = {"A": "北京", "B": "天津", "C": "石家庄", "D": "保定"}
yinsu1 = "C"
item1 = chengshi1[yinsu1]
def getyuanData(chengshi):
    ti1 = []
    ti2 = []
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    juece = {"23A":"1-2次","23B":"1-2次","23C":"3-4次","23D":"3-4次","23E":"4次以上","23F":"不一定"}
    age = {"12A":"18以上","12B":"18-30岁","12C":"30-40岁","12D":"40-50岁","12E":"50-60岁"}
    wenhua = {"13A": "初中及以下", "13B": "高中及中专", "13C": "本科及大专", "13D": "硕士研究生", "13E": "博士研究生及以上"}
    shouru = {"14A": "1000", "14B": "3000", "14C": "4000", "14D": "7000", "14E": "10000", "14F":"15000"}
    for i in range(6):
        sheets = workbook.sheet_by_name(sheet_names[i])
        hangshu = sheets.nrows
        for j in range(2,hangshu):
            for z in range(6):
                ti = []
                #if (sheets.row_values(j)[8]==chengshi and sheets.row_values(j)[11]!="F"):
                if (sheets.row_values(j)[8] == chengshi):
                    try:
                        ti1[z].append(str(z+11)+sheets.row_values(j)[z+2])
                    except:
                        ti.append(str(z+11)+sheets.row_values(j)[z+2])
                        ti1.append(ti)

            for z in range(4):
                ti = []
                #if (sheets.row_values(j)[8]==chengshi and sheets.row_values(j)[11]!="F"):
                if (sheets.row_values(j)[8] == chengshi):
                    try:
                        ti2[z].append(str(z+23)+sheets.row_values(j)[z+11])
                    except:
                        ti.append(str(z+23)+sheets.row_values(j)[z+11])
                        ti2.append(ti)
    zongshuju = ti1 + ti2
    itemset = []
    for i in range(len(zongshuju[0])):
        itemset1 = []
        for item in zongshuju:
            itemset1.append(item[i])

        del itemset1[7]
        cishu = itemset1[6]
        del itemset1[6]
        itemset1.append(juece[cishu])
        del itemset1[6]
        del itemset1[6]
        # itemset1[3] = age[itemset1[]]
        # itemset1[1] = wenhua[itemset1[1]]
        # itemset1[2] = shouru[itemset1[2]]
        itemset.append(itemset1)
    return itemset


# -*- coding: UTF-8 -*-
from math import log

"""
函数说明:创建测试数据集
"""


def createDataSet():
    dataSet = getyuanData(yinsu1)
    labels = ['性别', '年龄', '文化程度', '收入',"婚姻","家庭构成"]  # 分类属性
    return dataSet, labels  # 返回数据集和分类属性


"""
函数说明:计算给定数据集的经验熵(香农熵)
Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)
"""


def calcShannonEnt(dataSet):
    numEntires = len(dataSet)  # 返回数据集的行数
    labelCounts = {}  # 保存每个标签(Label)出现次数的字典
    for featVec in dataSet:  # 对每组特征向量进行统计
        currentLabel = featVec[-1]  # 提取标签(Label)信息
        if currentLabel not in labelCounts.keys():  # 如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1  # Label计数
    shannonEnt = 0.0  # 经验熵(香农熵)
    for key in labelCounts:  # 计算香农熵
        prob = float(labelCounts[key]) / numEntires  # 选择该标签(Label)的概率
        shannonEnt -= prob * log(prob, 2)  # 利用公式计算
    return shannonEnt  # 返回经验熵(香农熵)


"""
函数说明:按照给定特征划分数据集
Parameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
"""


def splitDataSet(dataSet, axis, value):
    retDataSet = []  # 创建返回的数据集列表
    for featVec in dataSet:  # 遍历数据集
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # 去掉axis特征
            reducedFeatVec.extend(featVec[axis + 1:])  # 将符合条件的添加到返回的数据集
            retDataSet.append(reducedFeatVec)
    return retDataSet  # 返回划分后的数据集


"""
函数说明:选择最优特征
Parameters:
    dataSet - 数据集
Returns:
    bestFeature - 信息增益最大的(最优)特征的索引值
"""


def chooseBestFeatureToSplit(dataSet,features):
    numFeatures = len(dataSet[0]) - 1  # 特征数量
    baseEntropy = calcShannonEnt(dataSet)  # 计算数据集的香农熵
    bestInfoGain = 0.0  # 信息增益
    bestFeature = -1  # 最优特征的索引值
    xinxi = {}
    for i in range(numFeatures):  # 遍历所有特征
        # 获取dataSet的第i个所有特征
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  # 创建set集合{},元素不可重复
        newEntropy = 0.0  # 经验条件熵
        for value in uniqueVals:  # 计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)  # subDataSet划分后的子集
            prob = len(subDataSet) / float(len(dataSet))  # 计算子集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  # 根据公式计算经验条件熵
        infoGain = baseEntropy - newEntropy  # 信息增益
        print("%s-特征的增益为%.3f" % (features[i], infoGain))  # 打印每个特征的信息增益
        xinxi[features[i]] = infoGain
        if (infoGain > bestInfoGain):  # 计算信息增益
            bestInfoGain = infoGain  # 更新信息增益，找到最大的信息增益
            bestFeature = i  # 记录信息增益最大的特征的索引值
    xinxi = sorted(xinxi.items(),key = lambda x:x[1],reverse = True)
    print(xinxi)
    return bestFeature # 返回信息增益最大的特征的索引值


if __name__ == '__main__':
    print(item1)
    dataSet, features = createDataSet()
    entropy = calcShannonEnt(dataSet)
    bestfeature = chooseBestFeatureToSplit(dataSet,features)
    print("训练集的熵为:%f" % (entropy))
    print("最优特征索引值:" ,features[bestfeature])