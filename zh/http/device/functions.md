# 设备功能参数
设备功能开关，核验模式，展示信息开关，记录存储开关，认证类型等。<br>
认证类型：<br>
    auth_mode = 0 本地认证：核验库中人人员身份，核验通过则设备发送开门信息。<br>
    auth_mode = 1 本地认证+远程开门：核验库中人人员身份，核验通过则推送人员信息到服务器验证通行权限，并返回相应权限.<br>
    auth_mode = 3 本地认证+服务器认证：核验库中人人员身份，核验通过则设备发送开门信息；对于非库中人，仅支持刷脸则推送人员图片到服务器验证人员身份和通行权限，并返回相应展示信息权限. 建议搭配后端比对服务使用。
    

## 提交配置

### 请求路径

> `​/v1​/device​/functions`

### 请求方式

> POST

- 请求体: `application/json`

| 字段            | 类型    | 必填 | 字段释义                                                     |
| --------------- | ------- | ---- | ------------------------------------------------------------ |
| device_run_type | Int     | N    | 设备运行状态配置， 1：运行；2：停机                          |
| mode            | Int     | N    | 核验模式: <br/>0：刷脸 <br/>1：刷脸或刷卡 <br/>2：刷脸且刷卡 <br/>3：刷脸或刷卡或刷二维码或PIN <br/>4：刷身份证 <br/>5：刷脸或刷身份证 <br/>6：刷脸且刷身份证 <br/>7：刷脸且输PIN <br/>8：刷脸且刷卡且输PIN <br/>9：刷卡且输PIN<br/>默认 0<br/>注:7与8模式暂不支持与远程服务器验证 |
| strong_hint     | Boolean | N    | 炫酷模式开关，false：关；true：开                            |
| avatar_status   | Int     | N    | 头像展示模式: <br/>0：不展示头像 <br/>1：展示头像 <br/>2：展示个性化头像 <br/>默认 1 |
| name_status     | Int     | N    | 展示姓名模式： <br/>0：不展示姓名 <br/>1：展示姓名 <br/>2：展示加密姓名 <br/>默认 1 |
| record          | Boolean | Y    | 事件记录存储开关，false：关；true：开                        |
| record_image    | Boolean | Y    | 事件记录图片存储开关，false：关；true：开                    |
| alarm_record    | Boolean | Y    | 告警记录存储开关，false：关；true：开                        |
| auth_mode       | Int     | N    | 认证类型：<br/>0: 本地认证, <br/>1: 本地认证+远程开门, <br/>2: 保留 <br/>3: 本地认证+服务器认证(本地认证结果为陌生人时) <br/>默认 0 |
| remote_authentication_address | String | N | 当auth_mode非0时启用,启用服务器认证<br/>请求支持http和https,例：`http://host:port/you_auth_uri` 或者 `https://host:port/you_auth_uri` <br/>且须返回指定格式的 Body，如下[远程服务器认证响应Body格式](https://webapi.gitbook.io/nebula-pass-web-api-guide/zh/http/device/functions#jump-request-body)所示. |
| remote_auth_timeout_to_local_auth    | Int | N    | 当auth_mode值非0时，该字段值则用于远程服务器不可达后的指定时间段后自动切换auth_mode为0(本地认证)模式.<br/>取值范围:0~60,单位分钟.<br/>默认: 0, 即永不做切换<br/>注: 远程认证服务需要实现`remote_authentication_address`同请求路径的`GET`请求方法,返回状态码`200`即可作为心跳判断,设备会每隔30秒请求一次 |

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
    "remote_authentication_address": "http://1.2.3.4:4321/auth/",
    "remote_auth_timeout_to_local_auth": 0
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
        "remote_authentication_address": "http://1.2.3.4:4321/auth/",
        "remote_auth_timeout_to_local_auth": 0
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
| recognizeScore  | Float   | 识别精度分值                                                 |
| mask            | Int   | 是否佩戴口罩： 0 未启用 1 未戴 2 佩戴                        |
| rgb_image       | String | Base64 后的jpeg格式的人脸抓拍图                              |
| timestamp       | Int    | 识别时间                                                     |
| bodyTemperature       | double     | 体温                                                    |
| entry_mode    | int       | 开门方式：1：刷脸；2：二维码；3：刷卡；4：刷脸+刷卡；5：刷身份证；6：刷脸且刷身份证；7：刷健康码；8：刷脸+PIN；9：刷卡+PIN；10：刷脸+刷卡+PIN；11：开门按钮；12：工号+PIN  |
| qrcode_content       | String     | 二维码信息字段                                                    |
| user            | Object | 事件用户对象                                                 |
| --name          | String | 用户名称                                                     |
| --user_id       | String | 用户id                                                       |
| --type          | Int    | 用户类型: 1:员工,2:访客,5:黑名单                                                     |
| --ic_number          | String    | IC 卡号                                                   |
| --id_number | String | ID卡号 |
| --job_number          | String    | 工号                                                     |
| --remark          | String    | 备注                                                     |
| --guest_time_start          | Int    | 访客开始时间                                                     |
| --guest_time_end          | Int    | 访客结束时间                                                     |
| -- pin       | String     | 密碼pin code                                            |
| -- groups | object array | user_id所在的组信息 |

**请求示例：**

``` json
{
	"deviceSN": "PSC700C0MC22F02542",
	"recognizeStatus": 2,
	"recognizeScore": 0.923655092716217,
	"entry_mode": 1,
	"mask": 0,
	"rgb_image": "我是远程鉴权/eventRcv",
	"bodyTemperature": 0.0,
	"timestamp": 1686189389,
	"qrcode_content": "",
	"user": {
		"name": "科恩",
		"ic_number": "",
		"id_number": "",
		"job_number": "",
		"pin": "",
		"user_id": "4bf5d479-f64e-4e35-907b-23a162b5d80f",
		"remark": "",
		"guest_time_start": 0,
		"guest_time_end": 0,
		"type": 1,
		"groups": []
	}
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
| --customtips   | String  | N    | 自定义提示信息(仅当开启个性化提示)                           |
| --user_id      | String  | N    | 当前用户id                                                   |
| --user_name    | String  | N    | 当前用户名称                                                 |
| --ic_number    | String  | N    | 开门卡号,开门方式为韦根输出时返回该字段                               |
| --verify_score | Float   | N    | 远程识别的相似度分值                                         |
| --verify_code  | Int     | N    | 识别状态码， 1：未激活，2：识别成功，3：没有权限，4：匹配失败，5：不在可通行时间范围内|

**返回示例:**

```json
{
    "code": 200,
    "msg": "OK",
    "data": {
        "pass": false,
        "customtips": "Hello world",
        "user_id":"111",
        "user_name":"xxx",
        "ic_number":"ic_123456",
        "verify_score":0.99,
        "verify_code": 1
    }
}
```
### 应用示例

**应用示例1:**

通过接口设置将面板机功能设置单—认证类型，设置成auth_mode=1：本地认证+远程开门，核验方式：脸或卡或二维码码或身份证或密码。
auth_mode = 1 本地认证+远程开门：核验库中人人员身份，核验通过则推送人员信息到服务器验证通行权限，并返回相应权限.


| 人员身份     | 核验方式     | 是否支持                                               | 设备UI文字提示           | 返回值 ：Pass = Ture                                         | 返回值 ：Pass =Flase                       |
| ------------ | ------------ | ------------------------------------------------------ | ------------------------ | ------------------------------------------------------------ | ------------------------------------------ |
| 陌生人       | 刷卡         | 陌生人在此模式下不符合本地库中人认证的要求,不上报数据. | 无效卡号，请联系管理员   | N/A                                                          | N/A                                        |
|              | 刷脸         | 陌生人在此模式下不符合本地库中人认证的要求,不上报数据  | 来访者，请联系管理员     | N/A                                                          | N/A                                        |
|              | 刷身份证     | 陌生人在此模式下不符合本地库中人认证的要求,不上报数据  | 无效身份证，请联系管理员 | N/A                                                          | N/A                                        |
|              | 刷PIN码      | 陌生人在此模式下不符合本地库中人认证的要求,不上报数据  | N/A                      | N/A                                                          | N/A                                        |
|              | 刷二维码     | 在此模式下支持刷二維碼                                 | N/A                      | 提示音：门已开<br />提示语：customtips<br />展示：身份卡片信息 | 提示音：无通行权限<br />提示语：customtips |
|              | 人证核验     | 在此模式下支持人证核验                                 | 识别成功卡片             | 提示音：门已开<br />提示语：customtips                       | 提示音：无通行权限<br />提示语：customtips |
|              |              |                                                        |                          |                                                              |                                            |
| **人员身份** | **核验方式** | **是否支持**                                           | **设备UI文字提示**       | **返回值 ：Pass = Ture**                                     | **返回值 ：Pass =Flase**                   |
| 库中人       | 刷卡         | 符合本地库中人认证的要求                               | 识别成功卡片             | 提示音：门已开<br />提示语：customtips                       | 提示音：无通行权限文字：customtips         |
|              | 刷脸         | 符合本地库中人认证的要求                               | 识别成功卡片             | 提示音：门已开<br />提示语：customtips                       | 提示音：无通行权限提示语：customtips       |
|              | 刷身份证     | 符合本地库中人认证的要求（刷身份证 / 人证核验 二选一） | 识别成功卡片             | 提示音：门已开<br />提示语：customtips                       | 提示音：无通行权限提示语：customtips       |
|              | 刷PIN码      | 符合本地库中人认证的要求                               | 识别成功卡片             | 提示音：门已开<br />提示语：customtips                       | 提示音：无通行权限提示语：customtips       |
|              | 刷二维码     | 在此模式下支持刷二維碼                                 | N/A                      | 提示音：门已开<br />提示语：customtips<br />展示：身份卡片信息 | 提示音：无通行权限提示语：customtips       |
|              | 人证核验     | 在此模式下支持人证核验（刷身份证 / 人证核验 二选一）   | 识别成功卡片             | 提示音：门已开提示语：customtips                             | 提示音：无通行权限提示语：customtips       |

**应用示例2:**

通过接口设置将面板机功能设置单—认证类型，设置成auth_mode=3： 本地认证+ 服务器认证，核验方式：脸或卡或二维码码或身份证或密码。
auth_mode = 3 本地认证+服务器认证：核验库中人人员身份，核验通过则设备发送开门信息；对于非库中人，仅支持刷脸则推送人员图片到服务器验证人员身份和通行权限，并返回相应展示信息权限. 建议搭配后端比对服务使用。

| 人员身份     | 核验方式     | 是否支持                                                     | 设备UI文字提示           | 返回值 ：Pass = Ture                                         | 返回值 ：Pass =Flase                                         |
| ------------ | ------------ | ------------------------------------------------------------ | ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 陌生人       | 刷卡         | 在此模式下不支持刷卡,不上报数据                              | 无效卡号，请联系管理员   | N/A                                                          | N/A                                                          |
|              | 刷脸         | 在此模式支持刷脸服务器核验                                   | N/A                      | 提示音：门已开<br />提示语：customtips<br />展示：身份卡片信息<br />"verify_code" = 2（识别成功） | 提示音：无通行权限<br />提示语：customtips<br />"verify_code": ≠ 2 |
|              | 刷身份证     | 在此模式下不支持刷身份证,不上报数据                          | 无效身份证，请联系管理员 | N/A                                                          | N/A                                                          |
|              | 刷PIN码      | 人在此模式下不支持刷PIN开门,不上报数据                       | N/A                      | N/A                                                          | N/A                                                          |
|              | 刷二维码     | 人在此模式下支持刷二維碼                                     | N/A                      | 提示音：门已开<br />提示语：customtips<br />展示：身份卡片信息 | 提示音：无通行权限<br />提示语：customtips                   |
|              | 人证核验     | 在此模式下支持人证核验,不上报数据                            | 识别成功卡片             | N/A                                                          | N/A                                                          |
|              |              |                                                              |                          |                                                              |                                                              |
| **人员身份** | **核验方式** | **是否支持**                                                 | **设备UI文字提示**       | **返回值 ：Pass = Ture**                                     | **返回值 ：Pass =Flase**                                     |
| 库中人       | 刷卡         | 符合本地库中人认证的要求，本地验证通过并开门                 | 识别成功卡片             | N/A                                                          | N/A                                                          |
|              | 刷脸         | 符合本地库中人认证的要求，本地验证通过并开门                 | 识别成功卡片             | N/A                                                          | N/A                                                          |
|              | 刷身份证     | 符合本地库中人认证的要求，本地验证通过并开门（刷身份证 / 人证核验 二选一） | 识别成功卡片             | N/A                                                          | N/A                                                          |
|              | 刷PIN码      | 符合本地库中人认证的要求，本地验证通过并开门                 | 识别成功卡片             | N/A                                                          | N/A                                                          |
|              | 刷二维码     | 在此模式下支持刷二維碼                                       | N/A                      | 提示音：门已开<br />提示语：customtips<br />展示：身份卡片信息 | 提示音：无通行权限提示语：customtips                         |
|              | 人证核验     | 在此模式下支持人证核验,不上报数据                            | 识别成功卡片             | N/A                                                          | N/A                                                          |