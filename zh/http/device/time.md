# 设备时间参数
配置设备当前时间，当manual_mode为flase，时间由NTP获取；manual_mode为true，需配置local_time

## 提交配置


### 请求路径

> `​/v1​/device​/time`

### 请求方式

> POST

- 请求体: `application/json`

| 字段           | 类型    | 是否必须 | 说明                                                          |
| -------------- | ------- | -------- | ------------------------------------------------------------- |
| local_time     | Long    | N        | 设备当前时间，毫秒级Unix时间戳                                |
| manual_mode    | Boolean | N        | 是否手动设置时间，false:自动获取， ture: 手动修改; 默认:false |
| time_zone      | String  | N        | 设备时区,范围：-11~12; 默认: 8                                |
| server_address | String  | N        | NTP 服务器地址                                                |


### 请求示例:

> `​/v1​/device​/time`

```json
{
    "local_time": 1660038297736,
    "manual_mode": false,
    "time_zone": 8,
    "server_address": "https://link.bi.sensetime.com/sl"
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

> `​/v1​/device​/time`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/time`

### 返回示例

```json
{
    "data": {
        "local_time": 1660310557866,
        "manual_mode": false,
        "time_zone": 8,
        "server_address": "ntp.aliyun.com"
    },
    "code": 200,
    "msg": "OK"
}
```

