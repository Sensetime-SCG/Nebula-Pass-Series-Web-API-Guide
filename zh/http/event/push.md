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
    "type": 0,
    "data": {
        "recognitionType": 1,
        "deviceSN":"PS71HD01MC22C00014",
        "recognizeScore": 0.9837480783462524,
        "mask": 1,
        "rgb_image": "xxxxxxxxxxxxxx=",
        "pass": true,
        "mode": 0,
        "user": {
            "name": "Q",
            "user_id": 1,
            "type": 1
        },
        "timestamp": 1660625866,
        "bodyTemperature": 36.53308868408203
    }
}
```

### 记录事件字段属性

| 参数名称        | 类型    | 说明                                                         |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | string  | 设备序列号                                                   |
| recognitionType | Int     | 识别类型: 1:员工,2:访客,3:陌生人,4:非活体,5:黑名单 |
| recognizeScore  | float   | 识别精度分值                                                 |
| mask            | int     | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| mode            | int     | 核验模式: 0：刷脸 1：刷脸或刷卡 2：刷脸或刷卡或刷二维码 3：刷脸且刷卡 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 |
| rgb_image       | string  | Base64 后的jpeg格式的人脸抓拍图                              |
| pass            | Boolean | 是否允许通行                                                 |
| timestamp       | int     | 识别时间                                                     |
| bodyTemperature       | double     | 体温                                                    |
| user            | object  | 事件用户对象                                                 |
| --name          | string  | 用户名称                                                     |
| --user_id       | int     | 用户id                                                       |
| --type          | int     | 用户类型                                                     |



