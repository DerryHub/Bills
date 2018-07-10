from django.shortcuts import render,redirect
from BillsApp.analyze.showpng import *
from django.http import HttpResponse
import json
from BillsApp.analyze.showimage import *
from prediction.showTypeMoney import *
from BillsApp import function as fun
from BillsApp.models import *
import numpy as np



# Create your views here.

# 登录函数
# 方法——post
# path-/login/
# 用户名——username
# 密码——password
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            if fun.exist(username):
                if fun.judgePassword(username, password):
                    dict = {'result': '1'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    dict = {'result': '-1'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
            else:
                dict = {'result': '0'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            ditc = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error':'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'login.html')  # test


# 登录功能正常


# 注册函数
# 方法——post
# path-/register/
# 用户名——username
# 性别——sex
# 年龄——age
# 密码——password
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        sex = request.POST.get('sex', None)
        age = request.POST.get('age', None)
        password = request.POST.get('password', None)
        if username and password:
            if fun.exist(username):
                dict = {'result': '0'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
            else:
                if not sex:
                    sex = np.nan
                if not age:
                    age = np.nan
                t = fun.addUser(username, password, sex, age)
                if t:
                    dict = {'result': '1'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    dict = {'error': 'unknown'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'register.html')  # test


# 注册功能正常

# 增删改查

# 查询账单
# 方法——get
# path-/bill/list/
# | 参数 | 说明           | 默认 | 是否必须 |
# | ---- | ------------- | ----| --------|
# | time | 月份，按月份查询| 25   | 是      |
# | username | 用户名 |   | 是       |
def getBills(request):
    if request.method == 'GET':
        time = str(request.GET.get('time', None))
        username = str(request.GET.get('username', None))
        if time and username:
            dictList = fun.searchBills(time, username)
            if dictList == 0:
                dict = {'error': 'bills do not exist'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
            else:
                list = []
                for d in dictList:
                    list.append(d)
                if len(list) == 0:
                    dict = {'error': 'bills do not exist'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    jList = json.dumps(list)
                    return HttpResponse(jList)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error': 'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)


# 查询账单功能正常


# 新增账单
# 方法-post
# path-/bill_list/new_bill/
# | 字段   | 数据类型 | 说明                  | 是否必须 |
# | ------ | -------- | --------------------- | -------- |
# | username   | string   | 用户名              | 是       |
# | time   | string   | 记账时间              | 是       |
# | money  | string   | 金额                  | 是       |
# | type   | string   | 账目类型              | 是     |
# | remark | string   | 备注                  | 否       |
# | mood   | string   | 心情级别(分1、2、3级) | 否       |
def addBills(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        remark = request.POST.get('remark', None)
        mood = request.POST.get('mood', None)
        if time and money and username and type:
            if (type != '-1' and int(money) < 0) or (type == '-1' and int(money) > 0):
                if fun.exist(username) == 0:
                    dict = {'error': 'username do not exist'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    if not remark:
                        remark = np.nan
                    if not mood:
                        mood = np.nan
                    t = fun.addBills(time, money, type, remark, mood, username)
                    if t:
                        dict = {'result': '1'}
                        jDict = json.dumps(dict)
                        return HttpResponse(jDict)
                    else:
                        dict = {'result': '0'}
                        jDict = json.dumps(dict)
                        return HttpResponse(jDict)
            else:
                dict = {'error': 'type and money error'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'addBills.html')  # test


# 新增账单功能正常


# 修改账单
# 方法-post
# path-/bill_list/update_bill/
# | 字段       | 数据类型 | 说明                           | 是否必须 |
# | ---------- | -------- | ------------------------------ | -------- |
# | username       | string   | 用户名             | 是       |
# | time       | string   | 记账时间，具体到日             | 是       |
# | money      | string   | 金额                           | 是       |
# | type       | string   | 记账类型                       | 是       |
# | new_money  | string   | 更新的金额                     | 否       |
# | new_type   | string   | 更新的账目类型                 | 否       |
# | new_remark | string   | 更新的备注                     | 否       |

def updateBills(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        new_money = request.POST.get('new_money', None)
        new_type = request.POST.get('new_type', None)
        new_remark = request.POST.get('new_remark', None)
        if time and money and username and type:
            if new_type:
                nt = int(new_type)
            else:
                nt = 0
            if new_money:
                nm = int(new_money)
            else:
                nm = 0
            if int(nt) * int(nm) < 0 or int(type) * int(nm) < 0 or int(nt) * int(money) < 0:
                if fun.exist(username) == 0:
                    dict = {'error': 'username do not exist'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    t = fun.changeBills(username, time, money, type, new_money, new_type, new_remark)
                    if t:
                        dict = {'result': '1'}
                        jDict = json.dumps(dict)
                        return HttpResponse(jDict)
                    else:
                        dict = {'result': '0'}
                        jDict = json.dumps(dict)
                        return HttpResponse(jDict)
            else:
                dict = {'error': 'type and money error'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'updataBills.html')  # test


# 修改账单功能正常


# 删除账单
# 方法-post
# path-/bill_list/delete_bill/
# | 参数  | 说明                         | 是否必须 |
# | ----- | ---------------------------- | -------- |
# | username  | 用户名           | 是       |
# | time  | 要删除的账单的时间           | 是       |
# | money | 金额                         | 是       |
# | type  | 账目类型                     | 是       |
def deleteBills(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        if time and money and type and username:
            if fun.exist(username) == 0:
                dict = {'error': 'username do not exist'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
            else:

                t = fun.deleteBills(time, money, type, username)
                if t:
                    dict = {'result': '1'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    dict = {'result': '0'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'deleteBills.html')  # test


# 删除账单功能正常


# 画图并发送
# 方法-post
# path-/image/
# |参数          |   说明    | 是否必须  | 数据类型 |
# |--------------|----------|---------|---------|
# |username      | 用户名 |  是    |  string|
# |filename      | 返回图片名 |  是    |  string|
# |coordinate_x  | x坐标对象  |  是    |  string|
# |coordinate_y  | y坐标对象   | 是    |  string|
# |type          | 数据图类型 |  是    |  string|
# |color         | 颜色       | 否     | string|
# |month    | 月份    | 是    |  string|
# |io    | 收入或支出    | 是    |  string|
# x,y坐标对象只可从['time','money','type']中选择
# type只可从['bar','line','pie']中选择，分别对应柱状图、折线图、饼图
# color只可从['red','blue','green','gray','black','yellow','purple','orange']中选择，其中饼图color无效，柱状图和折线图必须要color
# month形如'201807'
def sendImage(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        filename = request.POST.get('filename', None)
        coordinate_x = request.POST.get('coordinate_x', None)
        coordinate_y = request.POST.get('coordinate_y', None)
        type = request.POST.get('type', None)
        color = request.POST.get('color', None)
        month = request.POST.get('month', None)
        io = request.POST.get('io', None)
        if filename and coordinate_x and coordinate_y and type and month and username and io:
            if io in ['in', 'out']:
                if (coordinate_x, coordinate_y) in [('time', 'money'), ('type', 'money'), ('time', 'type')]:
                    if type in ['bar', 'line', 'pie']:
                        if type == 'pie':
                            dictList = fun.searchBills(month, username)
                            dataList2d = toDataList2d(dictList, coordinate_x, coordinate_y, io)
                            if dataList2d == 0:
                                dict = {'error': 'unknown'}
                                jDict = json.dumps(dict)
                                return HttpResponse(jDict)
                            savePng(dataList2d=dataList2d, filename=filename, type=type, xLabel=coordinate_x,
                                    yLabel=coordinate_y, color=color)
                            return showImage(filename)
                        else:
                            if color in ['red', 'blue', 'green', 'gray', 'black', 'yellow', 'purple', 'orange']:
                                dictList = fun.searchBills(month, username)
                                dataList2d = toDataList2d(dictList, coordinate_x, coordinate_y, io)
                                if dataList2d == 0:
                                    if dataList2d == 0:
                                        dict = {'error': 'unknown'}
                                        jDict = json.dumps(dict)
                                        return HttpResponse(jDict)
                                savePng(dataList2d=dataList2d, filename=filename, type=type, xLabel=coordinate_x,
                                        yLabel=coordinate_y, color=color)
                                return showImage(filename)
                            else:
                                dict = {'error': 'color error'}
                                jDict = json.dumps(dict)
                                return HttpResponse(jDict)
                    else:
                        dict = {'error': 'type error'}
                        jDict = json.dumps(dict)
                        return HttpResponse(jDict)
                else:
                    dict = {'error': 'coordinate error'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
            else:
                dict = {'error': 'io error'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'sendImage.html')


# 绘制数据图功能正常


# 消费分析预测
# 方法-get
# path-/prediction/
# 参数：username
# | 字段   | 数据类型 | 说明 |
# | ------ | -------- | ---- |
# | top1 | string   |用户最喜欢的消费类型 |
# | top2 | string   |用户第二喜欢的消费类型 |
# | top3 | string   |用户第三喜欢的消费类型 |
# | bottom1 | string   |用户最不喜欢的消费类型 |
# | bottom2 | string   |用户第二不喜欢的消费类型 |
# | bottom3 | string   |用户第三不喜欢的消费类型 |
# | top1_money | string   |用户最喜欢的消费类型对应金额 |
# | top2_money  | string   |用户第二喜欢的消费类型对应金额 |
# | top3_money  | string   |用户第三喜欢的消费类型对应金额 |
# | bottom1_money | string   |用户最不喜欢的消费类型对应金额 |
# | bottom2_money | string   |用户第二不喜欢的消费类型对应金额 |
# | bottom3_money | string   |用户第三不喜欢的消费类型对应金额 |
def consumePrediction(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            if fun.exist(username):
                lists = returnAllList(username)
                if lists == 0:
                    dict = {'error': 'unknown'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    moneyList, moodList, typeList = lists
                    top3, bottom3 = showType(x=typeList, y=moodList)
                    d = showMoney(xMood=moodList, xType=typeList, y=moneyList)
                    dict = {}
                    dict['top1_money'] = d[top3[0]][1]
                    dict['top2_money'] = d[top3[1]][1]
                    dict['top3_money'] = d[top3[2]][1]
                    dict['bottom1_money'] = d[bottom3[0]][3]
                    dict['bottom2_money'] = d[bottom3[1]][3]
                    dict['bottom3_money'] = d[bottom3[2]][3]
                    top3, bottom3 = [str(val) for val in top3], [str(val) for val in bottom3]
                    dict['top1'] = top3[0]
                    dict['top2'] = top3[1]
                    dict['top3'] = top3[2]
                    dict['bottom1'] = bottom3[0]
                    dict['bottom2'] = bottom3[1]
                    dict['bottom3'] = bottom3[2]
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
            else:
                dict = {'error': 'username do not exist'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error': 'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)


# 消费分析预测功能正常


# 注销用户信息
# 方法-get
# path-/writeoff/
# 参数：username
# 字段    	数据类型  	    说明
# result	string	"1"成功,"0"无此用户名
def writeOffUser(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            if fun.exist(username):
                t = fun.deleteUser(username)
                if t:
                    dict = {'result': '1'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    dict = {'result': '0'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
            else:
                dict = {'result': '0'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error': 'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)


# 注销功能正常


# 从云端同步数据
# 方法——get
# path-/synchronize/
# | 参数 | 说明          | 是否必须 |
# | ---- | -------------| --------|
# | username | 用户名   | 是       |
def synchronizeBills(request):
    if request.method == 'GET':
        username = str(request.GET.get('username', None))
        if username:
            dictList = fun.allBills(username)
            if dictList == 0:
                dict = {'error': 'bills do not exist'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
            else:
                if len(dictList) == 0:
                    dict = {'error': 'bills do not exist'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    jList = json.dumps(dictList)
                    return HttpResponse(jList)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error': 'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)


# 同步功能测试正常


# 数据初始化
def init(request):
    user_1 = request.GET.get('user1', None)
    user_2 = request.GET.get('user2', None)
    data_simulation_1 = pd.read_csv('./prediction/simulation_1.csv')
    data_simulation_2 = pd.read_csv('./prediction/simulation_2.csv')
    data_user = pd.read_csv('./prediction/users.csv')
    timeList_1 = data_simulation_1['time']
    moneyList_1 = data_simulation_1['money']
    typeList_1 = data_simulation_1['type']
    moodList_1 = data_simulation_1['mood']
    remarkList_1 = data_simulation_1['remark']
    timeList_2 = data_simulation_2['time']
    moneyList_2 = data_simulation_2['money']
    typeList_2 = data_simulation_2['type']
    moodList_2 = data_simulation_2['mood']
    remarkList_2 = data_simulation_2['remark']
    usernameList = data_user['username']
    passwordList = data_user['password']
    sexList = data_user['sex']
    ageList = data_user['age']

    m_1 = len(timeList_1)
    m_2 = len(timeList_2)
    n = len(usernameList)

    for i in range(n):
        addPeople = UserInfo(
            username=usernameList[i], password=passwordList[i], sex=sexList[i], age=ageList[i]
        )
        addPeople.save()

    user = UserInfo.objects.get(username=user_1)
    for i in range(m_1):
        addBills = OnesBills(
            time=timeList_1[i], money=moneyList_1[i], type=typeList_1[i], mood=moodList_1[i], remark=remarkList_1[i],
            host=UserInfo.objects.get(id=user.id)
        )
        addBills.save()

    user = UserInfo.objects.get(username=user_2)
    for i in range(m_2):
        addBills = OnesBills(
            time=timeList_2[i], money=moneyList_2[i], type=typeList_2[i], mood=moodList_2[i], remark=remarkList_2[i],
            host=UserInfo.objects.get(id=user.id)
        )
        addBills.save()
    return HttpResponse('Done')
# 初始化功能正常


######################################################################################################################

# 网页前端



def user(request, nid):
    obj = UserInfo.objects.get(id=nid)
    return render(request, 'user.html', {'user':obj})



# 登录函数
# 方法——post
# path-/login/
# 用户名——username
# 密码——password
def loginH(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            if fun.exist(username):
                if fun.judgePassword(username, password):
                    obj = UserInfo.objects.get(username=username)
                    return render(request, 'user.html', {'user':obj})
                else:
                    return render(request, 'login.html', {'error': 1})
            else:
                return render(request, 'login.html', {'error': 2})
        else:
            return render(request, 'login.html',{'error':0})
    else:
        return render(request, 'login.html',{'error':0})


# 登录功能正常


# 注册函数
# 方法——post
# path-/register/
# 用户名——username
# 性别——sex
# 年龄——age
# 密码——password
def registerH(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        sex = request.POST.get('sex', None)
        age = request.POST.get('age', None)
        password = request.POST.get('password', None)
        if sex == 'no':sex = None
        if username and password:
            if fun.exist(username):
                return render(request, 'register.html', {'error': 1})
            else:
                if not sex:
                    sex = np.nan
                if not age:
                    age = np.nan
                t = fun.addUser(username, password, sex, age)
                if t:
                    return render(request, 'login.html', {'register':1})
                else:
                    return render(request, 'register.html', {'error': 0})
        else:
            return render(request, 'register.html', {'error': 0})
    else:
        return render(request, 'register.html',{'error':0})


# 注册功能正常

# 增删改查

# 查询账单
# 方法——get
# path-/bill/list/
# | 参数 | 说明           | 默认 | 是否必须 |
# | ---- | ------------- | ----| --------|
# | time | 月份，按月份查询| 25   | 是      |
# | username | 用户名 |   | 是       |
def getBillsH(request, nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        time = request.POST.get('time', None)
        time = time[0:4]+time[5:7]
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        if time and username:
            dictList = fun.searchBills(time, username)
            if dictList == 0:
                return render(request, 'getBills.html', {'nid': nid, 'bill': 0,'user':obj})
            else:
                list = []
                for d in dictList:
                    list.append(d)
                if len(list) == 0:
                    return render(request, 'getBills.html', {'nid': nid, 'bill': 0,'user':obj})
                else:
                    l = []
                    for dict in list:
                        currentList = []
                        currentList.append(dict['time'])
                        currentList.append(dict['money'])
                        currentList.append(dict['type'])
                        currentList.append(dict['remark'])
                        currentList.append(dict['mood'])
                        l.append(currentList)
                    return render(request, 'showBills.html', {'list':l, 'nid':nid,'user':obj})
        else:
            return render(request, 'getBills.html', {'nid':nid,'bill':-1,'user':obj})
    else:
        return render(request, 'getBills.html', {'nid':nid, 'bill':-1,'user':obj})


# 查询账单功能正常


# 新增账单
# 方法-post
# path-/bill_list/new_bill/
# | 字段   | 数据类型 | 说明                  | 是否必须 |
# | ------ | -------- | --------------------- | -------- |
# | username   | string   | 用户名              | 是       |
# | time   | string   | 记账时间              | 是       |
# | money  | string   | 金额                  | 是       |
# | type   | string   | 账目类型              | 是     |
# | remark | string   | 备注                  | 否       |
# | mood   | string   | 心情级别(分1、2、3级) | 否       |
def addBillsH(request, nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        time = request.POST.get('time', None)
        time = time[0:4] + time[5:7]+time[8:10]
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        remark = request.POST.get('remark', None)
        mood = request.POST.get('mood', None)
        if time and money and username and type:
            if (type != '-1' and int(money) < 0) or (type == '-1' and int(money) > 0):
                if fun.exist(username) == 0:
                    return render(request, 'addBills.html', {'nid': nid, 'error': 1,'user':obj})
                else:
                    if not remark:
                        remark = np.nan
                    if not mood:
                        mood = np.nan
                    t = fun.addBills(time, money, type, remark, mood, username)
                    if t:
                        return render(request, 'addBills.html', {'nid': nid, 'error': 0,'user':obj})
                    else:
                        return render(request, 'addBills.html', {'nid': nid, 'error': 1,'user':obj})
            else:
                return render(request, 'addBills.html', {'nid': nid, 'error': 1,'user':obj})
        else:
            return render(request, 'addBills.html', {'nid': nid, 'error':1,'user':obj})
    else:
        return render(request, 'addBills.html', {'nid': nid, 'error': -1,'user':obj})


# 新增账单功能正常


# 修改账单
# 方法-post
# path-/bill_list/update_bill/
# | 字段       | 数据类型 | 说明                           | 是否必须 |
# | ---------- | -------- | ------------------------------ | -------- |
# | username       | string   | 用户名             | 是       |
# | time       | string   | 记账时间，具体到日             | 是       |
# | money      | string   | 金额                           | 是       |
# | type       | string   | 记账类型                       | 是       |
# | new_money  | string   | 更新的金额                     | 否       |
# | new_type   | string   | 更新的账目类型                 | 否       |
# | new_remark | string   | 更新的备注                     | 否       |

def updateBillsH(request, nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        time = request.POST.get('time', None)
        time = time[0:4] + time[5:7] + time[8:10]
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        new_money = request.POST.get('new_money', None)
        new_type = request.POST.get('new_type', None)
        new_remark = request.POST.get('new_remark', None)
        if time and money and username and type:
            if new_money or new_remark or new_type:
                if new_type:
                    nt = int(new_type)
                else:
                    nt = 0
                if new_money:
                    nm = int(new_money)
                else:
                    nm = 0
                if int(nt) * int(nm) < 0 or int(type) * int(nm) < 0 or int(nt) * int(money) < 0:
                    if fun.exist(username) == 0:
                        return render(request, 'login.html')
                    else:
                        t = fun.changeBills(username, time, money, type, new_money, new_type, new_remark)
                        if t:
                            return render(request, 'updataBills.html', {'nid': nid, 'error':0,'user':obj})
                        else:
                            return render(request, 'updataBills.html', {'nid': nid, 'error': -1,'user':obj})
                else:
                    return render(request, 'updataBills.html', {'nid': nid, 'error': 2,'user':obj})
            else:
                return render(request, 'updataBills.html', {'nid': nid, 'error': 1,'user':obj})
        else:
            return render(request, 'updataBills.html', {'nid': nid, 'error':-1,'user':obj})
    else:
        return render(request, 'updataBills.html', {'nid':nid, 'error':-1,'user':obj})


# 修改账单功能正常


# 删除账单
# 方法-post
# path-/bill_list/delete_bill/
# | 参数  | 说明                         | 是否必须 |
# | ----- | ---------------------------- | -------- |
# | username  | 用户名           | 是       |
# | time  | 要删除的账单的时间           | 是       |
# | money | 金额                         | 是       |
# | type  | 账目类型                     | 是       |
def deleteBillsH(request,nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        time = request.POST.get('time', None)
        time = time[0:4] + time[5:7] + time[8:10]
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        if time and money and type and username:
            if fun.exist(username) == 0:
                return render(request, 'login.html')
            else:

                t = fun.deleteBills(time, money, type, username)
                if t:
                    return render(request, 'deleteBills.html', {'nid': nid, 'error': 0,'user':obj})
                else:
                    return render(request, 'deleteBills.html', {'nid': nid, 'error': 1,'user':obj})
        else:
            return render(request, 'deleteBills.html', {'nid': nid, 'error': -1,'user':obj})
    else:
        return render(request, 'deleteBills.html', {'nid':nid,'error':-1,'user':obj})


# 删除账单功能正常




# 画图并发送
# 方法-post
# path-/image/
# |参数          |   说明    | 是否必须  | 数据类型 |
# |--------------|----------|---------|---------|
# |username      | 用户名 |  是    |  string|
# |filename      | 返回图片名 |  是    |  string|
# |coordinate_x  | x坐标对象  |  是    |  string|
# |coordinate_y  | y坐标对象   | 是    |  string|
# |type          | 数据图类型 |  是    |  string|
# |color         | 颜色       | 否     | string|
# |month    | 月份    | 是    |  string|
# |io    | 收入或支出    | 是    |  string|
# x,y坐标对象只可从['time','money','type']中选择
# type只可从['bar','line','pie']中选择，分别对应柱状图、折线图、饼图
# color只可从['red','blue','green','gray','black','yellow','purple','orange']中选择，其中饼图color无效，柱状图和折线图必须要color
# month形如'201807'
def sendImageH(request, nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        filename = username
        itype = int(request.POST.get('itype', None))
        time = request.POST.get('time', None)
        color = request.POST.get('color', None)
        month = time[0:4] + time[5:7]
        if color == '0' and itype != 5:return render(request, 'sendImage.html', {'user':obj, 'nid':nid, 'error':2})
        if itype:
            if itype == 1:
                coordinate_x = 'time'
                coordinate_y = 'money'
                type = 'line'
                io = 'out'
                tip = '消费金额趋势(折线图)'
            elif itype == 2:
                coordinate_x = 'time'
                coordinate_y = 'money'
                type = 'bar'
                io = 'out'
                tip = '消费金额趋势(柱状图)'
            elif itype == 3:
                coordinate_x = 'time'
                coordinate_y = 'money'
                type = 'line'
                io = 'in'
                tip = '收入金额趋势(折线图)'
            elif itype == 4:
                coordinate_x = 'time'
                coordinate_y = 'money'
                type = 'bar'
                io = 'in'
                tip = '收入金额趋势(柱状图)'
            elif itype == 5:
                coordinate_x = 'type'
                coordinate_y = 'money'
                type = 'pie'
                io = 'out'
                tip = '消费类型比例(饼图)'
            elif itype == 6:
                coordinate_x = 'time'
                coordinate_y = 'type'
                type = 'line'
                io = 'out'
                tip = '消费金额最多的类型(折线图)'
            elif itype == 7:
                coordinate_x = 'type'
                coordinate_y = 'money'
                type = 'bar'
                io = 'out'
                tip = '消费金额最多的类型(柱状图)'
            else:
                return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
        else:
            return render(request, 'sendImage.html', {'user':obj, 'nid':nid, 'error':1})
        if filename and coordinate_x and coordinate_y and type and month and username and io:
            if io in ['in', 'out']:
                if (coordinate_x, coordinate_y) in [('time', 'money'), ('type', 'money'), ('time', 'type')]:
                    if type in ['bar', 'line', 'pie']:
                        if type == 'pie':
                            dictList = fun.searchBills(month, username)
                            dataList2d = toDataList2d(dictList, coordinate_x, coordinate_y, io)
                            if dataList2d == 0:
                                return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
                            savePng(dataList2d=dataList2d, filename=filename, type=type, xLabel=coordinate_x,
                                    yLabel=coordinate_y, color=color)
                            # return render(request, 'showImage.html', {'user': obj, 'nid': nid, 'filename':filename, 'tip':tip})
                            return showImage(filename)
                        else:
                            if color in ['red', 'blue', 'green', 'gray', 'black', 'yellow', 'purple', 'orange']:
                                dictList = fun.searchBills(month, username)
                                dataList2d = toDataList2d(dictList, coordinate_x, coordinate_y, io)
                                if dataList2d == 0:
                                    if dataList2d == 0:
                                        return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
                                savePng(dataList2d=dataList2d, filename=filename, type=type, xLabel=coordinate_x,
                                        yLabel=coordinate_y, color=color)
                                # return render(request, 'showImage.html',
                                #               {'user': obj, 'nid': nid, 'filename': filename, 'tip':tip})
                                return showImage(filename)
                            else:
                                return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 2})
                    else:
                        return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
                else:
                    return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
            else:
                return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
        else:
            return render(request, 'sendImage.html', {'user': obj, 'nid': nid, 'error': 0})
    else:
        return render(request, 'sendImage.html', {'user':obj,'nid':nid,'error':0})


# 绘制数据图功能正常


# 消费分析预测
# 方法-get
# path-/prediction/
# 参数：username
# | 字段   | 数据类型 | 说明 |
# | ------ | -------- | ---- |
# | top1 | string   |用户最喜欢的消费类型 |
# | top2 | string   |用户第二喜欢的消费类型 |
# | top3 | string   |用户第三喜欢的消费类型 |
# | bottom1 | string   |用户最不喜欢的消费类型 |
# | bottom2 | string   |用户第二不喜欢的消费类型 |
# | bottom3 | string   |用户第三不喜欢的消费类型 |
# | top1_money | string   |用户最喜欢的消费类型对应金额 |
# | top2_money  | string   |用户第二喜欢的消费类型对应金额 |
# | top3_money  | string   |用户第三喜欢的消费类型对应金额 |
# | bottom1_money | string   |用户最不喜欢的消费类型对应金额 |
# | bottom2_money | string   |用户第二不喜欢的消费类型对应金额 |
# | bottom3_money | string   |用户第三不喜欢的消费类型对应金额 |
def consumePredictionH(request, nid):
    obj = UserInfo.objects.get(id=nid)
    try:
        username = UserInfo.objects.get(id=nid).username
    except:
        return render(request, 'login.html')
    if fun.exist(username):
        lists = returnAllList(username)
        if lists == 0:
            return render(request, 'user.html', {'error':1,'user':obj,'nid':nid})
        else:
            moneyList, moodList, typeList = lists
            top3, bottom3 = showType(x=typeList, y=moodList)
            d = showMoney(xMood=moodList, xType=typeList, y=moneyList)
            dict = {}
            dict['top1_money'] = d[top3[0]][1]
            dict['top2_money'] = d[top3[1]][1]
            dict['top3_money'] = d[top3[2]][1]
            dict['bottom1_money'] = d[bottom3[0]][3]
            dict['bottom2_money'] = d[bottom3[1]][3]
            dict['bottom3_money'] = d[bottom3[2]][3]
            top3, bottom3 = [str(val) for val in top3], [str(val) for val in bottom3]
            dict['top1'] = top3[0]
            dict['top2'] = top3[1]
            dict['top3'] = top3[2]
            dict['bottom1'] = bottom3[0]
            dict['bottom2'] = bottom3[1]
            dict['bottom3'] = bottom3[2]
            dict['user'] = obj
            dict['nid'] = nid
            return render(request, 'prediction.html', dict)
    else:
        return render(request, 'login.html')



# 消费分析预测功能正常


# 注销用户信息
# 方法-get
# path-/writeoff/
# 参数：username
# 字段    	数据类型  	    说明
# result	string	"1"成功,"0"无此用户名
def writeOffUserH(request,nid):
    obj = UserInfo.objects.get(id=nid)
    if request.method == 'POST':
        try:
            username = UserInfo.objects.get(id=nid).username
        except:
            return render(request, 'login.html')
        password = request.POST.get('password', None)
        if username and password:
            if fun.exist(username):
                if fun.judgePassword(username, password):
                    t = fun.deleteUser(username)
                    if t:
                            return render(request, 'login.html', {'writeoff':1})
                    else:
                        return render(request, 'login.html')
                else:
                    return render(request, 'writeoff.html', {'nid': nid, 'user': obj, 'error': 1})
            else:
                return render(request, 'writeoff.html', {'nid': nid, 'user': obj, 'error': -1})
        else:
            return render(request, 'writeoff.html', {'nid': nid, 'user': obj, 'error': -1})
    else:
        return render(request, 'writeoff.html', {'nid':nid,'user':obj,'error':-1})


# 注销功能正常


# 从云端同步数据
# 方法——get
# path-/synchronize/
# | 参数 | 说明          | 是否必须 |
# | ---- | -------------| --------|
# | username | 用户名   | 是       |
def synchronizeBillsH(request):
    if request.method == 'GET':
        username = str(request.GET.get('username', None))
        if username:
            dictList = fun.allBills(username)
            if dictList == 0:
                dict = {'error': 'bills do not exist'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
            else:
                if len(dictList) == 0:
                    dict = {'error': 'bills do not exist'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
                else:
                    jList = json.dumps(dictList)
                    return HttpResponse(jList)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error': 'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)


# 同步功能测试正常

def indexH(request):
    return render(request, 'index.html')

