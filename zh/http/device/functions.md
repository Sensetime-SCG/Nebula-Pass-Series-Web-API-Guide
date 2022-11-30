# 设备功能参数
设备功能开关，核验模式，展示信息开关，记录存储开关，认证类型等。
## 提交配置

### 请求路径

> `​/v1​/device​/functions`

### 请求方式

> POST

- 请求体: `application/json`

| 字段            | 类型    | 必填 | 字段释义                                                     |
| --------------- | ------- | ---- | ------------------------------------------------------------ |
| device_run_type | Int     | N    | 设备运行状态配置， 1：运行；2：停机                          |
| mode            | Int     | Y    | 核验模式: <br/>0：刷脸 <br/>1：刷脸或刷卡 <br/>2：刷脸且刷卡 <br/>3：刷脸或刷卡或刷二维码 <br/>4：刷身份证 <br/>5：刷脸或刷身份证 <br/>6：刷脸且刷身份证 <br/>7：刷脸且输PIN <br/>8：刷脸且刷卡且输PIN <br/>默认 0<br/>注:7与8模式暂不支持与远程服务器验证 |
| strong_hint     | Boolean | N    | 炫酷模式开关，false：关；true：开                            |
| avatar_status   | Int     | Y    | 头像展示模式: <br/>0：不展示头像 <br/>1：展示头像 <br/>2：展示个性化头像 <br/>默认 1 |
| name_status     | Int     | Y    | 展示姓名模式： <br/>0：不展示姓名 <br/>1：展示姓名 <br/>2：展示加密姓名 <br/>默认 1 |
| record          | Boolean | Y    | 事件记录存储开关，false：关；true：开                        |
| record_image    | Boolean | Y    | 事件记录图片存储开关，false：关；true：开                    |
| alarm_record    | Boolean | Y    | 告警记录存储开关，false：关；true：开                        |
| auth_mode       | Int     | Y    | 认证类型：<br/>0: 本地认证, <br/>1: 本地认证+远程开门, <br/>2: 服务器认证, <br/>3: 本地认证+服务器认证(本地认证结果为陌生人时) <br/>默认 0|
| remote_authentication_address | String | N | 当auth_mode非0时启用,启用服务器认证<br/>请求支持http和https,例：`http://host:port/you_auth_uri` 或者 `https://host:port/you_auth_uri` <br/>且须返回指定格式的 Body，如下[远程服务器认证响应Body格式](https://webapi.gitbook.io/nebula-pass-web-api-guide/zh/http/device/functions#jump-request-body)所示. |

### 请求示例:

> `​/v1​/device​/functions`

```json
{
    "device_run_type": 1,
    "mode": 0,
    "strong_hint": true,
    "avatar_status": 1,
    "name_status": 1,
    "record": true,
    "record_image": true,
    "alarm_record": true,
    "auth_mode": 0,
    "remote_authentication_address": "http://1.2.3.4:4321/record/"
}
```
### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---

## 获取配置

### 请求路径

> `​/v1​/device​/functions`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/functions`

### 返回示例

```json
{
    "data": {
        "device_run_type": 1,
        "mode": 0,
        "strong_hint": true,
        "avatar_status": 1,
        "name_status": 1,
        "record": true,
        "record_image": true,
        "alarm_record": true,
        "auth_mode": 0,
        "remote_authentication_address": "http://1.2.3.4:4321/record/"
    },
    "code": 200,
    "msg": "OK"
}
```



## 事件推送与远程服务器响应

### 事件推送的请求body内容

注: body 内容为json格式

| 参数名称        | 类型    | 说明                                                         |
| --------------- | ------- | ------------------------------------------------------------ |
| deviceSN        | String  | 设备序列号                                                   |
| recognizeStatus | Int    | 当前画面中人脸的分类: 0:未知,1:非活体,2:库中人,3:陌生人,4:已识别,5:认证通过,6:认证失败  |
| mask            | Int   | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| rgb_image       | String | Base64 后的jpeg格式的人脸抓拍图                              |
| timestamp       | Int    | 识别时间                                                     |
| bodyTemperature       | double     | 体温                                                    |
| user            | Object | 事件用户对象                                                 |
| --name          | String | 用户名称                                                     |
| --user_id       | Int    | 用户id                                                       |
| --type          | Int    | 用户类型                                                     |
| --ic_number          | String    | IC 卡号                                                   |
| --job_number          | String    | 工号                                                     |
| --remark          | String    | 备注                                                     |
| --guest_time_start          | Int    | 访客开始时间                                                     |
| --guest_time_end          | Int    | 访客结束时间                                                     |

**请求示例：**

``` json
{
        "recognizeStatus": 1,
        "deviceSN":"PS71HD01MC22C00114",
        "mask": 1,
        "rgb_image": "xxxxxxxxxxxxxx=",
        "user": {
            "name": "Q",
            "user_id": 1,
            "type": 1,
            "ic_number":"d144d33z95x",
            "job_number":"9833",
            "remark":"this is Q",
            "guest_time_start":0,
            "guest_time_end":0
        },
        "timestamp": 1660625866,
        "bodyTemperature": 36.53308868408203
}

```

### 远程服务器认证响应Body格式 {#jump-request-body}

当字段`auth_mode`为非0时，须返回如下格式的 Body。


| 字段           | 类型    | 必填 | 字段释义                                                     |
| -------------- | ------- | ---- | ------------------------------------------------------------ |
| code           | Int     | Y    | 状态码                                                       |
| msg            | String  | Y    | 状态对应信息                                                 |
| data           | Object  | Y    | 具体内容                                                     |
| --pass         | Boolean | Y    | 权限是否允许                                                 |
| --customtips   | Stringn | N    | 自定义提示信息(仅当开启个性化提示)                           |
| --user_id      | Int     | N    | 当前用户id                                                   |
| --user_name    | String  | N    | 当前用户名称                                                 |
| --ic_number    | String  | N    | 门卡号                                                       |
| --verify_score | Float   | N    | 远程识别的相似度分值                                         |
| --verify_code  | Int     | N    | 识别状态码， 1：未激活，2：识别成功，3：没有权限，4：匹配失败，5：不在可通行时间范围内 |


**返回示例:**
```json
{
    "code": 200,
    "msg": "OK",
    "data": {
        "pass": false,
        "customtips": "Hello world",
        "user_id":111,
        "user_name":"xxx",
        "ic_number":"ic_123456",
        "verify_score":0.99,
        "verify_code": 1
    }
}
```