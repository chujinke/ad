import xlrd
from numpy import *
import itertools

support_dic = {}

def getyuandata(chengshi):
    dicdatas = {}
    ti1 = []
    ti2 = []
    yinsutihao = 4
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据

    for i in range(6):
        sheets = workbook.sheet_by_name(sheet_names[i])
        hangshu = sheets.nrows
        for j in range(2,hangshu):
            for z in range(3):
                ti = []
                if (sheets.row_values(j)[8]==chengshi):
                    try:
                        ti1[z].append(str(z+12)+sheets.row_values(j)[z+3])
                    except:
                        ti.append(str(z+12)+sheets.row_values(j)[z+3])
                        ti1.append(ti)
            for z in range(2):
                ti = []
                if (sheets.row_values(j)[8]==chengshi):
                    try:
                        ti2[z].append(str(z+25)+sheets.row_values(j)[z+13])
                    except:
                        ti.append(str(z+25)+sheets.row_values(j)[z+13])
                        ti2.append(ti)

    # for j in range(14):
    #     data = []
    #     for i in range(6):
    #         sheets = workbook.sheet_by_name(sheet_names[i])
    #         lie = sheets.col_values(2+j)[2:]
    #         data.extend(lie)
    #     options = set(data)
    #     dicdata = {}
    #     for item in sorted(list(options)):
    #         dicdata[item] = item+"选项"+str(data.count(item))+"个占比" + str(round(data.count(item)/len(data)*100,2))+"%"

    #     dicdatas["第"+str(j+1)+"题"] = dicdata
    # return dicdatas

    zongshuju = ti1 + ti2
    # zongshuju.append(ti2)
    # zongshuju.append(ti1)
    print(ti2[0])
    itemset = []
    for i in range(len(zongshuju[0])):
        itemset1 = []
        for item in zongshuju:
            itemset1.append(item[i])
            #print(i,item[i])
        itemset.append(itemset1)
    # data = zongshuju[ye-1][tihao-1]# 获取哪一页的哪一题的数据
    # #计算
    # dicdata = {}
    # for item in sorted(list(set(data))):
    #     dicdata[item] = item + "选项" + str(data.count(item)) + "个占比" + str(round(data.count(item) / len(data) * 100, 2)) + "%"
    print(itemset)
    return itemset



# 获取整个数据库中的一阶元素
def createC1(dataSet):
    C1 = set([])
    for item in dataSet:
        C1 = C1.union(set(item))
    return [frozenset([i]) for i in C1]


# 输入数据库（dataset） 和 由第K-1层数据融合后得到的第K层数据集（Ck），
# 用最小支持度（minSupport)对 Ck 过滤，得到第k层剩下的数据集合（Lk）
def getLk(dataset, Ck, minSupport):
    global support_dic
    Lk = {}
    # 计算Ck中每个元素在数据库中出现次数
    for item in dataset:
        for Ci in Ck:
            if Ci.issubset(item):
                if not Ci in Lk:
                    Lk[Ci] = 1
                else:
                    Lk[Ci] += 1
    # 用最小支持度过滤
    Lk_return = []
    for Li in Lk:
        support_Li = Lk[Li] / float(len(dataSet))
        if support_Li >= minSupport:
            Lk_return.append(Li)
            support_dic[Li] = support_Li
    return Lk_return


# 将经过支持度过滤后的第K层数据集合（Lk）融合
# 得到第k+1层原始数据Ck1
def genLk1(Lk):
    Ck1 = []
    for i in range(len(Lk) - 1):
        for j in range(i + 1, len(Lk)):
            if sorted(list(Lk[i]))[0:-1] == sorted(list(Lk[j]))[0:-1]:
                Ck1.append(Lk[i] | Lk[j])
    return Ck1


# 遍历所有二阶及以上的频繁项集合
def genItem(freqSet, support_dic):
    for i in range(1, len(freqSet)):
        for freItem in freqSet[i]:
            genRule(freItem)


# 输入一个频繁项，根据“置信度”生成规则
# 采用了递归，对规则树进行剪枝
def genRule(Item, minConf=0.7):
    if len(Item) >= 2:
        for element in itertools.combinations(list(Item), 1):
            if support_dic[Item] / float(support_dic[Item - frozenset(element)]) >= minConf:
                print (str([Item - frozenset(element)]) + "----->" + str(element))
                print (support_dic[Item] / float(support_dic[Item - frozenset(element)]))
                genRule(Item - frozenset(element))

if __name__ == "__main__":
    chengshi = {"A":"北京","B":"天津","C":"石家庄","D":"保定"}
    yinsu = "D"
    item = chengshi[yinsu]
    #for item in chengshi:
    dataSet = getyuandata(yinsu)
    result_list = []
    Ck = createC1(dataSet)
    # 循环生成频繁项集合，直至产生空集
    while True:
        Lk = getLk(dataSet, Ck, 0.5)
        if not Lk:
            break
        result_list.append(Lk)
        Ck = genLk1(Lk)
        if not Ck:
            break
    # 输出频繁项及其“支持度”
    print(item,":城市成因分析")
    print(support_dic)
    # 输出规则
    genItem(result_list, support_dic)
    print("---"*10)