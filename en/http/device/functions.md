# Function Parameters

## Set device function parameters

Set device function parameters

### Request address

> `​/v1​/device​/functions`

### Request method

> POST

- Body Type: `application/json`

### Request parameters

| Parameter name  | Type    | Description                                                  |
| --------------- | ------- | ------------------------------------------------------------ |
| device_run_type | Int     | Device running status configuration, 1: running; 2: shutdown |
| mode            | Int     | Verification mode: 0: swipe face 1: swipe face or card 2: swipe face or card or swipe QR code 3: swipe face and swipe card 4: swipe ID card 5: swipe face or swipe ID card 6: swipe face and swipe ID card |
| strong_hint     | Boolean | Strong hint mode switch, false: off; true: on                |
| avatar_status   | Int     | Show avatar 0: Don't show avatar 1: Show avatar 2. Show personalized avatar |
| name_status     | Int     | Show name: 0: No name show 1: Show name 2: Show encrypted name |
| record          | Boolean | Event record storage switch, false: off; true: on            |
| record_image    | Boolean | Event record picture storage switch, false: off; true: on    |
| alarm_record    | Boolean | Alarm record storage switch, false: off; true: on            |
| auth_mode       | Int     | Authentication type: 0: local authentication 1: local authentication + remote door opening |
|remote_authentication_address | String | The address of the specified event receiving, using restful callback mode, supports http and https, the style is as follows: http://ip:port/eventRcv or https://ip:port/eventRcv<br/>The length is no more than 1024 bytes, the event receiving address is provided by the application side according to the specified specification, and the event receiving interface does not require authentication |
| remote_auth_timeout_to_local_auth    | Int |  when `auth_mode` value is not 0，该字段值则用于远程服务器不可达后的指定时间段后自动切换auth_mode为0(本地认证)模式.<br/>取值范围:0~60,单位分钟.<br/>默认: 0<br/>注: 远程认证服务需要实现`remote_authentication_address`同请求路径的`GET`请求方法,返回状态码`200`即可作为心跳判断,设备会每隔30秒请求一次 |


## Request example

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

### Response example

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---

##  Get device function parameters

Get device function parameters.

### Request address

> `​/v1​/device​/functions`

### Request method

> GET

### Response example

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

