# bill_list_API

**主键用数据库自己生成的自增id**

## 查询账单

#### HTTP Method

```http
[GET]
```

#### Path

```http
/bill/list/
```

###### 参数说明

| 参数 | 说明             | 是否必须 |
| ---- | ---------------- | -------- |
| time | 月份，按月份查询 | 是       |
| username | 用户名 | 是       |

###### 样例

```http
/bill/list/?time=201707&username=aaa
```

### Response

###### 实例:

```json
[
	{
        "time":"20170701",
        "money":"-200",
        "type":"6",
        "remark":"买了CSAPP",
        "mood":"1"
    },
    {
        "time":"20170702",
        "money":"100",
        "type":"-1",
        "mood":"2"
    }
]
```

#### 字段说明:

| 字段   | 数据类型 | 说明                  | 可否为空 |
| ------ | -------- | --------------------- | -------- |
| time   | string   | 记账时间              | 否       |
| money  | string   | 金额                  | 否       |
| type   | string   | 账目类型              | 否       |
| remark | string   | 备注                  | 是       |
| mood   | string   | 心情级别(分1、2、3级) | 是       |

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not get"
}

{
    "error":"bills do not exist"
}
```

#### 字段说明

| 字段  | 属性               | 数据类型 | 说明             |
| ----- | ------------------ | -------- | ---------------- |
| error | something absent   | string   | post部分数据缺失 |
| error | not get            | string   | 方法不是get      |
| error | bills do not exist | string   | 查找的账单不存在 |



## 新增账单

#### HTTP Method

```http
[POST]
```

#### Path

```http
/bill_list/new_bill/
```

### PostBody

| 字段   | 数据类型 | 说明                  | 是否必须 |
| ------ | -------- | --------------------- | -------- |
| username   | string   | 用户名              | 是       |
| time   | string   | 记账时间              | 是       |
| money  | string   | 金额                  | 是       |
| type   | string   | 账目类型              | 是     |
| remark | string   | 备注                  | 否       |
| mood   | string   | 心情级别(分1、2、3级) | 否       |

###### 示例

```json
{
    "username":"xxx",
 	"time":"20170701",
    "money":"-200",
    "type":"5",
    "remark":"买了CSAPP",
    "mood":"1"
}
```

### Response

#### 字段说明:

| 字段   | 数据类型 | 说明                                       |
| ------ | -------- | ------------------------------------------ |
| result | string   | 是否插入成功（1为成功，0为失败(未知错误)） |

###### 样例：

```json
{
    "result":"1"
}
```

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}

{
    "error":"username do not exist"
}

{
    "error"："type and money error"
}
```

#### 字段说明

| 字段  | 属性                  | 数据类型 | 说明                   |
| ----- | --------------------- | -------- | ---------------------- |
| error | something absent      | string   | post部分数据缺失       |
| error | not post              | string   | 方法不是post           |
| error | username do not exist | string   | 用户名不存在           |
| error | type and money error  | string   | 金额符号与type匹配错误 |



## 修改账单

#### HTTP Method

```http
[POST]
```

#### Path

```http
/bill_list/update_bill/
```

### PostBody

| 字段       | 数据类型 | 说明                           | 是否必须 |
| ---------- | -------- | ------------------------------ | -------- |
| username       | string   | 用户名             | 是       |
| time       | string   | 记账时间，具体到日             | 是       |
| money      | string   | 金额                           | 是       |
| type       | string   | 记账类型                       | 是     |
| new_money  | string   | 更新的金额                     | 否       |
| new_type   | string   | 更新的账目类型                 | 否       |
| new_remark | string   | 更新的备注                     | 否       |

###### 示例

```json
{
    "username":"xxx",
	"time":"20170512",
    "money":"-100",
    "type":"3",
    "order":"1",
    "new_money":"120"
}
```

#### Response

###### 字段说明:

| 字段   | 数据类型 | 说明                                   |
| ------ | -------- | -------------------------------------- |
| result | string   | 是否修改成功（1为成功，0为账单不存在） |

###### 样例：

```json
{
 	"result":  "1",
}
```

#### 错误反馈：

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}

{
    "error":"username do not exist"
}

