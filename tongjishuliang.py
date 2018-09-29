import xlrd

def getyuandata():
    dicdatas = {}
    workbook = xlrd.open_workbook(r'文化问卷\汇总统计表源.xlsx')
    sheet_names= workbook.sheet_names() # 获取样本数据
    for j in range(14):
        data = []
        for i in range(6):
            sheets = workbook.sheet_by_name(sheet_names[i])
            lie = sheets.col_values(2+j)[2:]
            data.extend(lie)
        options = set(data)
        dicdata = {}
        for item in sorted(list(options)):
            if item!="":
                dicdata[item] = item+"选项"+str(data.count(item))+"个占比" + str(round(data.count(item)/len(data)*100,2))+"%"
            else:
                dicdata["空值"] = data.count(item)

        dicdatas["第"+str(j+1)+"题"] = dicdata
    return dicdatas

if __name__ == "__main__":
    print(getyuandata())