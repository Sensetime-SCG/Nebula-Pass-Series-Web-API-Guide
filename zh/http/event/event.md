# 事件订阅

该接口为 Websocket 接口，由 GET 请求方式升级为 Websocket。

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

| 字段            | 类型    | 字段释义                                                                                                       |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| trackID         | Int     | 对当前图像人脸一个临时标记的ID                                                                                 |
| recognizeStatus | Int     | 当前画面中人脸的分类: 0:未知,1:非活体,2:库中人,3:陌生人,4:已识别,5:认证通过,6:认证失败                         |
| recognizeScore  | Float   | 识别精度分值                                                                                                   |
| livenessScore   | Float   | 活体精度分值                                                                                                   |
| mask            | Int     | 是否佩戴口罩: 0:未启用,1:未戴,2:佩戴                                                                           |
| mode            | Int     | 核验模式: 0:刷脸,1:刷脸或刷卡,2:刷脸或刷卡或刷二维码,3:刷脸且刷卡,4:刷身份证,5:刷脸或刷身份证,6:刷脸且刷身份证 |
| rgb_image       | String  | Base64后的jpeg格式的人脸抓拍图                                                                                 |
| pass            | Boolean | 是否允许通行                                                                                                   |
| timestamp       | Int     | 识别时间                                                                                                       |
| user            | Object  | 事件用户对象                                                                                                   |
| --name          | String  | 用户名称                                                                                                       |
| --user_id       | Int     | 用户id                                                                                                         |
| --type          | Int     | 用户类型                                                                                                       |

## 返回示例

```json
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