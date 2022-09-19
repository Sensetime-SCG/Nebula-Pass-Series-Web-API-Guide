# 第三方服务器推送配置[Deprecated]

该接口的功能已经整合到 `/v1/device/functions/`接口中的`auth_mode`与`auth_event_address`字段，后续该接口将会移除。

## 获取配置
获取第三方服务器推送配置，如第三方服务地址，是否启动推送功能。

### 请求地址

https://HOST:PORT/v1/event/subscribe

### 请求方式

GET

### 请求参数

| 名称 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| 无   | 无   | 无   | 无   |

### 响应参数

| 名称       | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| event_dest | string | 指定事件接收的地址，采用restful回调模式，支持http和https，样式如下：http://ip:port/eventRcv或者https://ip:port/eventRcv<br/> 不超过1024个字符，事件接收地址由应用方负责按指定的规范提供，事件接收接口不需要认证 |


响应示例：

```
{

    "code": 200,
    "msg": "OK",
    "data":null
}
```





## 设置配置


设置第三方服务器推送配置，如第三方服务地址，是否启动推送功能。

### 请求地址

https://HOST:PORT/v1/event/subscribe

### 请求方式

POST

### 请求参数

| 名称       | 类型   | 必填 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| event_dest | string | Y    | 指定事件接收的地址，采用restful回调模式，支持http和https，样式如下：http://ip:port/eventRcv或者https://ip:port/eventRcv<br/> 不超过1024个字符，事件接收地址由应用方负责按指定的规范提供，事件接收接口不需要认证 |


请求实例

```
{
    "event_dest" : "http://ip:port/eventRcv"
}
```

### 响应参数

| 名称 | 类型 | 说明 |
| ---- | ---- | ---- |
|      |      |      |

响应示例：

```
{

"code": 200,

"msg": "OK",

"data": {

}

}
```



## 事件推送协议（HTTP/HTTPS）

### 接收方式

POST application/json

### 响应结构

| **参数名称**    | **类型** | **是否必填** | **说明**                                                     |
| --------------- | -------- | ------------ | ------------------------------------------------------------ |
| **code**        | int      | Y            | 返回码，200表示成功，其它表示失败                            |
| **message**     | string   | Y            | 返回信息-记录接口执行情况说明信息，success表示成功描述，其他表示失败 |
| **data**        | Object   | Y            | 其他补充信息                                                 |
| \|-- pass       | boolean  | Y            | 是否开门                                                     |
| \|-- customtips | string   | N            | 界面提示的文字(建议内容 0- 10 字符)                          |

响应示例

```
{
    "code": 200,
    "msg": "success",
    "data": {
        "pass": true,
        "customtips":"Hello World"
    }
}  
```

### 事件推送示例

| **参数名称** | **类型** | **是否必填** | **说明**                         |
| ------------ | -------- | ------------ | -------------------------------- |
| **type**     | int      | Y            | 事件类型,当前仅有0，表示识别事件 |
| **data**     | object   | Y            | 事件对象                         |

识别记录

```
{
    "type": 0,
    "data": {
        "recognizeStatus": 2,
        "trackID": 13,
        "recognizeScore": 0.9837480783462524,
        "livenessScore": 0.9073520302772522,
        "mask": 1,
        "rgb_image": "xxxxxxxxxxxxxx=",
        "pass": true,
        "mode": 0,
        "user": {
            "name": "Q",
            "user_id": 1,
            "type": 1
        },
        "timestamp": 1660625866
    }
}

```

### 记录事件字段属性

| 参数名称        | 类型    | 说明                                                         |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | string  | 设备序列号                                                   |
| recognizeStatus | int     | 当前画面中人脸的分类： 0：未知 1：非活体 2：库中人 3：陌生人 4：已识别 5：认证通过 6：认证失败 |
| recognizeScore  | float   | 识别精度分值                                                 |
| livenessScore   | float   | 活体精度分值                                                 |
| mask            | int     | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| mode            | int     | 核验模式: 0：刷脸 1：刷脸或刷卡 2：刷脸或刷卡或刷二维码 3：刷脸且刷卡 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 |
| rgb_image       | string  | Base64 后的jpeg格式的人脸抓拍图                              |
| pass            | Boolean | 是否允许通行                                                 |
| timestamp       | int     | 识别时间                                                     |
| user            | object  | 事件用户对象                                                 |
| --name          | string  | 用户名称                                                     |
| --user_id       | int     | 用户id                                                       |
| --type          | int     | 用户类型                                                     |



