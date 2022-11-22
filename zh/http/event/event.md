# 事件订阅

该接口为 Websocket 接口，由 GET 请求方式升级为 Websocket。<br>Websocket接口最大支持三个客户端连接

## 请求路径

> `​/v1​/event`

## 请求方式

> GET => WSS

## 返回数据字段

| 字段 | 类型   | 字段释义                         |
| ---- | ------ | -------------------------------- |
| type | Int    | 事件类型,当前仅有0，表示识别事件 |
| data | Object | 其他补充信息                     |

### 各 type 的 data 数据字段

**识别事件数据**

| 字段            | 类型    | 字段释义                                                     |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | string  | 设备序列号                                                   |
| recognitionType | Int     | 识别类型: 1:员工,2:访客,3:陌生人,4:非活体,5:黑名单 |
| recognizeScore  | Float   | 识别精度分值                                                 |
| mask            | Int     | 是否佩戴口罩: 0:未启用,1:未戴,2:佩戴                         |
| mode            | Int     | 核验模式:  0：刷脸 1：刷脸或刷卡 2：刷脸且刷卡 3：刷脸或刷卡或刷二维码 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 |
| rgb_image       | String  | Base64后的jpeg格式的人脸抓拍图                               |
| pass            | Boolean | 是否允许通行                                                 |
| timestamp       | Int     | 识别时间                                                     |
| bodyTemperature       | double     | 体温                                                    |
| user            | Object  | 事件用户对象                                                 |
| --name          | String  | 用户名称                                                     |
| --user_id       | Int     | 用户id                                                       |
| --type          | Int     | 用户类型                                                     |
| --ic_number          | String     | IC 卡号                                                |
| --job_number          | String     | 工号                                                   |

## 返回示例

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
            "type": 1,
            "ic_number":"d144d33z95x",
            "job_number":"9833"
            
        },
        "timestamp": 1660625866,
        "bodyTemperature": 36.53308868408203
    }
}
```