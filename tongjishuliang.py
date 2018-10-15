import xlrd

def getyuandata(chengshi,ye,tihao,yinsu):
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
            for z in range(7):
                ti = []
                if (sheets.row_values(j)[8]==chengshi) and (sheets.row_values(j)[yinsutihao]==yinsu):
                    try:
                        ti1[z].append(sheets.row_values(j)[z+2])
                    except:
                        ti.append(sheets.row_values(j)[z+2])
                        ti1.append(ti)
            for z in range(7):
                ti = []
                if (sheets.row_values(j)[8]==chengshi) and (sheets.row_values(j)[yinsutihao]==yinsu):
                    try:
                        ti2[z].append(sheets.row_values(j)[z+9])
                    except:
                        ti.append(sheets.row_values(j)[z+9])
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

    zongshuju = []
    zongshuju.append(ti1)
    zongshuju.append(ti2)
    data = zongshuju[ye-1][tihao-1]# 获取哪一页的哪一题的数据
    #计算
    dicdata = {}
    for item in sorted(list(set(data))):
        dicdata[item] = item + "选项" + str(data.count(item)) + "个占比" + str(round(data.count(item) / len(data) * 100, 2)) + "%"
    return len(ti1[0]),dicdata

if __name__ == "__main__":
    chengshi = {"A":"北京","B":"天津","C":"石家庄","D":"保定"}
    yinsu = "A"
    for item in chengshi:
        print(chengshi[item]+"-人数:"+str(getyuandata(item,2,3,yinsu)[0])+"-次数:",getyuandata(item,2,3,yinsu)[1])
        print(chengshi[item] + "花费金额:", getyuandata(item, 2, 4,yinsu)[1])
        print("-"*10)