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
| **type**     | int      | Y            | 事件类型,当前仅有0，表示识别事件 |
| **data**     | object   | Y            | 事件对象                         |

识别记录

```json
{
    "type":0,
    "data":{
        "deviceSN":"PS71HD01MC22B00003",
        "recognitionType":1,
        "uuid":"f63cad1a-e12c-4ea6-8098-01e8240bfa5b",
        "recognizeScore":0.9499402046203613,
        "mask":0,
        "mode":3,
        "rgb_image":" ",
        "bodyTemperature":0,
        "pass":true,
        "timestamp":1678870602,
        "user":{
            "name":"张三",
            "ic_number":"1234",
            "id_number":"gO/i1UcxN3k=",
            "job_number":"",
            "user_id":"3",
            "remark":"",
            "guest_time_start":0,
            "guest_time_end":0,
            "type":1,
            "groups":[
                {
                    "id":"1",
                    "name":"测试1"
                },
                {
                    "id":"2",
                    "name":"测试2"
                }
            ]
        }
    }
}
```

### 记录事件字段属性

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
| user            | object  | 事件用户对象                                                 |
| --name          | String | 用户名称                                                     |
| --user_id       | String | 用户id                                                       |
| --type          | Int  | 用户类型                                                     |
| --ic_number          | String     | IC 卡号                                                  |
| --job_number          | String     | 工号                                                   |
| --id_number | String | ID卡号 |
| --guest_time_start | Int | 访客开始时间，毫秒级Unix时间戳 |
| --guest_time_end | Int | 访客结束时间，毫秒级Unix时间戳 |
| -- remark | String | 备注,上限256字节 |
| -- groups | object array | user_id所在的组信息 |