{
    "error"："type and money error"
}
```

#### 字段说明

| 字段  | 属性                  | 数据类型 | 说明                   |
| ----- | --------------------- | -------- | ---------------------- |
| error | something absent      | string   | post部分数据缺失       |
| error | not post              | string   | 方法不是post           |
| error | username do not exist | string   | 用户名不存在           |
| error | type and money error  | string   | 金额符号与type匹配错误 |



## 删除账单信息

#### HTTP Method

```http
[POST]
```

#### Path

```http
/bill_list/delete_bill/
```

###### 参数说明

| 参数  | 说明                         | 是否必须 |
| ----- | ---------------------------- | -------- |
| username  | 用户名           | 是       |
| time  | 要删除的账单的时间           | 是       |
| money | 金额                         | 是       |
| type  | 账目类型                     | 是     |

#### Response

###### 字段说明:

| 字段   | 数据类型 | 说明 |
| ------ | -------- | ---- |
| result | string   | "1"删除成功,"0"账单不存在 |

###### 样例：

```json
{
    "result":"1"
}
```

#### 错误反馈：

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}

{
    "error":"username do not exist"
}
```

#### 字段说明

| 字段  | 属性                  | 数据类型 | 说明             |
| ----- | --------------------- | -------- | ---------------- |
| error | something absent      | string   | post部分数据缺失 |
| error | not post              | string   | 方法不是post     |
| error | username do not exist | string   | 用户名不存在     |



# ldl-bills-api

## 注册

###  path

```http
/register/
```

### method

```http
[POST]
```

### 参数说明

| 参数     | 说明   | 是否必须 | 数据类型 |
| -------- | ------ | -------- | -------- |
| username | 用户名 | 是       | string   |
| password | 密码   | 是       | string   |
| sex      | 性别   | 否       | string   |
| age      | 年龄   | 否       | string   |

### response

示例

```json
{
    "result":"1"
}
```
| 字段   | 数据类型 | 说明 |
| ------ | -------- | ---- |
| result | string   | "1"成功,"0"用户名已存在 |

#### 错误反馈：

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}
```

#### 字段说明

| 字段  | 属性             | 数据类型 | 说明                 |
| ----- | ---------------- | -------- | -------------------- |
| error | not post         | string   | 方法不是post         |
| error | something absent | string   | post部分必需数据缺失 |

## 登录

### path

```http 
/login/
```

### method

```http
[POST]
```

### 参数说明

| 参数     | 说明   | 是否必须 | 数据类型 |
| -------- | ------ | -------- | -------- |
| username | 用户名 | 是       | string   |
| password | 密码   | 是       | string   |

### response

示例

```json
{
    "result":"1"
}
```
| 字段   | 数据类型 | 说明 |
| ------ | -------- | ---- |
| result | string   | "1"成功,"0"用户名错误,"-1"密码错误|

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}
```

#### 字段说明

| 字段  | 属性             | 数据类型 | 说明             |
| ----- | ---------------- | -------- | ---------------- |
| error | not post         | string   | 方法不是post     |
| error | something absent | string   | post部分数据缺失 |

## 注销

### path

```http 
/writeoff/
```

### method

```http
[GET]
```

### 参数说明

| 参数     | 说明   | 是否必须 | 数据类型 |
| -------- | ------ | -------- | -------- |
| username | 用户名 | 是       | string   |

### response

示例

```json
{
    "result":"1"
}
```

| 字段   | 数据类型 | 说明                  |
| ------ | -------- | --------------------- |
| result | string   | "1"成功,"0"无此用户名 |

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}
```

#### 字段说明

| 字段  | 属性             | 数据类型 | 说明             |
| ----- | ---------------- | -------- | ---------------- |
| error | not post         | string   | 方法不是post     |
| error | something absent | string   | post部分数据缺失 |

## 数据图

### path

```http
/image/
```

### method

```http
[POST]
```

### 参数说明

|参数          |   说明    | 是否必须  | 数据类型 |
|--------------|----------|---------|---------|
|username      | 用户名 |  是    |  string|
|filename      | 返回图片名 |  是    |  string|
|coordinate_x  | x坐标对象  |  是    |  string|
|coordinate_y  | y坐标对象   | 是    |  string|
|type          | 数据图类型 |  是    |  string|
|color         | 颜色       | 否     | string|
|month    | 月份  | 是   | string |
|io | 收入或支出 | 是 | string |

| 特殊说明                                                     |
| ------------------------------------------------------------ |
| x,y坐标对象只可从['time','money','type']中选择。             |
| (x,y)搭配限制为:[('time', 'money'), ('type', 'money'), ('time', 'type')]。其中('type', 'money')和('time', 'type')的io只可为‘out’。 |
| type只可从['bar','line','pie']中选择，分别对应柱状图、折线图、饼图。 |
| color只可从['red','blue','green','gray','black','yellow','purple','orange']中选择，其中饼图color无效，柱状图和折线图必须要color。 |
| month形如’201807‘。                                          |
| io为['in', 'out']之一。                                      |

### response

返回二进制文件：xxx.png

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not post"
}

{
    "error":"username do not exist"
}

{
    "error":"color error"
}

{
    "error":"type error"
}

{
    "error":"coordinate error"
}

{
    "error":"io error"
}
```

