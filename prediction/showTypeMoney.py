import pandas as pd
from sklearn.neural_network import MLPRegressor
import operator
import BillsApp.function as fun


def showType(x, y):
    x_list = x[:]
    x = [list([val]) for val in x_list]
    rgr = MLPRegressor()
    rgr.fit(x, y)
    x_list = list(set(x_list))
    x = [list([val]) for val in x_list]
    prediction = rgr.predict(x)
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
    x = [list([xType[i], xMood[i]]) for i in range(len(xType))]
    rgr = MLPRegressor()
    rgr.fit(x, y)
    test_x = []
    d = {}
    for xt in set(xType):
        d[xt] = {}
        for xm in set(xMood):
            d[xt][xm] = str(int(rgr.predict([[xt,xm]])))
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

