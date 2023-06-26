# 第三方服务器推送配置

该接口的功能可用于识别记录上传功能，当接收服务器断开，网络异常或者没收到请求应答，设备将缓存该记录，待网络状态恢复后上传识别记录,设备最大离线缓存50000条记录

## 提交配置
设置第三方服务器推送配置，如第三方服务地址，是否启动识别记录推送功能。

### 请求路径
>/v1/event/subscribe

### 请求方式

> POST

- 请求体: `application/json`

| 名称       | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| event_dest | string | 指定事件接收的地址，采用restful回调模式，支持http和https，样式如下：http://ip:port/Record或者https://ip:port/Reocrd<br/> 不超过1024个字符，事件接收地址由应用方负责按指定的规范提供，事件接收接口不需要认证 |
| enabled    | boolen | 是否启用，HTTP事件推送服务                                                    |

### 请求示例:
```json
{
    "event_dest" : "http://ip:port/Record",
    "enabled" :true
}
```

### 返回示例：
```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```


## 获取配置
获取第三方服务器推送配置，如第三方服务地址，是否启动识别记录推送功能。


### 请求地址

>/v1/event/subscribe

### 请求方式

> GET

### 请求实例
>/v1/event/subscribe


### 响应示例：

```json
{
    "code": 200,
    "msg": "OK",
    "data": null
}
```



## 事件推送协议（HTTP/HTTPS）

### 接收方式

POST application/json

### 响应结构

| **参数名称**    | **类型** | **是否必填** | **说明**                                                     |
| --------------- | -------- | ------------ | ------------------------------------------------------------ |
| **code**        | int      | Y            | 返回码，200表示成功；其它表示失败                            |
| **message**     | string   | Y            | 返回信息-记录接口执行情况说明信息，success表示成功描述，其他表示失败 |
| **data**        | Object   | Y            | 其他补充信息                                                 |

响应示例

```json
{
    "code": 200,
    "msg": "success",
    "data": {

    }
}  
```

### 事件推送示例

| **参数名称** | **类型** | **是否必填** | **说明**                         |
| ------------ | -------- | ------------ | -------------------------------- |
| **type**     | int      | Y            | 事件类型：<br />0，表示识别通行事件<br />1，表示设备告警事件  |
| **data**     | object   | Y            | 事件对象                         |


**type = 0 识别事件数据**

### 

**记录事件字段属性**

| 参数名称        | 类型    | 说明                                                         |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | String | 设备序列号                                                   |
| recognitionType | Int     | 识别类型: 1:员工,2:访客,3:陌生人,4:非活体,5:黑名单 |
| uuid | String | 记录事件唯一标识 |
| recognizeScore  | Float   | 识别精度分值                                                 |
| mask            | Int  | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| mode            | Int  | 核验模式: 0：刷脸 1：刷脸或刷卡 2：刷脸且刷卡 3：刷脸或刷卡或刷二维码或PIN 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 7：刷脸且PIN 8：刷脸且刷卡且PIN 9：刷卡且PIN |
| rgb_image       | String | Base64 后的jpeg格式的人脸抓拍图                              |
| pass            | Boolean | 是否允许通行                                                 |
| timestamp       | Int  | 识别时间                                                     |
| bodyTemperature       | Double     | 体温                                                    |
| entry_mode    | int       | 开门方式：1：刷脸；2：二维码；3：刷卡；4：刷脸+刷卡；5：刷身份证；6：刷脸且刷身份证；7：刷健康码；8：刷脸+PIN；9：刷卡+PIN；10：刷脸+刷卡+PIN；11：开门按钮；12：工号+PIN  |
| abnormal_type    | int       | 异常事件类型：0-无;10001-人证不匹配;  10002-人卡不匹配;  10003-人码不匹配;20001-访客不在有效期内   20002-不在通行时间内；30001-无效身份证;  30002-无效IC卡;   30003-无效二维码; 40001-体温异常；70001-PIN码错误；70002-PIN码错误次数过多|
| user            | object  | 事件用户对象                                                 |
| --name          | String | 用户名称                                                     |
| --user_id       | String | 用户id                                                       |
| --type          | Int  | 用户类型: 1:员工,2:访客,5:黑名单                                                     |
| --ic_number          | String     | IC 卡号                                                  |
| --job_number          | String     | 工号                                                   |
| --id_number | String | ID卡号 |
| --guest_time_start | Int | 访客开始时间，毫秒级Unix时间戳 |
| --guest_time_end | Int | 访客结束时间，毫秒级Unix时间戳 |
| -- remark | String | 备注,上限256字节 |
| -- pin       | String     | 密碼pin code                                            |
| -- groups | object array | user_id所在的组信息 |


```json
{
    "type": 0,
    "data": {
        "deviceSN": "PSC700C0MC22F02542",
        "recognitionType": 1,
        "entry_mode": 1,
        "abnormal_type": 0,
        "uuid": "4d3987c1-a3b3-470b-9fb7-e114772c069c",
        "recognizeScore": 0.9302213788032532,
        "mask": 0,
        "mode": 3,
        "rgb_image": " ",
        "bodyTemperature": 0.0,
        "pass": true,
        "timestamp": 1685343715,
        "user": {
            "name": "王五",
            "ic_number": "12345",
            "id_number": "",
            "job_number": "23385",
            "pin": "",
            "user_id": "5",
            "remark": "",
            "guest_time_start": 0,
            "guest_time_end": 0,
            "type": 1,
            "groups": [
                {
                    "id": "3",
                    "name": "测试3"
                },
                {
                    "id": "4",
                    "name": "测试4"
                }
            ]
        }
    }
}
```


**type =1 设备告警事件**

### 

**设备告警事件对象**：

| 参数名称    | 类型           | 是否必须        | 说明                                                         |
| ----------- | -------------- | --------------- | ------------------------------------------------------------ |
| trace_id    | string         | 必填            | 告警流水号 ，设备生成，告警的唯一标识号                      |
| description | string         | 非必填          | 告警描述                                                     |
| code        | int            | status为1时必填 | 告警编码 10001表示拆机告警，10002表示强制开门告警，10003表示门磁超时告警，10004表示密码攻击告警，20003表示消防告警， |
| user_id     | long           | 非必填          | 关联用户ID 用于关联用户                                      |
| event_time  | Long           | 必填            | 事件时间，新告警上报填写告警发生时间，告警处理结果上报填写处理时间 时间戳，精确到毫秒，13位 |
| status      | int            | 必填            | 告警上报事件，1为发生告警，2为告警解除失败，3为告警解除成功  |
| alarm_photo | String(BASE64) | 非必填          | 告警图片                                                     |



## 返回示例

```
{
    "type":1,
    "data":{
        "trace_id":"SPX-1684381418208-004-3Adb4v",
        "description":" ",
        "code":10001,
        "event_time":1684381433398,
        "status":1,
        "alarm_photo":" ",
    }
}
```