#### 字段说明

| 字段  | 属性                  | 数据类型 | 说明                   |
| ----- | --------------------- | -------- | ---------------------- |
| error | something absent      | string   | post部分数据缺失       |
| error | not post              | string   | 方法不是post           |
| error | username do not exist | string   | 用户名不存在           |
| error | color error           | string   | 颜色超出选择范围       |
| error | type error            | string   | 数据图类型超出选择范围 |
| error | coordinate error      | string   | 坐标选择错误           |
| error | io error              | string   | 收入支出选择错误       |

## 消费分析预测

### path

```http
/prediction/?username=username/
```

### method

```http
[GET]
```

### response

示例

```json
{
    "top1":"1",
    "top2":"4",
    "top3":"5",
    "bottom1":"7",
    "bottom2":"2",
    "bottom3":"3",
    "top1_money":"33",
    "top2_money":"33",
    "top3_money":"33",
    "bottom1_money":"22",
    "bottom2_money":"22",
    "bottom3_money":"22",
}
```
| 字段   | 数据类型 | 说明 |
| ------ | -------- | ---- |
| top1 | string   |用户最喜欢的消费类型 |
| top2 | string   |用户第二喜欢的消费类型 |
| top3 | string   |用户第三喜欢的消费类型 |
| bottom1 | string   |用户最不喜欢的消费类型 |
| bottom2 | string   |用户第二不喜欢的消费类型 |
| bottom3 | string   |用户第三不喜欢的消费类型 |
| top1_money | string   |用户最喜欢的消费类型对应金额 |
| top2_money  | string   |用户第二喜欢的消费类型对应金额 |
| top3_money  | string   |用户第三喜欢的消费类型对应金额 |
| bottom1_money | string   |用户最不喜欢的消费类型对应金额 |
| bottom2_money | string   |用户第二不喜欢的消费类型对应金额 |
| bottom3_money | string   |用户第三不喜欢的消费类型对应金额 |

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not get"
}

{
    "error":"username do not exist"
}
```

#### 字段说明

| 字段  | 属性                  | 数据类型 | 说明             |
| ----- | --------------------- | -------- | ---------------- |
| error | something absent      | string   | post部分数据缺失 |
| error | not get               | string   | 方法不是get      |
| error | username do not exist | string   | 用户名不存在     |

## 从云端同步数据

#### HTTP Method

```http
[GET]
```

#### Path

```http
/synchronize/
```

###### 参数说明

| 参数     | 说明   | 是否必须 |
| -------- | ------ | -------- |
| username | 用户名 | 是       |

###### 样例

```http
/synchronize/?username=aaa
```

### Response

###### 实例:

```json
[
	{
        "time":"20170701",
        "money":"-200",
        "type":"2",
        "remark":"买了CSAPP",
        "mood":"1"
    },
    {
        "time":"20170702",
        "money":"-100",
        "type":"3",
        "remark":"吃撑了",
        "mood":"2"
    }
]
```

#### 字段说明:

| 字段   | 数据类型 | 说明                  | 可否为空 |
| ------ | -------- | --------------------- | -------- |
| time   | string   | 记账时间              | 否       |
| money  | string   | 金额                  | 否       |
| type   | string   | 账目类型              | 否       |
| remark | string   | 备注                  | 是       |
| mood   | string   | 心情级别(分1、2、3级) | 是       |

#### 错误反馈

```json
{
    "error":"something absent"
}

{
    "error":"not get"
}

{
    "error":"bills do not exist"
}
```

#### 字段说明

| 字段  | 属性               | 数据类型 | 说明             |
| ----- | ------------------ | -------- | ---------------- |
| error | something absent   | string   | post部分数据缺失 |
| error | not get            | string   | 方法不是get      |
| error | bills do not exist | string   | 查找的账单不存在 |