from math import log
import xlrd
import operator

yinsu = "A"

def getyuanData(chengshi):
    ti1 = []
    ti2 = []
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    juece = {"23A":"1-2次","23B":"1-2次","23C":"3-4次","23D":"3-4次","23E":"4次以上","23F":"不一定"}
    xingbie = {}
    age = {"12A":"18以上","12B":"18-30岁","12C":"30-40岁","12D":"40-50岁","12E":"50-60岁"}
    wenhua = {"13A": "初中及以下", "13B": "高中及中专", "13C": "本科及大专", "13D": "硕士研究生", "13E": "博士研究生及以上"}
    shouru = {"14A": "1000", "14B": "3000", "14C": "4000", "14D": "7000", "14E": "10000", "14F":"15000"}
    jiatinggoucheng = {"16A":"有孩子（18岁以上）","16B":"有孩子（18岁以下）","16C":"没有孩子"}
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
        del itemset1[0]
        del itemset1[0]
        del itemset1[2]
        # itemset1[3] = age[itemset1[]]
        # itemset1[1] = wenhua[itemset1[1]]
        # itemset1[2] = shouru[itemset1[2]]
        itemset.append(itemset1)
        print(itemset)
    return itemset

def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # 计算单个类的熵值
        shannonEnt-=prob*log(prob,2) # 累加每个类的熵值
    return shannonEnt

def createDataSet1():    # 创造示例数据

    # 获取数据
    chengshi = {"A": "北京", "B": "天津", "C": "石家庄", "D": "保定"}
    item = chengshi[yinsu]
    dataSet = getyuanData(yinsu)
    print(dataSet)
    labels = ['年龄','文化程度',"收入"]  #两个特征
    return dataSet,labels

def splitDataSet(dataSet,axis,value): # 按某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # 原始的熵
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob =len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt(subDataSet)  # 按特征分类后的熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值
        if (infoGain>bestInfoGain):   # 若按某特征划分后，熵值减少的最大，则次特征为最优分类特征
            bestInfoGain=infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    tree = createTree(dataSet, labels)
    print(tree)  # 输出决策树模型结果

    import treePlotter as tp
    myTree = tp.retrieveTree(0,tree)
    tp.createPlot(myTree)