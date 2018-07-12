import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
import operator
import BillsApp.function as fun


def toOnehost(type):
    v = [0,0,0,0,0,0,0,0,0,0,0]
    v[int(type)] = 1
    return list(v)



def showType(x, y):
    x_list = x[:]
    x = [list([val]) for val in x_list]
    train_x = [toOnehost(int(val)) for val in x_list]
    rgr = MLPRegressor()
    rgr.fit(train_x, y)
    x_list = list(set(x_list))
    x = [list([val]) for val in x_list]
    test_x = [toOnehost(int(val)) for val in x_list]
    prediction = rgr.predict(test_x)
    m = len(x_list)
    d = {}
    for i in range(m):
        d[x_list[i]] = prediction[i]
    sorted_x = sorted(d.items(), key=operator.itemgetter(1))
    top3 = []
    bottom3 = []
    for i in range(3):
        top3.append(sorted_x[i][0])
        bottom3.append(sorted_x[-(i + 1)][0])
    return top3, bottom3





def showMoney(xType, xMood, y):
    print(xMood)
    x = [toOnehost(int(xType[i])) for i in range(len(xType))]
    train_x = []
    m = len(x)
    for i in range(m):
        x[i].append(xMood[i])
        train_x.append(x[i])
    rgr = MLPRegressor()
    rgr.fit(x, y)
    d = {}
    for xt in set(xType):
        d[xt] = {}
        for xm in set(xMood):
            test_x = toOnehost(int(xt))
            test_x.append(xm)
            d[xt][xm] = str(int(rgr.predict([test_x])))
    return d


def returnAllList(username):
    dictList = fun.allBills(username)
    if dictList == 0:return 0
    else:
        moneyList = []
        moodList = []
        typeList = []
        if len(dictList) == 0:return 0
        for d in dictList:
            if d['type'] != '-1':
                if d['mood'] == '1' or d['mood'] == '2' or d['mood'] == '3':
                    moneyList.append(int(d['money'])*-1)
                    moodList.append(int(d['mood']))
                    typeList.append(int(d['type']))
    return moneyList, moodList, typeList

