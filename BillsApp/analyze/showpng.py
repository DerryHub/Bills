import matplotlib.pyplot as plt
import os


l = [
    [0,1,2,3,4,5,6,7,8,9],
    [23,4,3,5,46,7,34,67,8,12]
]
color = ['red','blue','green','gray','black','yellow','purple','orange']

def showBar(dataList2d, xLabel='x', yLabel='y',color='blue'):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.bar(x,y,fc=color)
    plt.xlabel(xLabel,size=15)
    plt.ylabel(yLabel,size=15)
    plt.title('bar',size=30)


def showLine(dataList2d, xLabel='x', yLabel='y',color='blue'):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.plot(x,y,color=color,linewidth=5)
    plt.xlabel(xLabel, size=15)
    plt.ylabel(yLabel, size=15)
    plt.title('line', size=30)

def showPie(dataList2d):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.pie(x=y, labels=x, shadow=True, autopct='%2.1f', pctdistance=0.8)
    plt.title('pie', size=30)


def savePng(dataList2d, filename, type, xLabel='x', yLabel='y', color='blue'):
    plt.close('all')
    if type == 'bar':
        showBar(dataList2d, xLabel=xLabel, yLabel=yLabel, color=color)
    elif type == 'line':
        showLine(dataList2d, xLabel=xLabel, yLabel=yLabel, color=color)
    elif type == 'pie':
        showPie(dataList2d)
    for root, dirs, files in os.walk('./BillsApp/analyze/images'):
        for file in files:
            os.remove('./BillsApp/analyze/images/' + file)
    plt.savefig('./BillsApp/analyze/images/'+filename+'.png')


def toDataList2d(dictList, coordiante_x, coordinate_y, io):
    dataList2d = []
    if (coordiante_x, coordinate_y) == ('time', 'money'):
        x = []
        y = []
        for d in dictList:
            x.append(int(d[coordiante_x]))
        x = sorted(list(set(x)))
        x = [str(val) for val in x]
        for date in x:
            sum = 0
            for d in dictList:
                if io == 'out':
                    if d[coordiante_x] == date and float(d[coordinate_y]) < 0:
                        sum += float(d[coordinate_y]) * -1
                elif io == 'in':
                    if d[coordiante_x] == date and float(d[coordinate_y]) > 0:
                        sum += float(d[coordinate_y])
                else:
                    return 0
            y.append(sum)
        x = [int(val) for val in x]
        dataList2d.append(x)
        dataList2d.append(y)
        return dataList2d
    elif (coordiante_x, coordinate_y) == ('type', 'money') and io == 'out':
        x = []
        y = []
        for d in dictList:
            type = int(d[coordiante_x])
            if type != -1:
                x.append(type)
        x = sorted(list(set(x)))
        x = [str(val) for val in x]
        for type in x:
            sum = 0
            for d in dictList:
                if d[coordiante_x] == type:
                    sum += float(d[coordinate_y]) * -1
            y.append(sum)
        x = [int(val) for val in x]
        dataList2d.append(x)
        dataList2d.append(y)
        return dataList2d
    elif (coordiante_x, coordinate_y) == ('time', 'type') and io == 'out':
        x = []
        y = []
        t = []
        for d in dictList:
            x.append(int(d[coordiante_x]))
            type = int(d[coordinate_y])
            if type != -1:
                t.append(type)
        x = sorted(list(set(x)))
        x = [str(val) for val in x]
        t = sorted(list(set(t)))
        t = [str(val) for val in t]
        for date in x:
            maxtype = 0
            max = 0
            for type in t:
                sum = 0
                for d in dictList:
                    if d[coordinate_y] == type and d[coordiante_x] == date:
                        sum += float(d['money']) * -1
                if sum > max:
                    max = sum
                    maxtype = type
            y.append(int(maxtype))
        x = [int(val) for val in x]
        dataList2d.append(x)
        dataList2d.append(y)
        return dataList2d
    else:
        return 0