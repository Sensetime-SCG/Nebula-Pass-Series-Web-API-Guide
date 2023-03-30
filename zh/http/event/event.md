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
| data | Object | 对应事件类型的data,当前仅有识别事件数据 |

### 各 type 的 data 数据字段

**识别事件数据**

### 

| 参数名称           | 类型         | 说明                                                         |
| ------------------ | ------------ | ------------------------------------------------------------ |
| deviceSN           | String       | 设备序列号                                                   |
| recognitionType    | Int          | 识别类型: 1:员工,2:访客,3:陌生人,4:非活体,5:黑名单           |
| uuid               | String       | 记录事件唯一标识                                             |
| recognizeScore     | Float        | 识别精度分值                                                 |
| mask               | Int          | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| mode               | Int          | 核验模式: 0：刷脸 1：刷脸或刷卡 2：刷脸且刷卡 3：刷脸或刷卡或刷二维码或PIN 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 7：刷脸且PIN 8：刷脸且刷卡且PIN 9：刷卡且PIN |
| rgb_image          | String       | Base64 后的jpeg格式的人脸抓拍图                              |
| pass               | Boolean      | 是否允许通行                                                 |
| timestamp          | Int          | 识别时间                                                     |
| bodyTemperature    | Double       | 体温                                                         |
| user               | object       | 事件用户对象                                                 |
| --name             | String       | 用户名称                                                     |
| --user_id          | String       | 用户id                                                       |
| --type             | Int          | 用户类型                                                     |
| --ic_number        | String       | IC 卡号                                                      |
| --job_number       | String       | 工号                                                         |
| --id_number        | String       | ID卡号                                                       |
| --guest_time_start | Int          | 访客开始时间，毫秒级Unix时间戳                               |
| --guest_time_end   | Int          | 访客结束时间，毫秒级Unix时间戳                               |
| -- remark          | String       | 备注,上限256字节                                             |
| -- groups          | object array | user_id所在的组信息                                          |



## 返回示例

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